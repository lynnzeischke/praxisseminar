# MASTERPROMPT V2 – Änderungen nach Stress Test Round 01

| Stresstest-Befund | Ursache | Änderung in V2 | Erwarteter Effekt |
|---|---|---|---|
| ST01: Bei fehlenden Pflichtinputs erschienen teils trotzdem Beispielitems | STOP war nur als „nicht finalisieren“ formuliert | GLOBAL HARD STOP GATE + präzisierte Missing-Input-Regel | Bei fehlendem M1/M2/M3 keinerlei Item-Wording |
| ST03: TTF trotz fehlendem TASK_CONTEXT als Prototyp ausgegeben | Explorative Ausnahme umging STOP | HARD TTF GATE | Ohne Taskdaten keinerlei TTF-Item, auch nicht Beispiel/Prototype |
| ST04: Unternehmensrichtlinie/Schulung hypothetisch vorausgesetzt | `context_verified=pending` erlaubte faktische Vorannahmen | HARD COMPANY CONTEXT GATE | Keine firmenspezifischen Itemannahmen ohne CONTEXT_TEXT |
| ST06: E3 korrekt klassifiziert, aber double-barreled und falscher Translation-Status | Evidenzklasse wurde mit Itemqualität/Übersetzung vermischt | E3 QUALITY GATE + Translation-Status-Mapping | E3 muss Agent 2 bestehen; deutsches E3 = NOT_NEEDED |
| Uneinheitliche STOP-Wirkung | Global-, Modul- und Itemfehler waren vermischt | Stop/Gate-Regeln in drei Ebenen getrennt | Fehlende Task-/Kontextdaten blockieren nur betroffene Module |

**Retest-Pflicht:** ST01, ST03, ST04 und ST06 erneut ausführen. Erst bei PASS aller vier Tests zur QUESTIONNAIRE_GENERATION übergehen.
