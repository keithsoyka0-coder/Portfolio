# Showcase Package — CHANGELOG

WF-10 packaging. Every change narrated, every artifact versioned. Keith integrates (repo push, deploy).

## v1.4 — 2026-10-01
- Added `SHOWCASE_ADMIN_TOKEN` owner bypass to `api/showcase-proxy.js`: requests carrying cookie `showcase_admin=<token>` skip the per-IP rate limiter. Fails closed (unset = no bypass); validation, signing, and the runtime contract still apply.
- README: setup steps for the bypass (env var + console cookie snippet).
- Files touched: `api/showcase-proxy.js`, `showcase/README.md`.

## v1.3 — 2026-10-01
- Tribunal "convene" now staggers persona calls by `TRIBUNAL_STAGGER_MS` (default 4000, in `showcase-config.js`) with a "yielding" status between voices. Reason: the runtime's orchestrator trips its circuit breaker on rapid back-to-back calls and serves fallback content (observed: 7 calls in 9s → 1 live + 6 fallback).
- Privacy note + README updated to describe the stagger.
- Files touched: `showcase/tribunal.html`, `showcase/showcase-config.js`, `showcase/README.md`.

## v1.2 — 2026-10-01
- Drift fix: `RUNTIME_URL` → `INSIGHT_BOT_RUNTIME_URL`, `INSIGHT_SIGNING_SECRET` → `INSIGHT_BOT_SIGNING_SECRET` across proxy, config, demo pages, README. Official runtime names, per owner correction.
- Files touched: `api/showcase-proxy.js`, `showcase/showcase-config.js`, `showcase/billy-chat.html`, `showcase/tribunal.html`, `showcase/README.md`.

## v1.1 — 2026-10-01
- Added `showcase/registry.json` (14 entries — source of truth for the showcase directory) + `showcase/registry.md`.
- Added `showcase.html` (repo-root index page) with the new Live Demos section: Billy chat, Tribunal, Render Engine — same design language as the existing page.
- Files touched: new files only.

## v1.0 — 2026-10-01
- Initial build: `showcase/billy-chat.html`, `showcase/tribunal.html`, `showcase/render-engine.html`, `showcase/index.html`, `showcase/showcase-config.js`, `showcase/showcase.css`, `api/showcase-proxy.js` (Vercel serverless: validates, rate-limits 10 req/IP/min, signs `insight_bot_request.v2` with server-held secret, forwards to `/api/insight-bot/respond`), `showcase/README.md`.
- Neural Aurora canon; no secrets in client code; honest degraded states until the runtime allowlists channel `"showcase"`.

## v1.5 — 2026-10-01
- New page `showcase/community.html`: the Discord server embedded live (widget iframe, guild 1555057818787127316) with channel guide and join CTA, in the showcase design language.
- `showcase/index.html`: fourth demo card ("Join the Community"); lede updated to four demos; footer to v1.5.
- `registry.json` → v1.5.0, 15 entries (community.html added as STAGED).
- Owner actions before this goes live: enable the server widget (Discord → Server Settings → Widget), and paste a permanent invite link over `REPLACE-WITH-YOUR-INVITE` in community.html.
- Files touched: new `showcase/community.html`; `showcase/index.html`, `showcase/registry.json`, `showcase/registry.md`.
