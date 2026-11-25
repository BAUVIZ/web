#!/usr/bin/env python3
"""Verify all 7 changes on index.html + regenerated design prototypes."""
import os
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/data/.cache/ms-playwright"
from playwright.sync_api import sync_playwright

HERE = "/opt/data/workspace/Bauviz"
results = []

def check(name, cond):
    results.append(f"{'PASS' if cond else 'FAIL'}  {name}")
    if not cond:
        raise SystemExit(f"VERIFICATION FAILED: {name}")

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/data/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome",
                          args=["--no-sandbox", "--force-color-profile=srgb"])

    # ---- main page ----
    pg = b.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=2)
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(f"file://{HERE}/index.html")
    pg.wait_for_timeout(700)

    t = pg.evaluate("document.body.innerText")
    check("no 'Mar 05, 2027' date", "Mar 05, 2027" not in t)
    check("no 'Apr 16, 2027' date", "Apr 16, 2027" not in t)
    check("no 'May 03, 2027' date", "May 03, 2027" not in t)
    check("dates section has TBA rows", t.count("TBA") >= 4)
    check("EuroVis 2027 row present", "EuroVis 2027" in t)
    check("small 'workshop day tba' note", "Workshop day: TBA" in t and "early March 2027" in t)
    check("Support section gone", "IntCDC" not in t and "supported by the Cluster" not in t)
    check("new contact email", "bauviz@visus.uni-stuttgart.de" in t and "bauviz2027@" not in t)
    check("Kuno affiliation updated", "TU Darmstadt" not in t)

    # logo clipping: hero logo must show content in left 2% and right 98% of its box,
    # and in bottom 5% (subtitle was previously clipped)
    box = pg.evaluate("(() => { const r = document.querySelector('.hero .logo').getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; })()")
    l, tp, w, h = box
    shot = pg.screenshot(clip={"x": l - 4, "y": tp - 4, "width": w + 8, "height": h + 8})
    from PIL import Image
    import io
    im = Image.open(io.BytesIO(shot)).convert("L")
    W, H = im.size
    def nonwhite_frac(x0f, x1f, y0f, y1f):
        reg = im.crop((int(x0f * W), int(y0f * H), int(x1f * W), int(y1f * H)))
        px = list(reg.getdata())
        return sum(1 for v in px if v < 235) / len(px)
    check("logo not clipped LEFT  (left strip has content)", nonwhite_frac(0.0, 0.06, 0.1, 0.9) > 0.02)
    check("logo not clipped RIGHT (right strip has content)", nonwhite_frac(0.94, 1.0, 0.1, 0.9) > 0.02)
    check("logo subtitle visible (was clipped before)", nonwhite_frac(0.05, 0.95, 0.78, 0.94) > 0.02)

    # bullet consistency: all list items same font size
    fs = pg.evaluate("""(() => {
      const get = (sel) => { const el = document.querySelector(sel); return el ? getComputedStyle(el).fontSize : null; };
      return {aud: get('.aud li'), topic: get('.topic li'), sdesc: get('.s-desc'), paff: get('.p-aff')};
    })()""")
    check("aud li = 15px", fs["aud"] == "15px")
    check("topic li = 15px", fs["topic"] == "15px")
    check("s-desc = 15px", fs["sdesc"] == "15px")
    check("p-aff = 15px", fs["paff"] == "15px")
    sq = pg.evaluate("getComputedStyle(document.querySelector('.aud li'),'::before').backgroundColor")
    check("aud bullets are square teal", sq in ("rgb(45, 136, 157)", "rgb(108, 199, 216)"))
    sq2 = pg.evaluate("getComputedStyle(document.querySelector('.topic li'),'::before').backgroundColor")
    check("topic bullets match", sq2 == sq)

    pg.screenshot(path=f"{HERE}/index_light_hero.png")
    pg.click("#theme-toggle"); pg.wait_for_timeout(400)
    dbox = pg.evaluate("(() => { const r = document.querySelector('.hero .logo').getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; })()")
    dshot = pg.screenshot(clip={"x": dbox[0] - 4, "y": dbox[1] - 4, "width": dbox[2] + 8, "height": dbox[3] + 8})
    dim = Image.open(io.BytesIO(dshot)).convert("L")
    DW, DH = dim.size
    def dfrac(x0f, x1f, y0f, y1f):
        reg = dim.crop((int(x0f * DW), int(y0f * DH), int(x1f * DW), int(y1f * DH)))
        px = list(reg.getdata())
        return sum(1 for v in px if v > 25) / len(px)
    check("DARK logo not clipped LEFT", dfrac(0.0, 0.06, 0.1, 0.9) > 0.01)
    check("DARK logo not clipped RIGHT", dfrac(0.94, 1.0, 0.1, 0.9) > 0.01)
    check("DARK logo subtitle visible", dfrac(0.05, 0.95, 0.78, 0.94) > 0.02)
    check("dark hero logo src", pg.evaluate("document.querySelector('.hero .logo').src.endsWith('BAUVIZ-logo-dark.svg')"))
    pg.screenshot(path=f"{HERE}/index_dark_hero.png")
    check("no page errors", not errs)
    pg.close()

    # ---- design prototypes regenerated consistently ----
    for f in ["A-blueprint.html", "B-dark-twin.html", "C-editorial.html", "D-drafting.html"]:
        pg = b.new_page(viewport={"width": 1280, "height": 900})
        pg.goto(f"file://{HERE}/designs/{f}")
        pg.wait_for_timeout(400)
        t = pg.evaluate("document.body.innerText")
        check(f"{f}: no old dates", "Mar 05, 2027" not in t)
        check(f"{f}: TBA present", "TBA" in t)
        check(f"{f}: no Support section", "IntCDC" not in t)
        check(f"{f}: new email", "bauviz@visus.uni-stuttgart.de" in t and "bauviz2027@" not in t)
        pg.close()
    b.close()

from PIL import Image
for name, src in [("index_light_hero_preview.jpg", "index_light_hero.png"),
                  ("index_dark_hero_preview.jpg", "index_dark_hero.png")]:
    im = Image.open(f"{HERE}/{src}").convert("RGB")
    im.thumbnail((1100, 1100))
    im.save(f"{HERE}/{name}", quality=82)
print("\n".join(results))
print("previews refreshed")
