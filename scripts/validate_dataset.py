#!/usr/bin/env python3
"""Validate ContractPulse cleaned CSV and derived entity files. Python 3 stdlib only."""
from pathlib import Path
import csv, json, collections
ROOT=Path(__file__).resolve().parent.parent

def rows(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

source=rows(ROOT/'data/contractpulse_labelstudio_cleaned.csv')
entities=rows(ROOT/'data/contractpulse_entities.csv')
structured=rows(ROOT/'data/contractpulse_structured_records.csv')
allowed={'COMPANY','PERSON','LOCATION','DATE','MONEY'}
expected={'COMPANY':160,'PERSON':140,'LOCATION':120,'DATE':110,'MONEY':120}
assert len(source)==len(structured)==200
assert len(entities)==650
assert len(set(r['task_id'] for r in source))==200
counts=collections.Counter(); zeros=0
for r in source:
    spans=json.loads(r['label'] or '[]')
    if not spans: zeros+=1
    previous_end=0
    for sp in sorted(spans,key=lambda a:a['start']):
        assert 0<=sp['start']<sp['end']<=len(r['text'])
        assert sp['start']>=previous_end
        previous_end=sp['end']
        assert r['text'][sp['start']:sp['end']]==sp['text']
        assert sp['text']==sp['text'].strip()
        assert len(sp['labels'])==1 and sp['labels'][0] in allowed
        counts[sp['labels'][0]]+=1
assert counts==expected,(counts,expected)
assert zeros==20
assert sum(int(r['entity_count']) for r in structured)==650
assert sum(r['no_target_entities']=='yes' for r in structured)==20
assert sum(1 for r in structured if int(r['entity_count'])==4)==110
assert sum(1 for r in structured if int(r['entity_count'])==3)==70
for e in entities:
    assert e['entity_type'] in allowed
    assert e['source_text'][int(e['start_offset']):int(e['end_offset'])]==e['entity_text']
print('PASS: 200 tasks, 650 entities, 20 negative tasks, clean offsets and boundaries.')
print('By label: '+', '.join(f'{k}={counts[k]}' for k in sorted(counts)))
