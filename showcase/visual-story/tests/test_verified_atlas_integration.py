import csv
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "diagram_inventory.json"
ARTIFACT = ROOT / "index.html"
CORRECTIONS = ROOT / "wiki_claim_corrections.json"
EVIDENCE_INDEX = ROOT / "source_pack/v3-architecture-atlas/evidence-index.csv"


class VerifiedAtlasIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
        cls.items = cls.inventory["items"]
        cls.runtime_items = [item for item in cls.items if item.get("kind") == "runtime_map"]
        cls.legacy_items = [item for item in cls.items if item.get("kind") != "runtime_map"]

    def test_integrated_inventory_preserves_legacy_and_adds_runtime_lane(self):
        self.assertEqual(len(self.legacy_items), 54)
        self.assertEqual(len(self.runtime_items), 11)
        self.assertEqual(self.inventory["counts"]["total"], 65)
        self.assertEqual(self.inventory["source_layer_counts"], {"master_wiki_v4": 54, "v3_runtime": 11})
        self.assertEqual(
            (sum(item["kind"] == "curated" for item in self.legacy_items),
             sum(item["kind"] == "captioned_figure" for item in self.legacy_items),
             sum(item["kind"] == "mermaid_source" for item in self.legacy_items)),
            (13, 39, 2),
        )

    def test_every_runtime_map_has_source_snapshot_assets_and_three_depths(self):
        ids = [item["id"] for item in self.runtime_items]
        self.assertEqual(len(set(ids)), 11)
        for item in self.runtime_items:
            with self.subTest(map=item.get("id")):
                self.assertEqual(item["source_layer"], "v3_runtime")
                self.assertEqual(item["source_commit"], "03284ea")
                self.assertTrue(item["map_id"].startswith(("01-", "02-", "03-", "04-", "05-", "06-", "07-", "08-", "09-", "10-", "11-")))
                self.assertTrue((ROOT / item["source_map_path"]).is_file())
                self.assertTrue((ROOT / item["asset_path"]).is_file())
                self.assertTrue(item["source_ref"].strip())
                for depth in ("orientation", "system", "architecture"):
                    self.assertTrue(item["explanations"][depth].strip())

    def test_correction_ledger_is_line_cited_and_links_to_runtime_evidence(self):
        self.assertTrue(CORRECTIONS.is_file(), "correction ledger JSON has not been built")
        self.assertTrue(EVIDENCE_INDEX.is_file(), "pinned v3 evidence index is missing")
        ledger = json.loads(CORRECTIONS.read_text(encoding="utf-8"))
        with EVIDENCE_INDEX.open(encoding="utf-8", newline="") as handle:
            evidence_ids = {row["claim_id"] for row in csv.DictReader(handle)}
        runtime_map_ids = {item["map_id"] for item in self.runtime_items}
        self.assertGreaterEqual(len(ledger["entries"]), 6)
        for entry in ledger["entries"]:
            with self.subTest(correction=entry.get("id")):
                self.assertTrue(entry["wiki_lines"])
                self.assertTrue(all(isinstance(line, int) and line > 0 for line in entry["wiki_lines"]))
                self.assertTrue(entry["claim"].strip())
                self.assertTrue(entry["correction"].strip())
                self.assertIn(entry["disposition"], {"corrected", "qualified", "not established"})
                self.assertTrue(entry["source_paths"])
                self.assertTrue(all(path.get("path") for path in entry["source_paths"]))
                if entry["evidence_ids"]:
                    self.assertTrue(set(entry["evidence_ids"]).issubset(evidence_ids))
                self.assertTrue(set(entry["related_map_ids"]).issubset(runtime_map_ids))

    def test_static_story_exposes_runtime_lane_and_relevant_correction_callouts(self):
        html = ARTIFACT.read_text(encoding="utf-8")
        self.assertTrue(bool(re.search(r"Runtime maps — checked against v3 source", html)))
        self.assertTrue(bool(re.search(r"Claim correction", html)))
        self.assertIn("03284ea", html)
        self.assertIn("items.length", html)
        self.assertIsNone(re.search(r'<script\b[^>]*\bsrc\s*=\s*["\']https?://', html, re.I))
        self.assertIsNone(re.search(r'<img\b[^>]*\bsrc\s*=\s*["\']https?://', html, re.I))


if __name__ == "__main__":
    unittest.main()
