import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "diagram_inventory.json"
ARTIFACT = ROOT / "index.html"
TEMPLATE = ROOT / "story_template.html"


class StoryArtifactAcceptanceTests(unittest.TestCase):
    def test_room_flow_correction_and_stale_inventory_warning_are_present(self):
        inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
        items = {item["id"]: item for item in inventory["items"]}
        diw = items["curated-04"]
        diw_text = json.dumps(diw, ensure_ascii=False)
        self.assertIn("Historical diagram", diw.get("evidence_status", ""))
        self.assertIn("supersedes", diw["context"].lower())
        self.assertIn("Distilled / Reflective", diw_text)
        self.assertIn("manual promotion", diw_text.lower())
        self.assertIn("does not assign", diw_text.lower())
        self.assertNotIn("organize raw captures by their relationship", diw_text.lower())
        self.assertNotIn("attention and history", diw_text.lower())

        inventory_figure = items["figure-p026-3-room-state-and-theme-pipeline"]
        self.assertIn("stale", inventory_figure.get("evidence_status", "").lower())
        self.assertIn("not a current", inventory_figure["context"].lower())
        self.assertIn("route", inventory_figure["context"].lower())

        html = ARTIFACT.read_text(encoding="utf-8")
        self.assertIn("Historical diagram", html)
        self.assertIn("Stale page-inventory warning", html)

    def test_complete_source_mapped_story_artifact_exists(self):
        self.assertTrue(INVENTORY.is_file(), "diagram inventory has not been built")
        self.assertTrue(ARTIFACT.is_file(), "standalone story artifact has not been built")

        inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
        items = inventory["items"]
        self.assertGreaterEqual(len(items), 54)
        self.assertEqual(sum(item["kind"] == "curated" for item in items), 13)
        self.assertEqual(sum(item["kind"] == "captioned_figure" for item in items), 39)
        self.assertEqual(sum(item["kind"] == "mermaid_source" for item in items), 2)
        self.assertIn("inventory_notes", inventory)
        self.assertEqual(inventory["exceptions"], [])
        self.assertGreaterEqual(sum(bool(item.get("parts")) for item in items), 13)

        ids = set()
        textual_fields = []
        for item in items:
            self.assertTrue(item["id"])
            self.assertNotIn(item["id"], ids)
            ids.add(item["id"])
            if item["kind"] == "runtime_map":
                self.assertIsNone(item["page"])
                self.assertEqual(item["source_commit"], "03284ea")
            elif item["kind"] == "principle":
                self.assertIsNone(item["page"])
                self.assertEqual(item["source_layer"], "principles")
            else:
                self.assertGreaterEqual(item["page"], 1)
                self.assertLessEqual(item["page"], 116)
            self.assertTrue(item["title"].strip())
            self.assertTrue(item["source_ref"].strip())
            self.assertTrue(item["source_form"].strip())
            self.assertEqual(item["confidence"], "high")
            self.assertTrue(item["confidence_note"].strip())
            self.assertTrue(item["explanations"]["orientation"].strip())
            self.assertTrue(item["explanations"]["system"].strip())
            self.assertTrue(item["explanations"]["architecture"].strip())
            self.assertTrue((ROOT / item["asset_path"]).is_file())
            if item.get("parts"):
                self.assertTrue(all(all(part["explanations"].get(level) for level in ("orientation", "system", "architecture")) for part in item["parts"]))
            textual_fields.extend(item.get(key, "") for key in ("title", "section", "caption", "context"))

        story_text = "\n".join(textual_fields)
        for broken in ("De fi nitions", "fl ow", "pro fi "):
            self.assertNotIn(broken, story_text)

        mermaid_items = [item for item in items if item["kind"] == "mermaid_source"]
        mermaid = [item["mermaid_source"] for item in mermaid_items]
        self.assertEqual(len(mermaid), 2)
        self.assertTrue(all(source.startswith("graph TD") for source in mermaid))
        self.assertIn('NL2["768-dim Vector Representation"] --> CE2', mermaid[1])
        self.assertIn('NL3["Bulk Embedding Update"] --> CE3', mermaid[1])
        self.assertIn("Mermaid source unavailable", " ".join(item["source_form"] for item in items if item["kind"] == "curated"))

        html = ARTIFACT.read_text(encoding="utf-8")
        for expected in (
            "Get oriented",
            "Understand the system",
            "Explore the architecture",
            "Search the visual atlas",
            "Digital Intelligence",
            "prefers-reduced-motion",
            "const storyIndex = items.findIndex(item => item.id === id);",
            "const next = items[storyIndex + 1];",
            "explore-parts",
            "part-detail",
        ):
            self.assertIn(expected, html)
        self.assertNotIn('src="http', html, "artifact must not require remote assets")
        self.assertIn('rel="icon" href="data:image/svg+xml', TEMPLATE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
