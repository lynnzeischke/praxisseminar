# Employee AI Readiness

Begleitmaterial zur Hausarbeit im Praxisseminar Master CMP. Das untersuchte Artefakt ist ein versionierter Masterprompt für die quellengebundene Fragebogenerstellung mit NotebookLM. Stand: 26.10.2026.

## Prüfweg

| Schritt | Unterlagen | Prüfzweck |
|---|---|---|
| 1 Artefakt ansehen | [Masterprompt R6.2](artefakt/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_2_NOTEBOOKLM.txt) · [Anleitung](artefakt/README.md) | Vollständige geprüfte Promptfassung einschließlich Design Audit |
| 2 Aktuellen Test prüfen | [Vollständiger R6.2-Lauf](evaluation/R6_2_Vollproduktion_2026-10-26/README.md) · [Erzeugter Fragebogen](evaluation/R6_2_Vollproduktion_2026-10-26/Fragebogen_B5.md) | Vorabplan, Originalantwort, JSON, externe Prüfung und Lesefassung des Fragebogens |
| 3 Evaluation einordnen | [Evaluationsübersicht](evaluation/README.md) | Basisvergleich, Einzelitemtests und Grenzen |
| 4 Entwicklung nachverfolgen | [Modellhistorie](MODELLHISTORIE.md) · [Iterationen](ITERATIONEN.md) | Frühere Artefakte und ihre Entwicklung |
| 5 Belege zuordnen | [Ablage und Hausarbeitsverweise](STRUKTUR.md) | Quellenpfade zu den Anhängen A bis D |

## Ergebnis

**R6.2 bleibt TEST_CANDIDATE.** Der vollständige Lauf vom 26.10.2026 enthält 18 eindeutige Messitems in sechs Dreiergruppen und besteht den implementierten JSON-Strukturcheck. Zugleich stehen B1–B5 doppelt in der Gesamtantwort; drei AISES-Wortlautanker nennen die falsche Tabelle. Die modellseitige Konformitätsmeldung ist deshalb nicht bestätigt.

Basis und R6.1 erreichen im kleinen Vergleich jeweils 21/24 Kriterien. R6.2 erreicht in den Einzelitem-Regressionen 22/24; ein angeleiteter Transferlauf erreicht 4/4. Diese Befunde belegen weder allgemeine Überlegenheit noch Robustheit oder psychometrische Validität.

## Belege nachrechnen

Vom Repository-Hauptordner aus; die Prüfer benötigen Python 3:

```sh
python3 evaluation/R6_2_Vollproduktion_2026-10-26/pruefe_gesamtantwort.py
python3 tools/check_output.py notebooklm_tests/NotebookLM_Ausgabe_R6_1.txt
python3 Nachweise/check_chat_evidence.py
```

Die Skripte prüfen archivierte Ausgaben. Sie ersetzen keine Originalquellenprüfung und erzeugen keine identischen neuen Modellantworten. Aktuelle Dateiintegrität: [SHA256SUMS.txt](SHA256SUMS.txt). Datierte frühere Prüflisten dokumentieren frühere Dateibäume.

## Umfang und Zugang

Die Hausarbeit wird separat abgegeben. Wissenschaftliche Verlags-PDFs und individuelle Befragtenantworten sind nicht enthalten. Die Eingabequellen des vollständigen Laufs sind im [Vorabplan](evaluation/R6_2_Vollproduktion_2026-10-26/Vorabplan.json) mit Dateinamen und Hashes dokumentiert. Prüfende benötigen Zugang zum privaten Repository; Notebook-Zugriff ist gesondert geregelt.

Die 50 dokumentierten Promptdateien und die ursprünglichen NotebookLM-Exporte bleiben als Belege erhalten. Die 24 historischen Chatdateien mit 66 Austauschen sind keine 24 unabhängigen Tests. Zusätzliche ChatGPT-Arbeitsprotokolle, ein ergänzender Chatauszug, die redaktionelle Chat-Zusammenfassung, Veröffentlichungshinweise und der alte visuelle Zeitstrahl wurden aus dem aktuellen Dateibaum entfernt. Frühere Git-Stände bleiben erhalten; negative Testergebnisse wurden nicht entfernt.

NotebookLM erzeugte Testantworten; ChatGPT unterstützte Entwicklung, Quellenabgleich, Kodierung und Redaktion; Python prüfte Dateien. Es wurden keine Human-Pretests oder psychometrischen Validierungen durchgeführt.
