# Business Use Case — Procurement and Vendor Operations

## Scenario
A procurement operations team receives short messages discussing quotations, vendor meetings, inspections, payment instructions, and delivery milestones. Critical information is embedded in narrative text rather than typed into consistent database fields.

## Stakeholder questions
- Which supplier or organization is involved?
- Which named person should be contacted?
- Which city, branch, or work site is mentioned?
- Which explicit calendar dates require attention?
- What amount and currency is being discussed?

## Current pain points the case study models
Manual transcription can miss complete organization names, accidentally treat invoice reference numbers as financial values, select incomplete dates, or introduce whitespace around named entities. These errors can affect matching, filtering, and downstream processing.

## Demonstrated workflow
**Unstructured message → NER labeling → span/offset QA → corrected structured export → business-review-ready columns.**

The provided structured-record file demonstrates one possible downstream representation; the entity-register file preserves exact traceability to source text. This allows a reviewer to check how each business field was obtained.

## What could come next
- Enrich vendor master data after matching extracted companies against verified internal vendor IDs.
- Display payment or quotation amounts in a review queue, subject to currency validation.
- Create a human-reviewed calendar or deadline index from extracted dates.
- Index communications for procurement search and routing.

These are future applications, not deployed features. A production rollout would require access permissions, PII safeguards, data retention policies, document-level evaluation, and human approval for financial actions.
