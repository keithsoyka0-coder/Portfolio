# GestaltView v3 Architecture Atlas

**Source baseline:** private repository `keithsoyka0-coder/GestaltView-v3`, branch `main`, commit `03284ea` (inspected 2026-10-08). This atlas maps only behavior supported by the checked-out implementation and its runtime/deployment wiring. It does not map the Vision Blueprint or treat the wiki as runtime authority.

## Pick an entry point

- **Plain-language:** Start with [system context](01-system-context.md), then follow each domain's first reader layer. It answers what talks to what without asking you to read the repository.
- **Product/system:** Read [client surfaces](02-client-surfaces.md), [API surface](03-api-surface.md), [knowledge and memory](06-knowledge-and-memory.md), and [creation/exports](09-creation-and-exports.md) to see the user-facing and operational loops.
- **Architectural engineering:** Begin with [scope and method](00-scope-and-method.md), then traverse [trust boundaries](04-auth-and-trust.md), [Billy/DI runtime](05-billy-di-runtime.md), [persistence](07-persistence-topology.md), [workers](08-trainer-and-workers.md), and [operations](11-build-deploy-operations.md). Use the evidence index to jump to source.

## Maps

| Map | What it covers |
|---|---|
| [01 — System context](01-system-context.md) | Runtime nodes, external boundaries, and configured execution surfaces |
| [02 — Client surfaces](02-client-surfaces.md) | Browser bootstrap, routes, providers, and client/API links |
| [03 — API surface](03-api-surface.md) | Handler families, routing conventions, and source-derived inventory |
| [04 — Authentication and trust](04-auth-and-trust.md) | Session exchange, identity, route guards, cron and Edge Function boundaries |
| [05 — Billy and DI runtime](05-billy-di-runtime.md) | Request assembly, retrieval, provider cascade, fallback, and continuity |
| [06 — Knowledge and memory](06-knowledge-and-memory.md) | Corpus ingestion, retrieval modes, embeddings, and memory lifecycle |
| [07 — Persistence topology](07-persistence-topology.md) | Supabase-backed stores, migrations, snapshots, and persistence caveats |
| [08 — Trainer and background work](08-trainer-and-workers.md) | Admin trainer routes, orchestrator, cron, Edge Functions, and worker gaps |
| [09 — Creation and exports](09-creation-and-exports.md) | Gen Engine, Codex bridge, durable export jobs, and immediate exports |
| [10 — Voice and media](10-voice-and-media.md) | Billy speech modes, Deepgram boundary, and action-dispatch surfaces |
| [11 — Build, deploy, and operations](11-build-deploy-operations.md) | Build entrypoints, Vercel/Azure configuration, telemetry, and drift |

Every map has **Plain-language**, **Product/system**, and **Engineering** entrypoints, an independent Mermaid diagram, evidence IDs, and a boundary/caveat section. Links point into the repository at the baseline snapshot.

## Companion material

- [Scope and method](00-scope-and-method.md) — evidence rules and confidence limits.
- [`inventory.json`](inventory.json) — client routes, API handler candidates, all SQL migration filenames and detected DDL anchors, configured cron/Edge Function entrypoints, and persistence anchor groups.
- [`evidence-index.csv`](evidence-index.csv) — claim-to-source ledger with line ranges where supplied, module-level anchors otherwise, and evidence/confidence labels.
- [`build_evidence_index.py`](build_evidence_index.py) — rebuild the evidence ledger from each map's evidence-key links.
- [`generate_inventory.py`](generate_inventory.py) — rebuild the deterministic inventory from this checkout.
- [`validate_atlas.py`](validate_atlas.py) — standard-library link, evidence, map-shape, and inventory checks; optionally renders Mermaid.
- [`rendered/`](rendered/) — PNG previews generated from the Mermaid source after validation.

## Rebuild and validate

From the repository root:

```bash
python3 docs/architecture-atlas/build_evidence_index.py
python3 docs/architecture-atlas/generate_inventory.py
python3 -m unittest discover -s docs/architecture-atlas/tests -v
python3 docs/architecture-atlas/validate_atlas.py --render-dir docs/architecture-atlas/rendered
```

The last command requires the `manus-render-diagram` executable for actual Mermaid parsing/rendering. The inventory generator and tests otherwise use only the Python standard library. Rendering validates syntax/renderability; it does **not** validate whether a diagram is architecturally true.

## Important reading note

Counts are derived from this tree, not copied from the generated v2-era manifest. The `115` client routes are literal `path=` declarations; the `169` API handlers are default-export TypeScript/JavaScript files outside the helper/test directories and are therefore **route candidates**, not proof of deployed routes. Vercel crons and Supabase Edge Functions are configuration declarations, not deployment-health evidence. Read [scope and method](00-scope-and-method.md) before using the atlas as an operational runbook.
