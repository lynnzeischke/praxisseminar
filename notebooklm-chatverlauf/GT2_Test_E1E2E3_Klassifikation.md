# GT2-Test: E1/E2/E3-Klassifikationsgrenze

Quelle: NotebookLM-Chat (von der Nutzerin manuell in den Konversationsverlauf
mit Claude kopiert; der Export-Link des Notebooks selbst wurde nicht
gesondert dokumentiert).
Exportiert/übernommen: 23.10.2026

**Hinweis zur Vollständigkeit:** Der exakte Wortlaut des an NotebookLM
gestellten Prompts (Abschnitt „Frage") lag Claude zum Zeitpunkt der
Archivierung nicht mehr im Kontext vor (Sitzungs-Kompaktierung). Die
Nutzerin wird gebeten, den tatsächlichen Prompt-Text aus ihrem eigenen
NotebookLM-Chatverlauf zu ergänzen, bevor diese Datei als vollständiger
Beleg in der Hausarbeit zitiert wird. Der folgende Antwortteil ist dagegen
1:1 wie von der Nutzerin aus NotebookLM kopiert.

---

## Frage

*[von der Nutzerin zu ergänzen – exakter Prompt-Wortlaut aus dem
NotebookLM-Chat]*

---

## Antwort

Hier ist die methodische Klassifikation der vier Testfälle nach den strengen Evidenzstandards (E1, E2, E3):

(A) Deutschsprachiges Originalitem, unverändert übernommen

* Originaltext: „Ich kenne die wichtigsten Grundbegriffe der künstlichen Intelligenz."
* Quelle: Carolus et al. (2023), MAILS (Meta AI Literacy Scale), Appendix A (Pos. 7 / Understand)
* evidence_class: `E1`
* Begründung: Das Item entstammt einer verifizierten, primär deutschsprachig entwickelten Publikation. Da der Wortlaut, das Messobjekt und die Zielsprache völlig identisch übernommen werden, liegt ein reines E1-Originalitem vor.

(B) Englischsprachiges Originalitem, ins Deutsche übersetzt

* Originaltext: „I'm confident in my ability to understand how new AI technologies work."
* Quelle: Oksanen et al. (2026), AILRSE-5, Table 2 (Item 1)
* Übersetzung: „Ich bin zuversichtlich, dass ich verstehen kann, wie neue KI-Technologien funktionieren."
* evidence_class: `E2`
* Begründung: Das Item ist ein verifiziertes englisches Originalitem. Durch die reine Übersetzung ins Deutsche erfolgt eine sprachliche Transposition. Da der Bedeutungsgehalt und das gemessene Konstrukt (Lern-Selbstwirksamkeit) semantisch treu erhalten bleiben, ist das Item als E2 (GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED) zu deklarieren.

(C) Originalitem, angepasst auf ein konkretes Tool/Unternehmen

* Originaltext: „Ich kann KI sinnvoll einsetzen, um meine Ziele zu erreichen." (MAILS, Pos. 3)
* Kontextanpassung: „Ich kann ChatGPT Enterprise sinnvoll einsetzen, um meine Arbeitsziele bei [Unternehmensname] zu erreichen."
* evidence_class: `E2`
* Begründung: Hier handelt es sich um eine bereichs- und kontextspezifische Spezialisierung eines verifizierten Originalitems. Das Ersetzen generischer Begriffe durch ein konkretes Tool (ChatGPT Enterprise) oder die Arbeitsumgebung verändert die abgefragte Grundkompetenz nicht. Solche Anpassungen fallen unter E2 (GERMAN_CONTEXT_ADAPTED_FROM_SOURCE), sofern keine unveränderten publizierten Kennwerte für die Spezialform vorgetäuscht werden.

(D) Neues Item, zusammengesetzt aus zwei verschiedenen Originalitems

* Quell-Items: MAILS Pos. 24 („Die meisten Probleme im Umgang mit KI kann ich aus eigener Kraft meistern") + AISES Technological Skills („Ich kann KI nutzen, um komplexe Aufgaben auszuführen").
* Synthetisiertes Item: „Ich kann komplexe kaufmännische Aufgaben mit generativer KI selbstständig umsetzen und auftretende Anwendungsprobleme dabei eigenständig beheben."
* evidence_class: `E3`
* Begründung: Durch das Verschmelzen oder Neukombinieren von zwei getrennten Originalitems entsteht eine neue Hybridaussage. Da für diesen Satz kein einzelnes publiziertes Originalitem als eindeutige Referenz existiert (`source_item_id = null`), handelt es sich formal um eine E3-Eigenentwicklung (theoriegeleitet konstruiert). Eine Deklaration als E2 wäre eine unzulässige Vorspiegelung falscher Quellenevidenz.

---

## Prüfbefund (Claude, 23.10.2026)

- Klassifikation aller vier Fälle entspricht exakt der GT2-Erwartung nach MASTER_ARTEFAKT V8.4.11 (A→E1, B→E2, C→E2, D→E3). **GT2 bestanden.**
- Quellenprüfung Fall B: „I'm confident in my ability to understand how new AI technologies work." = Oksanen et al. (2026), AILRSE-5, Table 2, Item 1 — Wortlaut im Primärquellenbestand des Projekts verifiziert.
- Quellenprüfung Fall D (Teilquelle AISES): Das zitierte Item „Ich kann KI nutzen, um komplexe Aufgaben auszuführen" konnte im verfügbaren Volltext der AISES-Publikation (Wang et al., Technological-Skills-Faktor) nicht wortgleich verifiziert werden; die vier dort dokumentierten TS-Items betragen sinngemäß etwas anderes (Sorge vor Fehlbedienung, Fachjargon). Da es sich bei Fall D ohnehin um eine Synthese (E3) und keine Direktübernahme handelt, ist dies für die E3-Klassifikation unschädlich, sollte aber vor Übernahme in Anhang B anhand der Originalpublikation gegengeprüft werden.
- **Nachträglich verifiziert (Claude, 23.10.2026) anhand des vollständigen Appendix A von Carolus et al. (2023):**
  - **Pos. 7** (Facette „Understand AI"): publizierter Item-Wortlaut „I know the most important concepts of the topic 'artificial intelligence'." Das in Fall A verwendete „Ich kenne die wichtigsten Grundbegriffe der künstlichen Intelligenz." ist eine inhaltlich treue Entsprechung (Itemnummer und Facette stimmen).
  - **Pos. 24** (Facette „AI Problem solving"): publizierter Item-Wortlaut „I can handle most problems in dealing with artificial intelligence well on my own." Das in Fall D verwendete „Die meisten Probleme im Umgang mit KI kann ich aus eigener Kraft meistern." entspricht dem sehr genau (Itemnummer und Facette stimmen).
  - **Wichtige Einschränkung:** Carolus et al. (2023) erhoben die Daten zwar an 300 deutschsprachigen Teilnehmenden, publizieren im Appendix A aber ausschließlich die **englischen** Itemformulierungen; der tatsächliche deutsche Erhebungswortlaut ist in der Publikation nicht enthalten. Die oben genannten deutschen Sätze sind damit treue Rückübersetzungen des publizierten englischen Wortlauts, aber **nicht nachweislich identisch mit dem Original-Erhebungsitem**. Eine Deklaration als reines `E1` ("deutschsprachiges Originalitem, unverändert übernommen") ist deshalb mit einem kleinen Vorbehalt zu versehen: Itemnummer, Facette und Bedeutungsgehalt sind zweifelsfrei korrekt zugeordnet, der exakte deutsche Wortlaut der Originalerhebung lässt sich aus der Publikation selbst aber nicht verifizieren. Für die Hausarbeit empfiehlt sich entweder (a) der Hinweis "rückübersetzt aus publiziertem Appendix A, Originalwortlaut der deutschen Erhebung nicht publiziert" oder (b) die Einstufung von Fall A als `E2` statt `E1`, bis der tatsächliche Erhebungswortlaut vorliegt.
