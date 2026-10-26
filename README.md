# Employee AI Readiness

Theoriegeleitete NotebookLM-Leitlinien für Fragebogenentwürfe · Praxisseminar Master CMP · Stand 26.10.2026.

Das zentrale Artefakt ist ein versionierter Masterprompt. Die Hausarbeit untersucht seine Entwicklung und formative Prüfung. Ein technisch konsistenter Fragebogenentwurf ist kein psychometrisch validiertes Messinstrument.

## Einstieg für Prüfende

| Gesucht | Einstieg |
|---|---|
| Ausführbares Leitlinienartefakt | [R6.2 TXT](artefakt/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_2_NOTEBOOKLM.txt) und [Anleitung](artefakt/README.md) |
| Vollständige R6.2-Generierung vom 26. Oktober | [Vorabplan, Originalantwort und externe Prüfung](evaluation/R6_2_Vollproduktion_2026-10-26/README.md) |
| Vergleich, Regressionen und historische Prüfungen | [Evaluationsübersicht](evaluation/README.md) |
| Vollständige Ablageübersicht | [Repository-Struktur](STRUKTUR.md) |

## Aktueller Befund

**R6.2 bleibt TEST_CANDIDATE.** Ein neuer vollständiger Lauf vom 26.10.2026 liefert 18 eindeutige Messitems in einem parsebaren JSON mit sechs Dreiergruppen. Der bisherige Strukturprüfer besteht. Die Gesamtantwort enthält jedoch B1–B5 doppelt, und drei AISES-Comfort-Wortlautanker nennen die Ladungstabelle statt der Wortlauttabelle. Die modellseitige Meldung CONFORMANT_GENERATION ist deshalb nicht bestätigt.

Die früheren Einzelitemtests vom 24.10.2026 erreichen 22/24 Kriterien; der angeleitete Transferlauf erreicht 4/4. Basis und R6.1 erreichen im kleinen Vergleich jeweils 21/24. Diese Ergebnisse belegen weder allgemeine Robustheit noch Überlegenheit, betriebliche Nützlichkeit oder psychometrische Güte.

## Nachvollziehen und nachrechnen

Der vollständige Originalprompt einschließlich Design-Audit steht unverändert in [artefakt/](artefakt/). Die Hausarbeit und ihre Word-Anhänge werden separat abgegeben und sind nicht Teil dieses Repositorys.

```bash
# Neue vollständige R6.2-Ausgabe nachrechnen
python3 evaluation/R6_2_Vollproduktion_2026-10-26/pruefe_gesamtantwort.py

# Historische R6.1-Ausgabe auf implementierte Strukturbedingungen prüfen
python3 tools/check_output.py notebooklm_tests/NotebookLM_Ausgabe_R6_1.txt

# Historischen Chat-/JSON-/Textabgleich wiederholen
python3 Nachweise/check_chat_evidence.py
```

Die Skripte prüfen gespeicherte Ausgaben. Sie reproduzieren keine identischen neuen Modellantworten und ersetzen keine fachliche Originalquellenprüfung. [Details und Grenzen](evaluation/README.md).

## Ablagelogik

- `artefakt/`: R6.2 als aktiver Testkandidat, FC-Auszug und historische R6.1-Referenz.
- `evaluation/`: Prüfberichte, Kodierungen und neue vollständige R6.2-Testbelege.
- `notebooklm_tests/`: unveränderte historische Vollausgaben R5/R6/R6.1.
- `notebooklm-chatverlauf/`: historische Exporte N01–N24 mit 66 Austauschen, keine 24 unabhängigen Tests.
- `modelle_historisch/`: ältere Promptfamilien; nicht parallel aktivieren.
- `tools/` und `Nachweise/`: vorhandene externe Prüfer.
- `chat_beleg/`, `chatgpt-entwicklungsprotokoll/`, `CHATVERLAUF.md`: ergänzende Entwicklungsdokumentation mit ihren jeweiligen Authentizitätsgrenzen.

Bestehende Nachweispfade bleiben erhalten. Git dokumentiert frühere Fassungen der Übersichtsdateien. Die historischen Prüfsummen vom 24. Oktober bleiben als datierter Snapshot erhalten; die aktuelle Liste enthält den erweiterten Stand und schließt sich selbst aus.

## Zugang und Quellen

Das Repository ist privat; Prüfende benötigen einen eingerichteten Zugang. Notebook-Links richten sich zusätzlich nach dem Google-Zugang. Freigabe- und Sichtbarkeitseinstellungen wurden durch diese Ergänzung nicht geändert.

Wissenschaftliche Original-PDFs, individuelle Befragtenantworten und SmartPLS-Rohdaten sind bewusst nicht enthalten. Die zwölf Eingabequellen des neuen Laufs sind im [Vorabplan](evaluation/R6_2_Vollproduktion_2026-10-26/Vorabplan.json) mit Dateinamen und Hashes dokumentiert. Die Originale sind über die im Literaturverzeichnis genannten Publikationen beziehungsweise die Modulunterlagen zu beschaffen.

Es wurden keine Human-Pretests oder psychometrischen Validierungen durchgeführt. NotebookLM erzeugte Testantworten; ChatGPT unterstützte Entwicklung, Quellenabgleich, Kodierung und Redaktion; Python prüfte Dateien und gespeicherte Ausgaben. Wissenschaftliche Bewertung und Verantwortung für die Einreichung verbleiben bei der Autorin.

[Historische Iterationen](ITERATIONEN.md) · [Modellhistorie](MODELLHISTORIE.md) · [Veröffentlichungshinweise](VEROEFFENTLICHUNG_HINWEISE.md).
