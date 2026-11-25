#!/usr/bin/env python3
"""Screenshot all 4 designs: hero viewport (1280x900) + full page."""
import os, pathlib
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/data/.cache/ms-playwright"
from playwright.sync_api import sync_playwright

CHROME = "/opt/data/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome"
HERE = pathlib.Path("/opt/data/workspace/Bauviz/designs")
FILES = ["A-blueprint", "B-dark-twin", "C-editorial", "D-drafting"]

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox", "--force-color-profile=srgb"])
    for name in FILES:
        url = (HERE / f"{name}.html").resolve().as_uri()
        pg = b.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=2)
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(url)
        pg.wait_for_timeout(600)
        # ensure logo + any webfont settled
        pg.screenshot(path=str(HERE / f"{name}_hero.png"))
        pg.screenshot(path=str(HERE / f"{name}_full.png"), full_page=True)
        # sanity: logo loaded?
        ok = pg.evaluate("document.querySelector('.logo') && document.querySelector('.logo').complete")
        print(f"{name}: logo_complete={ok} pageerrors={errs[:2] or 'none'} "
              f"hero={os.path.getsize(HERE/(name+'_hero.png'))//1024}KB "
              f"full={os.path.getsize(HERE/(name+'_full.png'))//1024}KB")
        pg.close()
    b.close()
print("done")
