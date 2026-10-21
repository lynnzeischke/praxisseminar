# Artefakt-Referenzen

Dieses Verzeichnis dokumentiert die für die Hausarbeit relevanten
Artefakt-Kennungen. Die vollständigen Dateien (Masterprompt-Fassungen,
NotebookLM-Ausgaben, Regressionsprüfungen) liegen bei der Verfasserin vor
und werden vor Abgabe auf Vollständigkeit und Zugänglichkeit geprüft.

- [`artefakt-zeitstrahl.html`](./artefakt-zeitstrahl.html) – visueller
  Zeitstrahl der gesamten DSR-Entwicklung (Build-Versionsketten,
  Evaluate→Learn-Schleife R1–R6.1, Reproduzierbarkeits- und
  Stresstest-Befunde), rekonstruiert aus dem ChatGPT-Entwicklungsprotokoll,
  den realen Masterprompt-/Master-Artefakt-Dateien und dem vollständigen
  NotebookLM-Chatexport (siehe `../notebooklm-chatverlauf/`). Im Browser
  öffnen (HTML-Datei).

| Kennung | Wert |
|---|---|
| Masterprompt (finale, extern strukturgeprüfte Fassung) | `V3.5-R6.1` (Evidence-Locked) |
| Design Audit | `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL` |
| Gespeicherte, extern strukturgeprüfte Kernläufe | R5 (FAIL, erwartet — korrektes Gate-Blockierverhalten), R6 (PASS), R6.1 (PASS; B2/B5/B7 wortlautidentisch) |
| Zusätzliche Reproduzierbarkeitsläufe | 18/18 Generierungsläufe `CONFORMANT_GENERATION`, 3/3 Stresstests korrekt blockiert (siehe `../notebooklm-chatverlauf/README.md`) |
| Start-Kommando für die Demonstration | `Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.` |

## Verwendete Hilfsmittel (Transparenz)

- **Google NotebookLM**: quellenbasierte Demonstration (Ausführung des
  Masterprompts, Generierung des Fragebogen-Outputs). Chatverlauf-Export
  siehe `../notebooklm-chatverlauf/`.
- **ChatGPT**: Entwicklung, Reflexion, redaktionelle Bearbeitung und
  technische Prüfung der Artefakte während der Entwicklung. Vollständiger
  Chatverlauf siehe `../chatgpt-entwicklungsprotokoll/`.

Siehe Hausarbeit, Anhang "Projektinterne Nachweise und Werkzeuge" sowie
die Eigenständigkeitserklärung für die vollständige Offenlegung der
KI-Nutzung.
