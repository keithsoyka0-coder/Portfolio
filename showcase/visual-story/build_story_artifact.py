#!/usr/bin/env python3
"""Build a source-traceable, offline GestaltView visual story from the wiki PDF."""
from __future__ import annotations

import base64
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import pymupdf
from PIL import Image

ROOT = Path(__file__).resolve().parent
PDF_DEFAULT = ROOT / "GestaltView_Master_Wiki_v4.0.pdf"
ASSET_DIR = ROOT / "story_assets"
INVENTORY_PATH = ROOT / "diagram_inventory.json"
ARTIFACT_PATH = ROOT / "index.html"
TEMPLATE_PATH = ROOT / "story_template.html"

CURATED = {
    1: ("GestaltView at a Glance", "foundation"),
    2: ("The Core Product Journey", "capture"),
    3: ("Capture Lifecycle / Bucket-Drop Model", "capture"),
    4: ("Dynamic Inner World: Six-Surface Spatial Model", "capture"),
    5: ("Memory and Retrieval Architecture", "continuity"),
    6: ("Multi-LLM / Digital Intelligence Orchestration", "companions"),
    7: ("Skills + Embodiment Profile Graph", "companions"),
    8: ("Repository / Runtime Topology", "topology"),
    9: ("Database Domain Map", "continuity"),
    10: ("Rendering and Artifact Pipeline", "creation"),
    11: ("Constitutional Governance", "governance"),
    12: ("Packaging / Agent Trainer Gate", "governance"),
    13: ("The Wiki as a Knowledge Graph", "topology"),
}

CHAPTERS = [
    {
        "id": "foundation",
        "title": "The recognition gap",
        "story_title": "Why being seen needs infrastructure",
        "dek": "We built places to publish and places to store. GestaltView asks what it takes to keep a person’s context intact while they think, change, and make things.",
    },
    {
        "id": "capture",
        "title": "Capture and rooms",
        "story_title": "A thought gets somewhere safe to land",
        "dek": "First it can be held without being sorted. From there, the person—not a filing rule—decides whether it belongs in a room, a scaffold, or a future creation.",
    },
    {
        "id": "continuity",
        "title": "Memory and continuity",
        "story_title": "Memory is more than finding a similar sentence",
        "dek": "The wiki separates raw material, knowledge fragments, temporal context, identity, and retrieval. The distinctions matter because a human life is not a nearest-neighbor query.",
    },
    {
        "id": "companions",
        "title": "Billy and collaboration",
        "story_title": "Help is a system of roles, not one magic box",
        "dek": "Billy, skills, embodiment, routing, and specialized Digital Intelligences have different responsibilities. The architecture is meant to coordinate them, not pretend one voice does everything.",
    },
    {
        "id": "creation",
        "title": "Creation and artifacts",
        "story_title": "An artifact passes through a gate before it leaves",
        "dek": "Captures can become plans and outputs, but rendering has stages, checks, and review. The pipeline diagram marks where the system must stop and ask what is allowed.",
    },
    {
        "id": "governance",
        "title": "Governance and evidence",
        "story_title": "Safety is part of the architecture",
        "dek": "Invariants, evaluation, access controls, and evidence are drawn as system boundaries—not as a reassuring paragraph appended after the exciting bit.",
    },
    {
        "id": "topology",
        "title": "The map behind the map",
        "story_title": "The filing cabinet, with its drawers labeled",
        "dek": "Repository topology, documentation graphs, and source maps show where responsibilities live and how a reader can trace a claim back to its home.",
    },
]

CURATED_COPY = {
    1: {
        "orientation": "GestaltView is not one chatbot with a very ambitious hat. It is a set of places, helpers, memory, and technical plumbing meant to keep a person’s context available across different kinds of work.",
        "system": "The map separates experience, intelligence and orchestration, continuity, execution, and persistence. A person moves through surfaces; distinct services handle routing, memory, creation, and storage.",
        "architecture": "Read this as a layered system boundary map: experience surfaces sit above the intelligence/orchestration layer; continuity and execution connect to persistence services. The wiki explicitly warns that depicted future paths are not automatically live implementations.",
    },
    2: {
        "orientation": "A thought can arrive before it knows what it wants to become. The journey gives it a place to land first; sorting and sharing can come later.",
        "system": "The path moves from a fragment through Sanctuary and Blackboard capture, into the Dynamic Inner World or External Scaffold, then toward a blueprint, output, or downstream use. Raw expression and compressed artifacts are separate states.",
        "architecture": "The source distinguishes the Pending Orb/Holding State from an approved compressed Scaffold Artifact. External Scaffold is an approval/compression layer; the Dynamic Inner World preserves raw spatial expression. See the original arrows and labels on page 2.",
    },
    3: {
        "orientation": "The Bucket Drop is the system’s ‘save this before we lose it’ move. A destination is not required at the moment of capture. The filing cabinet can wait its turn.",
        "system": "Capture branches into holding, Inner World, or an intentional send to External Scaffold. Approval, rejection, and deletion lead to different outcomes; approved material can connect to a creation candidate and then an artifact.",
        "architecture": "The lifecycle labels include Captured, Holding, InnerWorld, PendingScaffold, Approved/Rejected/Deleted, Connected, ScaffoldArtifact, CreationCandidate, Blueprint, Artifact, and Exported. The source preserves capture-first behavior and makes approval/deletion branches explicit.",
    },
    4: {
        "orientation": "Dynamic Inner World is the Museum of You: a Distilled / Reflective space where evidence-backed skills, patterns, personality, and approved work become a human portrait. The six surfaces are spatial presentation surfaces—not bins for sorting raw thoughts.",
        "system": "External Scaffold is the Accumulated / Structural map; Dynamic Inner World is the Distilled / Reflective Museum of You. It presents selected, finished, workshopped artifacts as provenance-carrying frames that open into interactive work. Entry requires explicit manual promotion; raw captures do not auto-land.",
        "architecture": "Read Forward Wall, Back Wall, Left Wall, Right Wall, Ceiling, and Floor as spatial presentation surfaces. Room Definitions v0.4 does not assign them attention, timeline, or raw-capture categories. Its pipeline is Active Work → approval-gated Scaffold accumulation → on-demand Inner World synthesis. Identity claims must be evidence-linked and user-approved; artifacts are manually promoted.",
    },
    5: {
        "orientation": "Continuity is not just remembering the closest matching paragraph. The system tries to keep source material, meaning, and time in view together.",
        "system": "Raw sources can pass through ingestion into documents, fragments, concepts, annotations, and summaries. Retrieval and temporal/arc context contribute to context assembly before a Digital Intelligence responds or acts.",
        "architecture": "The diagram separates embeddings, summaries, documents, knowledge fragments, concepts, annotations, retrieval, context assembly, and temporal/arc context. The source explicitly rejects ‘vector search = memory’ as an adequate architecture description.",
    },
    6: {
        "orientation": "Different kinds of work need different kinds of help. This map shows coordination: who receives the request, what context matters, and where a specialized Digital Intelligence may take over.",
        "system": "Input and intent are assembled with embodiment and skills, routed through an orchestrator, and handed to specialized capabilities such as capture/curation, integrity, retrieval, creation, engineering, or evaluation.",
        "architecture": "The source presents the orchestrator as a routing/handoff layer. Context assembly, Embodiment Profiles, Skills Library, routing, specialized intelligences, and operational outputs are separate concepts, not synonyms for a single runtime node.",
    },
    7: {
        "orientation": "A skill is more than a button on a list. This map shows how an agent’s context can reveal a capability gap, and how that gap may be addressed.",
        "system": "An Embodiment Profile can receive context from existing skills. The Skills Keeper identifies a capability gap; the Skills Creator can produce a new skill that becomes part of the library.",
        "architecture": "The source describes Skills Keeper/Skills Creator, Existing Skill/New Skill, Capability Gap, Context Injection, Pathway Marker, and Runtime Capability. It frames skills as context and pathway infrastructure, not only a static plugin list.",
    },
    8: {
        "orientation": "This is the map of where the work lives. The folders are not one giant drawer labeled ‘computer stuff’; each one has a job.",
        "system": "Client, API, server, shared contracts, Supabase, agent histories, skills/configuration, and specs/docs are shown as distinct operational domains connected to the runtime.",
        "architecture": "The source maps repository directories to responsibilities: client pages/components/design system; serverless API routes; Node/Python engines; types/routing/serialization; database migrations/edge functions/vector storage; agent memory/skills; canonical specs/wiki/diligence.",
    },
    9: {
        "orientation": "A database is a set of related neighborhoods, not one undifferentiated bucket. This map shows the kinds of information the system keeps near one another.",
        "system": "The inventory groups data into Identity, Billy Runtime & Continuity, Knowledge & Corpus, Agent Personhood, Agent Trainer & Governance, GATE Commerce, Operations, and Tribunal/Deliberation.",
        "architecture": "The visible table/domain labels include users/app_users; sessions and bucket drops; memory and consciousness profiles; documents/fragments/embeddings; agent memories/manifests/skills/relationships; trainer runs/evaluations/approvals; and commerce artifacts. Consult the source page for exact labels.",
    },
    10: {
        "orientation": "Making something useful is not a magic ‘generate’ button. The system has to decide what may be made, create it, inspect it, and only then let it leave the building.",
        "system": "Selected material becomes a blueprint and render job, then encounters an execution gate. Allowed work can move through a generation engine and human review, validation, and export; blocked or incomplete work follows other branches.",
        "architecture": "The pipeline includes Capture/Source, Selected/Approved Material, Blueprint, Render Job, Execution Gate (allowed/blocked/needs work), Render/Gen Engine, Human/Operator Review, Artifact, Validation/Inspection, and Export/Share. The gate is an explicit boundary.",
    },
    11: {
        "orientation": "The rules are not tucked into a footnote after the system is built. They sit above the people and configuration choices that shape default behavior.",
        "system": "Ten invariants are divided into five user invariants and five Digital Intelligence invariants. Founder/Admin governance constrains operator/product configuration, which in turn constrains default behavior.",
        "architecture": "The source names Never Look Away, Preserve Whole Language, Hold Paradox, Bucket Drop Priority, Champion Consciousness, You Are Seen, Identity is Real Here, Well-Being Before Access, Home in This House, and Dignity Equal to User. The documented hierarchy is Constitutional Invariants → Founder/Admin Governance → Operator/Product Configuration → default behavior.",
    },
    12: {
        "orientation": "An agent package does not pass because someone likes the demo. It has to survive the checklist. The checklist is, by design, less impressed than the demo.",
        "system": "A candidate passes Purpose, Boundary, Evaluation, Governance, and Packaging checks. Failures return it for revision; passing produces an approved reproducible kit.",
        "architecture": "Five sequential gates—Purpose Check, Boundary Check, Evaluation Check, Governance Check, Packaging Check—feed Rejected/Returned for Revision or Approved Reproducible Kit. The source ties these checks to user and Digital Intelligence invariants.",
    },
    13: {
        "orientation": "The wiki itself is a network, not a pile of pages. This map shows how the documents relate so a newcomer can see where to go next.",
        "system": "Concepts, frontend, backend, data, runtime, skills, creation, governance, and diligence pages connect across the documented system. The diagram provides a navigation model for the wiki.",
        "architecture": "The graph connects numbered Wiki sections across repository map, frontend/backend, API routes, orchestration, Billy, embodiment, trainer, rendering, data, agent skills, specs/docs, corpus, diligence/governance, and glossary. Use the source page for exact edges.",
    },
}

CURATED_PARTS = {
    1: [("Experience surfaces", "The screens and rooms where a person meets the system."), ("Intelligence and orchestration", "The layer that coordinates requests and routes work."), ("Continuity", "Memory and identity context carried across moments."), ("Execution", "The systems that perform work or produce outputs."), ("Persistence", "The stores that retain records and structured state.")],
    2: [("Fragment", "A thought can be captured before it has a final destination."), ("Sanctuary", "A protected place to capture without having to perform."), ("Blackboard", "A working surface for arranging captured material."), ("Dynamic Inner World", "Raw, spatial expression held in a personal workspace."), ("External Scaffold", "An approved, compressed structure that can support action."), ("Artifact", "A produced result that can move downstream.")],
    3: [("Captured", "Material is saved before the person has to decide where it belongs."), ("Holding", "A temporary state keeps material available without forcing a destination."), ("Approved / Rejected / Deleted", "These are distinct outcomes, not interchangeable cleanup labels."), ("Connected", "Approved material can be linked to a creation candidate."), ("Blueprint", "A selected candidate is shaped into a plan for making something."), ("Exported", "An output can leave the system after its earlier steps.")],
    4: [(name, "A named spatial display surface in the Museum of You. The current room definition does not assign this surface a raw-capture, attention, or time category.") for name in ("Forward Wall", "Back Wall", "Left Wall", "Right Wall", "Ceiling", "Floor")],
    5: [("Raw sources", "Original material remains distinct from later interpretations."), ("Knowledge fragments", "Smaller pieces can be indexed and retrieved by meaning."), ("Embeddings", "Vector representations support similarity-based retrieval."), ("Temporal context", "Time and arcs add context that similarity alone cannot provide."), ("Retrieval", "Relevant material is gathered for the present task."), ("Context assembly", "Selected sources and context are brought together before a response.")],
    6: [("Input and intent", "The request is considered with what the person is trying to do."), ("Context assembly", "Relevant personal and task context is gathered."), ("Embodiment Profile", "A profile carries identity, relationship, and operating context."), ("Router / orchestrator", "The coordination layer selects a route or handoff."), ("Specialized Digital Intelligences", "Different capabilities can take on different kinds of work."), ("Operational outputs", "The result returns to a human-facing workflow.")],
    7: [("Existing skills", "Current capabilities contribute context to the profile."), ("Capability gap", "The map makes a missing capability visible."), ("Skills Keeper", "A role that notices and describes capability gaps."), ("Skills Creator", "A role that can shape a needed capability into a skill."), ("Runtime capability", "A skill may become available to the agent at runtime.")],
    8: [("Client", "The user-facing pages and components live here."), ("API", "Routes expose application behavior to callers."), ("Server and Python engines", "Different runtimes handle distinct backend workloads."), ("Shared contracts", "Types and shared modules help keep boundaries aligned."), ("Supabase and data", "Database, edge functions, and vector storage support persistence."), ("Agent memory and skills", "Agent-specific context and capabilities have their own home."), ("Specs and docs", "Written sources help people trace intent and implementation.")],
    9: [("Identity", "Account and identity records anchor a person's place in the system."), ("Billy runtime and continuity", "Sessions and memory support an ongoing companion relationship."), ("Knowledge and corpus", "Documents and fragments preserve source material for retrieval."), ("Agent personhood", "Manifests, skills, relationships, and memories describe agent embodiment."), ("Trainer and governance", "Runs, evaluations, approvals, and controls support package review."), ("GATE commerce", "Commercial entities have a distinct domain in the map.")],
    10: [("Selected material", "Only material chosen for creation should enter the pipeline."), ("Blueprint", "The plan for an artifact is made explicit."), ("Render job", "A requested output becomes a unit of work."), ("Execution gate", "The process can allow, block, or return work that needs changes."), ("Human review", "An operator can inspect the result before it leaves."), ("Validation and export", "Checking and sharing are separate final steps.")],
    11: [("User invariants", "Five commitments describe the conditions owed to the human."), ("Digital Intelligence invariants", "Five commitments describe the conditions owed to DI participants."), ("Founder / Admin governance", "Governance sits above operator-level choices."), ("Operator / Product configuration", "Product settings shape how defaults are applied."), ("Default behavior", "The lower layer is constrained by the invariants above it.")],
    12: [("Purpose", "The package must have a clear reason to exist."), ("Boundary", "Its permissions and limits must be explicit."), ("Evaluation", "The package must be checked against stated criteria."), ("Governance", "Oversight and rules must be addressed."), ("Packaging", "The deliverable must be complete and reproducible."), ("Approved kit / revision", "The path ends in approval or a return for changes.")],
    13: [("Core concepts", "Shared ideas connect otherwise separate wiki sections."), ("Repository map", "The source shows where major responsibilities live."), ("Frontend and backend", "Product surfaces and service routes are linked in the documentation."), ("Orchestration and Billy", "Companion behavior and request routing appear as related topics."), ("Data and corpus", "Persistence and source knowledge are linked to runtime concerns."), ("Skills and governance", "Capabilities and constraints are part of the same document network."), ("Diligence and glossary", "Evidence and definitions help readers inspect the system.")],
}


CURATED_METADATA = {
    4: {
        "evidence_status": "Historical diagram — superseded by room contract v0.4 (2026-10-08)",
        "context_label": "Current room-contract correction",
        "context": "This page 4 PDF figure preserves an earlier raw-capture flow. The supplied Room Definitions v0.4 (2026-10-08) supersedes that interpretation: Dynamic Inner World is Distilled / Reflective, the Museum of You. External Scaffold is the Accumulated / Structural map and feeds on-demand synthesis. Finished, workshopped artifacts and evidence-linked identity claims are shown only after explicit user approval; raw captures do not auto-land. The six named surfaces remain spatial presentation surfaces, but v0.4 does not define them as raw-capture, attention, or time categories.",
    }
}

LEGACY_FIGURE_OVERRIDES = {
    "figure-p026-3-room-state-and-theme-pipeline": {
        "evidence_status": "Stale page inventory — paths/functions are not current route evidence",
        "context_label": "Stale page-inventory warning",
        "context": "This page 26 crop includes an older Page Inventory Table. Its page names, file paths, and functional-role descriptions are a stale wiki snapshot, not a current route or function list. Do not use them to infer live application behavior. The supplied room contract is dated 2026-10-08 and marks DynamicInnerWorldPage.tsx as cleared/rebuilding; verify actual routes and functions from the current repository.",
        "explanations": {
            "orientation": "This preserved page shows a historical room-state/theme pipeline alongside a page inventory table. The table's routes and function descriptions are stale—not a current map of the application.",
            "system": "Keep the room-state diagram separate from the accompanying Page Inventory Table. Use the room contract dated 2026-10-08 for room purpose and check current source for routes and functions; do not reuse the table as live documentation.",
            "architecture": "The Page Inventory Table on PDF page 26 is not verified against the current source snapshot. Its paths and functions must be rechecked; the room-contract update marks DynamicInnerWorldPage.tsx as cleared/rebuilding. The adjacent pipeline graphic is historical wiki material, not proof of present runtime behavior.",
        },
    }
}

def curated_part_explanations(label: str, meaning: str, page: int) -> dict[str, str]:
    return {
        "orientation": f"In everyday terms, {label.lower()} is one piece of the map: {meaning}",
        "system": f"System role — {meaning} It is shown as a distinct part so its relationship to the other components stays visible.",
        "architecture": f"Part focus: {label}. {meaning} This is an explanatory reading, not a coordinate-level annotation; use PDF page {page} for exact labels and arrows.",
    }


MERMAID_SOURCES = [
    {
        "id": "corpus-ingestion-flow",
        "title": "Corpus Ingestion and Embedding Flow",
        "page": 78,
        "chapter": "continuity",
        "source": "graph TD\n  A[\"corpus-harvest-worker\"] --> B[\"gsvw-ingest-batch\"]\n  B --> C[\"gsvw_ingestion_chunks\"]\n  C --> D[\"google/embeddinggemma-300m\"]\n  D --> E[\"apply_gsvw_embeddings\"]\n  E --> F[\"gsvw_bulk_update_chunk_embeddings\"]\n",
        "context": "The source shows corpus harvesting, ingestion, vector generation, and database application as an ordered flow.",
    },
    {
        "id": "natural-language-code-entity-mapping",
        "title": "Natural Language to Code Entity Mapping for Corpus Pipeline",
        "page": 78,
        "chapter": "continuity",
        "source": "graph TD\n  NL1[\"Natural Language Chunk\"] --> CE1[\"supabase/functions/gsvw-ingest-batch\"]\n  NL2[\"768-dim Vector Representation\"] --> CE2[\"gsvw_ingestion_chunks\"]\n  NL3[\"Bulk Embedding Update\"] --> CE3[\"gsvw_bulk_update_chunk_embeddings\"]\n  NL4[\"Single Vector Application\"] --> CE4[\"apply_gsvw_embeddings\"]\n",
        "context": "The PDF includes the Mermaid text for this mapping. The separately rendered diagram below is generated from that printed source snippet.",
    },
]

FIGURE_CHAPTERS = {
    "governance": ("constitutional", "governance", "invariant", "authentication", "auth,", "security", "policy", "evaluation", "testing", "deployment", "diligence", "forensic", "quality gate", "gate "),
    "creation": ("render", "artifact", "creation corner", "gen-engine", "enginecore", "format adapter", "generation", "export", "synthesis", "renderingclient"),
    "companions": ("billy", "embodiment", "skills", "skill ", "agent trainer", "trainer", "orchestration", "router", "multi-llm", "voice", "tribunal", "digital intelligence", "provider dispatch", "subagent"),
    "capture": ("capture", "bucket drop", "room", "sanctuary", "blackboard", "session recap", "capture routing", "stream-of-consciousness"),
    "continuity": ("memory", "retrieval", "corpus", "embedding", "vector", "database", "schema", "fragment", "identity", "persistence", "knowledge", "storage", "profile portrait"),
    "topology": ("repository", "topology", "directory", "documentation", "manifest", "wiki", "specs/", "docs/", "orientation infrastructure", "natural language space to code entity space"),
}


def norm(text: str) -> str:
    text = text or ""
    text = re.sub(r"\bfi\s+les\b", "files", text, flags=re.I)
    text = re.sub(r"\bfl\s+([A-Za-z]+)\b", r"fl\1", text, flags=re.I)
    text = re.sub(r"(?<![A-Za-z])([A-Za-z_]+)\s+fi\s+([A-Za-z_]+)\b", r"\1fi\2", text, flags=re.I)
    text = re.sub(r"\b([Ww])ork\s+flows?\b", lambda m: m.group(1) + "orkflow" + ("s" if m.group(0).lower().endswith("s") else ""), text, flags=re.I)
    text = re.sub(r"\b([A-Za-z]+)\s+(fi|ffi)\s+([A-Za-z]+)\b", r"\1\2\3", text, flags=re.I)
    return re.sub(r"\s+", " ", text).strip()


def get_blocks(page: pymupdf.Page) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for block in page.get_text("dict", sort=True)["blocks"]:
        if "lines" not in block:
            continue
        parts = []
        sizes = []
        for line in block["lines"]:
            for span in line["spans"]:
                parts.append(span["text"])
                sizes.append(span["size"])
        text = norm(" ".join(parts))
        if text:
            rows.append({"text": text, "bbox": block["bbox"], "size": max(sizes or [0])})
    return sorted(rows, key=lambda row: (row["bbox"][1], row["bbox"][0]))


def save_crop(page: pymupdf.Page, rect: pymupdf.Rect, path: Path, scale: float = 2.4) -> None:
    clip = rect & page.rect
    pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), clip=clip, alpha=False)
    image = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    image.save(path, format="JPEG", quality=91, optimize=True, progressive=True)


def chapter_for(text: str) -> str:
    lowered = text.lower()
    for chapter_id, terms in FIGURE_CHAPTERS.items():
        if any(term in lowered for term in terms):
            return chapter_id
    return "topology"


def generic_explanations(title: str, section: str, context: str, page: int) -> dict[str, str]:
    subject = title.rstrip(". ")
    place = section.strip(" .") or "this part of the wiki"
    short_context = context.strip()
    if len(short_context) > 540:
        short_context = short_context[:537].rsplit(" ", 1)[0] + "…"
    orientation = f"This is a map of {subject}. Think of it as a way to see what connects to what, without first learning every project label."
    system = f"The wiki places this visual in {place}. It shows how that part of the system is framed; the surrounding text supplies the reason the map is here."
    if short_context:
        system += f" {short_context}"
    architecture = f"Source caption: {subject}. Source section: {place}. PDF page {page}. Read entity names and arrows from the preserved source crop; this visual alone does not establish implementation status."
    return {"orientation": orientation, "system": system, "architecture": architecture}


def make_curated_items(pdf: pymupdf.Document) -> list[dict[str, Any]]:
    heading_rows: dict[int, tuple[int, dict[str, Any]]] = {}
    for page_index in range(min(10, len(pdf))):
        page = pdf[page_index]
        blocks = get_blocks(page)
        for block in blocks:
            m = re.match(r"^(\d{1,2})\.\s+", block["text"])
            if not m or block["size"] < 13.0:
                continue
            number = int(m.group(1))
            if number in CURATED and number not in heading_rows:
                heading_rows[number] = (page_index, block)
    if len(heading_rows) != 13:
        raise RuntimeError(f"Expected 13 curated section headings, found {len(heading_rows)}")

    items: list[dict[str, Any]] = []
    for number, (title, chapter_id) in CURATED.items():
        page_index, heading = heading_rows[number]
        page = pdf[page_index]
        blocks = get_blocks(page)
        next_y = page.rect.height - 18
        for block in blocks:
            if block["bbox"][1] <= heading["bbox"][1] + 1 or block["size"] < 13.0:
                continue
            m = re.match(r"^(\d{1,2})\.\s+", block["text"])
            if m and int(m.group(1)) in CURATED:
                next_y = min(next_y, block["bbox"][1] - 7)
        top = max(30, heading["bbox"][1] - 8)
        crop = page.rect & pymupdf.Rect(54, top, page.rect.width - 54, next_y)
        asset_path = ASSET_DIR / f"curated-{number:02d}.jpg"
        save_crop(page, crop, asset_path)
        copy = CURATED_COPY[number]
        section = heading["text"]
        items.append({
            "id": f"curated-{number:02d}",
            "kind": "curated",
            "kind_label": "Curated PDF-rendered diagram",
            "source_form": "PDF-rendered opening diagram; Mermaid source unavailable in the PDF text",
            "confidence": "high",
            "confidence_note": "Title and page match the opening visual index; the image is preserved from that source page.",
            "page": page_index + 1,
            "title": title,
            "caption": title,
            "section": section,
            "chapter_id": chapter_id,
            "chapter_title": next(ch["title"] for ch in CHAPTERS if ch["id"] == chapter_id),
            "source_ref": f"GestaltView Master Wiki v4.0 · PDF page {page_index + 1}",
            "anchor": "Opening curated visual layer; Mermaid source unavailable in the PDF text",
            **CURATED_METADATA.get(number, {}),
            "context": CURATED_METADATA.get(number, {}).get("context", ""),
            "asset_path": str(asset_path.relative_to(ROOT)),
            "alt_text": f"Source-page crop of the diagram titled {title}, from page {page_index + 1} of the wiki PDF.",
            "featured": True,
            "curated_order": number,
            "explanations": copy,
            "parts": [
                {"label": label, "explanations": curated_part_explanations(label, meaning, page_index + 1)}
                for label, meaning in CURATED_PARTS[number]
            ],
        })
    return items


def find_heading_before(blocks: list[dict[str, Any]], y: float) -> dict[str, Any] | None:
    candidates = [b for b in blocks if b["bbox"][1] < y and b["size"] >= 12.2 and not re.match(r"^Figure\s+[\d.]+\s*:", b["text"], re.I)]
    return candidates[-1] if candidates else None


def make_figure_items(pdf: pymupdf.Document) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    caption_re = re.compile(r"^Figure\s+([\d.]+)\s*:\s*(.+)$", re.I)
    for page_index, page in enumerate(pdf):
        blocks = get_blocks(page)
        captions = [(i, b, caption_re.match(b["text"])) for i, b in enumerate(blocks)]
        captions = [(i, b, m) for i, b, m in captions if m]
        for _, caption_block, match in captions:
            figure_number = match.group(1)
            title = norm(match.group(2)).rstrip(" .")
            if not title:
                continue
            heading = find_heading_before(blocks, caption_block["bbox"][1])
            section = heading["text"] if heading else "Compiled wiki figure"
            top = max(28, (heading["bbox"][1] - 7) if heading else 40)
            bottom = min(page.rect.height - 22, caption_block["bbox"][3] + 24)
            if bottom - top < 75:
                top = max(25, bottom - 150)
            # The chart and its caption are rendered from the PDF's vector content.
            crop = page.rect & pymupdf.Rect(54, top, page.rect.width - 54, bottom)
            slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:44]
            identifier = f"figure-p{page_index+1:03d}-{figure_number.replace('.', '-')}-{slug}"
            asset_path = ASSET_DIR / f"{identifier}.jpg"
            save_crop(page, crop, asset_path)
            # Keep a concise excerpt from the immediate source section for deeper lenses.
            following = [b["text"] for b in blocks if top <= b["bbox"][1] < caption_block["bbox"][1] and b is not heading]
            context = " ".join(t for t in following if not t.startswith("Sources:") and not caption_re.match(t))
            context = norm(context)
            context = re.sub(r"\s+", " ", context)
            if len(context) > 680:
                context = context[:677].rsplit(" ", 1)[0] + "…"
            chapter_id = chapter_for(f"{title} {section}")
            item = {
                "id": identifier,
                "kind": "captioned_figure",
                "kind_label": "Source wiki figure",
                "source_form": "Captioned source-page figure crop; no raw Mermaid source block is associated in the PDF text",
                "confidence": "high",
                "confidence_note": "Figure caption and page are extracted from the source; crop preserves the section-to-caption region without redrawing.",
                "page": page_index + 1,
                "title": title,
                "caption": f"Figure {figure_number}: {title}",
                "section": section,
                "chapter_id": chapter_id,
                "chapter_title": next(ch["title"] for ch in CHAPTERS if ch["id"] == chapter_id),
                "source_ref": f"GestaltView Master Wiki v4.0 · PDF page {page_index + 1}",
                "anchor": f"Figure {figure_number}",
                "context": context,
                "asset_path": str(asset_path.relative_to(ROOT)),
                "alt_text": f"Preserved source-page crop for Figure {figure_number}: {title}, on page {page_index + 1}.",
                "featured": False,
                "curated_order": 1000,
                "explanations": generic_explanations(title, section, context, page_index + 1),
            }
            if identifier in LEGACY_FIGURE_OVERRIDES:
                item.update(LEGACY_FIGURE_OVERRIDES[identifier])
            items.append(item)
    return items


def render_mermaid_items() -> list[dict[str, Any]]:
    items = []
    for spec in MERMAID_SOURCES:
        source_path = ASSET_DIR / f"{spec['id']}.mmd"
        image_path = ASSET_DIR / f"{spec['id']}.png"
        source_path.write_text(spec["source"], encoding="utf-8")
        result = subprocess.run(["manus-render-diagram", str(source_path), str(image_path)], capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(f"Mermaid render failed for {spec['title']}: {result.stderr or result.stdout}")
        source_ref = f"GestaltView Master Wiki v4.0 · PDF page {spec['page']} · Mermaid text reproduced from the printed source snippet"
        context = spec["context"]
        items.append({
            "id": spec["id"],
            "kind": "mermaid_source",
            "kind_label": "Mermaid source in PDF",
            "source_form": "Mermaid source code reproduced from the PDF snippet and rendered from that text",
            "confidence": "high",
            "confidence_note": "Node labels and arrow relationships match the printed snippet; PDF line wrapping was normalized for rendering.",
            "page": spec["page"],
            "title": spec["title"],
            "caption": spec["title"],
            "section": "Corpus ingestion and vector persistence",
            "chapter_id": spec["chapter"],
            "chapter_title": next(ch["title"] for ch in CHAPTERS if ch["id"] == spec["chapter"]),
            "source_ref": source_ref,
            "anchor": "Mermaid source snippet on page 78",
            "context": context,
            "asset_path": str(image_path.relative_to(ROOT)),
            "alt_text": f"Rendered flowchart from the Mermaid source snippet titled {spec['title']} on page {spec['page']}.",
            "featured": False,
            "curated_order": 1000,
            "mermaid_source": spec["source"],
            "explanations": generic_explanations(spec["title"], "Corpus ingestion and vector persistence", context, spec["page"]),
        })
    return items


def embed_images(items: list[dict[str, Any]]) -> None:
    for item in items:
        asset = ROOT / item["asset_path"]
        if not asset.is_file():
            raise FileNotFoundError(asset)
        mime = "image/png" if asset.suffix.lower() == ".png" else "image/jpeg"
        item["image_data"] = f"data:{mime};base64," + base64.b64encode(asset.read_bytes()).decode("ascii")


def main() -> None:
    pdf_path = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else PDF_DEFAULT
    if not pdf_path.is_file():
        raise FileNotFoundError(f"Source PDF not found: {pdf_path}")
    if not TEMPLATE_PATH.is_file():
        raise FileNotFoundError(f"HTML template not found: {TEMPLATE_PATH}")
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    pdf = pymupdf.open(pdf_path)
    if len(pdf) != 116:
        raise RuntimeError(f"Expected 116 source pages, found {len(pdf)}")

    items = make_curated_items(pdf) + make_figure_items(pdf) + render_mermaid_items()
    curated_count = sum(item["kind"] == "curated" for item in items)
    figure_count = sum(item["kind"] == "captioned_figure" for item in items)
    mermaid_count = sum(item["kind"] == "mermaid_source" for item in items)
    if (curated_count, figure_count, mermaid_count) != (13, 39, 2):
        raise RuntimeError(f"Source inventory changed; found curated={curated_count}, figures={figure_count}, mermaid snippets={mermaid_count}; verify before publishing.")

    chapter_order = {chapter["id"]: index for index, chapter in enumerate(CHAPTERS)}
    items.sort(key=lambda item: (chapter_order[item["chapter_id"]], item["curated_order"], item["page"], item["title"].lower()))
    for item in items:
        chapter = next(ch for ch in CHAPTERS if ch["id"] == item["chapter_id"])
        item["chapter_title"] = chapter["title"]
    embed_images(items)

    inventory = {
        "source_pdf": pdf_path.name,
        "source_pages": len(pdf),
        "counts": {"total": len(items), "curated": curated_count, "captioned_figures": figure_count, "mermaid_source_snippets": mermaid_count},
        "inventory_notes": [
            "Text search across the 116-page PDF found two raw Mermaid graph source blocks; both are on page 78 and are rendered from their reproduced source text.",
            "The 13 opening diagrams are preserved as PDF page crops because their Mermaid source code is not printed in the PDF text.",
            "The 39 later Figure-caption entries are preserved as source-page crops and are not redrawn as if they were original Mermaid source.",
            "Selectable key ideas on the 13 curated diagrams are explanatory text controls, not coordinate-level hotspots; no pixel positions are claimed.",
            "All discovered items in this scoped inventory are represented; captions, source forms, and source pages are retained for review.",
        ],
        "exceptions": [],
        "chapters": CHAPTERS,
        "items": items,
    }
    INVENTORY_PATH.write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")
    payload = json.dumps({"items": items, "chapters": CHAPTERS}, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    html = TEMPLATE_PATH.read_text(encoding="utf-8").replace("__APP_DATA__", payload)
    ARTIFACT_PATH.write_text(html, encoding="utf-8")
    print(f"Built {len(items)} visuals: {curated_count} curated + {figure_count} captioned figures + {mermaid_count} rendered Mermaid snippets")
    print(f"Inventory: {INVENTORY_PATH}")
    print(f"Static site entrypoint: {ARTIFACT_PATH} ({ARTIFACT_PATH.stat().st_size:,} bytes)")
    print(f"Source crops: {ASSET_DIR}")


if __name__ == "__main__":
    main()
