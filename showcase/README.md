# GestaltView Showcase v1 — drop-in demo bundle

Three working demos of the live GestaltView runtime, rebuilt in the current
product language (Neural Aurora canon) and wired honestly: everything either
calls the real runtime or says exactly what it is.

**Copy-in:** drop `showcase/` and `api/` at the Portfolio repo root
(`keithsoyka0-coder/Portfolio`). The demos live at `showcase/*.html`;
Vercel serves `api/showcase-proxy.js` at `/api/showcase-proxy`. Nothing else
moves.

## What's inside

| Path | What it is |
|---|---|
| `showcase/index.html` | Landing — the three demos, one line each on what they prove |
| `showcase/billy-chat.html` | Demo 01 — live chat with Billy via signed proxy |
| `showcase/tribunal.html` | Demo 02 — one question, seven tribunal lenses |
| `showcase/render-engine.html` | Demo 03 — source material in, styled artifact out |
| `showcase/showcase-config.js` | Single wiring config (runtime URL, proxy path, channel, limits) |
| `showcase/showcase.css` | Neural Aurora canon, shared by all pages |
| `api/showcase-proxy.js` | Same-origin serverless proxy — holds `INSIGHT_BOT_SIGNING_SECRET`, signs the `insight_bot_request.v2` payload, forwards to `/api/insight-bot/respond` |

## Deploy (Vercel)

1. Copy `showcase/` and `api/` into the repo root. Commit + push.
2. In the Vercel project: set env var **`INSIGHT_BOT_SIGNING_SECRET`** to the same
   shared adapter secret the Discord adapter uses. **Never hardcode it,
   never put it in client-side code.**
3. `INSIGHT_BOT_RUNTIME_URL` defaults to `https://gestaltview-three.vercel.app`; override
   via env if the runtime moves.
4. **Owner testing bypass (optional):** the proxy rate-limits to 10 req/IP/min.
   To test without tripping it, set **`SHOWCASE_ADMIN_TOKEN`** to a long random
   string (`openssl rand -hex 32`), redeploy, then run this once in the browser
   console on your portfolio domain (replace `PASTE_TOKEN`):

   ```js
   document.cookie = "showcase_admin=PASTE_TOKEN; path=/; max-age=604800; SameSite=Lax";
   ```

   Requests carrying that cookie skip the rate limiter. Validation, the signing
   secret, and the runtime contract all still apply — and if the env var is
   unset, no bypass exists at all.
5. **Runtime allowlist (required — Keith/Codex action):**
   `/api/insight-bot/respond` must accept the new adapter identity, or every
   demo degrades. The exact change, in the runtime's adapter/channel check:

   ```ts
   // allow alongside the existing "discord" / "portfolio" entries:
   const ALLOWED_ADAPTERS = ["discord", "portfolio", "showcase"];
   // and accept channel: "showcase" in the v2 payload
   // (header x-insight-bot-adapter: "showcase")
   ```

   Until that ships, the demos show their honest degraded states — nothing
   fakes a live reply.

## Test each demo

1. **Billy chat** — open `showcase/billy-chat.html`. The status line should read
   `LIVE — CONNECTED TO THE GESTALTVIEW RUNTIME` (the page pings through the
   signed path on load). Send a message; Billy replies. Clear wipes the view
   (nothing was stored anywhere).
2. **Tribunal** — open `showcase/tribunal.html`, pick a lens, ask a question.
   Then "Convene the full tribunal" — 7 sequential calls staggered ~4s apart
   (keeps the runtime's orchestrator from tripping its circuit breaker),
   ~a minute, progress bar throughout.
3. **Render engine** — open `showcase/render-engine.html`, pick artifact type +
   style, paste source material, Render. The styled artifact appears with a
   copy-markdown button.

To test locally before deploying: the pages need the proxy, so serve the repo
root (`npx vercel dev`) with `INSIGHT_BOT_SIGNING_SECRET` set — static file serving
alone will show the degraded states, which is itself a useful test.

## LIVE vs STUBBED — the honest table

| Demo / piece | State | What that means |
|---|---|---|
| Billy chat replies | **LIVE** (once allowlisted) | Real `/api/insight-bot/respond` via signed proxy. Degraded label until then. |
| Tribunal synthesis | **LIVE** (once allowlisted) | Same contract; each lens is framing applied in-page. |
| Tribunal endpoint | **NOT ASSUMED** | No dedicated tribunal route is called or invented. If one is verified on the runtime later, wire it in `api/showcase-proxy.js`. |
| Render synthesis | **LIVE** (once allowlisted) | Billy synthesizes via the engine's real prompt logic (style guides, artifact formats, PLK constraint — ported from `gen-engine/artifacts.ts`). |
| Render export formats | **LOCAL ONLY** | Markdown→styled-HTML happens in-browser. Server-side PDF/PNG/audio export is not in this demo. |
| Persona lens text | **DEMO COPY** | Architect/Guardian/Weaver grounded in canonical embodiment profiles; Mirror/Philosopher/Witness per the Tribunal's documented roles; Steward written for the seventh seat. Not canonical profiles. |
| Secrets | **NONE CLIENT-SIDE** | The signing secret lives only in the serverless function env. |

## Notes for future work

- The seven tribunal lenses live in `tribunal.html` as a `PERSONAS` array —
  easy to extend when canonical Steward/Mirror/etc. profiles land.
- Rate limit is 10 req/IP/min, mirrored in `showcase-config.js` so the UI can
  pace itself (tribunal council mode stays under it by construction).
- Everything is ephemeral: no localStorage, no cookies, no analytics on
  visitor words — same posture as the portfolio Insight-Bot embed.
