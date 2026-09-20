"""Small browser smoke test for the static coursework page."""

import os
from pathlib import Path

from playwright.sync_api import sync_playwright


URL = os.environ.get("SMOKE_URL", "http://127.0.0.1:8000")
OUTPUT = Path(os.environ.get("SCREENSHOT_DIR", "screenshots"))
OUTPUT.mkdir(exist_ok=True)


def check_page(browser, name, width, height):
    page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    response = page.goto(URL, wait_until="networkidle")
    assert response and response.status == 200, f"{name}: page did not load"
    assert page.title() == "VitalTrace — Patient monitoring record"
    assert page.locator("h1").count() == 1
    assert page.locator(".sensor-card").count() == 5
    for card in page.locator(".sensor-card").all():
        assert card.locator("h3").count() == 1
        assert card.locator("data").count() == 1
        assert card.locator(".status").count() == 1
    assert page.locator(".patient-details div").count() == 5
    assert page.locator(".attention-band").is_visible()
    assert page.locator(".alert-item").count() == 2
    assert page.locator("tbody tr").count() == 4
    assert page.locator(".status-review").count() == 1
    assert page.locator(".demo-notice").is_visible()
    assert page.locator(".site-footer a[href^='mailto:']").count() == 1
    for link in page.locator("a[href^='#']").all():
        assert page.locator(link.get_attribute("href")).count() == 1, f"{name}: broken internal link"

    for image in page.locator("img").all():
        assert image.evaluate("img => img.complete && img.naturalWidth > 0"), f"{name}: broken image"
    assert page.locator(".sensor-card").first.evaluate(
        "el => getComputedStyle(el).borderTopStyle === 'solid'"
    ), f"{name}: CSS did not load"
    assert page.evaluate(
        "() => document.documentElement.scrollWidth <= window.innerWidth"
    ), f"{name}: horizontal overflow"
    assert not errors, f"{name}: page errors: {errors}"

    # Internal navigation should land on a visible section.
    page.locator(".main-nav a[href='#alerts']").click()
    assert page.evaluate("location.hash") == "#alerts"
    assert page.locator("#alerts").is_visible()

    if name == "desktop":
        nav = page.locator(".main-nav a").first
        before = nav.evaluate("el => getComputedStyle(el).color")
        nav.hover()
        page.wait_for_timeout(250)
        after = nav.evaluate("el => getComputedStyle(el).color")
        assert before != after, "navigation hover effect missing"
        button = page.locator(".attention-link")
        before = button.evaluate("el => getComputedStyle(el).backgroundColor")
        button.hover()
        page.wait_for_timeout(250)
        assert before != button.evaluate("el => getComputedStyle(el).backgroundColor"), "button hover effect missing"
        row = page.locator("tbody tr").first
        before = row.evaluate("el => getComputedStyle(el).backgroundColor")
        row.hover()
        page.wait_for_timeout(250)
        assert before != row.evaluate("el => getComputedStyle(el).backgroundColor"), "row hover effect missing"

    page.evaluate("window.scrollTo(0, 0)")
    page.screenshot(path=str(OUTPUT / f"{name}.png"), full_page=True)
    print(f"PASS {name}: {width}x{height}, 5 sensors, 2 alerts, navigation, assets, no overflow/errors")
    page.close()


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(channel="chrome", headless=True)
    check_page(browser, "desktop", 1440, 900)
    check_page(browser, "mobile", 390, 844)
    check_page(browser, "small-mobile", 320, 700)
    browser.close()
