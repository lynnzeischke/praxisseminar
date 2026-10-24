# Employee AI Readiness – wissenschaftliche NotebookLM-Leitlinien

**Praxisseminar | Master CMP | Design Science Research**

Dieses Repository dokumentiert die iterative Entwicklung eines **Leitlinien-/Masterprompt-Artefakts**, das in **Google NotebookLM** einen wissenschaftlich nachvollziehbar abgeleiteten Fragebogen zur Employee AI Readiness kaufmännischer Mitarbeitender erstellen soll. Leitidee sind nachvollziehbare Quellenbindungen, feste Designgrenzen und eine unabhängige Prüfung der NotebookLM-Ausgabe – nicht eine behauptete empirische Validierung durch das Sprachmodell.

## Geprüfte Weiterentwicklung vom 24 Oktober 2026

- **[Aktueller Testkandidat R6.2](artefakt/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_2_NOTEBOOKLM.txt)**
- **[Prüfbericht R6.2](evaluation/R6_2_PRUEFBERICHT.md)** und **[vollständige Testnachweise](evaluation/R6_2_TESTNACHWEISE.zip)**
- Drei neue Einzelitemläufe: **22/24** Kriterienerfüllungen (8/8, 7/8, 7/8).
  Historische R6.1-Serie: 21/24. Bekannte Fälle und zeitlich getrennte kleine
  Serien erlauben keinen allgemeinen Wirksamkeitsnachweis. Ein separater
  angeleiteter Transferlauf erfüllt 4/4 Kriterien.
- R6.2 bleibt **TEST_CANDIDATE**. Offene Quellen-/Fundstellenfehler und
  methodische Nebenfehler sind dokumentiert; eine neue vollständige
  18-Item-Generierung ist noch nicht geprüft. Die unten beschriebene
  vollständige Demonstration bezieht sich auf das historische R6.1.

## Schnellzugriff

- **[Erweiterter Chat- und Entwicklungsverlauf](CHATVERLAUF.md)** – echte überlieferte Dialogzitate sowie als Rekonstruktion markierte frühere Entwicklungsphasen.
- **[Vollständiges Archiv früherer Masterprompt-Modelle](MODELLHISTORIE.md)** – 41 historische Promptdateien aus früheren Entwicklungszweigen.
- **[Vom Nutzer bereitgestellter früherer Chat-Auszug](chat_beleg/Vom_Nutzer_bereitgestellter_Chatauszug_R6_bis_Pretest.txt)** – unveränderter Belegauszug (kein Plattform-Rohdatenexport).
- **[Historische NotebookLM-Testbelege](evaluation/HISTORISCHE_MODELLTESTS.md)** – frühere Fehlzustände und Zuordnungsgrenzen.
- **[Iterations- und Evaluationsmatrix](ITERATIONEN.md)** – Probleme, Lösungsschritte, Testbefunde und Grenzen.
- **[Masterprompt V3.5-R6.1](artefakt/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_1_NOTEBOOKLM.txt)** – historische Referenz mit gespeichertem Fragebogenlauf und integriertem Design Audit.
- **NotebookLM-Testausgaben:** [R5](notebooklm_tests/NotebookLM_Ausgabe_R5.txt) · [R6](notebooklm_tests/NotebookLM_Ausgabe_R6.txt) · [R6.1](notebooklm_tests/NotebookLM_Ausgabe_R6_1.txt).
- **[Änderungsprotokoll zu R6.1](evaluation/V3_5_R6_1_AENDERUNGSPROTOKOLL_UND_REGRESSION.md)**
- **[Reproduzierbare technische Prüfergebnisse](evaluation/TECHNISCHE_PRUEFERGEBNISSE.md)** – R5 FAIL, R6/R6.1 Struktur-PASS; wissenschaftliche Grenzen klar getrennt.
- **[Technischer JSON-Check](tools/check_output.py)** – kleine, unabhängig ausführbare Formatprüfung ohne Fremdbibliotheken.

## Entwicklungsstand und Versionsfamilien

Das Repository enthält neben der weiterentwickelten **R6.2** und der historischen Referenz **R6.1** jetzt die tatsächlich vorhandenen Vorläufer aus den Familien **frühe Masterprompts (1.0 bis V8.1)**, **V8.x-Masterartefakte**, **OPERATIONAL V2–V3.5** sowie **AUTORUN R3–R6**. Sie sind als historische Belege archiviert, nicht als parallel aktivierte NotebookLM-Quellen. **Nur eine Promptversion pro Notebook aktivieren.** Für die R6.2-Einzelitemprüfung gelten die Dateien und Grenzen im neuen Prüfbericht; historische vollständige Läufe werden mit R6.1 repliziert. Auch bei früher als `FINAL` benannten Dateien ist eine externe Freigabe oder psychometrische Validierung nicht belegt. Details: [MODELLHISTORIE.md](MODELLHISTORIE.md).

## Replikation der historischen R6.1-Demonstration mit NotebookLM

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

## Zugang für die Prüfung

Das Repository ist privat; Prüfende benötigen ausdrücklich eingerichteten Zugriff.
Das historische Korpus enthält 24 Markdown-Dateien mit 66 exportierten
Frage-Antwort-Paaren (N01–N24; siehe [Chatverlauf](notebooklm-chatverlauf/)).
Diese Belegkennungen sind keine gesicherte Zählung unabhängiger Versuche.
N22–N24 setzen denselben operativen R6.1-Chat fort. Schriftliche Exporte
stützen Nachvollziehbarkeit, ersetzen aber weder sämtliche Live-Metadaten
noch eine unabhängige Quellenprüfung. Die sechs ergänzenden Basis-/R6.1-
Vergleichsläufe und vier R6.2-Läufe werden separat im neuen Testnachweispaket
archiviert; sie verändern die historischen N01–N24 nicht.

## Wissenschaftliche Einordnung

Zielpopulation sind kaufmännische Mitarbeitende eines mittelständischen Unternehmens. Das Instrument enthält **18 reflektive Item-Kandidaten** in sechs dreiteiligen Konstrukten, davon fünf Readiness- und eine Kontext-Subskala; Bedarfsfragen und Minimaldemografie werden gesondert behandelt. Einzelne Items sind aus validierten Originalinstrumenten **kontextspezifisch abgeleitet/übersetzt** oder wurden theoriegeleitet neu entwickelt. Daraus folgt **nicht**, dass die zusammengesetzten deutschen Drei-Item-Kurzskalen bereits validiert sind.

Das Design folgt der übergeordneten Projektaufgabe zur DSR-Methode nach Peffers et al. (2007). Die in einem separaten Bewertungsbogen genannten Kriterien – Wissenschaftlichkeit, nachvollziehbare Operationalisierung, Problemlösungskompetenz, Kreativität, Forschungstransfer und Grenzen – werden anhand der Iterationen und der Quellenprüfungen adressiert, aber nicht allein durch das Repository als erfüllt erklärt.

**Literaturhinweis:** Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. Die vollständigen Literaturangaben der Itemquellen müssen in der Hausarbeit anhand der Originalpublikationen geprüft werden.

## Veröffentlichungs- und Authentizitätshinweis

Die Datei `CHATVERLAUF.md` ist **kein Rohdatenexport** des gesamten Chats. Sie enthält wörtliche Zitat-Auszüge aus dem vorliegenden Gespräch, einen vom Nutzer nachgereichten Teil-Auszug sowie klar gekennzeichnete **dateigestützt rekonstruierte frühere Entwicklungsphasen**. Es wurden keine fehlenden Chat-Turns erfunden. Unveränderte Originalexporte mit vollständigen Metadaten sind über die verwendeten Chat-Plattformfunktionen gesondert zu beschaffen, falls für den Nachweis verlangt.

Nicht enthalten: personenbezogene Befragtenantworten, SmartPLS-Rohdaten, vollständige wissenschaftliche Verlags-PDFs oder vermeintliche Human-Pretestergebnisse. Die Testnachweise enthalten gesicherte sichtbare Seitenaufnahmen der neuen Modellantworten.

## Stand

Version: **V3.5-R6.2 (`TEST_CANDIDATE`)**, historische Vollausgabe: R6.1  
Status: R6.2 in begrenzten Einzelitemprüfungen untersucht, allgemeine Freigabe ausstehend; **empirische Validierung und realer kognitiver Pretest stehen aus**.

## Zusätzliche Materialien (separat ergänzt)

- **[Visueller Entwicklungs-Zeitstrahl](artefakt/artefakt-zeitstrahl.html)** – Build-/Evaluate-Learn-Übersicht der gesamten Versionskette (im Browser öffnen).
- **[Vollständiger NotebookLM-Chatexport](notebooklm-chatverlauf/)** – 24 Markdown-Exporte mit 66 Frage-Antwort-Paaren, Grundlage der N01–N24-Belege.
- **[ChatGPT-Entwicklungsprotokoll](chatgpt-entwicklungsprotokoll/)** – vollständiger Chatverlauf der Masterprompt-Entwicklung mit ChatGPT.
- **[Nachweise/](Nachweise/)** – Hash- und Textabgleich der NotebookLM-Rohexporte gegen die archivierten R5/R6/R6.1-Ausgaben (`check_chat_evidence.py`, `Chatbelege_Pruefergebnisse.json`).
