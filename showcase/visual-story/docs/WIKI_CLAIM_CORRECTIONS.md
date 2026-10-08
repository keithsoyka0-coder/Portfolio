# Deep Wiki claim corrections

**Wiki snapshot:** `GestaltView-DeepWiki-Compiled_2026-10-08.md` (2026-10-08)  
**Runtime baseline:** GestaltView-v3 `03284ea`  
**Status:** Source-checked against the pinned repository snapshot; this is not a live deployment audit.

The correction entries below keep documentation claims separate from implemented code paths, checked-in configuration, and measured production behavior.

## Billy and DI runtime — `billy-browser-path`

**Deep Wiki lines:** 104, 180, 916, 919  
**Disposition:** qualified

**Wiki claim:** The wiki presents Billy's primary real-time path as direct browser-side Gemini Flash calls.

**Source-checked correction:** The traced BillyLive interaction calls callBillyApi and /api/billy. A separate BillyEngine path calls /api/llm-proxy, and another branch calls /api/billy. These are backend-facing calls. Gemini is present in server-side provider routing; that does not establish a direct browser-to-provider path for the traced flow. Do not generalize beyond these specific paths.

**Repository source references:**
- `client/src/components/BillyLive.tsx` — 455
- `client/src/lib/billyApi.ts` — 244
- `client/src/lib/BillyEngine.ts` — 1261, 1485
- `api/billy.ts` — 552
- `api/_lib/llmRouter.ts` — 60, 598
- Atlas evidence IDs: 05-E01–E04-1, 05-E01–E04-3, 05-E05-1, 01-E05-1
**Related maps:** 05-billy-di-runtime

## Performance claims — `billy-sub-100ms`

**Deep Wiki lines:** 180, 2494  
**Disposition:** not established

**Wiki claim:** The wiki describes sub-100ms interactions and latency profiling in a way that may read as achieved runtime performance.

**Source-checked correction:** The repository documents performance targets and optimization guidance, but the source-tracing work did not benchmark live requests or verify a sub-100ms result. Keep the statement labeled as a target unless measured evidence is supplied.

**Repository source references:**
- `.agents/agents/categories/05-data-ai/machine-learning-engineer.md` — 37-56
- `client/src/components/BillyLive.tsx` — source call path; no latency benchmark
**Related maps:** 05-billy-di-runtime, 11-build-deploy-operations

## API surface — `flat-api-entrypoints`

**Deep Wiki lines:** 1053, 1054, 1055  
**Disposition:** corrected

**Wiki claim:** The endpoint catalog names api/trainer.ts, api/gate.ts, and api/gen-engine.ts as handler files.

**Source-checked correction:** Those flat files are absent at this baseline. The checked tree has directory-based handler families, including api/trainer/agents.ts, api/gate/[...path].ts, and api/gen-engine/artifacts.ts. Describe the names as route families and cite concrete handlers; do not imply each flat file exists.

**Repository source references:**
- `api/trainer.ts` — absent at commit 03284ea
- `api/trainer/agents.ts` — present handler
- `api/gate.ts` — absent at commit 03284ea
- `api/gate/[...path].ts` — present catch-all handler
- `api/gen-engine.ts` — absent at commit 03284ea
- `api/gen-engine/artifacts.ts` — present handler
- Atlas evidence IDs: 03-E08-1, 03-E09-1
**Related maps:** 03-api-surface

## Scheduled work — `cron-inventory`

**Deep Wiki lines:** 2818  
**Disposition:** corrected

**Wiki claim:** The wiki describes generic memory-compaction, embedding-refresh, and agent-state-sync cron jobs.

**Source-checked correction:** The four checked-in Vercel cron declarations are provenance-upgrade, codex-drain, profile-portrait-drain, and profile-portrait-cadence. They do not match the listed tasks. Configuration proves declaration only, not live execution.

**Repository source references:**
- `vercel.json` — 6-29
- `api/cron/` — specific scheduled handlers
- Atlas evidence IDs: 11-E03-1, 08-E07–E09-1
**Related maps:** 08-trainer-and-workers, 11-build-deploy-operations

## Health checks — `health-check-scope`

**Deep Wiki lines:** 2815, 2817  
**Disposition:** corrected

**Wiki claim:** A generic api/health endpoint is described as validating database connectivity, pgvector, and external provider availability.

**Source-checked correction:** The checkout has specific health handlers. api/billy-health.ts checks Supabase pipeline status, invokes the search_knowledge_fragments RPC, reports configured-provider status, and returns voice status. Its top-level ok result combines Supabase, RPC, and configured-provider checks; voice is reported separately. This does not establish a generic endpoint with every claimed check.

**Repository source references:**
- `api/billy-health.ts` — specific Billy pipeline/readiness handler
- `api/_lib/supabase.ts` — pipeline health and RPC helpers
- `api/_lib/llmRouter.ts` — configured-provider status
- `api/_lib/billyVoice.ts` — voice status payload
**Related maps:** 03-api-surface, 11-build-deploy-operations

## Supabase Edge Functions — `edge-function-names`

**Deep Wiki lines:** 1648, 1730, 1755, 1759, 1760, 1761  
**Disposition:** corrected

**Wiki claim:** The wiki names gsvw-auth, gsvw-ingest, and gsvw-sync as Edge Function workers.

**Source-checked correction:** At commit 03284ea, supabase/config.toml enables five functions: corpus-harvest-worker, gsvw-capture-event, gsvw-dormancy-review, gsvw-ingest-batch, and gsvw-runtime-health. The three wiki-named folders are absent from this checkout. Enabled configuration and source folders are not evidence of live deployment.

**Repository source references:**
- `supabase/config.toml` — 391-409
- `supabase/functions/` — corresponding checked-in function directories
- Atlas evidence IDs: 01-E09-1, 04-E13–E14-1, 08-E11–E12-1
**Related maps:** 04-auth-and-trust, 08-trainer-and-workers

## Trainer and background workers — `trainer-worker-entrypoint`

**Deep Wiki lines:** 1411, 2449, 2473, 2477, 2491  
**Disposition:** qualified

**Wiki claim:** The wiki presents the Agent Trainer pipeline and asynchronous worker system as implemented deployment routines.

**Source-checked correction:** workers/codex exists and contains Codex worker code. Separately, package.json declares trainer:worker as tsx worker/trainer/main.ts, but that target path is absent from the checked-out tree. Distinguish existing Codex workers and trainer API routes from the missing trainer-worker entrypoint; do not describe that script as verified execution or production model deployment.

**Repository source references:**
- `workers/codex/` — present Codex worker files
- `package.json` — 20
- `worker/trainer/main.ts` — absent at commit 03284ea
- Atlas evidence IDs: 08-E13-1, 11-E10-1
**Related maps:** 08-trainer-and-workers, 11-build-deploy-operations

## Deployment and operations — `active-deployment-and-monitoring`

**Deep Wiki lines:** 2956  
**Disposition:** qualified

**Wiki claim:** The wiki presents Vercel as the primary active production/staging target and says health is continuously monitored.

**Source-checked correction:** Vercel configuration and a push-triggered Azure deployment workflow coexist in the repository. The active production target and actual monitoring state were not queried and remain unresolved. Present the checked-in files as declarations, not proof of a live deployment or continuous monitoring.

**Repository source references:**
- `vercel.json` — build/output and cron configuration
- `.github/workflows/main_gestaltview.yml` — Azure deployment workflow declaration
- Atlas evidence IDs: 11-E03-1, 11-E06-1, 01-E10-1
**Related maps:** 11-build-deploy-operations

## Quality and security metrics — `quality-metrics-not-results`

**Deep Wiki lines:** 2909, 2910  
**Disposition:** qualified

**Wiki claim:** The wiki reports an >80% test-coverage threshold and more than 347 validated security controls as diligence metrics.

**Source-checked correction:** The >80% value appears in a code-review checklist as a target, not measured coverage. The 347 value appears in a sample security-audit progress JSON marked auditing; it is not proof that a real audit reviewed 347 controls or completed successfully. Label both as guidance/example content, not results.

**Repository source references:**
- `.agents/agents/categories/04-quality-security/code-reviewer.md` — 17-25
- `.agents/agents/categories/04-quality-security/security-auditor.md` — 196-208
**Related maps:** 11-build-deploy-operations

## Reading boundary

Presence in source or configuration establishes a repository-level declaration, not successful execution or live deployment. Absence is scoped to commit `03284ea`; it is not a claim about other repositories or private infrastructure.
