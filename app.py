"""Streamlit app to display scraped quotes."""

from pathlib import Path
import json
import streamlit as st


def load_quotes() -> list[dict]:
    """Load quotes from the JSON export."""
    paths = [Path("quotes.json"), Path("data/quotes.json")]
    for path in paths:
        if path.exists():
            with path.open("r", encoding="utf-8") as handle:
                return json.load(handle)
    return []


def main() -> None:
    """Render the quote viewer interface."""
    st.set_page_config(page_title="Frontier Prospector — Quote Viewer", page_icon="🧭")
    st.title("🧭 Frontier Prospector — Quote Viewer")

    quotes = load_quotes()

    st.sidebar.header("Quote Controls")
    st.sidebar.write(f"Total quotes: **{len(quotes)}**")
    author_filter = st.sidebar.text_input("Filter by author", placeholder="Start typing a name...")

    if author_filter:
        needle = author_filter.strip().lower()
        quotes = [quote for quote in quotes if quote.get("author", "").lower().find(needle) != -1]

    if not quotes:
        st.info("No quotes available. Add data by running the scraper.")
        return

    for quote in quotes:
        text = quote.get("text", "").strip()
        author = quote.get("author", "Unknown").strip() or "Unknown"
        st.markdown(
            f"""
            <div style="border: 1px solid #dcdcdc; border-radius: 8px; padding: 16px; margin-bottom: 12px; background-color: #fdfdfd;">
                <div style="font-size: 1.1rem; line-height: 1.6;">{text}</div>
                <div style="font-size: 0.9rem; font-style: italic; color: #555; margin-top: 8px;">— {author}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
