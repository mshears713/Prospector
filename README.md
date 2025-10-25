# Frontier Data Prospector

## Quartermaster Prototype

This repository contains the first version of the Quartermaster described in [PRD1 – The Interview](PRD1.md). The goal is to prove that the recruit can read a written manifest and report its contents without embellishment.

## Files
- `inventory.json` – Sample manifest with five expedition supplies.
- `quartermaster.py` – Python script that reads the manifest and prints the report.
- `PRD1.md` – Product requirements document that guides this implementation.

## Usage
Run the script with Python 3.10 or newer:

```bash
python quartermaster.py
```

Expected console output:

```
Quartermaster: Reading manifest...
Quartermaster: Item: compass | Quantity: 2 | Description: Navigation instruments
Quartermaster: Item: flint | Quantity: 5 | Description: For fire starting
Quartermaster: Item: rope | Quantity: 3 | Description: For securing cargo
Quartermaster: Item: telescope | Quantity: 1 | Description: For scouting terrain
Quartermaster: Item: preserved_meat | Quantity: 10 | Description: Food supply
Quartermaster: Report complete. All items accounted for, sir!
Quartermaster Report: 5 items successfully cataloged.
```
