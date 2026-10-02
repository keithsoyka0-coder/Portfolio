# Showcase Package — CHANGELOG

WF-10 packaging. Every change narrated, every artifact versioned. Keith integrates (repo push, deploy).

## v1.9 — 2026-10-02
- Diagram-family types (mermaid/diagram/graph) no longer render as paragraph soup: `renderDiagramAware()` detects raw diagram syntax (or the type selection) and shows it as a labeled, theme-aware source block ("… SOURCE — STAGED · NATIVE RENDERER IN PRODUCTION") instead of feeding it to the markdown renderer. Honest copy updated to match.
- 4s post-render cooldown on the Generate button: switching formats and re-rendering quickly was serving the runtime's local-fallback content (reported 2026-10-02) — same circuit-breaker root cause as the v1.3 tribunal stagger, so the demo now enforces the same 4s spacing. Cooldown status names the reason.
- Footer/provenance/registry → v1.9.0.
- Files touched: `showcase/render-engine.html`, `showcase/registry.json`, `showcase/registry.md`.

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

## v1.5.1 — 2026-10-01
- Wired the permanent invite link (https://discord.gg/HjdKeU9dV) into `showcase/community.html`'s join button.
- Added the community card to the repo-root `showcase.html` Live Demos grid (it was only on `showcase/index.html`).
- Files touched: `showcase/community.html`, `showcase.html`.

## v1.6 — 2026-10-01
- New page `showcase/billy-unslashed-council.html`: portfolio announcement post — Billy unslashed (plain conversation on the portfolio, no slash commands) and the Tribunal's next evolution into a multi-model council. Statuses labeled honestly: unslashed chat STAGED (runtime allowlist pending), council announced as the next build, not claimed as shipped.
- `showcase/render-engine.html`: new render themes (Obsidian / Parchment / Terminal, switchable live) and new export modes — copy plain text, download .md, download standalone .html (in the active theme), print / save-as-PDF. Honest callout updated (production still adds server-side PNG/audio).
- Announcement linked from `showcase/tribunal.html` and `showcase/billy-chat.html`.
- All showcase footers bumped to v1.6; `registry.json` → v1.6.0, 16 entries.
- Files touched: new `showcase/billy-unslashed-council.html`; `showcase/render-engine.html`, `showcase/tribunal.html`, `showcase/billy-chat.html`, `showcase/index.html`, `showcase/community.html`, `showcase/registry.json`, `showcase/registry.md`.

## v1.7 — 2026-10-01
- Contract alignment: the demo now drives the production Gen-Engine's actual contract, verified against `server/gen-engine-templates.ts` and `server/routers.ts` from the Gen-Render Studio source.
- Added the missing synthesis style `revolutionary` and PLK mode `score-only`; artifact types expanded from 6 to the full 15 (markdown, pdf-ready-html, blueprint-json, agent-prompt, image-prompt, code, diagram, mermaid, graph, workflow added).
- Style guides and format directives now quoted verbatim from the engine source; prompt assembly mirrors `buildSystemPrompt` + `buildUserPrompt` (concatenated — the proxy takes a single text field; production uses separate system/user messages, and the page says so).
- New: destination selector (5 production destinations, declared intent only — the page says production routes for real) and a demo-computed provenance envelope line under each artifact (source hash, type, style, destination, engine version, timestamp).
- Correction: the v1.6 callout claimed production "adds export formats (PDF, PNG, audio)" — wrong. Production tRPC export covers html/json/markdown; audio/video/image/pdf are content formats with dedicated Studio renderers. The callout now states this correctly.
- Files touched: `showcase/render-engine.html`, `showcase/registry.json`, `showcase/registry.md`.

## v1.8 — 2026-10-01
- Bug fix (found by dogfooding): `pdf-ready-html` artifacts were fed through the markdown renderer, which saw the ```html fence and escaped the whole document into a code block — the user got a text dump of HTML source instead of a document.
- `pdf-ready-html` now renders natively in a sandboxed iframe (sandbox="", no scripts) — the same approach as the Studio's HtmlRenderer. Fence-stripping plus a guarded unescape for models that emit literal \n.
- Per-type export: for HTML artifacts the buttons become Copy HTML / Download .html / Print-PDF, and Download/Print operate on the artifact document itself (the actual print-ready file), not the demo wrapper. Markdown-oriented buttons hide for this type.
- Theme selector disables for `pdf-ready-html` (the artifact carries its own print styles).
- Fix verified by replaying the exact failing payload through the new extraction code: valid complete document out, fence-free.
- Files touched: `showcase/render-engine.html`, `showcase/registry.json`, `showcase/registry.md`.
