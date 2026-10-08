# Scope, method, and confidence

## Plain-language

This atlas is a map of what the repository can demonstrate, not a promise about what is deployed. If a path is only configured, disconnected, or missing its target, it is labeled that way instead of being drawn as an accomplished runtime.

## Product/system

The source snapshot is `main` at `03284ea`, inspected 2026-10-08. Evidence was traced manually through executable client/API code, schema migrations, worker entrypoints, package scripts, CI/deployment configuration, and selected tests. The failed agent workflow supplied no evidence and is not part of this atlas.

The user's selected scope is **implemented runtime only**. The Vision Blueprint, unverified wiki statements, historical docs, and generated manifests were not used to assert current behavior. They may help orient a reader, but this atlas cites source/configuration instead.

## Engineering

### Evidence labels

- **Direct code path:** an import, call, route, data operation, or handler branch visible in source.
- **Configuration-dependent:** a path enabled or scheduled by checked-in configuration, or gated by environment values. Configuration is not proof of live deployment or credentials.
- **Optional/degraded:** fallback, local-only, non-default, best-effort, or failure recovery path.
- **Unresolved:** the repository does not establish the next boundary, reachability, consumer, or live system state.

`evidence-index.csv` records claim, repository-relative file, symbol/line range, evidence type, confidence, and scope note. Line ranges are checked against the files in this checkout. Confidence describes how directly the repository supports the claim; it does not describe the quality of a production deployment.

### Extraction and counting rules

- Client routes are unique literal values of the `path=` JSX attribute in `client/src/App.tsx`; catch-all routing is described separately.
- API handlers are default-export `.ts`/`.js` files under `api/`, excluding helper and test directories and underscore-prefixed helper files. The Vercel route shape is inferred from each file path and can be changed by platform settings.
- Migration anchors are parsed from the 94 checked-in SQL migration files. The inventory records detected `CREATE/ALTER TABLE` and `CREATE FUNCTION` names; dynamic SQL and every RLS policy relationship are not exhaustively inferred from that extraction.
- Vercel cron schedules and enabled Supabase Edge Functions come from `vercel.json` and `supabase/config.toml`. Neither proves a production deployment.

### Known limits and source drift

- No live Supabase project, Vercel deployment, Azure deployment, or external provider was queried. Runtime secrets and private prompt text are intentionally excluded.
- The repository contains v2-labeled orientation material and a generated manifest with older commit metadata. This atlas uses the `03284ea` source tree instead.
- `supabase/visual/CompleteSchema.sql`, schema reports, and dated database dumps are snapshot artifacts. They are not asserted to match a live database or to supersede migration history.
- The package declares Prisma scripts/dependencies, but the inspected tree has no `prisma/` directory and a source scan found no `PrismaClient` instantiation. This is not mapped as an active persistence path.
- A Vite development proxy points to a configurable external default, and the Azure deployment workflow coexists with Vercel configuration. The actual currently deployed target is unresolved.
- Route, migration, and worker inventory validation checks deterministic repository consistency only. It does not prove authorization completeness, production behavior, data correctness, or architectural quality.
- The application build, full application test suite, migrations against a database, provider calls, and production deployments were not run as part of this documentation task.

## Boundaries

Each domain page distinguishes what the source establishes from what it cannot establish. Any statement about a configured service, a missing consumer, or an absent source target is scoped to this repository snapshot and is not a claim about other repositories or private infrastructure.
