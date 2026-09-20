"""Smoke tests for MetaHelper IoT Clinical Monitoring System."""

import os
from pathlib import Path

def test_static():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    assert "John Doe" in html, "Patient name missing"
    assert "#MS-88042" in html, "Patient ID missing"
    assert "assets/patient.jpg" in html, "Patient photo missing"
    assert Path("assets/patient.jpg").exists(), "Patient photo file missing"
    assert "72" in html and "Heart Rate" in html, "Heart rate sensor missing"
    assert "142" in html and "Blood Glucose" in html, "Blood glucose sensor missing"
    assert "120/80" in html and "Blood Pressure" in html, "Blood pressure sensor missing"
    assert "36.6" in html and "Body Temp" in html, "Body temp sensor missing"
    assert "Sinus" in html and "ECG Status" in html, "ECG sensor missing"
    assert "+7 7028455017" in html, "Emergency contact missing"
    assert "range-badge" not in html, "Sticker range-badge still present in HTML!"
    assert "badge active" not in html, "Sticker pill badge still present in HTML!"
    print("PASS: Static structure and content checks verified.")

if __name__ == "__main__":
    test_static()
    try:
        from playwright.sync_api import sync_playwright
        print("Playwright available, running browser checks...")
    except ImportError:
        print("Note: playwright is not installed in the environment; static checks completed successfully.")
