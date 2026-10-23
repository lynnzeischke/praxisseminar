# Employee AI Readiness – wissenschaftliche NotebookLM-Leitlinien

**Praxisseminar | Master CMP | Design Science Research**

Dieses Repository dokumentiert die iterative Entwicklung eines **Leitlinien-/Masterprompt-Artefakts**, das in **Google NotebookLM** einen wissenschaftlich nachvollziehbar abgeleiteten Fragebogen zur Employee AI Readiness kaufmännischer Mitarbeitender erstellen soll. Leitidee sind nachvollziehbare Quellenbindungen, feste Designgrenzen und eine unabhängige Prüfung der NotebookLM-Ausgabe – nicht eine behauptete empirische Validierung durch das Sprachmodell.

## Schnellzugriff

- **[Erweiterter Chat- und Entwicklungsverlauf](CHATVERLAUF.md)** – echte überlieferte Dialogzitate sowie als Rekonstruktion markierte frühere Entwicklungsphasen.
- **[Vollständiges Archiv früherer Masterprompt-Modelle](MODELLHISTORIE.md)** – 41 historische Promptdateien aus früheren Entwicklungszweigen.
- **[Vom Nutzer bereitgestellter früherer Chat-Auszug](chat_beleg/Vom_Nutzer_bereitgestellter_Chatauszug_R6_bis_Pretest.txt)** – unveränderter Belegauszug (kein Plattform-Rohdatenexport).
- **[Historische NotebookLM-Testbelege](evaluation/HISTORISCHE_MODELLTESTS.md)** – frühere Fehlzustände und Zuordnungsgrenzen.
- **[Iterations- und Evaluationsmatrix](ITERATIONEN.md)** – Probleme, Lösungsschritte, Testbefunde und Grenzen.
- **[Masterprompt V3.5-R6.1](artefakt/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_1_NOTEBOOKLM.txt)** – zuletzt getestete Prompt-Version mit integriertem freigegebenem Design Audit.
- **NotebookLM-Testausgaben:** [R5](notebooklm_tests/NotebookLM_Ausgabe_R5.txt) · [R6](notebooklm_tests/NotebookLM_Ausgabe_R6.txt) · [R6.1](notebooklm_tests/NotebookLM_Ausgabe_R6_1.txt).
- **[Änderungsprotokoll zu R6.1](evaluation/V3_5_R6_1_AENDERUNGSPROTOKOLL_UND_REGRESSION.md)**
- **[Reproduzierbare technische Prüfergebnisse](evaluation/TECHNISCHE_PRUEFERGEBNISSE.md)** – R5 FAIL, R6/R6.1 Struktur-PASS; wissenschaftliche Grenzen klar getrennt.
- **[Technischer JSON-Check](tools/check_output.py)** – kleine, unabhängig ausführbare Formatprüfung ohne Fremdbibliotheken.

## Entwicklungsstand und Versionsfamilien

Das Repository enthält neben dem zuletzt getesteten **R6.1** jetzt die tatsächlich vorhandenen Vorläufer aus den Familien **frühe Masterprompts (1.0 bis V8.1)**, **V8.x-Masterartefakte**, **OPERATIONAL V2–V3.5** sowie **AUTORUN R3–R6**. Sie sind als historische Belege archiviert, nicht als parallel aktivierte NotebookLM-Quellen. **Für neue Läufe nur R6.1 aktivieren.** Auch bei früher als `FINAL` benannten Dateien ist eine externe Freigabe oder psychometrische Validierung nicht belegt. Details: [MODELLHISTORIE.md](MODELLHISTORIE.md).

## Replikation mit NotebookLM

1. Neues NotebookLM-Notebook erstellen und die wissenschaftlichen Originalquellen **MAILS, AILRSE-5, AISES, AIRS und Lambiase et al.** sowie die für den theoretischen Kontext erforderlichen ergänzenden Papers als Quellen bereitstellen.
2. Den dokumentierten **FC-Originalitem-Auszug ohne Befragtendaten** ergänzen. Eine Kopie dieses Auszugs ist [hier](artefakt/NOTEBOOKLM_FC_ORIGINALITEMS_OHNE_TEILNEHMERDATEN.txt) enthalten, um die ursprünglichen Formulierungen kenntlich zu machen. Aus Vertraulichkeitsgründen **keine individuellen Antwortdaten auf GitHub hochladen**.
3. Als einzigen Masterprompt die Datei `artefakt/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_1_NOTEBOOKLM.txt` hochladen und auswählen. Der Original-Design-Audit ist darin unverändert integriert und muss nicht separat als zweite Prompt-Datei geladen werden.
4. Im Chat **genau diesen einen Befehl** eingeben:

   ```text
   Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.
   ```

5. Die Antwort sichern und die tatsächlich vorliegenden Quellenbelege überprüfen. Ein NotebookLM-eigenes `PASS` ersetzt **keine unabhängige fachliche Prüfung**. Zum technischen Check einer exportierten `.txt`-Datei:

   ```bash
   python tools/check_output.py notebooklm_tests/NotebookLM_Ausgabe_R6_1.txt
   ```

6. Für eine tatsächliche Unternehmensbefragung sind die rechtlich/organisatorisch nötigen Studien- und Datenschutzinformationen einzusetzen, ein echter kognitiver Pretest durchzuführen und erst danach ein empirisches Validierungskonzept zu beschließen.

## NotebookLM-Freigabelink

**Noch durch die projektverantwortliche Person einzutragen:** `NOTEBOOKLM_FREIGABELINK_HIER_EINFUEGEN`.

Ein Link wird nicht erfunden. Die Freigabe muss so eingestellt sein, dass die vorgesehenen Prüfenden das Notebook öffnen können und keine nicht zur Veröffentlichung vorgesehenen Daten offenliegen. Im Zweifel ist ein separater, bereinigter Publikations-Stand anzulegen.

## Wissenschaftliche Einordnung

Zielpopulation sind kaufmännische Mitarbeitende eines mittelständischen Unternehmens. Das Instrument enthält **18 reflektive Item-Kandidaten** in sechs dreiteiligen Konstrukten, davon fünf Readiness- und eine Kontext-Subskala; Bedarfsfragen und Minimaldemografie werden gesondert behandelt. Einzelne Items sind aus validierten Originalinstrumenten **kontextspezifisch abgeleitet/übersetzt** oder wurden theoriegeleitet neu entwickelt. Daraus folgt **nicht**, dass die zusammengesetzten deutschen Drei-Item-Kurzskalen bereits validiert sind.

Das Design folgt der übergeordneten Projektaufgabe zur DSR-Methode nach Peffers et al. (2007). Die in einem separaten Bewertungsbogen genannten Kriterien – Wissenschaftlichkeit, nachvollziehbare Operationalisierung, Problemlösungskompetenz, Kreativität, Forschungstransfer und Grenzen – werden anhand der Iterationen und der Quellenprüfungen adressiert, aber nicht allein durch das Repository als erfüllt erklärt.

**Literaturhinweis:** Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. Die vollständigen Literaturangaben der Itemquellen müssen in der Hausarbeit anhand der Originalpublikationen geprüft werden.

## Veröffentlichungs- und Authentizitätshinweis

Die Datei `CHATVERLAUF.md` ist **kein Rohdatenexport** des gesamten Chats. Sie enthält wörtliche Zitat-Auszüge aus dem vorliegenden Gespräch, einen vom Nutzer nachgereichten Teil-Auszug sowie klar gekennzeichnete **dateigestützt rekonstruierte frühere Entwicklungsphasen**. Es wurden keine fehlenden Chat-Turns erfunden. Unveränderte Originalexporte mit vollständigen Metadaten sind über die verwendeten Chat-Plattformfunktionen gesondert zu beschaffen, falls für den Nachweis verlangt.

Nicht enthalten: personenbezogene Befragtenantworten, SmartPLS-Rohdaten, vollständige wissenschaftliche Verlags-PDFs, unbereinigte Chat-Exporte oder vermeintliche Human-Pretestergebnisse.

## Stand

Version: **V3.5-R6.1 (`TEST_CANDIDATE`)**  
Status: technisch wiederholt demonstriertes Artefakt; **empirische Validierung und realer kognitiver Pretest stehen aus**.

## Zusätzliche Materialien (separat ergänzt)

- **[Visueller Entwicklungs-Zeitstrahl](artefakt/artefakt-zeitstrahl.html)** – Build-/Evaluate-Learn-Übersicht der gesamten Versionskette (im Browser öffnen).
- **[Vollständiger NotebookLM-Chatexport](notebooklm-chatverlauf/)** – 21 Rohexporte (Design Audits, 18 Generierungsläufe, 3 Stresstests), Grundlage der N01–N21-Zitate.
- **[ChatGPT-Entwicklungsprotokoll](chatgpt-entwicklungsprotokoll/)** – vollständiger Chatverlauf der Masterprompt-Entwicklung mit ChatGPT.
- **[Nachweise/](Nachweise/)** – Hash- und Textabgleich der NotebookLM-Rohexporte gegen die archivierten R5/R6/R6.1-Ausgaben (`check_chat_evidence.py`, `Chatbelege_Pruefergebnisse.json`).
