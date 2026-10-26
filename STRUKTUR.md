# Ablage und Nachweise

| Bereich | Zweck | Status |
|---|---|---|
| [artefakt](artefakt/README.md) | Ausführbare R6.2-Governance, R6.1-Referenz, FC-Auszug | R6.2 TEST_CANDIDATE |
| [evaluation](evaluation/README.md) | Evaluationsübersicht; Einzelitem- und Vollproduktion getrennt | Neue Vollproduktion vom 26.10.2026 ergänzt |
| [notebooklm_tests](notebooklm_tests/) | Gespeicherte Vollausgaben R5/R6/R6.1 | Historische Belege |
| [notebooklm-chatverlauf](notebooklm-chatverlauf/) | N01–N24, ursprüngliche Exporte | 66 Austausche, keine unabhängige Testserie |
| [modelle_historisch](modelle_historisch/) | Frühere Versionen und Versionsfamilien | Unverändert archiviert |
| [tools](tools/) und [Nachweise](Nachweise/) | Bestehende unabhängige Struktur- und Textprüfer | Prüfgrenzen in den Berichten |

## Referenzzuordnung der Hausarbeit

- Kapitel 2 und Anhang D: R6.2 in `artefakt/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_2_NOTEBOOKLM.txt`.
- Anhang A: Versionsübersicht, `MODELLHISTORIE.md` und `modelle_historisch/`.
- Anhang B: `notebooklm-chatverlauf/`, `notebooklm_tests/`, `Nachweise/check_chat_evidence.py` und `Chatbelege_Pruefergebnisse.json`.
- Anhang C1–C3: `evaluation/R6_2_PRUEFBERICHT.md`, `R6_2_KODIERUNG.csv`, `R6_2_ERGEBNISSE.json` und das vollständige damalige `R6_2_TESTNACHWEISE.zip` (enthält auch den ergänzenden Basisvergleich).
- Anhang C4: `evaluation/R6_2_Vollproduktion_2026-10-26/` mit Originalantwort, Vorabplan und Prüfer.
- Anhang D wird lokal mit der Hausarbeit abgegeben; seine unveränderte Textquelle liegt unter `artefakt/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_2_NOTEBOOKLM.txt`.

Die zuvor lokal verwendeten Ordnernamen `Nachweise/Promptarchiv` und `Ergänzendes_Nachweispaket` beziehen sich auf das lokale Abgabepaket. Im Repository sind dieselben Nachweisfamilien den bestehenden Bereichen `modelle_historisch/`, `artefakt/` und `evaluation/` zugeordnet. Für den aktuellen vollständigen Lauf gilt der oben genannte eindeutige Pfad.

## Umfang der Ablage

Das Repository bündelt die Projektartefakte und die gesicherten Prüfbelege. Die Hausarbeit und ihre Word-Anhänge werden separat abgegeben. Wissenschaftliche Verlags-PDFs und individuelle Befragtenantworten sind nicht Teil des Repositorys. GitHub-Zugriff und Notebook-Zugriff sind getrennte Berechtigungen. Frühere Aussagen in historischen Berichten werden durch die aktuellen Prüfberichte eingeordnet, nicht rückwirkend zu bestätigten Befunden erklärt.

## Bereinigung am 26 Oktober 2026

Aus dem aktuellen Dateibaum wurden sechs ergänzende Arbeits- und Darstellungsdateien entfernt. Unveränderte Primärartefakte, ursprüngliche NotebookLM-Exporte und sämtliche zitierten Testnachweise bleiben erhalten. Die entfernten Dateien sind im vorherigen Git-Stand wiederherstellbar. Die aktuelle Prüfsummenliste bildet ausschließlich den bereinigten Stand ab; frühere Listen unter evaluation/ sind historische Snapshots.


## Duplikate in modelle_historisch

`modelle_historisch/` enthält sechs Dateipaare mit inhaltsgleichem Text (per Git-Blob-Hash geprüft, nicht nur am Dateinamen erkannt):

| Datei A | Datei B |
|---|---|
| `operational/MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_FINAL.md` | `operational/MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_FINAL_Kopie.md` |
| `operational/MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V3_5_SOURCE_CLOSURE_FINAL_TEST_CANDIDATE.md` | `operational/MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V3_5_SOURCE_CLOSURE_FINAL_TEST_CANDIDATE_Kopie.md` |
| `operational/MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V3_FINAL.md` | `operational/MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V3_FINAL.txt` |
| `masterartefakt_v8/MASTER_ARTEFAKT_Employee_AI_Readiness_V8_4_11_TEST_CANDIDATE.md` | `masterartefakt_v8/MASTER_ARTEFAKT_Employee_AI_Readiness_V8_4_11_TEST_CANDIDATE_Kopie.md` |
| `autorun_r3_bis_r6/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_INTEGRATED_AUDIT_AUTORUN_OUTPUT_LOCKED_NOTEBOOKLM.txt` | `autorun_r3_bis_r6/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_INTEGRATED_AUDIT_AUTORUN_OUTPUT_LOCKED_TEST_CANDIDATE.md` |
| `artefakt/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_1_NOTEBOOKLM.txt` | `autorun_r3_bis_r6/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_1_INTEGRATED_AUDIT_EVIDENCE_LOCKED_TEST_CANDIDATE.md` |

Ähnlich benannte, aber **inhaltlich unterschiedliche** Dateien (z. B. `..._SOURCE_CLOSURE_TEST_CANDIDATE.md` vs. `..._SOURCE_CLOSURE_TEST_CANDIDATE_Kopie.md`, ohne „FINAL") sind keine Duplikate und wurden entsprechend nicht zusammengeführt.

Die Duplikate stammen aus dem iterativen Entwicklungsprozess (parallele Arbeitskopien, Exportbenennungen) und wurden bewusst nicht bereinigt: Die Hausarbeit (Anhang A, Modellhistorie) verlinkt jede Datei in `modelle_historisch/` einzeln über ihren GitHub-Blob-Pfad. Ein Löschen würde diese bereits gesetzten Verweise ungültig machen. Die Dopplung ist damit ein dokumentiertes Merkmal des Archivs, kein unbeabsichtigter Rest.

