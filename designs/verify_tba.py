#!/usr/bin/env python3
"""Verify index.html: TBA program, dark-logo swap on toggle, new About text."""
import os
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/data/.cache/ms-playwright"
from playwright.sync_api import sync_playwright

HERE = "/opt/data/workspace/Bauviz"
url = f"file://{HERE}/index.html"

def logo_srcs(page):
    return page.evaluate("Array.from(document.querySelectorAll('.logo')).map(function(i){return i.getAttribute('src')})")

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/data/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome",
                          args=["--no-sandbox", "--force-color-profile=srgb"])
    pg = b.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=2)
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(url)
    pg.wait_for_timeout(600)

    # light state
    tba = pg.evaluate("(() => { const el = document.querySelector('#program .tba'); return el ? el.textContent.trim() : null; })()")
    rows = pg.evaluate("document.querySelectorAll('#program .pg-row').length")
    old_note = pg.evaluate("document.body.innerText.includes('provisional')")
    about = pg.evaluate("document.querySelector('#about .lead').innerText")
    about_new = "AEC disciplines" in about and "circularity" in about and "districts and urban systems" in about
    light_srcs = logo_srcs(pg)
    pg.screenshot(path=f"{HERE}/index_light_hero.png")

    # toggle -> dark
    pg.click("#theme-toggle")
    pg.wait_for_timeout(400)
    dark = pg.evaluate("document.body.classList.contains('dark')")
    dark_srcs = logo_srcs(pg)
    pg.screenshot(path=f"{HERE}/index_dark_hero.png")

    # toggle -> light again
    pg.click("#theme-toggle")
    pg.wait_for_timeout(400)
    back_light = pg.evaluate("!document.body.classList.contains('dark')")
    back_srcs = logo_srcs(pg)

    # confirm both logo files actually load (no 404)
    light_ok = pg.evaluate("document.querySelector('.hero .logo').complete && document.querySelector('.hero .logo').naturalWidth > 0")

    print(f"tba={tba!r} pg_rows={rows} old_note_present={old_note}")
    print(f"about_new_text={about_new}")
    print(f"light_srcs={light_srcs}")
    print(f"dark_srcs={dark_srcs} dark={dark}")
    print(f"back_light={back_light} back_srcs={back_srcs}")
    print(f"hero_logo_loaded={light_ok} pageerrors={errs[:3] or 'none'}")
    b.close()

from PIL import Image
for name, src in [("index_light_hero_preview.jpg", "index_light_hero.png"),
                  ("index_dark_hero_preview.jpg", "index_dark_hero.png")]:
    im = Image.open(f"{HERE}/{src}").convert("RGB")
    im.thumbnail((1100, 1100))
    im.save(f"{HERE}/{name}", quality=82)
    print(name, im.size)
