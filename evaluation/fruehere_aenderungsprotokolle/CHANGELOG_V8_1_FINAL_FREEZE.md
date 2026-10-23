# CHANGELOG V8.1 – FINAL FREEZE

V8.1 ergänzt V8 gezielt, ohne die Kernarchitektur erneut umzubauen.

## Neu
1. `RUN_MODE`: DESIGN_AUDIT / QUESTIONNAIRE_GENERATION / FULL_PIPELINE.
2. `INSTRUMENT_PURPOSE`: DIAGNOSTIC / RESEARCH_MODEL.
3. Exaktes Item-Provenienzmodell mit `source_locator`, `source_item_id`, `source_item_text_verified`.
4. Admission-Gate für `READINESS_CORE`: Definition + Itemquelle; E3 nur explorativ mit hohem Evidenzrisiko.
5. Experience-Routing für NO_EXPERIENCE / LIMITED_EXPERIENCE / REGULAR_USER.
6. Evidence Conflict Log für widersprüchliche Quellen.
7. Zweckabhängige Konstruktauswahl: Diagnose vs. Forschungsmodell.
8. Reproduzierbarkeits-Metadaten um Run Mode und Instrument Purpose erweitert.
9. JSON-Schema um Provenienz- und Evidenzrisikofelder erweitert.
10. Freeze-Status: Weitere Änderungen nur noch nach dokumentierter Evaluation.

## Unverändert eingefroren
- READINESS_CORE / CONTEXT / RELATED_CONSTRUCT / OUTCOME
- E1–E4
- fünf Modul-Papers + METHOD_SOURCE
- Module Paper Coverage Gate
- Design Requirements
- Methodiker → Kritiker → simulierter Proband
- Originalskalen-Audit
- Generic/Contextualized als Kandidaten
- maximal drei Iterationen
- kein automatischer Gesamtscore
- Audit-Dossier + Teilnehmerfragebogen + JSON
