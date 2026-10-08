#!/usr/bin/env python3
"""Integrate the pinned v3 runtime atlas into the offline wiki visual story."""
from __future__ import annotations

import base64
import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
COMMIT = "03284ea"
SOURCE_PACK = Path("source_pack/v3-architecture-atlas")
MAPS_DIR = SOURCE_PACK / "maps"
RENDERED_DIR = SOURCE_PACK / "rendered"
EVIDENCE_INDEX = SOURCE_PACK / "evidence-index.csv"
CORRECTIONS_PATH = Path("wiki_claim_corrections.json")
INVENTORY_PATH = Path("diagram_inventory.json")
TEMPLATE_PATH = Path("story_template.html")
ARTIFACT_PATH = Path("index.html")
CSV_INDEX_PATH = Path("diagram_index.csv")
CORRECTIONS_MD_PATH = Path("docs/WIKI_CLAIM_CORRECTIONS.md")

RUNTIME_CHAPTER = {
    "id": "v3_runtime",
    "title": "Runtime maps — checked against v3 source",
    "story_title": "What the checked-in code can show",
    "dek": (
        "These maps follow executable code and configuration at commit 03284ea. "
        "A checked-in path is evidence about that snapshot—not proof of a live "
        "deployment, configured secrets, or successful production behavior."
    ),
}

CSV_FIELDS = [
    "id", "kind", "type", "chapter", "title", "caption", "section", "pdf_page",
    "source_ref", "source_form", "confidence", "confidence_note", "part_labels",
    "asset_path", "mermaid_source_file", "source_layer", "source_commit", "map_source",
    "evidence_keys", "correction_ids",
]


def extract_section(markdown: str, heading: str) -> str:
    """Return a Markdown heading section, stopping at the next same-level heading."""
    lines = markdown.splitlines()
    start = None
    level = None
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index + 1
            level = len(line) - len(line.lstrip("#"))
            break
    if start is None or level is None:
        return ""
    collected: list[str] = []
    for line in lines[start:]:
        stripped = line.lstrip()
        if stripped.startswith("#"):
            heading_level = len(stripped) - len(stripped.lstrip("#"))
            if heading_level <= level:
                break
        collected.append(line)
    return "\n".join(collected).strip()


def clean_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^\s{0,3}#{1,6}\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\s*\n\s*", " ", text)
    return re.sub(r"\s{2,}", " ", text).strip()


def evidence_keys(markdown: str) -> list[str]:
    body = extract_section(markdown, "### Evidence keys")
    found: set[str] = set()
    for match in re.finditer(r"\bE(\d{2})(?:[–-]E(\d{2}))?\b", body):
        first, last = match.group(1), match.group(2)
        if last:
            found.update(f"E{number:02d}" for number in range(int(first), int(last) + 1))
        else:
            found.add(f"E{first}")
    return sorted(found, key=lambda value: int(value[1:]))


def extract_matching_section(markdown: str, pattern: str) -> str:
    for line in markdown.splitlines():
        if re.match(pattern, line.strip()):
            return extract_section(markdown, line.strip())
    return ""


def map_title(markdown: str, map_id: str) -> str:
    match = re.search(r"(?m)^#\s+\d{2}\s+[—–-]\s+(.+?)\s*$", markdown)
    return match.group(1).strip() if match else map_id.replace("-", " ").title()


def source_map_ids(map_paths: list[Path]) -> set[str]:
    return {path.stem for path in map_paths}


def build_runtime_items(root: Path, corrections: dict[str, Any]) -> list[dict[str, Any]]:
    map_paths = sorted(
        path for path in MAPS_DIR.glob("[0-9][0-9]-*.md")
        if path.name[:2] in {f"{number:02d}" for number in range(1, 12)}
    )
    if len(map_paths) != 11:
        raise RuntimeError(f"Expected 11 runtime maps in {root / MAPS_DIR}; found {len(map_paths)}")
    known_maps = source_map_ids(map_paths)
    entries = corrections.get("entries", [])
    for entry in entries:
        unknown = set(entry.get("related_map_ids", [])) - known_maps
        if unknown:
            raise RuntimeError(f"Correction {entry.get('id')} refers to unknown map IDs: {sorted(unknown)}")

    items: list[dict[str, Any]] = []
    for order, path in enumerate(map_paths, start=1):
        markdown = path.read_text(encoding="utf-8")
        map_id = path.stem
        title = map_title(markdown, map_id)
        plain = clean_markdown(extract_section(markdown, "## Plain-language"))
        product = clean_markdown(extract_section(markdown, "## Product/system"))
        evidence = clean_markdown(extract_section(markdown, "### Evidence keys"))
        boundaries = clean_markdown(extract_matching_section(markdown, r"##\s+Boundaries\b"))
        if not plain or not product or not evidence or not boundaries:
            raise RuntimeError(f"Map {path.name} is missing a required reader-depth or evidence section")

        source_map_path = (SOURCE_PACK / "maps" / path.name).as_posix()
        asset_path = (SOURCE_PACK / "rendered" / f"{map_id}.png").as_posix()
        if not (root / asset_path).is_file():
            raise FileNotFoundError(root / asset_path)
        related_corrections = [
            {
                "id": entry["id"],
                "category": entry["category"],
                "wiki_lines": entry["wiki_lines"],
                "claim": entry["claim"],
                "correction": entry["correction"],
                "disposition": entry["disposition"],
                "source_paths": entry["source_paths"],
                "evidence_ids": entry.get("evidence_ids", []),
            }
            for entry in entries
            if map_id in entry.get("related_map_ids", [])
        ]
        items.append({
            "id": f"runtime-{map_id}",
            "kind": "runtime_map",
            "kind_label": "Code-verified runtime map",
            "source_layer": "v3_runtime",
            "source_form": "Mermaid source map rendered from the manually traced v3 architecture atlas",
            "source_commit": COMMIT,
            "source_map_path": source_map_path,
            "evidence_index_path": (SOURCE_PACK / "evidence-index.csv").as_posix(),
            "map_id": map_id,
            "evidence_keys": evidence_keys(markdown),
            "evidence_status": "Checked against the repository snapshot; not a live deployment check",
            "confidence": "high",
            "confidence_note": "Source-traced at the pinned commit; deployment state and environment-specific behavior remain outside this map.",
            "page": None,
            "title": title,
            "caption": f"Runtime map from GestaltView-v3 at {COMMIT}.",
            "section": "Code-verified v3 runtime atlas",
            "chapter_id": RUNTIME_CHAPTER["id"],
            "chapter_title": RUNTIME_CHAPTER["title"],
            "source_ref": f"GestaltView-v3 source snapshot · {COMMIT} · {source_map_path}",
            "anchor": "Source map and claim-to-source evidence index are included in this package",
            "context": boundaries,
            "context_label": "Runtime boundary and caveat",
            "asset_path": asset_path,
            "alt_text": f"Mermaid architecture map: {title}, traced against GestaltView-v3 commit {COMMIT}.",
            "featured": False,
            "curated_order": 1000 + order,
            "explanations": {
                "orientation": plain,
                "system": product,
                "architecture": (
                    f"Engineering view: follow the E-labels in this diagram. The included evidence index maps "
                    f"those keys to source paths, symbols or line ranges, evidence type, confidence, and scope notes. "
                    f"Evidence notes: {evidence} Boundary: {boundaries}"
                ),
            },
            "claim_corrections": related_corrections,
        })
    return items


def render_corrections_markdown(corrections: dict[str, Any]) -> str:
    lines = [
        "# Deep Wiki claim corrections",
        "",
        f"**Wiki snapshot:** `{corrections['source_document']}` ({corrections['source_snapshot_date']})  ",
        f"**Runtime baseline:** GestaltView-v3 `{corrections['baseline_commit']}`  ",
        "**Status:** Source-checked against the pinned repository snapshot; this is not a live deployment audit.",
        "",
        "The correction entries below keep documentation claims separate from implemented code paths, checked-in configuration, and measured production behavior.",
        "",
    ]
    for entry in corrections["entries"]:
        wiki_lines = ", ".join(str(number) for number in entry["wiki_lines"])
        lines.extend([
            f"## {entry['category']} — `{entry['id']}`",
            "",
            f"**Deep Wiki lines:** {wiki_lines}  ",
            f"**Disposition:** {entry['disposition']}",
            "",
            f"**Wiki claim:** {entry['claim']}",
            "",
            f"**Source-checked correction:** {entry['correction']}",
            "",
            "**Repository source references:**",
        ])
        for source in entry["source_paths"]:
            details = source.get("line_range") or source.get("finding", "")
            lines.append(f"- `{source['path']}`" + (f" — {details}" if details else ""))
        if entry.get("evidence_ids"):
            lines.append(f"- Atlas evidence IDs: {', '.join(entry['evidence_ids'])}")
        lines.extend([f"**Related maps:** {', '.join(entry['related_map_ids'])}", ""])
    lines.extend([
        "## Reading boundary",
        "",
        "Presence in source or configuration establishes a repository-level declaration, not successful execution or live deployment. Absence is scoped to commit `03284ea`; it is not a claim about other repositories or private infrastructure.",
        "",
    ])
    return "\n".join(lines)


def write_csv_index(root: Path, items: list[dict[str, Any]]) -> None:
    with (root / CSV_INDEX_PATH).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for item in items:
            writer.writerow({
                "id": item.get("id", ""),
                "kind": item.get("kind", ""),
                "type": item.get("kind_label", ""),
                "chapter": item.get("chapter_title", ""),
                "title": item.get("title", ""),
                "caption": item.get("caption", ""),
                "section": item.get("section", ""),
                "pdf_page": item.get("page") if item.get("page") is not None else "",
                "source_ref": item.get("source_ref", ""),
                "source_form": item.get("source_form", ""),
                "confidence": item.get("confidence", ""),
                "confidence_note": item.get("confidence_note", ""),
                "part_labels": "; ".join(part.get("label", "") for part in item.get("parts", [])),
                "asset_path": item.get("asset_path", ""),
                "mermaid_source_file": item.get("source_map_path", item.get("mermaid_source_file", "")),
                "source_layer": item.get("source_layer", "master_wiki_v4"),
                "source_commit": item.get("source_commit", ""),
                "map_source": item.get("source_map_path", ""),
                "evidence_keys": "; ".join(item.get("evidence_keys", [])),
                "correction_ids": "; ".join(note["id"] for note in item.get("claim_corrections", [])),
            })


def embed_for_page(root: Path, items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    payload_items: list[dict[str, Any]] = []
    for item in items:
        payload_item = dict(item)
        asset = root / item["asset_path"]
        if not asset.is_file():
            raise FileNotFoundError(asset)
        mime = "image/png" if asset.suffix.lower() == ".png" else "image/jpeg"
        payload_item["image_data"] = f"data:{mime};base64," + base64.b64encode(asset.read_bytes()).decode("ascii")
        payload_items.append(payload_item)
    return payload_items


def integrate(root: Path = ROOT) -> dict[str, Any]:
    root = root.resolve()
    inventory_path = root / INVENTORY_PATH
    template_path = root / TEMPLATE_PATH
    if not inventory_path.is_file():
        raise FileNotFoundError(f"Legacy inventory not found: {inventory_path}")
    if not template_path.is_file():
        raise FileNotFoundError(f"HTML template not found: {template_path}")
    evidence_path = root / EVIDENCE_INDEX
    if not evidence_path.is_file():
        raise FileNotFoundError(f"Pinned atlas evidence index not found: {evidence_path}")

    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
    corrections = json.loads((root / CORRECTIONS_PATH).read_text(encoding="utf-8"))
    if corrections.get("baseline_commit") != COMMIT:
        raise RuntimeError(f"Correction ledger must match baseline {COMMIT}")

    legacy_items = [item for item in inventory["items"] if item.get("kind") != "runtime_map"]
    for item in legacy_items:
        item["source_layer"] = "master_wiki_v4"
        item.pop("image_data", None)
    if len(legacy_items) != 54:
        raise RuntimeError(f"Expected 54 preserved wiki visuals, found {len(legacy_items)}")

    runtime_items = build_runtime_items(root, corrections)
    items = legacy_items + runtime_items
    if len({item["id"] for item in items}) != len(items):
        raise RuntimeError("Item IDs are not unique after integration")
    chapters = [chapter for chapter in inventory["chapters"] if chapter.get("id") != RUNTIME_CHAPTER["id"]]
    chapters.append(RUNTIME_CHAPTER)

    counts = dict(inventory.get("counts", {}))
    counts.update({"total": len(items), "runtime_maps": len(runtime_items)})
    inventory["counts"] = counts
    inventory["source_layer_counts"] = {"master_wiki_v4": len(legacy_items), "v3_runtime": len(runtime_items)}
    inventory["source_baselines"] = {
        "master_wiki_v4": "GestaltView_Master_Wiki_v4.0.pdf (source PDF not included)",
        "v3_runtime": COMMIT,
    }
    notes = inventory.setdefault("inventory_notes", [])
    runtime_note = "The 11 runtime maps are source-traced to v3 commit 03284ea; checked-in configuration is not proof of live deployment."
    if runtime_note not in notes:
        notes.append(runtime_note)
    inventory["chapters"] = chapters
    inventory["items"] = items

    inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_csv_index(root, items)
    (root / CORRECTIONS_MD_PATH).parent.mkdir(parents=True, exist_ok=True)
    (root / CORRECTIONS_MD_PATH).write_text(render_corrections_markdown(corrections), encoding="utf-8")

    template = template_path.read_text(encoding="utf-8")
    if "__APP_DATA__" not in template:
        raise RuntimeError("HTML template is missing the __APP_DATA__ placeholder")
    payload = json.dumps({"items": embed_for_page(root, items), "chapters": chapters}, ensure_ascii=False, separators=(",", ":"))
    payload = payload.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    html = template.replace("__APP_DATA__", payload)
    (root / ARTIFACT_PATH).write_text(html, encoding="utf-8")

    print(f"Integrated {len(legacy_items)} wiki visuals + {len(runtime_items)} runtime maps = {len(items)} total")
    print(f"Runtime source baseline: GestaltView-v3@{COMMIT}")
    print(f"Claim corrections: {len(corrections['entries'])}")
    print(f"Inventory: {inventory_path}")
    print(f"Static entrypoint: {root / ARTIFACT_PATH} ({(root / ARTIFACT_PATH).stat().st_size:,} bytes)")
    return inventory


def main() -> None:
    root = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else ROOT
    integrate(root)


if __name__ == "__main__":
    main()
