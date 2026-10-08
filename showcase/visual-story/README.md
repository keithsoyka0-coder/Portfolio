# GestaltView Visual Story

A self-hostable static guide that combines **54 historical visuals from GestaltView Master Wiki v4.0** with **11 code-verified runtime maps** from the `GestaltView-v3` repository at commit `03284ea`. The host-ready entry point is [`index.html`](index.html).

## Host it

There is **no runtime build step**: no Node install, backend, API key, database, CDN, external font, or remote image dependency. Publish the repository root as a static site document root. The only file required to serve the experience is `index.html`; the remaining files are included for source review, rebuilding, provenance, and tests.

For a local preview:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000`, or open `index.html` directly in a modern browser.

## What readers get

The opening screen offers three levels: **Get oriented**, **Understand the system**, and **Explore the architecture**. The searchable atlas contains 65 visuals across two clearly labeled source layers:

- **Master Wiki v4.0:** 13 curated opening diagrams, 39 later captioned figures, and 2 printed Mermaid source snippets. Wiki items retain PDF page references.
- **GestaltView-v3 runtime atlas:** 11 Mermaid maps traced to commit `03284ea`. Each map links to its Markdown source and the included claim-to-source evidence index. These are repository-snapshot maps, not live deployment reports.

The guide includes depth-specific explanations, source/correction callouts, image zoom, keyboard navigation, and selectable key-idea explanations on the 13 curated wiki diagrams. Those selectors are reading aids, not coordinate-level hotspots.

Two room-related wiki visuals are explicitly caveated: the page 4 Dynamic Inner World diagram is retained as a historical source but marked superseded by the supplied v0.4 room definition; the page 26 Page Inventory Table is marked stale and is not presented as a current route/function list. The room-definition summary is bundled at [`source_pack/room-definitions/RoomsandSpaces.md`](source_pack/room-definitions/RoomsandSpaces.md).

The [Deep Wiki correction ledger](docs/WIKI_CLAIM_CORRECTIONS.md) records the claims reviewed, their source lines, and the code-verified correction or evidence boundary. The original Deep Wiki and the full v3 checkout are intentionally not included.

## Repository contents

- `index.html` — complete self-contained static experience
- `story_template.html`, `build_story_artifact.py`, `build_integrated_story.py` — editable template and separate source-layer builders
- `story_assets/` — historical PDF crops and Mermaid renders
- `source_pack/v3-architecture-atlas/` — 11 Mermaid map sources/renders, scope note, pinned inventory, and evidence index
- `source_pack/room-definitions/RoomsandSpaces.md` — supplied room-definition summary used for the room-card correction; product contract, not runtime proof
- `diagram_inventory.json`, `diagram_index.csv` — combined 65-item catalog and provenance
- `wiki_claim_corrections.json`, `docs/WIKI_CLAIM_CORRECTIONS.md` — machine-readable and readable correction ledger
- `tests/` — acceptance checks for inventory, source paths, depth lenses, corrections, and static-host constraints
- `docs/` — source provenance and implementation notes
- `requirements-build.txt` — Python dependencies used only for rebuilding the historical PDF layer

## Rebuild

### Rebuild the integrated site from the bundled package data

The integrated builder uses only Python's standard library and the bundled source pack; the original PDF is not required:

```bash
python3 build_integrated_story.py
python3 -m unittest discover -s tests -v
```

### Refresh the historical Master Wiki layer

The source PDF is not included. To refresh its 54 visuals, provide your own `GestaltView_Master_Wiki_v4.0.pdf`, then rerun the integration builder afterward:

```bash
python3 -m pip install -r requirements-build.txt
python3 build_story_artifact.py /path/to/GestaltView_Master_Wiki_v4.0.pdf
python3 build_integrated_story.py
python3 -m unittest discover -s tests -v
```

The first builder regenerates the historical 54-item layer and temporarily writes a 54-item entry page. The second restores the integrated 65-item inventory and final static page. `manus-render-diagram` is needed only for re-rendering the two historical Mermaid snippets; the v3 maps' PNGs are already bundled.

## Source boundary

The v3 atlas is limited to implemented code and checked-in configuration at `03284ea`. Source presence does not prove successful runtime execution, environment configuration, live deployment, or measured performance. The correction ledger explicitly distinguishes verified paths, absent paths at that commit, guidance/examples, and unresolved operational claims. No Vision Blueprint or future design-intent material is presented as implemented behavior. The bundled room-definition summary is a user-supplied product contract, not evidence that the rebuilding Dynamic Inner World page is already implemented.

## Rights and publication

No open-source license is assigned by this package. Before public hosting or redistribution, confirm that you have the necessary rights for the wiki content and derived visual crops. See [`LICENSE-NOTICE.md`](LICENSE-NOTICE.md).
