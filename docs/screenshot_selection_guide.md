# Screenshot Evidence Guide

These are original screenshots supplied by the project author; files were copied into this repository without image edits.

| File | What it proves | README use |
|---|---|---|
| `01-project-completion.png` | All 200 tasks submitted in the data manager | Primary project-status evidence |
| `02-four-entity-contract-example.png` | COMPANY/LOCATION/DATE/MONEY extracted in one message | Main evidence |
| `03-person-company-payment-deadline.png` | PERSON/COMPANY/MONEY/DATE together | Main evidence |
| `04-multicurrency-vendor-quotation.png` | Naira-denominated vendor quote and work location | Additional evidence |
| `05-complete-company-name.png` | Complete company name rather than truncated proper noun | Main boundary evidence |
| `06-negative-reference-identifiers.png` | Invoice/PO identifiers correctly left unselected | Main negative-example evidence |
| `07-multiclass-procurement-deadline.png` | Company/person/location/date co-occurrence | Main evidence |
| `08-negative-unstructured-request.png` | Generic request correctly left without target entities | Optional second negative example |
| `09-supplier-briefing-and-date.png` | Supplier name, location and planned date | Additional evidence |
| `10-international-currency-and-deadline.png` | Named contact, business, euro amount and deadline | Additional evidence |
| `11-boundary-before-correction.png` | Earlier partial company-name span (`Quartzline`) | Optional QA before comparison, not a finished sample |
| `12-label-before-correction.png` | Earlier incorrect COMPANY assignment to a named person | Optional QA before comparison, not a finished sample |

**Recommended GitHub front page:** completion screenshot; one diverse 4-entity sample; one contact-and-payment sample; one reference-ID negative example; one corrected company-name example; one city/deadline example. Keep optional and historical QA screenshots in the evidence folder rather than displaying them all inline.

**Important distinction:** The screenshots depict Label Studio annotations. The 52 remaining trailing spaces were corrected **in the derived CSV**, not in the screenshots or saved Label Studio task state. The correction log and validation script document the exported-data cleanup. Never describe unmodified screenshots as evidence of a corrected Label Studio backend state.
