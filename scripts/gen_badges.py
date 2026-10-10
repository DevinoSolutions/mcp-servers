"""Generate badges/add-to-<agent>.svg and add-to-<agent>-light.svg.

32px pill, the agent's official mark in a 16px slot, system sans-serif text.
Marks are read verbatim from scripts/badge-marks/ (see MARKS for where each came
from); an agent without a mark keeps the generic plus-in-circle glyph.
Add an agent to AGENTS to get a new badge pair.
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
OUT = ROOT / "badges"
OUT.mkdir(exist_ok=True)
MARKS_DIR = Path(__file__).resolve().parent / "badge-marks"

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

# One official source per brand, all fetched 2026-10-10.
#   mono:    single-colour mark, drawn in the badge text colour (currentColor)
#   variant: the brand ships a dark and a white file; <slug>.svg on the light pill,
#            <slug>-white.svg on the dark pill, both used exactly as provided
#   asis:    full-colour mark the brand does not allow to be recoloured, used as provided
# ChatGPT and Codex are left out on purpose: OpenAI's brand page (openai.com/brand) could
# not be reached to confirm third-party use, and simple-icons dropped the OpenAI mark.
MARKS = {
    "claude": ("mono", "simple-icons 16.34.0 'claude', CC0, https://cdn.jsdelivr.net/npm/simple-icons@16.34.0/icons/claude.svg"),
    "cursor": ("mono", "simple-icons 16.34.0 'cursor', CC0, https://cdn.jsdelivr.net/npm/simple-icons@16.34.0/icons/cursor.svg"),
    "vscode": ("asis", "Microsoft VS Code icon (vscode.svg), https://code.visualstudio.com/assets/branding/visual-studio-code-icons.zip, per https://code.visualstudio.com/brand"),
    "kiro": ("asis", "Kiro site icon, https://kiro.dev/icon.svg"),
    "replit": ("mono", "simple-icons 16.34.0 'replit', CC0, https://cdn.jsdelivr.net/npm/simple-icons@16.34.0/icons/replit.svg"),
    "antigravity": ("variant", "Google Antigravity press kit icon (one-color / white), https://antigravity.google/press"),
    "gemini": ("mono", "simple-icons 16.34.0 'googlegemini', CC0, https://cdn.jsdelivr.net/npm/simple-icons@16.34.0/icons/googlegemini.svg"),
    "perplexity": ("mono", "simple-icons 16.34.0 'perplexity', CC0, https://cdn.jsdelivr.net/npm/simple-icons@16.34.0/icons/perplexity.svg"),
    "mistral": ("mono", "simple-icons 16.34.0 'mistralai', CC0, https://cdn.jsdelivr.net/npm/simple-icons@16.34.0/icons/mistralai.svg"),
    "grok": ("variant", "xAI Grok logomark (Grok_Logomark_Dark / _Light), https://data.x.ai/logos/SpaceXAI_Grok_Assets.zip, per https://x.ai/legal/brand-guidelines"),
}
FETCHED = "2026-10-10"

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


def read_mark(name: str) -> tuple[str, str, str]:
    """Return (viewBox, root fill attribute or '', inner markup) of a mark file."""
    src = (MARKS_DIR / f"{name}.svg").read_text(encoding="utf-8")
    root = re.search(r"<svg\b[^>]*>", src).group(0)
    view_box = re.search(r'viewBox="([^"]+)"', root).group(1)
    fill = re.search(r'\sfill="([^"]+)"', root)
    inner = src[src.index(root) + len(root):src.rindex("</svg>")]
    inner = re.sub(r"<title>.*?</title>", "", inner, flags=re.S)
    inner = re.sub(r">\s+<", "><", " ".join(inner.split("\n"))).strip()
    return view_box, (f' fill="{fill.group(1)}"' if fill else ""), inner


def glyph(slug: str, fg: str, dark: bool) -> str:
    x, y = PAD, (H - GLYPH) / 2
    box = f'x="{x}" y="{y}" width="{GLYPH}" height="{GLYPH}"'
    if slug not in MARKS:
        cx, cy = PAD + GLYPH / 2, H / 2
        return (
            f'<circle cx="{cx}" cy="{cy}" r="7" fill="none" stroke="{fg}" stroke-width="1.6"/>'
            f'<path d="M{cx} {cy - 3.5}v7M{cx - 3.5} {cy}h7" stroke="{fg}" stroke-width="1.6" stroke-linecap="round"/>'
        )
    kind, source = MARKS[slug]
    comment = f"<!-- {slug} mark: {source}, fetched {FETCHED} -->"
    if kind == "mono":
        view_box, _, inner = read_mark(slug)
        return f'{comment}<svg {box} viewBox="{view_box}" color="{fg}" fill="currentColor" aria-hidden="true">{inner}</svg>'
    name = f"{slug}-white" if kind == "variant" and dark else slug
    view_box, fill, inner = read_mark(name)
    return f'{comment}<svg {box} viewBox="{view_box}"{fill} aria-hidden="true">{inner}</svg>'


def svg(slug: str, label: str, bg: str, fg: str, border: str | None) -> str:
    text = f"Add to {label}"
    tw = text_width(text)
    width = PAD + GLYPH + GAP + tw + PAD
    r = H / 2
    rect = (
        f'<rect x=".5" y=".5" width="{width - 1}" height="{H - 1}" rx="{r - .5}" fill="{bg}" stroke="{border}"/>'
        if border
        else f'<rect width="{width}" height="{H}" rx="{r}" fill="{bg}"/>'
    )
    cy = H / 2
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{H}" viewBox="0 0 {width} {H}" role="img" aria-label="{text}">'
        f"<title>{text}</title>"
        f"{rect}"
        f"{glyph(slug, fg, border is None)}"
        f'<text x="{PAD + GLYPH + GAP}" y="{cy}" dominant-baseline="central" font-family="{FONT}" '
        f'font-size="{SIZE}" font-weight="600" fill="{fg}" textLength="{tw}" lengthAdjust="spacingAndGlyphs">{text}</text>'
        "</svg>\n"
    )


for slug, label in AGENTS:
    (OUT / f"add-to-{slug}.svg").write_text(svg(slug, label, "#1f2328", "#ffffff", None), encoding="utf-8", newline="\n")
    (OUT / f"add-to-{slug}-light.svg").write_text(svg(slug, label, "#ffffff", "#1f2328", "#d0d7de"), encoding="utf-8", newline="\n")
print("wrote", 2 * len(AGENTS), "badges to", OUT)
