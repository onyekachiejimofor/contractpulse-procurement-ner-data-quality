# Data Dictionary and CSV Usage

## Primary Label Studio export: `data/contractpulse_labelstudio_cleaned.csv`
The primary file retains **all 12 source columns** and their values except for normalizing excess entity-edge whitespace inside the JSON in the `label` column. When a span was modified, its character offset was adjusted accordingly.

| Column | Meaning | Status |
|---|---|---|
| `annotation_id` | Label Studio annotation identifier | Preserved |
| `annotator` | Label Studio annotator identifier | Preserved |
| `confidence` | Optional custom confidence field | Preserved blank; not invented |
| `created_at` | Annotation creation timestamp | Preserved |
| `id` | Label Studio internal task ID | Preserved |
| `label` | Serialized JSON array of labeled text spans, with `start`, `end`, `text`, and `labels` | Cleaned at 52 boundaries; no label changes |
| `lead_time` | Label Studio interaction duration metadata | Preserved; not used to claim productivity |
| `review_note` | Optional review note field | Preserved blank; not invented |
| `task_id` | Project reference such as `NER-0001` | Preserved |
| `text` | Original complete business message | Preserved verbatim |
| `updated_at` | Label Studio last-update timestamp | Preserved verbatim, not artificially incremented |
| `your_spans_json` | Optional task-data field | Preserved as found; do not confuse with `label` |

**Offset convention:** Python/Label Studio character offsets are zero-based; `start` is inclusive and `end` is exclusive. `text[start:end] == span.text` for every cleaned annotation.

## Flattened entity register: `data/contractpulse_entities.csv`
One entity per row; 650 rows. Fields: `task_id`, `entity_number`, `entity_type`, `entity_text`, `start_offset`, `end_offset`, `source_text`. This is useful for inspecting entities, filtering types, and validating traceability.

## Structured business records: `data/contractpulse_structured_records.csv`
One communication per row; 200 rows. Fields: `task_id`, `source_message`, `company`, `person`, `location`, `date`, `money`, `entity_count`, `no_target_entities`.

Any future record with multiple values of a single entity type is represented by a ` | ` separator in the relevant wide column. This delimiter is a display convention, not a recommended enterprise database design; the entity register is the lossless representation of multiple spans. A blank entity cell means **not detected in text**, not that a real-world entity is known to be absent.

## Excel / Google Sheets usage
Open CSV files using UTF-8 encoding so `₦`, `£`, and `€` render correctly. Preserve `task_id` as text and all monetary amounts as **text** until the currency and locale are explicitly parsed. Do not treat `lead_time` as a verified operational throughput metric.
