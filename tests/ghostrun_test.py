"""Simple Playwright check for the Streamlit dashboard."""

from pathlib import Path
import json
import subprocess
import time

from playwright.sync_api import sync_playwright


def main() -> None:
    """Start Streamlit, capture a screenshot, and write small reports."""
    output_dir = Path("tests")
    screenshot_path = output_dir / "ghostrun_screenshot.png"
    result_path = output_dir / "ghostrun_result.json"
    log_path = output_dir / "ghostrun_log.txt"

    # Store short log messages for this run.
    log_lines = []

    def log(message: str) -> None:
        log_lines.append(message)

    output_dir.mkdir(parents=True, exist_ok=True)
    log("Starting Streamlit app")
    app_process = subprocess.Popen(
        [
            "streamlit",
            "run",
            "streamlit_app.py",
            "--server.headless=true",
            "--server.port=8501",
            "--server.address=127.0.0.1",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    try:
        log("Waiting for the dashboard to load")
        time.sleep(5)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("http://127.0.0.1:8501", wait_until="networkidle")
            log("Taking screenshot")
            page.screenshot(path=str(screenshot_path), full_page=True)
            browser.close()

        log("Writing JSON result")
        result_path.write_text(
            json.dumps(
                {
                    "status": "success",
                    "url": "http://127.0.0.1:8501",
                    "screenshot": str(screenshot_path),
                },
                indent=2,
            )
        )
    finally:
        log("Stopping Streamlit app")
        app_process.terminate()
        try:
            app_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            app_process.kill()

        if app_process.stdout:
            log("Collecting Streamlit logs")
            log_lines.extend(line.strip() for line in app_process.stdout.readlines())

        log("Writing log file")
        log_path.write_text("\n".join(log_lines))


if __name__ == "__main__":
    main()
