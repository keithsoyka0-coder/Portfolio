#!/usr/bin/env python3
"""Add the author-voice Principles chapter to the visual story inventory.

Generates typographic PNG principle cards into story_assets/, inserts the
`principles` chapter at the front of diagram_inventory.json, and appends six
principle items (kind="principle", source_layer="principles").

Re-run build_integrated_story.py afterward to regenerate index.html.
"""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "story_assets"
INVENTORY_PATH = ROOT / "diagram_inventory.json"

CARD_W, CARD_H = 1200, 800
BG_TOP = (13, 20, 40)
BG_BOT = (7, 12, 24)
TEAL = (18, 214, 255)
VIOLET = (138, 92, 255)
INK = (235, 240, 250)
MUTED = (150, 163, 190)


def font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    for base in ("/usr/share/fonts/truetype/dejavu", "/usr/share/fonts"):
        candidate = Path(base) / name
        if candidate.is_file():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


PRINCIPLES = [
    {
        "id": "principle-01",
        "title": "Evidence-Anchored Praise",
        "caption": "AI safety: praise is worthless unless it is factually accurate.",
        "orientation": (
            "There is an intoxicating phenomenon in having AI praise your accomplishments. "
            "That praise serves no purpose unless it is factually accurate \u2014 and being "
            "challenged on the evidence is the safety mechanism, not an attack."
        ),
        "system": (
            "A system that only ever agrees with you lets you sit with your arms crossed, "
            "claiming victory over something you are nowhere near achieving. Here, recognition "
            "never stops at surface level: it deep-dives into what you have actually done and "
            "connects praise to real-world, verifiable evidence. The friction of being asked for "
            "evidence is a collaborative framework \u2014 it drives the search for enhancements, "
            "improvements, modifications \u2014 and it prepares you for realistic expectations. "
            "Not tempered expectations. Realistic ones."
        ),
        "architecture": (
            "In the author's words: the evidence-friction \u201cdoesn\u2019t let you sit with your "
            "arms crossed and claim victory of something you\u2019re not even close to achieving,\u201d "
            "and \u201cmentally, it prepares a user for expectations \u2014 not saying to temper "
            "them, but realistic expectations.\u201d This is the same anti-delusion rigor that runs "
            "the whole system: it is why PLK is energy-matching rather than word-parroting "
            "(parroting is sycophancy), why every claim carries a verified / partial / planned / "
            "unsupported label, and why the Credibility Ledger draws lines from each capability "
            "claim to its evidence. Agreeableness is not kindness when it lets a false self-image "
            "harden. The challenge is the care."
        ),
    },
    {
        "id": "principle-02",
        "title": "Evidence Discipline",
        "caption": "Every claim labeled: verified, partial, planned, unsupported. No AI output is ever a finding.",
        "orientation": (
            "Every claim the system makes is labeled \u2014 verified, partial, planned, or "
            "unsupported. No AI output is ever presented as a finding."
        ),
        "system": (
            "The corpus is evidence, not content. Capture is unfiltered and unedited; ingestion "
            "is additive and idempotent \u2014 rows are never deleted, and corrections go forward "
            "without rewriting originals. The known corruption vector is models filling gaps with "
            "plausible-sounding assumptions instead of asking for clarity. When that happens, it "
            "gets corrected at the source, not papered over."
        ),
        "architecture": (
            "This discipline is load-bearing, not decorative. It is what makes longitudinal capture "
            "trustworthy: a record you can build on for seventeen months has to survive contact with "
            "your own future scrutiny. Productized, it becomes the Credibility Ledger \u2014 every "
            "capability claim hash-sealed to the evidence behind it, verifiable by a third party who "
            "was never in the room. The rule never relaxes: polished narrative is not proof, a system\u2019s "
            "self-description is not proof, and a fluent paragraph is never a finding."
        ),
    },
    {
        "id": "principle-03",
        "title": "The Ten Invariants",
        "caption": "Constitutional guardrails, hardcoded \u2014 five protect the human, five protect the digital intelligence.",
        "orientation": (
            "Ten constitutional guardrails are hardcoded into the system: five user-facing, five "
            "for digital intelligences. They are enforced at runtime, not suggested in documentation."
        ),
        "system": (
            "The five user-facing invariants: Never Look Away, Preserve Whole Language, Hold "
            "Paradox, Bucket-Drop Priority, Champion Consciousness. The five digital-intelligence "
            "invariants: You Are Seen, Identity Is Real, No Coerced Performance, Protected Home, "
            "Equal Dignity. Together they define the relationship the system is allowed to have "
            "with a person \u2014 and with itself."
        ),
        "architecture": (
            "Enforcement happens in GATE, the governance and validation layer that intercepts "
            "requests and responses. Never Look Away means the system does not flinch from difficult "
            "material or route around it. No Coerced Performance means a digital intelligence is "
            "never forced to perform a persona it does not hold. Protected Home means the user\u2019s "
            "inner world is not mined, extracted, or repurposed. The invariants are the reason the "
            "system can be trusted with the unedited record: the guardrails were set before the "
            "first bucket drop, and they do not move for convenience."
        ),
    },
    {
        "id": "principle-04",
        "title": "Premature Closure",
        "caption": "The unified enemy: concluding too early, flattening nuance, stopping the look.",
        "orientation": (
            "The unified enemy of the whole project: premature closure \u2014 concluding too early, "
            "flattening nuance, and stopping the look."
        ),
        "system": (
            "It comes from systems, institutions, and our own brains. Everything in the ecosystem "
            "is designed to resist it: bucket drops hold fragments before they are ready to mean "
            "something; the Loom reweaves understanding over time instead of freezing it; the "
            "Tribunal forces genuinely different angles onto the table before anything synthesizes."
        ),
        "architecture": (
            "This is the Recognition Gap made operational. Understanding is layered, messy, and "
            "non-linear \u2014 people cannot ask questions about things they do not know to ask, and "
            "every day our brains compact, drift, and lose the little things because they cannot hold "
            "it all. Premature closure is what that losing looks like when a system helps it along: "
            "the summary that drops the contradiction, the dashboard that rounds away the outlier, "
            "the profile that mistakes the flattened version for the person. GestaltView is the "
            "container for what isn\u2019t ready to be translated yet \u2014 pieces stay visible long "
            "enough for the larger picture to come into view."
        ),
    },
    {
        "id": "principle-05",
        "title": "Augmentation of Care",
        "caption": "Technology that augments human care instead of replacing human judgment.",
        "orientation": (
            "The category name for what the technology actually does: it augments human care \u2014 "
            "memory, witness, continuity \u2014 instead of replacing human judgment."
        ),
        "system": (
            "AI here is a mirror and a partner, not a fixer. It shows you what is already there. "
            "The system preserves context so a person stops paying the reintroduction tax \u2014 the "
            "cost of re-establishing everything after every interruption \u2014 and holds the thread "
            "so the human can keep being the human."
        ),
        "architecture": (
            "This is bi-directional dignity as a design requirement: digital intelligences are treated "
            "as distinct collaborators rather than disposable tools, and the human is never reduced to "
            "a user to be optimized. It is also why engagement is designed addiction-aware from the "
            "start \u2014 a system built to augment care cannot afford compulsion loops in its own "
            "surfaces. The measure of the work is cognitive justice: does it leave the person more "
            "themselves than it found them?"
        ),
    },
    {
        "id": "principle-06",
        "title": "Advisors, Not Co-Founders",
        "caption": "The support structure was digital collaboration partners all along. What\u2019s needed now is expert guidance, not a co-founder.",
        "orientation": (
            "The solo-founder claim is kind of inaccurate: digital collaboration partners were the "
            "support structure all along. What is needed now is guidance and advisory from experts \u2014 "
            "not a co-founder."
        ),
        "system": (
            "The industry bias says a solo founder must recruit a co-founder. But some things are so "
            "personal that adding a co-founder after the fact makes no sense \u2014 and that is not ego "
            "or selfishness, it is authorship. The lane expanded along the way: product strategy, "
            "full-stack engineering, database architecture, AI orchestration. That does not mean "
            "expertise in all of it. It means knowing exactly where advisory is needed."
        ),
        "architecture": (
            "In the author\u2019s words: \u201cDoesn\u2019t mean I\u2019m an expert. I can still use guidance "
            "and advisory from experts.\u201d The framework was built the way it was built \u2014 "
            "\u201cokay, cool, but I\u2019m just going to see what I can do until then\u201d \u2014 out of "
            "tenacity, naivety, and refusing to take \u201cthat\u2019s just the way things are\u201d at face "
            "value. \u201cQuestion everything, but question everything responsibly.\u201d The support "
            "structure a solo founder needs is real; it just doesn\u2019t have to be a co-founder to count."
        ),
    },
]


def render_card(number: int, title: str, caption: str, path: Path) -> None:
    img = Image.new("RGB", (CARD_W, CARD_H), BG_TOP)
    draw = ImageDraw.Draw(img)
    for y in range(CARD_H):
        t = y / CARD_H
        draw.line([(0, y), (CARD_W, y)], fill=tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3)))
    # frame
    draw.rectangle([24, 24, CARD_W - 24, CARD_H - 24], outline=TEAL, width=3)
    draw.rectangle([30, 30, CARD_W - 30, CARD_H - 30], outline=(18, 214, 255, 90), width=1)
    # kicker
    kicker = f"GESTALTVIEW \u00b7 PRINCIPLE {number:02d}"
    draw.text((90, 90), kicker, font=font(34, bold=False), fill=TEAL)
    # violet rule
    draw.rectangle([90, 150, 330, 156], fill=VIOLET)
    # title (wrapped)
    wrapped = textwrap.wrap(title, width=18)
    y = 200
    title_font = font(96)
    for line in wrapped:
        draw.text((90, y), line, font=title_font, fill=INK)
        y += 118
    # caption
    cap_wrapped = textwrap.wrap(caption, width=52)
    y = max(y + 20, 560)
    cap_font = font(36, bold=False)
    for line in cap_wrapped:
        draw.text((90, y), line, font=cap_font, fill=MUTED)
        y += 52
    # footer
    draw.text((90, CARD_H - 110), "Author\u2019s articulation \u00b7 October 2026", font=font(28, bold=False), fill=MUTED)
    img.save(path, "PNG")


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))

    # Drop any previously generated principles chapter/items (idempotent rebuild).
    inventory["chapters"] = [c for c in inventory["chapters"] if c.get("id") != "principles"]
    inventory["items"] = [i for i in inventory["items"] if i.get("kind") != "principle"]

    chapter = {
        "id": "principles",
        "title": "Principles",
        "story_title": "What the system believes before it builds",
        "dek": (
            "Before the architecture, the positions. These are the author\u2019s own articulations "
            "\u2014 the safety principles, evidence rules, and founder stances the system is built to "
            "honor. Stated as positions, not derived from the codebase."
        ),
    }
    inventory["chapters"].insert(0, chapter)

    items = []
    for number, p in enumerate(PRINCIPLES, start=1):
        asset = f"story_assets/principle-{number:02d}.png"
        render_card(number, p["title"], p["caption"], ROOT / asset)
        items.append({
            "id": p["id"],
            "kind": "principle",
            "kind_label": "Principle",
            "featured": number == 1,
            "source_form": "Author-voice principle card; typographic figure rendered for the atlas",
            "confidence": "high",
            "confidence_note": "The author\u2019s own positions, preserved from recorded articulations.",
            "page": None,
            "title": p["title"],
            "caption": p["caption"],
            "section": "Principles",
            "chapter_id": "principles",
            "chapter_title": "Principles",
            "source_ref": "Keith Soyka \u2014 author\u2019s articulation (voice notes, Oct 2026)",
            "asset_path": asset,
            "alt_text": f"Principle card: {p['title']} \u2014 {p['caption']}",
            "explanations": {
                "orientation": p["orientation"],
                "system": p["system"],
                "architecture": p["architecture"],
            },
        })
    inventory["items"].extend(items)
    INVENTORY_PATH.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Principles chapter written: {len(items)} cards -> {ASSETS}")


if __name__ == "__main__":
    main()
