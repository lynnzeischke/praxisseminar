#!/usr/bin/env python3
"""Minimaler unabhängiger Strukturcheck für eine NotebookLM-B7-Ausgabe.

WICHTIG: Prüft nur parsebare JSON-Struktur und ausgewählte Designrestriktionen,
keine Originalitemtreue oder psychometrische Validität.
"""
import json, pathlib, re, sys, collections

EXPECTED={"READINESS_CORE_LIT", "READINESS_CORE_LEARN", "READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT", "CONTEXT_FC"}

def run(path):
    s=path.read_text(encoding='utf-8-sig')
    blocks=re.findall(r'```json\s*(\{[\s\S]*?\})\s*```', s, flags=re.IGNORECASE)
    if len(blocks)!=1: raise AssertionError(f'Erwartet genau einen JSON-Block, gefunden {len(blocks)}')
    j=json.loads(blocks[0]); items=j['items']
    assert len(items)==18, f'Itemzahl {len(items)} statt 18'
    ids=[i['item_id'] for i in items]
    assert len(set(ids))==18,'Nicht eindeutige Item-IDs'
    c=collections.Counter(i['construct_code'] for i in items)
    assert set(c)==EXPECTED and all(x==3 for x in c.values()), f'Konstruktverteilung fehlerhaft: {dict(c)}'
    assert j['metadata']['overall_score_supported'] is False, 'Gesamtscore unzulässig'
    routing=j['routing']
    for group in ('NO_EXPERIENCE','LIMITED_EXPERIENCE','REGULAR_USER'):
        assert group in routing, f'Routinggruppe fehlt: {group}'
    ne=routing['NO_EXPERIENCE']; include=ne['included_modules']; skip=ne['skipped_modules']
    assert {'READINESS_CORE_LIT','READINESS_CORE_LEARN','CONTEXT_FC','DIAGNOSTIC_NEEDS','DEMOGRAPHICS_MINIMAL'}<=set(include)
    assert {'READINESS_CORE_APPLY','READINESS_CORE_DETECT','READINESS_CORE_COMFORT'}==set(skip)
    e3=[i for i in items if i['evidence_class']=='E3']
    assert len(e3)==1 and e3[0]['item_id']=='DETECT_03'
    assert e3[0]['source_evidence'].get('source_item_id') is None
    for i in items:
        if i['construct_code']=='CONTEXT_FC':
            assert (i.get('additional_response_option_coding') or i.get('source_evidence',{}).get('additional_response_option_coding'))=='MISSING_NOT_SCORED'
    print(f'PASS: JSON parsebar; {len(items)} Items; sechs 3er-Konstrukte; Routing/E3/FC und kein Gesamtscore. Datei: {path}')
    print('HINWEIS: Kein Beweis für korrekte Quellen, Itemvalidität, kognitiven Pretest oder wissenschaftliche Freigabe.')

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Aufruf: python tools/check_output.py PATH_ZUR_NOTEBOOKLM_DATEI')
    run(pathlib.Path(sys.argv[1]))
