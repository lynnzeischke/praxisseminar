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
| Historischer Masterprompt mit gespeicherten Strukturprüfungen | `V3.5-R6.1` (Evidence-Locked) |
| Design Audit | `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL` |
| Gespeicherte, extern strukturgeprüfte Kernläufe | R5 (Schema-FAIL; zusätzlich inhaltlicher Routingfehler dokumentiert), R6 (PASS), R6.1 (PASS; B2/B5/B7 wortlautidentisch) |
| Weitere historische Generierungsläufe | Modellinterne `CONFORMANT_GENERATION`-Angaben, mit dokumentierten Gegenfällen (N10, N16) und nicht lückenlos blockierten Stresstests (N04); differenzierter Befund in `../notebooklm-chatverlauf/README.md` |
| Start-Kommando für die Demonstration | `Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.` |

## Aktueller geprüfter Testkandidat R6.2

[R6.2 herunterladen](MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_2_NOTEBOOKLM.txt) ·
[Prüfbericht und Testnachweise](../evaluation/R6_2_PRUEFBERICHT.md)

Stand 24.10.2026: Drei neue Einzelitem-Regressionsläufe erzielen **22/24**
Kriterienerfüllungen (8/8, 7/8, 7/8), ein separater angeleiteter Transferlauf
**4/4**. Die deutsche E1-Verifikation und die E3-Klassifikation wurden verbessert;
Quellen-/Fundstellenfehler und methodische Nebenfehler bleiben dokumentiert.
**TEST_CANDIDATE; keine allgemeine Freigabe.** Die vollständige 18-Item-Produktion
wurde für R6.2 noch nicht getestet. R6.1 bleibt als historische Referenz erhalten.
Nie R6.1 und R6.2 gleichzeitig als aktive Governance-Quelle auswählen.

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
