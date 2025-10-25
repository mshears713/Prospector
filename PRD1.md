# PRD 1 – The Interview
*First Hiring Round for the Expedition Quartermaster*

---

## 1. Objective
Build the **first version of the Quartermaster** — a simple program that can:
1. Create a new GitHub repository called `quartermaster` if one does not already exist.
2. Generate a supply manifest file (`inventory.json`) in the repository root.
3. Build a Python script (`quartermaster.py`) that reads the manifest and prints its contents.

No persistence, no reasoning — only literacy and basic file interaction.

---

## 2. Background / Rationale
Before trusting the Quartermaster to handle the expedition’s provisions, the Captains must ensure he can correctly interpret written orders (JSON). This test confirms the link between **Codex → GitHub Repo → Program Output**.

---

## 3. Scope
### In Scope
- Creation of GitHub repository (`quartermaster`).
- Creation of `inventory.json` with five sample items.
- Creation of `quartermaster.py` that reads and prints inventory details.

### Out of Scope
- Persistent databases or file writes beyond the above.
- Error handling for malformed JSON.
- Calculations, reporting, or reasoning.

---

## 4. Inputs
File: `inventory.json`
Format: array of objects

```json
[
  {"item": "compass", "quantity": 2, "description": "Navigation instruments"},
  {"item": "flint", "quantity": 5, "description": "For fire starting"},
  {"item": "rope", "quantity": 3, "description": "For securing cargo"},
  {"item": "telescope", "quantity": 1, "description": "For scouting terrain"},
  {"item": "preserved_meat", "quantity": 10, "description": "Food supply"}
]
```

---

## 5. Expected Behavior / Outputs
When executed, `quartermaster.py` shall:
1. Open `inventory.json`.
2. Parse its contents.
3. For each object, print a line formatted as:

```
Item: <item> | Quantity: <quantity> | Description: <description>
```
4. Print a closing message:
```
Quartermaster Report: 5 items successfully cataloged.
```

---

## 6. Implementation Notes
- Use Python ≥ 3.10.
- Utilize `json` module for parsing.
- Maintain clean function structure.
- Include docstrings describing the purpose of each function.
- Ensure predictable output for testing.
- Codex should automatically create the repository on the connected GitHub account, commit files, and include a basic README referencing this PRD.

---

## 7. Acceptance Criteria
| ID | Criteria | Verification |
|----|-----------|--------------|
| AC-1 | GitHub repo created successfully | Repository `quartermaster` visible on connected account. |
| AC-2 | JSON file created correctly | File matches schema provided above. |
| AC-3 | Program runs without error | Execute script, expect no exceptions. |
| AC-4 | JSON parsed successfully | Console output matches JSON contents. |
| AC-5 | Output formatting consistent | Each line follows `Item | Quantity | Description` pattern. |

---

## 8. Tone / Personality
Quartermaster is an inexperienced but polite recruit. Log messages should sound factual, slightly formal, and eager to serve.

Example:
```
Quartermaster: Reading manifest...
Quartermaster: Item: rope | Quantity: 3 | Description: For securing cargo
Quartermaster: Report complete. All items accounted for, sir!
```

---

## 9. Artifacts / Deliverables
- GitHub repo `quartermaster`
- `quartermaster.py`
- `inventory.json`
- `README.md` referencing this PRD
- Console log output example

---

## 10. Versioning Plan
File: `PRD1.md`
Minor revisions: `PRD1.1.md`, `PRD1.2.md`, etc.
Major revision: PRD2 when persistence and database storage are added.
