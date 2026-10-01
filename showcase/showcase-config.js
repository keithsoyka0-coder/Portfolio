/**
 * SHOWCASE wiring — single place for every demo's runtime connection.
 *
 * Drop-in: copy this file with the showcase/ directory. The demo pages
 * POST to PROXY_PATH on the same origin; the proxy (api/showcase-proxy.js)
 * holds the signing secret server-side. Nothing secret ever ships here.
 */
window.SHOWCASE_CONFIG = {
  // Public base of the live GestaltView runtime. Used for status links only;
  // demo traffic always goes through the same-origin proxy below.
  RUNTIME_URL: "https://gestaltview-three.vercel.app",

  // Same-origin serverless proxy. In the Portfolio repo this resolves to
  // <site>/api/showcase-proxy once api/showcase-proxy.js is deployed.
  PROXY_PATH: "/api/showcase-proxy",

  // Adapter/channel identity the runtime must allowlist (see README).
  CHANNEL: "showcase",

  // Mirrors the proxy's server-side rate limit. The UI uses this to
  // pre-emptively pace multi-call demos (tribunal council mode).
  RATE_LIMIT_PER_MIN: 10,

  // How long a demo waits for the runtime before calling it degraded.
  TIMEOUT_MS: 20000,

  // Max characters per message.
  MAX_TEXT: 4000,
};
