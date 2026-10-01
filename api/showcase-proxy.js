/**
 * POST /api/showcase-proxy
 *
 * Same-origin serverless proxy for the GestaltView Showcase demos
 * (showcase/billy-chat.html, showcase/tribunal.html, showcase/render-engine.html).
 *
 * The browser demos post { text } here with no credentials. This function —
 * running server-side on Vercel — validates, rate-limits, builds the signed
 * insight_bot_request.v2 payload with the server-held INSIGHT_SIGNING_SECRET,
 * and forwards it to the GestaltView runtime's /api/insight-bot/respond.
 * The secret never enters browser code.
 *
 * All three demos share ONE verified runtime contract. No tribunal or
 * render-engine server routes are assumed: persona lenses and artifact
 * rendering happen in the demo pages; synthesis always goes through
 * /api/insight-bot/respond. If a dedicated tribunal/render contract is
 * verified later, extend here — don't invent one.
 *
 * Deploy: place at api/showcase-proxy.js in the repo (Vercel picks up
 * api/*.js as serverless functions). Same project that serves showcase/.
 *
 * Env required:
 *   INSIGHT_SIGNING_SECRET   shared adapter secret (same one the Discord
 *                            adapter uses). NEVER hardcode it.
 *   RUNTIME_URL              e.g. https://gestaltview-three.vercel.app
 *                            (defaults to the live runtime)
 *
 * Runtime delta required (one allowlist change — Keith/Codex action):
 *   /api/insight-bot/respond must accept x-insight-bot-adapter: "showcase"
 *   and channel: "showcase". Everything else in the v2 contract is unchanged.
 */
import { createHash, createHmac } from "node:crypto";

const MAX_TEXT = 4000;
const WINDOW_MS = 60_000;
const MAX_PER_WINDOW = 10; // per IP, per minute
const UPSTREAM_TIMEOUT_MS = 15_000;

// In-memory, therefore per serverless instance. Fine for showcase traffic;
// graduate to Redis/Upstash if abuse ever appears.
const hits = new Map();

function clientIp(req) {
  const fwd = req.headers["x-forwarded-for"];
  if (typeof fwd === "string") return fwd.split(",")[0].trim();
  return req.socket?.remoteAddress ?? "unknown";
}

function rateLimited(ip) {
  const now = Date.now();
  const window = (hits.get(ip) ?? []).filter((t) => now - t < WINDOW_MS);
  window.push(now);
  hits.set(ip, window);
  return window.length > MAX_PER_WINDOW;
}

function send(res, status, body) {
  res.status(status).setHeader("Content-Type", "application/json").end(JSON.stringify(body));
}

export default async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    send(res, 405, { error: "Method not allowed" });
    return;
  }
  if (rateLimited(clientIp(req))) {
    send(res, 429, { error: "Too many requests — please wait a minute.", code: "rate_limited" });
    return;
  }

  let body = req.body;
  if (typeof body === "string") {
    try { body = JSON.parse(body); } catch { body = null; }
  }
  const text = typeof body?.text === "string" ? body.text.trim() : "";
  if (!text || text.length > MAX_TEXT) {
    send(res, 400, { error: "Message must be 1–4000 characters.", code: "bad_input" });
    return;
  }

  const runtimeUrl = (process.env.RUNTIME_URL || "https://gestaltview-three.vercel.app").trim();
  const signingSecret = (process.env.INSIGHT_SIGNING_SECRET || "").trim();
  if (!signingSecret) {
    send(res, 503, { error: "The GestaltView connection has not been configured.", code: "not_configured" });
    return;
  }

  // Stable per-request id without storing anything.
  const requestId = createHash("sha256")
    .update(`showcase:${clientIp(req)}:${Date.now()}`)
    .digest("hex");

  const runtimeRequest = {
    schema_version: "insight_bot_request.v2",
    request_id: requestId,
    channel: "showcase",
    installation_id: "showcase",
    actor: { platform_user_id: "anonymous" },
    conversation: { platform_conversation_id: requestId.slice(0, 16), visibility: "ephemeral" },
    input: { text },
    consent: { response_public: false, retain_input: false, allow_gestaltview_handoff: false },
    policy: { trigger: "custom_post", allow_external_post: false },
  };

  const serialized = JSON.stringify(runtimeRequest);
  const signedAt = Math.floor(Date.now() / 1000).toString();
  const signature = createHmac("sha256", signingSecret)
    .update(`${signedAt}.${serialized}`)
    .digest("hex");

  try {
    const upstream = await fetch(`${runtimeUrl.replace(/\/+$/, "")}/api/insight-bot/respond`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "x-insight-bot-adapter": "showcase",
        "x-insight-bot-timestamp": signedAt,
        "x-insight-bot-signature": `${signedAt}.${signature}`,
      },
      body: serialized,
      signal: AbortSignal.timeout(UPSTREAM_TIMEOUT_MS),
    });
    const data = await upstream.json().catch(() => null);
    if (!upstream.ok || !data || data.request_id !== requestId || typeof data.text !== "string") {
      send(res, 502, { error: "GestaltView is temporarily unavailable. Please retry in a moment.", code: "upstream_unavailable" });
      return;
    }
    send(res, 200, { text: data.text.slice(0, 4000), reply_mode: "ephemeral", live: true });
  } catch (error) {
    console.error("Showcase proxy upstream failed:", error instanceof Error ? error.message : "unknown");
    send(res, 502, { error: "Insight-Bot could not reach GestaltView. Please retry.", code: "upstream_error" });
  }
}
