# Source provenance and inventory scope

## Source layers

This guide keeps two evidence layers separate. Their counts are not interchangeable.

| Layer | Baseline | Items | Included evidence | What it does not establish |
|---|---|---:|---|---|
| Master Wiki visuals | `GestaltView_Master_Wiki_v4.0.pdf` (116 pages; PDF not bundled) | 54 | 13 curated opening diagrams, 39 later captioned figures, and 2 Mermaid snippets printed on page 78 | That each documented relationship is implemented or live |
| v3 runtime atlas | `GestaltView-v3` commit `03284ea` | 11 | Mermaid maps and a claim-to-source evidence index copied from `docs/architecture-atlas/` | Successful runtime behavior, environment-specific configuration, live deployment, or measured performance |
| **Combined inventory** | Two independent source baselines | **65** | 54 wiki visuals + 11 v3 maps | A unified implementation state across documentation and production |

The historical wiki layer remains intact. The opening diagrams and captioned figures are preserved as source-page crops rather than redrawn. The two printed Mermaid graphs have normalized line wrapping in their `.mmd` source files while retaining labels and edge relationships. The 13 curated cards' key-idea controls are explanatory text, not coordinate-level overlays.

## Room-definition corrections

The page-4 **Dynamic Inner World: Six-Surface Spatial Model** crop is preserved for historical traceability but is tagged as superseded by the supplied room-definition summary, version 0.4 (2026-10-08). Its older raw-capture flow is not the current room contract: Dynamic Inner World is Distilled / Reflective, an evidence-linked Museum of You for finished, workshopped artifacts and approved identity synthesis. Its six named surfaces are described as spatial presentation surfaces; the current definition does not give each surface a raw-capture, attention, or time category. The summary is bundled at `source_pack/room-definitions/RoomsandSpaces.md` and identifies `GestaltView-v3/docs/ROOM_DEFINITIONS.md` as its canonical source. This is a product contract, not proof that the D.I.W. page has finished rebuilding.

The page-26 **Room State and Theme Pipeline** crop is also preserved, but its surrounding Page Inventory Table is marked stale. The table's route names, file paths, and functional-role descriptions are not treated as a current application inventory or as runtime evidence.

## v3 runtime map package

`source_pack/v3-architecture-atlas/` includes:

- 11 Mermaid Markdown maps (`maps/01-…` through `maps/11-…`) and their rendered PNGs;
- the scope/method note, atlas README, pinned `inventory.json`, and `evidence-index.csv`;
- repository-relative source paths and evidence labels from the atlas snapshot.

The full v3 code checkout, original source PDFs, uploaded Deep Wiki, credentials, deployment secrets, and external-service keys are not bundled. The baseline is pinned to the short commit ID `03284ea`; map sources and rendered images are a source-pack snapshot, not a live connection to GitHub.

## Correction ledger

[`WIKI_CLAIM_CORRECTIONS.md`](WIKI_CLAIM_CORRECTIONS.md) and [`../wiki_claim_corrections.json`](../wiki_claim_corrections.json) record nine line-cited Deep Wiki claims and their dispositions. They distinguish corrected endpoint/function names, qualified route/performance descriptions, missing paths at the pinned commit, and guidance/example metrics from measured results. The notes do not assert that a path absent at this commit is absent from all deployments or later branches.

## Limits and reading rule

The 54-item wiki inventory covers the explicit opening diagram set, 39 later `Figure` captions, and Mermaid syntax blocks found in extracted PDF text. It does not claim every uncaptioned illustration or decorative graphic in the PDF has been catalogued. Some page crops retain nearby text for attribution and context.

The v3 atlas is restricted to checked-in code and configuration at commit `03284ea`; Vision Blueprint and future-design material are outside that runtime scope. Source presence proves a repository declaration or code path, not successful execution, deployed configuration, observability, or outcome. The included evidence index identifies paths and confidence boundaries for technical review.
