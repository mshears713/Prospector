"""Quartermaster report: read a JSON manifest and print each entry."""

import json

MANIFEST_FILE = "inventory.json"  # The manifest sits next to this script.


def read_manifest():
    """Return the list of items from the manifest file."""
    with open(MANIFEST_FILE, "r", encoding="utf-8") as manifest:
        return json.load(manifest)


def print_report(items):
    """Print every item line followed by the closing messages."""
    print("Quartermaster: Reading manifest...")

    for item in items:
        line = (
            "Quartermaster: "
            f"Item: {item['item']} | Quantity: {item['quantity']} | Description: {item['description']}"
        )
        print(line)

    print("Quartermaster: Report complete. All items accounted for, sir!")
    print(f"Quartermaster Report: {len(items)} items successfully cataloged.")


def main():
    """Load the manifest and show the report."""
    items = read_manifest()  # Read the JSON file.
    print_report(items)  # Output each line.


if __name__ == "__main__":
    main()
