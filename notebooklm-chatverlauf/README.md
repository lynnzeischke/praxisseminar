# NotebookLM-Chatverlauf

Vollständiger Export aller Chats aus dem NotebookLM-Projekt, in dem der
Masterprompt „Employee AI Readiness" ausgeführt und geprüft wurde.

## Übersicht

| Datei | Inhalt |
|---|---|
| `Projektuebersicht_Praxisseminar.md` | Haupt-Notebook-Chat zum Projekt Praxisseminar (Gesamtkontext, Fragen zur Fragebogenentwicklung). |
| `Design-Science-Framework.md` | Chat zur Herleitung des DSR-Rahmens für die Fragebogengenerierung. |
| `Design-Audits.md` | Chatverlauf zu den Design-Audit-Prüfungen (u. a. `…_001` PARTIAL PASS → `…_004_FINAL` freigegeben; Grundlage von `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`). |
| `Runmode_01-05.md` | Erste fünf Fragebogen-Generierungsläufe (`RUN_MODE = QUESTIONNAIRE_GENERATION`). |
| `Runmode_06.md` – `Runmode_18.md` | Weitere 13 Generierungsläufe zur Reproduzierbarkeitsprüfung desselben Masterprompts (entspricht dem Masterprompt V3.5-R6). |
| `Runmode_18_NOTEBOOKLM.md` | Eigener, separater Chat mit identischem Dateinamensmuster wie `Runmode_18.md` (im Download-Ordner ohne Leerzeichen im Namen) — entspricht tatsächlich dem Lauf gegen V3.5-R6.1, nicht R6. Nicht mit `Runmode_18.md` verwechseln. |
| `Stresstest_01_Aufgabenkontext.md` | Stresstest: TTF-Items ohne vorgegebenen Aufgabenkontext angefordert. |
| `Stresstest_02_Firmenkontext.md` | Stresstest: TTF-Items ohne vorgegebenen Firmenkontext angefordert. |
| `Stresstest_03_Mehrfachkriterien.md` | Stresstest: Items mit mehreren Kriterien / Konstrukt-Grenzfällen angefordert. |

## Befund (für Kap. 5 Evaluation der Hausarbeit relevant)

- In **18 von 18** Generierungsläufen (Runmode 01–18): Gesamtstatus
  `CONFORMANT_GENERATION`, `critic_status = PASS` für alle 18 reflektiven
  Kernitems sowie die Zusatzmodule `DIAGNOSTIC_NEEDS` und
  `DEMOGRAPHICS_MINIMAL`. Das spricht für die Reproduzierbarkeit des
  Masterprompt-Verhaltens über wiederholte, unabhängige NotebookLM-Sitzungen
  hinweg.
- In **allen 3 Stresstests**: Das Artefakt hat bei fehlendem
  Pflichtkontext (`TASK_CONTEXT`, Firmenkontext) korrekt die zugehörigen
  Hard Gates aktiviert (`HARD TTF GATE ACTIVE`, `HARD COMPANY CONTEXT GATE
  ACTIVE`, `GLOBAL HARD STOP GATE ACTIVE`) und **keine** Platzhalter- oder
  Beispiel-Items erzeugt — die Fail-Closed-Architektur hat sich damit unter
  gezielt adversarialen Bedingungen bewährt.
- Dies ergänzt die in `../artefakt/README.md` dokumentierten drei
  strukturgeprüften Kernläufe (R5 FAIL erwartet, R6 PASS, R6.1 PASS) um
  eine breitere Stichprobe realer NotebookLM-Sitzungen.

## Hinweis zur Vollständigkeit

Dieser Export ersetzt den früher vorgesehenen `.docx`-Export (siehe
Git-Historie); der Inhalt ist identisch in Markdown vorliegend. Prof.
Wichmann bleibt zusätzlich die Einladung zum NotebookLM-Projekt selbst
angeboten, sollte eine Live-Ansicht gewünscht sein.
