# Quality Assurance Report — ContractPulse

**Source of truth:** `project-10-at-2026-10-28-23-22-6cdd0f43.csv` (Label Studio export, 28 October 2026).  
**Scope:** 200 source tasks / 650 labeled entity spans.  
**Method:** exact, non-destructive normalization of span boundaries, followed by full-dataset structural validation.  
**Source SHA-256:** `6bc64b6c7d8d91ee691f7d86b8bf1961f7911b30226ca7452dc1443cfb4689ba`

## Executive summary

The last submitted Label Studio export had **52 annotation spans with unwanted trailing whitespace**, affecting **52 different tasks**. The issues comprised **51 LOCATION** spans and **one MONEY** span. Each was cleaned by removing the trailing space from its `text` value and reducing the span's `end` offset by one character.

No original sentence, task ID, entity label, unaffected span, timestamp, annotator identifier, or other export-field value was changed. The cleaned export contains the same 200 tasks, the same 650 annotations, and the same five-class distribution as the supplied file.

| QA measure | Verified post-clean result |
|---|---:|
| Source tasks | 200 |
| Unique task IDs | 200 |
| Total entity spans | 650 |
| Negative tasks with no entity spans | 20 |
| Corrected trailing-space spans | 52 |
| Remaining leading/trailing whitespace in spans | 0 |
| Mismatches between span text and source offsets | 0 |
| Overlapping/invalid spans | 0 |
| Unrecognized entity labels | 0 |
| Tasks failing supplied reference-count expectations | 0 |
| Unchanged original source messages | 200 / 200 |
| Unchanged non-annotation data fields | 200 / 200 rows |

### Entity counts

| Label | Count |
|---|---:|
| COMPANY | 160 |
| PERSON | 140 |
| LOCATION | 120 |
| DATE | 110 |
| MONEY | 120 |
| **Total** | **650** |

### Task composition
- 110 tasks contain four spans.
- 70 tasks contain three spans.
- 20 tasks contain zero spans and are intentionally negative examples.

## Character-offset correction example

If an annotation stores `Seattle ` with `start = 15`, `end = 23`, then its content includes a trailing space. The corrected annotation stores `Seattle`, `start = 15`, `end = 22`. The original message is not modified. (Offsets shown here are illustrative; actual changed offsets are recorded in the CSV correction log.)

**Every change is documented** in [`qa_correction_log.csv`](qa_correction_log.csv), including the original entity as a quoted string representation so trailing spaces are visible, original/corrected offsets, and full source message.

## Release checks performed

1. Matched all 200 source sentences against the provided original imported task dataset.
2. Compared each task's annotation count against the provided reference task-count file.
3. Confirmed every span falls within the original message and matches `source_text[start:end]`.
4. Confirmed every entity belongs to the defined taxonomy and each span has exactly one label.
5. Confirmed there are no overlapping spans or empty annotation spans.
6. Confirmed no entity has unintended leading or trailing whitespace.
7. Confirmed all non-`label` export fields are identical before and after cleaning.
8. Confirmed no entity category, annotation order, or task count changed.

## Release interpretation and limits

This is a **structural data-integrity and consistency audit**. It is not an independently verified gold-standard evaluation. Matching expected counts does not alone prove that every label is semantically correct; no second annotator or expert-adjudicated reference set was used. Metrics such as precision, recall, F1 score, and inter-annotator agreement are deliberately **not** claimed. The source examples are synthetic and relatively short/templated.

The final CSV is a clean **derived export**. Its `updated_at` field preserves the recorded Label Studio timestamp; it should not be represented as if this normalization were performed within Label Studio itself.

## Files validated

- [`../data/contractpulse_labelstudio_cleaned.csv`](../data/contractpulse_labelstudio_cleaned.csv)
- [`../data/contractpulse_entities.csv`](../data/contractpulse_entities.csv)
- [`../data/contractpulse_structured_records.csv`](../data/contractpulse_structured_records.csv)
- [`qa_correction_log.csv`](qa_correction_log.csv)
