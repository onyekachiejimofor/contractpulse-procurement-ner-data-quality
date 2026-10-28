# GitHub Publication Guide

## Suggested repository name
`contractpulse-procurement-ner-data-quality`

## Repository description (copy-ready)
Business-focused NER portfolio: 200 procurement communications, 650 manually labeled entities, structured vendor records, and reproducible annotation QA.

## Recommended GitHub topics
`named-entity-recognition` · `label-studio` · `data-annotation` · `data-quality` · `information-extraction` · `procurement` · `vendor-management` · `nlp` · `data-operations` · `entity-extraction`

## Recommended upload order
1. Create a new public GitHub repository using the suggested name. Leave "Initialize with README" unchecked if you plan to upload this package's README.
2. Unzip the portfolio package. Upload the **contents** of the folder (README.md, data/, docs/, evidence/, scripts/), preserving the directory structure. Do not upload the zip as the only file.
3. Verify all screenshots render correctly in the README and that the CSV files are present.
4. Add the description and topics from this guide in repository settings.
5. Decide whether you want to permit reuse, and if so, choose a suitable license; no license has been assigned automatically.

## Accuracy in the portfolio narrative
Use these formulations:
- **200/200 tasks completed** in Label Studio.
- **650 manually identified entity spans across five categories**.
- **20 deliberate no-target-entity cases**.
- **52 leading/trailing-boundary issues corrected in the derived CSV** (all 52 were trailing spaces in the last export).
- **0 remaining whitespace or offset mismatches under structural validation**.

Avoid presenting the output as an independently verified 100%-accurate NER dataset, a trained AI model, or an integration already operating for real clients.
