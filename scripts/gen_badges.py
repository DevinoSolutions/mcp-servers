"""Generate badges/add-to-<agent>.svg and add-to-<agent>-light.svg.

32px pill, generic plus-in-circle glyph (no vendor artwork), system sans-serif text.
Add an agent to AGENTS to get a new badge pair.
"""
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
OUT = ROOT / "badges"
OUT.mkdir(exist_ok=True)

AGENTS = [
    ("claude", "Claude"),
    ("chatgpt", "ChatGPT"),
    ("cursor", "Cursor"),
    ("vscode", "VS Code"),
    ("kiro", "Kiro"),
    ("replit", "Replit"),
    ("antigravity", "Antigravity"),
    ("gemini", "Gemini"),
    ("codex", "Codex"),
    ("perplexity", "Perplexity"),
    ("mistral", "Mistral"),
    ("grok", "Grok"),
]

FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
H = 32
PAD = 12          # left/right padding
GLYPH = 16        # glyph box
GAP = 8           # glyph -> text
SIZE = 14         # font size

# rough advance widths at 14px semibold; textLength pins the final layout anyway
WIDE = set("mwMW")
NARROW = set("iljtfI ")


def text_width(s: str) -> int:
    w = 0.0
    for ch in s:
        if ch in WIDE:
            w += 12
        elif ch in NARROW:
            w += 4.5
        elif ch.isupper():
            w += 9.5
        else:
            w += 7.8
    return round(w)


def svg(label: str, bg: str, fg: str, border: str | None) -> str:
    text = f"Add to {label}"
    tw = text_width(text)
    width = PAD + GLYPH + GAP + tw + PAD
    r = H / 2
    rect = (
        f'<rect x=".5" y=".5" width="{width - 1}" height="{H - 1}" rx="{r - .5}" fill="{bg}" stroke="{border}"/>'
        if border
        else f'<rect width="{width}" height="{H}" rx="{r}" fill="{bg}"/>'
    )
    cx = PAD + GLYPH / 2
    cy = H / 2
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{H}" viewBox="0 0 {width} {H}" role="img" aria-label="{text}">'
        f"<title>{text}</title>"
        f"{rect}"
        f'<circle cx="{cx}" cy="{cy}" r="7" fill="none" stroke="{fg}" stroke-width="1.6"/>'
        f'<path d="M{cx} {cy - 3.5}v7M{cx - 3.5} {cy}h7" stroke="{fg}" stroke-width="1.6" stroke-linecap="round"/>'
        f'<text x="{PAD + GLYPH + GAP}" y="{cy}" dominant-baseline="central" font-family="{FONT}" '
        f'font-size="{SIZE}" font-weight="600" fill="{fg}" textLength="{tw}" lengthAdjust="spacingAndGlyphs">{text}</text>'
        "</svg>\n"
    )


for slug, label in AGENTS:
    (OUT / f"add-to-{slug}.svg").write_text(svg(label, "#1f2328", "#ffffff", None), encoding="utf-8", newline="\n")
    (OUT / f"add-to-{slug}-light.svg").write_text(svg(label, "#ffffff", "#1f2328", "#d0d7de"), encoding="utf-8", newline="\n")
print("wrote", 2 * len(AGENTS), "badges to", OUT)
