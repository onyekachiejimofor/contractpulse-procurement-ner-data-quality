#!/usr/bin/env python3
"""Non-destructively trim whitespace at NER span boundaries in a Label Studio CSV export.

Usage: python scripts/normalize_labelstudio_export.py INPUT.csv OUTPUT.csv
Requires only Python 3 standard library. Never modifies the input file.
"""
from pathlib import Path
import sys, csv, json

def clean(source,output):
    with source.open(encoding='utf-8-sig',newline='') as inp:
        rd=csv.DictReader(inp);fields=list(rd.fieldnames);rows=list(rd)
    fixed=0
    for row in rows:
        spans=json.loads(row['label'] or '[]')
        changed=False
        for sp in spans:
            t=sp['text'];leading=len(t)-len(t.lstrip());trailing=len(t)-len(t.rstrip())
            if leading or trailing:
                sp['start']+=leading;sp['end']-=trailing;sp['text']=t.strip()
                assert row['text'][sp['start']:sp['end']]==sp['text']
                fixed+=1;changed=True
        if changed:row['label']=json.dumps(spans,ensure_ascii=False,separators=(',',':'))
    with output.open('w',encoding='utf-8-sig',newline='') as out:
        wr=csv.DictWriter(out,fieldnames=fields,lineterminator='\n');wr.writeheader();wr.writerows(rows)
    print(f'Normalized {fixed} spans across {len(rows)} tasks. Input left unchanged.')
if __name__=='__main__':
    if len(sys.argv)!=3:raise SystemExit('Usage: normalize_labelstudio_export.py INPUT.csv OUTPUT.csv')
    source,output=map(Path,sys.argv[1:]);
    if source.resolve()==output.resolve():raise SystemExit('Input and output must be different files.')
    clean(source,output)
