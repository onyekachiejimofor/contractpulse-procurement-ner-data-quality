# ContractPulse — Annotation Guidelines

## Objective
Identify complete, explicit spans of these five entity types in individual business communications. Do not infer an entity that is not present in the text.

| Label | Include | Exclude |
|---|---|---|
| `COMPANY` | Complete proper name of an organization, including a legal or branded suffix such as `Ltd`, `Foods`, `Advisory`, `Studio` | Generic references such as *our team*, *department*, or *the company* without an actual named company |
| `PERSON` | Complete explicitly named person, including given name and surname | Pronouns, generic positions such as *the coordinator*, *someone*, *manager* |
| `LOCATION` | Place name such as `Boston`, `Cape Town`, `Port Harcourt` | Generic *office*, *branch*, or *site* when they merely describe the place |
| `DATE` | Complete explicit date in the text, e.g. `2026-12-01`, `April 8, 2027`, `7 December 2026` | Vague temporal references such as *after the planning call* without a calendar date |
| `MONEY` | Explicit monetary amounts with currency units, e.g. `₦2,400,000`, `£1,250`, `USD 890`, `$420.50` | Generic financial terms such as *payment*, *invoice*, *budget* without an amount |

## Span rules
1. Highlight the **complete named entity**, not just its first word. `Quartzline Retail` is one company span.
2. Include multiword places as one span. `Port Harcourt` and `Cape Town` should not be split.
3. Include the currency symbol/code and the full numerical amount, including decimal digits when present.
4. Include the full date but exclude the trailing semicolon or sentence-ending period.
5. Exclude whitespace directly before or after the entity. Offset accounting is **zero-based; end is exclusive**.
6. Do not include a generic noun when the proper noun alone identifies the entity: `Nairobi` rather than `Nairobi office`.
7. Do not label invoice or purchase-order references such as `INV-2047` or `PO-918` as MONEY or DATE.
8. It is correct to submit **zero spans** when none of the five entity types occurs.
9. Keep the text unchanged; normalize annotations rather than changing the original business communication.

## Edge-case examples

| Text fragment | Correct interpretation | Reason |
|---|---|---|
| `Hassan Adeyemi at Maplecrest Advisory` | `Hassan Adeyemi` → PERSON; `Maplecrest Advisory` → COMPANY | A named person is not a company |
| `Quartzline Retail representatives` | `Quartzline Retail` → COMPANY | `Retail` is part of the proper company name; `representatives` is not |
| `Nairobi office` | `Nairobi` → LOCATION | `office` is a generic site descriptor |
| `the Manchester branch of Willowgate Foods` | `Manchester` → LOCATION; `Willowgate Foods` → COMPANY | Place and organization are distinct |
| `USD 6,800` | Whole string → MONEY | Currency and amount belong in one span |
| `please release payment` | No MONEY span | No numerical monetary amount |
| `The invoice number is INV-2047 and the reference is PO-918` | Zero target entities | These are reference identifiers |
| `after the planning call` | No DATE span | No explicit calendar value |

## Known limitations
This is a controlled five-label schema for synthetic short-form messages, not a universal NER taxonomy. Vendor IDs, invoice identifiers, product references, contract types, and named departments would require new labels and explicit guidelines in a future dataset.
