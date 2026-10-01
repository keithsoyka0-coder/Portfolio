# Showcase Registry — `registry.json` is the source of truth

**14 entries · v1.0.0 · updated 2026-10-01.** A file not listed in `registry.json` is not part of the showcase. The showcase page should render from the registry.

## Sections
| Section | Entries |
|---|---|
| Inner World Exhibits | Dynamic Inner World Exhibit · Dynamic Wiki — Interactive Index · Musical DNA · Audio Analysis |
| Systems & Method | Systems Architecture — Portfolio View · Comprehensive Professional Profile |
| **Live Demos** *(new)* | Billy — Live Chat · Tribunal of Understanding · Generative Render Engine |
| Product Package — Agent Trainer | Agent Trainer Sprint · Agent Trainer — Pricing |
| Brand Boards & Templates | Brand Board · UI Component Sheet · Square Social Template · Story Template |

## Evidence states
- Existing exhibits: **VERIFIED** — inspectable artifacts, open in full in the browser.
- New demos: **STAGED** — built and wired, live once the runtime allowlists channel `"showcase"`. Each demo's page carries its own honest state (live vs. degraded); the registry's `note` field records the caveat.

## To add an entry
Append to `entries[]` in `registry.json` with: `id`, `title`, `file`, `section`, `kind`, `description`, `live`, `runtime_wired`, `evidence`, `added`. Bump `updated`. Kinds: `exhibit` · `demo` · `reference` · `profile` · `package` · `pricing` · `brand` · `ui-kit` · `template`.
