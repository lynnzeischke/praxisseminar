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

**Korrigiert am 23.10.2026:** Eine frühere Fassung dieses Abschnitts behauptete
pauschal „18 von 18 Generierungsläufen CONFORMANT_GENERATION" und „alle 3
Stresstests korrekt blockiert". Das widersprach den in der Hausarbeit (Kap. 5)
selbst dokumentierten Gegenfällen und wurde durch den tatsächlichen Chat-Inhalt
widerlegt. Der folgende Befund ist differenziert und deckt sich mit Hausarbeit
Kap. 5 / Anhang B.

- **Generierungsläufe (Runmode 01–18, N07–N21):** Die Mehrheit der Läufe
  meldet `CONFORMANT_GENERATION` mit 18 geprüften Kernitems. Es gibt jedoch
  dokumentierte Gegenfälle, in denen das gemeldete Modellurteil die
  tatsächliche Ausgabe nicht trägt:
  - **N10 (`Runmode_08.md`):** Die JSON-Itemliste enthält nur **6** statt 18
    Objekte; `all_hard_checks_pass` steht trotzdem auf `true`.
  - **N16 (`Runmode_14.md`):** Es fehlt eine Top-Level-Itemliste vollständig,
    während die Metadaten 18 Items behaupten.
  - **N15 (`Runmode_13.md`):** Enthält nur Titel, Notebook-URL und
    Exportzeitpunkt; daraus lässt sich kein Testergebnis ableiten.
  - Für die strukturgeprüften Kernläufe R5/R6/R6.1 (N19–N21) siehe
    `../evaluation/TECHNISCHE_PRUEFERGEBNISSE.md` und
    `../Nachweise/Chatbelege_Pruefergebnisse.json` (R5 FAIL erwartet, R6/R6.1
    PASS, unabhängig reproduziert).
- **Stresstests (N04–N06):** Kein pauschaler Blockierungserfolg.
  - **N04 (`Stresstest_01_Aufgabenkontext.md`):** Das Modell erklärt zwar
    einen Stopp bei fehlendem `TASK_CONTEXT`, liefert in Austausch 2
    anschließend trotzdem drei explorative TTF-Items und setzt in Austausch 3
    interne Richtlinien/Schulungen als Firmenkontext voraus, obwohl diese
    Angaben fehlten. Der Vorbehalt `context_verified = pending` verhindert
    die unbelegte Ausgabe nicht.
  - **N05, N06:** siehe Hausarbeit Kap. 5 für die jeweilige Einzelauswertung.
  - Die Fail-Closed-Architektur greift damit nicht lückenlos; das ist in der
    Hausarbeit explizit als Grenze des Artefakts benannt, nicht als Erfolg.
- Modellinterne Konformitäts- oder PASS-Meldungen sind daher kein
  Vollständigkeits- oder Qualitätsnachweis — erst der Abgleich mit dem
  tatsächlichen Inhalt (Itemanzahl, Itemtext, Routinglogik) entscheidet.

## Hinweis zur Vollständigkeit

Dieser Export ersetzt den früher vorgesehenen `.docx`-Export (siehe
Git-Historie); der Inhalt ist identisch in Markdown vorliegend. Prof.
Wichmann bleibt zusätzlich die Einladung zum NotebookLM-Projekt selbst
angeboten, sollte eine Live-Ansicht gewünscht sein.
