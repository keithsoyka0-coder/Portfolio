# Visual Story Layer — Implementation Notes

**Source design:** `docs/superpowers/specs/2026-10-08-self-host-verified-runtime-story-integration-design.md`  
**State:** Integrated static artifact with room-definition corrections; acceptance suite passed on 2026-10-08

## Completed work

### 1. Preserved wiki visual layer

- Retained the original 54-item inventory: 13 curated diagrams, 39 captioned figures, and 2 printed Mermaid snippets.
- Kept page references, source forms, confidence notes, and explanatory key-idea controls intact.
- Preserved source crops, while marking the page-4 Dynamic Inner World figure as historical/superseded and the page-26 Page Inventory Table as stale.
- Corrected the D.I.W. explanations at all three depths and for all six surfaces: the room is Distilled / Reflective, not a raw-capture sorting layout; surfaces remain spatial presentation surfaces without unsupported attention/time categories.

### 2. Added code-verified v3 runtime atlas

- Added 11 Mermaid maps and rendered images, sourced from the architecture atlas at commit `03284ea`.
- Bundled the Markdown map sources, scope/method note, inventory, and evidence index under `source_pack/v3-architecture-atlas/` without copying the v3 code checkout.
- Kept the runtime lane separate from the wiki lane and labeled it as a repository snapshot, not a live deployment report.
- Added a nine-entry, line-cited correction ledger for stale or unsupported Deep Wiki claims about Billy paths/performance, API path names, cron jobs, health checks, Edge Functions, trainer workers, deployment state, and quality metrics.
- Bundled the user-supplied room-definition summary as a product-contract reference, not as proof of current implementation.

### 3. Integrated self-hosted experience

- Retained the three reading depths: orientation, product/system, and architecture.
- Added runtime-source and evidence links, correction callouts, source-layer-aware navigation labels, and search across map/evidence/correction text.
- Kept image zoom, keyboard navigation, mobile navigation, and historical page attribution.
- The final page remains a single HTML file with embedded image data and no external runtime assets.

### 4. Build and verification

- `python3 -m py_compile build_story_artifact.py` — passed.
- `python3 build_integrated_story.py` — generated 54 historical visuals + 11 runtime maps = 65 total.
- `python3 -m unittest discover -s tests -v` — 6 tests passed, 0 failures, including the new room-copy and stale-inventory regression test.
- The integrated UI was not re-run through a browser smoke test in this correction pass; use a local static preview before a public launch if visual QA is required.

## Rebuild

The integrated builder uses Python's standard library and the bundled package data. To regenerate the historical PDF layer, first supply the omitted Master Wiki PDF and use the optional PDF dependencies; then rerun `build_integrated_story.py` to restore the combined 65-item artifact. The two-map wiki Mermaid renderer remains an external build utility; v3 map renders are bundled.

## Scope and limitations

The runtime atlas represents checked-in code and configuration at commit `03284ea`. It does not verify production deployments, credentials, environment-specific provider behavior, successful live requests, or performance measurements. Vision Blueprint/design-intent content is excluded from that runtime atlas. The correction ledger records claim-level reconciliation, not a comprehensive audit of every sentence in the Deep Wiki. The room-definition reference is clearly labeled as a product contract and does not claim the rebuilding D.I.W. page is live.
