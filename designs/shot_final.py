#!/usr/bin/env python3
import os, pathlib
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/data/.cache/ms-playwright"
from playwright.sync_api import sync_playwright
CHROME = "/opt/data/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome"
HERE = pathlib.Path("/opt/data/workspace/Bauviz")
url = (HERE / "index.html").resolve().as_uri()

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox", "--force-color-profile=srgb"])
    pg = b.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=2)
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(url); pg.wait_for_timeout(600)

    # default (light) — confirm no dark class
    state0 = pg.evaluate("document.body.classList.contains('dark')")
    pg.screenshot(path=str(HERE/"index_light_hero.png"))
    pg.screenshot(path=str(HERE/"index_light_full.png"), full_page=True)

    # click the toggle -> should go dark
    pg.click("#theme-toggle"); pg.wait_for_timeout(350)
    state1 = pg.evaluate("document.body.classList.contains('dark')")
    lbl = pg.evaluate("document.getElementById('theme-toggle').textContent.trim()")
    pg.screenshot(path=str(HERE/"index_dark_hero.png"))
    pg.screenshot(path=str(HERE/"index_dark_full.png"), full_page=True)

    # click again -> back to light (toggle works both ways)
    pg.click("#theme-toggle"); pg.wait_for_timeout(350)
    state2 = pg.evaluate("document.body.classList.contains('dark')")
    stored = pg.evaluate("(function(){try{return localStorage.getItem('bauviz-theme')}catch(e){return 'x'}})()")

    # logo loaded + no numbering
    logo_ok = pg.evaluate("document.querySelector('.logo').complete")
    nums = pg.evaluate("document.querySelectorAll('.num').length")

    print(f"light_state={state0} dark_after_click={state1} btn_label={lbl!r} back_light={state2}")
    print(f"localStorage_theme={stored!r} logo_complete={logo_ok} num_spans={nums}")
    print(f"pageerrors={errs[:3] or 'none'}")
    for f in ["index_light_hero","index_dark_hero"]:
        print(f, os.path.getsize(HERE/(f+'.png'))//1024, "KB")
    b.close()
