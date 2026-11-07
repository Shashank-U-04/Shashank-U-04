"""Draw a "Languages by repo count" card (one stacked bar + legend) as light and dark SVGs.

Counts the primary language of each public, non-fork repository the account owns.
Usage: GITHUB_TOKEN=... python lang_card.py <login> <output-dir>
"""
import json
import os
import sys
import urllib.request
from collections import Counter

LOGIN, OUT = sys.argv[1], sys.argv[2]
TOKEN = os.environ["GITHUB_TOKEN"]
TOP = 6

QUERY = """
query($login: String!, $after: String) {
  user(login: $login) {
    repositories(first: 100, after: $after, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      pageInfo { hasNextPage endCursor }
      nodes { primaryLanguage { name color } }
    }
  }
}"""


def fetch_languages():
    counts, colors, after = Counter(), {}, None
    while True:
        body = json.dumps({"query": QUERY, "variables": {"login": LOGIN, "after": after}}).encode()
        req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=body,
            headers={"Authorization": f"bearer {TOKEN}", "User-Agent": "lang-card"},
        )
        data = json.load(urllib.request.urlopen(req))
        if "errors" in data:
            raise SystemExit(data["errors"])
        repos = data["data"]["user"]["repositories"]
        for node in repos["nodes"]:
            lang = node["primaryLanguage"]
            if lang:
                counts[lang["name"]] += 1
                colors[lang["name"]] = lang["color"] or "#8b949e"
        if not repos["pageInfo"]["hasNextPage"]:
            return counts, colors
        after = repos["pageInfo"]["endCursor"]


THEMES = {
    "light": dict(bg="#ffffff", border="#d0d7de", title="#1f2328", text="#424a53"),
    "dark": dict(bg="#0d1117", border="#3d444d", title="#f0f6fc", text="#d1d7e0"),
}
FONT = "'Segoe UI', -apple-system, 'Helvetica Neue', Arial, sans-serif"
W, H, PAD = 480, 186, 26
BAR_Y, BAR_H = 60, 10


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(counts, colors, theme):
    t = THEMES[theme]
    top = counts.most_common(TOP)
    total = sum(counts.values())
    shown = sum(n for _, n in top) or 1
    bar_w = W - 2 * PAD

    segs, x = [], PAD
    for i, (name, n) in enumerate(top):
        w = bar_w - (x - PAD) if i == len(top) - 1 else bar_w * n / shown
        segs.append(f'<rect x="{x:.2f}" y="{BAR_Y}" width="{w:.2f}" height="{BAR_H}" fill="{colors[name]}"/>')
        x += w

    legend = []
    for i, (name, n) in enumerate(top):
        col, row = divmod(i, 3)
        lx, ly = PAD + col * (bar_w / 2), 104 + row * 30
        legend.append(
            f'<circle cx="{lx + 7}" cy="{ly - 5}" r="7" fill="{colors[name]}"/>'
            f'<text x="{lx + 22}" y="{ly}" font-family="{FONT}" font-size="15" fill="{t["text"]}">'
            f"{esc(name)} {100 * n / total:.2f}%</text>"
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Languages by repo count">
  <defs><clipPath id="bar"><rect x="{PAD}" y="{BAR_Y}" width="{bar_w}" height="{BAR_H}" rx="{BAR_H / 2}"/></clipPath></defs>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="8" fill="{t['bg']}" stroke="{t['border']}"/>
  <text x="{PAD}" y="40" font-family="{FONT}" font-size="22" font-weight="600" fill="{t['title']}">Languages by repo count</text>
  <g clip-path="url(#bar)">{''.join(segs)}</g>
  {''.join(legend)}
</svg>
"""


counts, colors = fetch_languages()
os.makedirs(OUT, exist_ok=True)
for theme in THEMES:
    with open(os.path.join(OUT, f"langs-{theme}.svg"), "w", encoding="utf-8", newline="\n") as f:
        f.write(render(counts, colors, theme))
print(", ".join(f"{k} {v}" for k, v in counts.most_common()))
