#!/usr/bin/env python3
"""Measure true content bbox of both BAUVIZ logos (content spills outside viewBox).

Method: render each SVG with a generously padded viewBox on a magenta page,
screenshot, diff against magenta, get content bbox in user units.
Prints per-logo bbox + a common (union) viewBox to apply.
"""
import os, re
from PIL import Image, ImageChops

os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/data/.cache/ms-playwright"
HERE = "/opt/data/workspace/Bauviz"
TMP = "/tmp/logo_measure"
os.makedirs(TMP, exist_ok=True)
PAD = 100.0
DISP_W = 1200.0

meta = {}
for name in ["BAUVIZ-logo.svg", "BAUVIZ-logo-dark.svg"]:
    s = open(f"{HERE}/{name}", encoding="utf-8").read()
    m = re.search(r'viewBox="([^"]+)"', s)
    x, y, w, h = [float(v) for v in m.group(1).split()]
    px, py = x - PAD, y - PAD
    pw, ph = w + 2 * PAD, h + 2 * PAD
    t = re.sub(r'viewBox="[^"]+"', f'viewBox="{px} {py} {pw} {ph}"', s, count=1)
    t = re.sub(r'\s(width|height)="[\d.]+mm"', "", t, count=2)  # only root svg attrs (mm)
    p = f"{TMP}/{name}.pad.svg"
    open(p, "w", encoding="utf-8").write(t)
    disp_h = DISP_W * ph / pw
    html = (f'<html><head><style>body{{margin:0;background:#ff00ff}}'
            f'img{{display:block;width:{DISP_W}px;height:{disp_h}px}}</style></head>'
            f'<body><img src="file://{p}"></body></html>')
    open(f"{TMP}/{name}.pad.html", "w", encoding="utf-8").write(html)
    meta[name] = (px, py, pw, disp_h)

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/data/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome",
                          args=["--no-sandbox"])
    for name in meta:
        pg = b.new_page(viewport={"width": int(DISP_W), "height": int(meta[name][3] + 5)})
        pg.goto(f"file://{TMP}/{name}.pad.html")
        pg.wait_for_timeout(800)
        pg.screenshot(path=f"{TMP}/{name}.png")
        pg.close()
    b.close()

boxes = {}
for name, (px, py, pw, disp_h) in meta.items():
    img = Image.open(f"{TMP}/{name}.png").convert("RGB")
    bg = Image.new("RGB", img.size, (255, 0, 255))
    diff = ImageChops.difference(img, bg)
    l, t, r, bo = diff.getbbox()
    sx, sy = pw / img.width, pw / img.height
    boxes[name] = (px + l * sx, py + t * sy, px + r * sx, py + bo * sy)
    print(f"{name}: content bbox = {boxes[name][0]:.1f},{boxes[name][1]:.1f} -> {boxes[name][2]:.1f},{boxes[name][3]:.1f}"
          f"  (w={boxes[name][2]-boxes[name][0]:.1f} h={boxes[name][3]-boxes[name][1]:.1f})")

# union across both logos so light & dark align identically
x0 = min(b[0] for b in boxes.values()); y0 = min(b[1] for b in boxes.values())
x1 = max(b[2] for b in boxes.values()); y1 = max(b[3] for b in boxes.values())
M = 3.0  # small margin
print(f"COMMON viewBox = '{x0-M:.2f} {y0-M:.2f} {x1-x0+2*M:.2f} {y1-y0+2*M:.2f}'")
with open(f"{TMP}/common_viewbox.txt", "w") as f:
    f.write(f"{x0-M:.2f} {y0-M:.2f} {x1-x0+2*M:.2f} {y1-y0+2*M:.2f}")
