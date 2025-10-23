"""Simple scraper for Lesson 5."""

from pathlib import Path
import json

from playwright.sync_api import sync_playwright


URL = "https://quotes.toscrape.com"
OUTPUT_PATH = Path(__file__).resolve().parent / "data" / "scrape_output.json"
MAX_QUOTES = 5


def main() -> None:
    """Run the scraper and print the results."""
    # Keep the results in a plain list for easy reading.
    results = []

    # Start Playwright and open the page in headless mode.
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, wait_until="domcontentloaded")

        # Grab the first few quote blocks on the page.
        quote_blocks = page.query_selector_all("div.quote")[:MAX_QUOTES]

        # Pull out the quote text and author name.
        for block in quote_blocks:
            text = block.query_selector("span.text").inner_text().strip()
            author = block.query_selector("small.author").inner_text().strip()
            results.append({"quote": text, "author": author})

        browser.close()

    # Show the results in the logs for the lesson.
    print("=== SCRAPER RESULTS ===")
    for item in results:
        print(f"\"{item['quote']}\" — {item['author']}")

    # Save the same data to the data folder.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(results, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
