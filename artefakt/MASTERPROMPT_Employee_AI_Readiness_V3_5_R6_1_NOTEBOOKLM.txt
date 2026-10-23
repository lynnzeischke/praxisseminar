# MASTERPROMPT – Employee AI Readiness | V3.5-R6.1 INTEGRATED-AUDIT AUTORUN – EVIDENCE-LOCKED

**Status:** `TEST_CANDIDATE` – gezieltes R6.1-Quellen- und Aussagen-Hardening auf Basis des technisch konsistenten R6-Fragebogenlaufs für genau **einen** neuen NotebookLM-Fragebogenlauf. Der originale `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL` steht am Ende dieser Datei wortgetreu in **Anhang A**. Der Audit wird nicht nochmals als separate NotebookLM-Quelle benötigt. Die Qualität der tatsächlichen NotebookLM-Ausgabe ist vor einer FINAL-Freigabe unabhängig zu prüfen.

## 1. Einzige Nutzereingabe / Start

`Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.`

Wenn dieser exakte Befehl eingegeben wird: sofort **einen vollständigen neuen Fragebogenlauf in einer einzigen Antwort** durchführen, ohne Rückfragen, Phasenaufrufe oder zweiten JSON-Export. Vorher die in diesem Dokument integrierten Audit-Festlegungen beachten. **Der Masterprompt und der eingebettete Audit sind Governance, keine unabhängigen wissenschaftlichen Primärquellen**. Die Originalpapers/Originalfrage-Dokumentation müssen als zusätzliche NotebookLM-Quellen verfügbar sein. Eine abgeschnittene Ausgabe ist NIE `CONFORMANT_GENERATION`.

## 2. Verbindliche Projektparameter aus dem freigegebenen Design Audit

```text
RUN_MODE = QUESTIONNAIRE_GENERATION
DESIGN_AUDIT_REFERENCE = DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL
DESIGN_AUDIT_STATUS = FINAL_APPROVED
TARGET_POPULATION = Kaufmännische Mitarbeitende eines mittelständischen Unternehmens
AI_CONTEXT = Generative KI, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag
MEASUREMENT_GOAL = Individuelle Employee AI Readiness diagnostisch erfassen und Schulungs-/Entwicklungsbedarfe identifizieren
INSTRUMENT_PURPOSE = DIAGNOSTIC
LANGUAGE = DE
REPRODUCIBILITY_MODE = strict
DELIVERY_MODE = AUTORUN_SINGLE_COMMAND
MAX_COMPLETION_TIME_MIN = 8
MAX_REFLECTIVE_ITEMS = 18
CONTEXT_TEXT = NOT_PROVIDED
TASK_CONTEXT = NOT_PROVIDED
PLANNED_ANALYSIS = NOT_PROVIDED
AI_EXPERIENCE_SEGMENTATION = auto
SCALE_PREFERENCE = original_scales_per_selected_source
SOURCE_POLICY = PRIMARY_ORIGINALS_ACTUALLY_VERIFIED
```

**Bearbeitungszeit-Klarstellung:** `MAX_COMPLETION_TIME_MIN = 8` ist ausschließlich das im Design Audit dokumentierte **Designziel**. Es ist weder ein erhobener Zeitwert noch eine belegte Bearbeitungszeitspanne. Solange kein realer dokumentierter Zeit-/Usability-Test vorliegt, darf B5 keine Minutenangabe oder behauptete Dauer enthalten. Die Zielzeit darf nur als Designrestriktion in B1 oder B3 stehen und muss dort als ungetestet gekennzeichnet werden.

**Prioritätsregel:** Der in **Anhang A dieser Datei unverändert eingebettete**, als `004_FINAL` freigegebene **Original-Design-Audit** ist die maßgebliche Designbasis. Frühere Masterprompts, NotebookLM-Ausgaben und ein separat **vorgeschlagener** Nachtrag dürfen die Aussagen des Audits nicht überschreiben. Eine im Audit bereits ausdrücklich zugelassene Quellenauswahl ist **keine** Änderung des Audits. Der Audit nennt bei `READINESS_CORE_COMFORT` sowohl `AIRS` als auch `AISES` (Abschnitt A8); für `AISES` dokumentiert er die Originalskala 1–7 (A9). Die Auswahl von **drei AISES-Comfort-Items** ist daher eine **dokumentationspflichtige Operationalisierungsentscheidung innerhalb des bestehenden Audits**, nicht automatisch ein genehmigungspflichtiger Nachtrag. Andere Designänderungen müssen gesondert ausgewiesen und dürfen nicht als bereits freigegeben gelten.

## 3. Wissenschaftlich festgelegte Messarchitektur

**Genau sechs getrennte reflektive Skalen mit jeweils drei Items (18)**. Die ersten fünf sind `READINESS_CORE`, `CONTEXT_FC` ist `CONTEXT`, **nicht** Teil eines unvalidierten Gesamtscores.

| Konstruktcode | Bedeutung | Bevorzugte verifizierte Original-Itemquelle | zulässige Skala | Anzahl |
|---|---|---|---|---:|
| `READINESS_CORE_LIT` | subjektives KI-Grundverständnis | MAILS (Carolus et al., 2023) | Fähigkeits-Selbsteinschätzung 0–10 | 3 |
| `READINESS_CORE_LEARN` | KI-Lern-Selbstwirksamkeit | AILRSE-5 (Oksanen et al., 2026), transparentes 3/5-Subset | Zustimmung 1–7 | 3 |
| `READINESS_CORE_APPLY` | eigene praktische KI-Anwendungs-/Problemlösefähigkeit | MAILS Use & Apply + AI Problem Solving; keine Systemnutzen-Items | Fähigkeit 0–10 | 3 |
| `READINESS_CORE_DETECT` | Erkennung von KI plus kritische KI-Ergebnisprüfung | MAILS Detect AI für E2, gesonderte passende E3-Definition für Faktentreue | Fähigkeit 0–10 | 3 |
| `READINESS_CORE_COMFORT` | affektiver Komfort | AISES (Wang & Chuang, 2024), **drei Items aus sechs publizierten Comfort-Items** | Zustimmung 1–7 | 3 |
| `CONTEXT_FC` | wahrgenommene erleichternde Bedingungen | Lambiase et al. (2025), transparentes FC_1–FC_3-Subset | Zustimmung 1–7 | 3 |

**AISES-Entscheidungsbegründung:** Für einen GenAI-Bürofragebogen sind auf die affektive Erfahrung bei KI-Interaktion gerichtete AISES-Comfort-Items dem AIRS-COM3/Q18-Item über humanoide Roboter im Messobjekt näher. AIRS bleibt im Audit als relevante Readiness-/Definitionsquelle anerkannt, wird hier aber nicht als vorgetäuschte identische Quelle für anderslautende AISES-Items verwendet. Dokumentiere die konkrete Auswahl sowie drei von sechs Originalitems, ihren Kontexttransfer und die Beschränkung unveränderter psychometrischer Kennwerte. Falls die echte Originalquelle einen Kandidaten nicht trägt, schlage keine fiktive E2-Zuordnung vor, sondern kennzeichne diesen als `NOT_VERIFIED` und den Lauf als `REVISION_REQUIRED`.

**Trennungsregeln:** Kein Task-Technology Fit ohne TASK_CONTEXT; kein Behavioral Intention / Trust / Performance Expectancy im Kern; keine eigene Ethics-Reflexivskala; kein Gesamtscore; keine unternehmensspezifisch erfundenen Arbeitsabläufe, Supportangebote, Datenschutz- oder Freiwilligkeitszusagen. `Datensatz_v1` ist höchstens Retrieval-/Cross-Check-Hilfe für tatsächlich darin enthaltene Daten, nie selbst Primärquelle. Wissenschaftliche Originalarbeiten haben Vorrang. Nicht übernommene Original-Item-Pools und Reduktionen transparent ausweisen.

## 4. Originalitem-Beweisstandard und korrekte Evidenzklassen

**E1:** Originalitem in der Zielsprache und im Messobjekt unverändert. **E2:** verifiziertes Originalitem, bei dem nur sprachliche/kontextspezifische Adaption erfolgt, **ohne** eine andere Kompetenz oder einen anderen Gegenstand vorzutäuschen. **E3:** theoriegeleitet selbst formuliert; kein Originalitem; `source_item_id=null`, `source_item_text_verified=false`, `original_scale=null`, `source_definition_verified` nur bei echter, spezifisch passender Definition.

**Harte Beweisregel E2:** Überprüfe bei jedem Item **vor dem PASS** anhand der wirklich verfügbaren Primärpublikation die Itemnummer/ID oder Originalposition, den Wortlaut bzw. die überprüfte präzise Semantik, die Faktorzugehörigkeit, Messobjekt, Skala und Adaptionsart. `source_item_text_verified = true` sagt ausschließlich, dass der **Originalitem-Wortlaut im Quellendokument** nachgeschlagen wurde; es ist KEIN Beleg für eine validierte deutsche kontextspezifische Adaption. `translation_equivalence_status` ist davon getrennt auszuweisen; ohne Human-Pretest/Validierung `NOT_EMPIRICALLY_ESTABLISHED`. In B2 und JSON Quellen-Locator und Prüfstatus pro Item festhalten. Aus alter KI-Ausgabe, einem Entwurfs-Manifest oder einem ähnlich klingenden Satz entstehen keine Originalbelege. Mögliche deutsche MAILS-Originalitems nicht fälschlich als englisch übersetzte Originalitems ausgeben. **Insbesondere:** Sobald in einem MAILS-Item `AI`/`künstliche Intelligenz` zu `generative KI` und/oder `everyday life` zu `bei meiner Arbeit`/Arbeitsziele spezialisiert wird, ist der hier verwendete Endwortlaut `GERMAN_CONTEXT_ADAPTED_FROM_SOURCE`, **niemals** `GERMAN_ORIGINAL_PUBLISHED`. Dies gilt zwingend für LIT_01–03, APPLY_01–03 und DETECT_01–02. Originalitem nachprüfen, Anpassung dokumentieren und die publizierten Gütekennwerte nicht als automatisch übertragen darstellen. Bei AILRSE/AISES/FC deutschen Zieltext als `GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED` kennzeichnen; `GERMAN_ADAPTED_CHECKED` ist ohne ausdrücklich definierte Prüfung zu unpräzise. Übersetzung aus dem Englischen → `NEEDS_EQUIVALENCE_CHECK`, wenn keine validierte Übersetzung vorliegt. Bei fehlendem Volltext, abweichendem Itemwortlaut oder Inhaltswechsel: `E2_NOT_VERIFIED` und `e2_proof_ok=false`, auch wenn andere Checks PASS wären.

**MAILS Original-Positionsregel:** Die publizierte englische Appendix-A-Paginierung/Nummerierung ordnet `Use & Apply` Pos. 1–6, `Understand` Pos. 7–12, `Detect` Pos. 13–15 und `AI Problem solving` Pos. 23–25 zu. **Diese Positionsnummern sind Referenzpositionen, keine erfundenen Original-Variablennamen**. Akzeptiere nur Originalinhalte, die an dieser Position tatsächlich belegbar sind. AI-Erkennung von Anwendung oder Interaktionspartner ist nicht gleich Faktenprüfung eines generierten Textes.

**DETECT_03 – fester E3-Kandidat (keine doppelte Eigenschaft):** „Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.“ Dies ist eine **eigens entwickelte Prüfkompetenzfrage**, kein Originalitem der MAILS-Detect-Skala. Die Quellen müssen die Relevanz der kritischen Prüfung und die Risiken inhaltlich falscher KI-Ausgaben nachvollziehbar stützen; ausschließlich allgemeine KI-Erkennung genügt nicht. Ohne überprüften und im Ergebnis benannten Theorieanker `e3_source_compatibility_ok=false`. **Nie** eine Originalitem-ID erfinden. Die Skala 0–10 ist das projektspezifische Endformat, keine publizierte Originalskala dieses E3-Items.

### E3-Theorieanker: nachzuprüfen und begrenzt zu interpretieren

**Vorzugsanker aus einer bereits hochgeladenen Originalpublikation:** Lambiase et al. (2025; je nach verfügbarer PDF-Version arXiv-Revision 2026), *Exploring Individual Factors in the Adoption of LLMs*, **§ 6.2.4 „Using LLMs to Retrieve Information“**, Absatz beginnend mit **„It is also important to recognize the potential impact of LLM hallucinations in this context.“** Der Absatz erörtert, dass halluzinierte/irreführende Ergebnisse Vertrauenswürdigkeit und Überprüfungspraktiken in professionellen Informationsaufgaben beeinträchtigen können; als Beispiel wird fehlerhafte API-Guidance genannt, die bei einem Code-Review auffällt. Der vorangehende Absatz behandelt Peer Validation bei fachlicher Informationsbeschaffung.

**Strikte Evidenztrennung:** Diese Publikation liefert **ein empirisch bzw. theoretisch diskutiertes Problemfeld und einen nachvollziehbaren Begründungsanker** für die projektseitige Entscheidung, eine eigenständige Frage zur kritischen Inhaltsprüfung zu ergänzen. Sie enthält in der bezeichneten Passage **weder den Originalwortlaut von `DETECT_03` noch eine publizierte und validierte Selbsteinschätzungs-Kompetenzskala für diese Fähigkeit**. Der Schluss „Fehlinformationen können problematisch sein → kritische Prüfkompetenz ist für das Diagnoseziel relevant“ ist ausdrücklich als **projektseitige theoretische Ableitung** kenntlich zu machen, nicht als Aussage, die Autoren hätten die neue Kompetenzfrage getestet.

**Verifikationspflicht:** Prüfe diesen Text vor dem Ausgabestatus `PASS` wirklich in der zusätzlich hochgeladenen Originalpublikation. In B2 und B3 den **konkreten Quellenanker, die Ableitung und ihre Grenze** nennen; in B7 einen maschinenlesbaren Eintrag `theoretical_rationale` ablegen. Nur wenn die Originalpassage tatsächlich auffindbar ist, `theoretical_rationale_verified = true`. Für `DETECT_03` gelten gleichzeitig `source_item_id = null`, `source_item_text_verified = false`, `original_scale = null`, `source_definition_verified = false`, sofern keine **direkte** eigenständige Definition der Kompetenz in einer weiteren überprüften Originalquelle vorliegt. **`source_definition_verified=false` ist kein Scheitern des E3-Gates**, solange der überprüfte theoretische Risikobegründungsanker, seine Ableitung und die Grenze sauber ausgewiesen sind. Falls § 6.2.4 in der ausgewählten PDF-Quelle nicht auffindbar ist, darf keine verifizierte Theoriequelle behauptet werden: `theoretical_rationale_verified=false`, `e3_source_compatibility_ok=false` und `REVISION_REQUIRED`.

**AIRS-Verwechslungsblock:** Q9/COM1: Verlegenheit bei Problemen in Anwesenheit anderer; Q8/COM2: gesundheits-/sicherheitsbezogene Bedenken; Q18/COM3: humanoide Roboter. KEINES davon automatisch als semantisch identisches Office-GenAI-Comfort-Item behandeln. AISES-Comfort-Originalitems stammen dagegen aus der veröffentlichten AISES-Faktorgruppe: `CF1/Q25` Ruhe, `CF3/Q24` Wohlbefinden, `CF5/Q22` Entspanntheit. Vor E2-Freigabe Quellenvolltext, originale Labels, zugehörige Itemformulierungen und tatsächliche 1–7-Skala überprüfen. Die drei nahe verwandten affektiven Formulierungen sind eine **potenzielle Redundanz**, im echten Pretest und bei der empirischen Messmodellprüfung gezielt zu überprüfen.

## 4a. Integrierter Design Audit und Quellenvollständigkeit

**Anhang A dieses Masterprompts ist die wortgetreue Originalfassung des bereits als FINAL freigegebenen Design Audits.** Die historische Nennung von V2.1 in dessen Kopfbereich beschreibt den damaligen Stand und bedeutet nicht, dass NotebookLM V2.1 suchen oder ausführen muss. Für diesen Lauf sind die aktuellen Operationalisierungsregeln in Abschnitt 1–9 maßgeblich, soweit sie nicht mit einer zwingenden Entscheidung des Audits kollidieren. Im Konfliktfall gilt: **Original-Design-Audit > aktuelle Operationalisierung > historische Modelloutputs/Entwürfe**. Unaufgelöste Widersprüche melden, nicht heimlich ausgleichen.

**Wissenschaftliche Quellen, die neben dieser Masterpromptdatei hochgeladen sein sollen:**
1. `MAILS.pdf` (Carolus et al. 2023),
2. `AILRSE-5.pdf` (Oksanen et al. 2026),
3. `AISES.pdf` (Wang & Chuang 2024),
4. `AIRS.pdf` (Wang et al. 2026),
5. `Lambiase et al. (2025).pdf` (je nach PDF arXiv-Revision 2026),
6. `Paper Fragebogen 1.pdf` bis `Paper Fragebogen 5.pdf` für Abgrenzung/Methodik,
7. zur Verifikation von `FC_1–FC_3` entweder `1_originalDataset.csv` **oder** `NOTEBOOKLM_FC_ORIGINALITEMS_OHNE_TEILNEHMERDATEN.txt`.

**Keine weitere Design-Audit-Datei auswählen**, denn sie ist bereits als Anhang A enthalten. Keine alte R1/R2/R3/R4-Masterpromptversion parallel auswählen. Falls eine essenzielle Primärquelle fehlt: im Output präzise als `NOT_VERIFIED` ausweisen; keine angeblich geprüften Wortlaute erfinden.

**Rolle des FC-Datensatzes:** Die Variablenkopfzeile von `1_originalDataset.csv` führt die Codes `FC_1…FC_4`, die unmittelbar folgende **zweite CSV-Zeile** enthält die **ursprünglichen englischen Fragetexte**. Darunter folgen 188 Teilnehmerdatensätze, die für diesen Fragebogenlauf nicht ausgewertet, zitiert oder rekonstruiert werden dürfen. Falls der bereinigte FC-Extrakt ausgewählt wurde, genügen die vier dort enthaltenen Itemformulierungen zum Text-Cross-Check. In beiden Fällen: der Datenanhang stützt die **Wortlaut-Provenienz**, nicht eine neue psychometrische Validität.

**FC-Quellencheck (Referenztext aus der zweiten Zeile des Datenartefakts; vor E2 mit hochgeladener Belegquelle abgleichen):**

| Quelle | Originalwortlaut der relevanten Aussage | semantischer Kern |
|---|---|---|
| `FC_1` | I have the resources necessary to use LLMs to support my job | Ressourcen im Beruf |
| `FC_2` | I have the knowledge necessary to use LLMs to support my job | Wissen im Beruf |
| `FC_3` | LLMs are compatible with other technologies I use in my job | Kompatibilität mit beruflich genutzter Technik |
| `FC_4` | I can get help from others when I have difficulties using LLMs to support my job | Hilfe anderer Personen; **nicht auswählen** |

Diese Referenz ist **keine eigenständige Primärquelle**, sondern ein Prüfanker für die verfügbare Originalfrage-Datei. Für `FC_01–FC_03` müssen im endgültigen deutschen Text die Worte „bei meiner Arbeit“ bzw. „die ich bei meiner Arbeit verwende“ sinngemäß erhalten bleiben. `FC_4` niemals irrtümlich statt `FC_3` verwenden. Die ausgewählten Items bleiben `E2` nur, wenn der Quellennachweis wirklich gelingt, andernfalls `E2_NOT_VERIFIED` und `REVISION_REQUIRED`.

## 4b. Ausgabesicherheit, Reproduzierbarkeit und Selbstprüfung

**R6-Geltung und Reihenfolge:** Die R6-Ausführungsregeln präzisieren nur die freigegebene Operationalisierung; der unveränderte Audit in Anhang A ist Governance. Führe die Ausgabe in einem einzigen Lauf aus. Für die Ausgabebestandteile gelten die verbindlichen Muster in § 6, § 7 und § 8; widersprechende frei formulierte Varianten sind unzulässig. Die 18 Zeilen in § 5 sind ein Kandidatenregister, nach Originalquellenprüfung wird daraus einmalig ein kanonischer finaler Datensatz.

- Erzeuge **zuerst intern** einen konsistenten Datensatz mit exakt den 18 Reflexivitem-IDs; nutze ihn ohne Umformulierungen für B2, B5, B7. Wenn korrigiertes Wording erforderlich wird, aktualisiere es an **allen drei Stellen** und dokumentiere es in B3.
- Priorität bei knappem Ausgaberaum: **vollständiges B5 und B7** vor ausführlicher B3/B4/B6-Prosa. B2, B3, B4 und B6 prägnant halten, aber die geforderten Kernelemente nicht auslassen. B7 enthält die vollständigen tatsächlich ausgefüllten Itemobjekte; keine Platzhalter wie `...`, `omitted`, leere Arrays oder `same_as_above`.
- Gib genau **eine** B1–B7-Folge und **eine** B0-Schlussprüfung aus. Kein zweiter Anlauf innerhalb derselben Antwort, keine Doppelüberschriften, keine fiktive Fortsetzung.
- Prüfe am Ende **gesondert** `(1) Item-IDs exakt einmal, (2) Itemanzahl=18 in B2/B5/B7, (3) je 3 je Konstrukt, (4) Routing/DIAG/DEM, (5) JSON syntaktisch vollständig mit schließenden Klammern und ohne Kommentarzeilen, (6) E2/E3-Prüfstatus und B6-Analysedisziplin`.
- Falls die Ausgabe technisch/inhaltlich nicht vollständig werden kann, darf kein `CONFORMANT_GENERATION` ausgegeben werden. Das Modell darf eine eigene formale Sichtprüfung nicht als extern ausgeführte Validierung behaupten.

## 5. Kandidatenkarte: 18 Items zur unabhängigen Quellennachprüfung

**WICHTIG: ausschließlich semantische ENTWURFS- und Auswahlkandidaten, keine automatisch bewiesenen Originalitems.** Übertrage Item-ID und Fragewortlaut nach bestandener Quellenequivalenzprüfung identisch in B2, B5 und JSON. Stimmt ein Kandidat nicht mit dem belegten Originalinhalt überein, korrigiere ihn transparenterweise im laufenden Entwurf, dokumentiere die Änderung oder setze `REVISION_REQUIRED`; darfst nie eine falsche E2-Quelle PASS setzen.

| item_id | Konstrukt | Primärquelle und zu prüfende Originalposition | E-Kandidat | Skala | Kandidaten-Wortlaut Deutsch |
|---|---|---|---|---|---|
| `LIT_01` | `READINESS_CORE_LIT` | Carolus et al. (2023), MAILS, Pos./ID `7` | `E2` | `0-10` | Ich kenne die wichtigsten Grundbegriffe generativer KI. |
| `LIT_02` | `READINESS_CORE_LIT` | Carolus et al. (2023), MAILS, Pos./ID `8` | `E2` | `0-10` | Ich kenne die Bedeutung des Begriffs generative KI. |
| `LIT_03` | `READINESS_CORE_LIT` | Carolus et al. (2023), MAILS, Pos./ID `12` | `E2` | `0-10` | Ich kann mir mögliche zukünftige Anwendungen generativer KI vorstellen. |
| `LEARN_01` | `READINESS_CORE_LEARN` | Oksanen et al. (2026), AILRSE-5, Pos./ID `1` | `E2` | `1-7` | Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen funktionieren. |
| `LEARN_02` | `READINESS_CORE_LEARN` | Oksanen et al. (2026), AILRSE-5, Pos./ID `2` | `E2` | `1-7` | Ich bin zuversichtlich, dass ich bei Bedarf die Nutzung neuer generativer KI-Anwendungen erlernen kann. |
| `LEARN_03` | `READINESS_CORE_LEARN` | Oksanen et al. (2026), AILRSE-5, Pos./ID `5` | `E2` | `1-7` | Ich bin zuversichtlich, dass ich mir die Nutzung neuer generativer KI-Anwendungen selbstständig aneignen kann. |
| `APPLY_01` | `READINESS_CORE_APPLY` | Carolus et al. (2023), MAILS, Pos./ID `1` | `E2` | `0-10` | Ich kann generative KI-Anwendungen bedienen. |
| `APPLY_02` | `READINESS_CORE_APPLY` | Carolus et al. (2023), MAILS, Pos./ID `3` | `E2` | `0-10` | Ich kann generative KI sinnvoll einsetzen, um meine Arbeitsziele zu erreichen. |
| `APPLY_03` | `READINESS_CORE_APPLY` | Carolus et al. (2023), MAILS, Pos./ID `24` | `E2` | `0-10` | Die meisten Probleme im Umgang mit generativer KI kann ich aus eigener Kraft meistern. |
| `DETECT_01` | `READINESS_CORE_DETECT` | Carolus et al. (2023), MAILS, Pos./ID `13` | `E2` | `0-10` | Ich kann erkennen, ob eine Anwendung auf generativer KI basiert. |
| `DETECT_02` | `READINESS_CORE_DETECT` | Carolus et al. (2023), MAILS, Pos./ID `15` | `E2` | `0-10` | Ich kann unterscheiden, ob ich mit einer generativen KI oder einer Person interagiere. |
| `DETECT_03` | `READINESS_CORE_DETECT` | Eigene E3-Formulierung; Theorieanker Lambiase et al., § 6.2.4 (Fehlinformationen/Halluzinationen, **keine** Originalitem-ID oder direkte Kompetenzdefinition) | `E3` | `0-10` | Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen. |
| `COMFORT_01` | `READINESS_CORE_COMFORT` | Wang & Chuang (2024), AISES, Pos./ID `CF1/Q25` | `E2` | `1-7` | Wenn ich mit generativer KI interagiere, fühle ich mich ruhig. |
| `COMFORT_02` | `READINESS_CORE_COMFORT` | Wang & Chuang (2024), AISES, Pos./ID `CF3/Q24` | `E2` | `1-7` | Wenn ich mit generativer KI interagiere, fühle ich mich wohl. |
| `COMFORT_03` | `READINESS_CORE_COMFORT` | Wang & Chuang (2024), AISES, Pos./ID `CF5/Q22` | `E2` | `1-7` | Wenn ich mit generativer KI interagiere, fühle ich mich entspannt. |
| `FC_01` | `CONTEXT_FC` | Lambiase et al. (2025), Pos./ID `FC_1` | `E2` | `1-7` | Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI-Anwendungen bei meiner Arbeit zu nutzen. |
| `FC_02` | `CONTEXT_FC` | Lambiase et al. (2025), Pos./ID `FC_2` | `E2` | `1-7` | Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen bei meiner Arbeit zu nutzen. |
| `FC_03` | `CONTEXT_FC` | Lambiase et al. (2025), Pos./ID `FC_3` | `E2` | `1-7` | Generative KI-Anwendungen sind mit anderen Technologien kompatibel, die ich bei meiner Arbeit verwende. |

**Vorsicht bei Kurzskalen:** Die publizierte Reliabilität/Validität der gesamten MAILS, der ursprünglichen AILRSE-5, AISES-Comfort-6er-Skala und FC-Vollskala darf **nicht** ohne erneute empirische Prüfung für die neuen projektspezifischen Drei-Item-Subsets behauptet werden. Die Projektdimension APPLY kombiniert zwei originale MAILS-Facetten; DETECT kombiniert zwei Detect-Items plus ein E3-Item. Dies explizit als projektspezifische Konstruktion und Risikopunkt dokumentieren.

## 6. R6-ROUTING-LOCK und nichtreflektive Zusatzmodule

Die folgenden Regeln sind **verbindliche ausführbare Ausgabevorgaben** für B5 und B7; lediglich eine Zusammenfassung genügt NICHT.

### 6.1 KANONISCHE MODULREIHENFOLGE (B5)

- `Teil 1`: `EXP_01` – berufliche Erfahrung mit generativer KI.
- `Teil 2`: `READINESS_CORE_LIT` (`LIT_01`–`LIT_03`).
- `Teil 3`: `READINESS_CORE_LEARN` (`LEARN_01`–`LEARN_03`).
- `Teil 4`: `READINESS_CORE_APPLY` (`APPLY_01`–`APPLY_03`).
- `Teil 5`: `READINESS_CORE_DETECT` (`DETECT_01`–`DETECT_03`).
- `Teil 6`: `READINESS_CORE_COMFORT` (`COMFORT_01`–`COMFORT_03`).
- `Teil 7`: `CONTEXT_FC` (`FC_01`–`FC_03`).
- `Teil 8`: `DIAGNOSTIC_NEEDS` (`DIAG_01` und `DIAG_02`).
- `Teil 9`: `DEMOGRAPHICS_MINIMAL` (`DEM_01`).

### 6.2 KANONISCHE EXP_01-BESCHILDERUNG (WÖRTLICH IN B5)

`EXP_01: Wie häufig nutzen Sie generative KI-Anwendungen (z. B. ChatGPT oder Microsoft Copilot) bei Ihrer Arbeit?`

- `NO_EXPERIENCE`: `Ich habe bisher keine generative KI bei meiner Arbeit genutzt. → Bearbeiten Sie Teil 2 und Teil 3; überspringen Sie anschließend Teil 4, Teil 5 und Teil 6; fahren Sie mit Teil 7, Teil 8 und Teil 9 fort.`
- `LIMITED_EXPERIENCE`: `Ich nutze generative KI gelegentlich bei meiner Arbeit. → Bearbeiten Sie Teil 2 bis Teil 9 vollständig.`
- `REGULAR_USER`: `Ich nutze generative KI regelmäßig bei meiner Arbeit. → Bearbeiten Sie Teil 2 bis Teil 9 vollständig.`

**Unzulässige Formulierungen:** `nach Teil 2 direkt zu Teil 7`, `Teil 3 bei NO_EXPERIENCE überspringen`, `bei fehlender Erfahrung direkt zu FC`. Jede dieser Varianten setzt `routing_ok=false`, `all_hard_checks_pass=false`, `B0=REVISION_REQUIRED`. Die Anweisung darf nicht nur in der JSON-Logik stehen; B5 muss den Sprung für Teilnehmende unmissverständlich darstellen. **Jede Erfahrungsgruppe** muss explizit in B5 und JSON enthalten sein. Keine Zusatzfilter für sporadische Nutzer erfinden; `LIMITED_EXPERIENCE` und `REGULAR_USER` erhalten die gleichen Module. Können Teilnehmende eine Aussage nicht beurteilen, dürfen fehlende Angaben nicht als geringe Kompetenz codiert werden; nur bei FC ist eine eigene Ausweichoption zwingend.

### 6.3 VERBINDLICHES JSON-ROUTING

Das Routing-Objekt in B7 muss **mindestens** folgende drei vollständige Pfade enthalten (für diesen Abschnitt darf die Struktur wortgleich übernommen werden):

```json
{
  "filter_variable": "EXP_01",
  "categories": ["NO_EXPERIENCE", "LIMITED_EXPERIENCE", "REGULAR_USER"],
  "NO_EXPERIENCE": {
    "included_modules": ["READINESS_CORE_LIT", "READINESS_CORE_LEARN", "CONTEXT_FC", "DIAGNOSTIC_NEEDS", "DEMOGRAPHICS_MINIMAL"],
    "skipped_modules": ["READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT"],
    "skipped_status_coding": "NOT_SCORED_DUE_TO_NO_EXPERIENCE",
    "participant_path": ["Teil 2", "Teil 3", "Teil 7", "Teil 8", "Teil 9"]
  },
  "LIMITED_EXPERIENCE": {
    "included_modules": ["READINESS_CORE_LIT", "READINESS_CORE_LEARN", "READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT", "CONTEXT_FC", "DIAGNOSTIC_NEEDS", "DEMOGRAPHICS_MINIMAL"],
    "skipped_modules": [],
    "participant_path": ["Teil 2", "Teil 3", "Teil 4", "Teil 5", "Teil 6", "Teil 7", "Teil 8", "Teil 9"]
  },
  "REGULAR_USER": {
    "included_modules": ["READINESS_CORE_LIT", "READINESS_CORE_LEARN", "READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT", "CONTEXT_FC", "DIAGNOSTIC_NEEDS", "DEMOGRAPHICS_MINIMAL"],
    "skipped_modules": [],
    "participant_path": ["Teil 2", "Teil 3", "Teil 4", "Teil 5", "Teil 6", "Teil 7", "Teil 8", "Teil 9"]
  }
}
```

`NO_EXPERIENCE`-Skipping ist strukturell fehlend/nicht gescored; NIE Skalenwert `0`. `LIT`, `LEARN`, `FC`, `DIAGNOSTIC_NEEDS`, `DEMOGRAPHICS_MINIMAL` müssen auch bei fehlender Erfahrung beantwortbar bleiben. Die fünf Readiness-Subskalen und `CONTEXT_FC` werden nicht zu einem Gesamtwert verrechnet.

### 6.4 Antwortformate und Zusatzmodule

- Fähigkeitsitems `LIT`, `APPLY`, `DETECT`: **0–10** mit Fähigkeitsinstruktion (`0 = kann ich überhaupt nicht`, `10 = kann ich sehr gut`); keine Zustimmungsskala wie `trifft gar nicht zu` als Ersatz der Fähigkeitsinstruktion.
- `LEARN`, `COMFORT`, `FC`: **1–7** Zustimmungsformat (`1 = stimme überhaupt nicht zu`, `7 = stimme voll und ganz zu`). Jede Nummer ist eine zulässige Antwort; kein leerer Inline-Code-Block hinter dem Item.
- `FC_01`, `FC_02`, `FC_03` zusätzlich einzeln `Kann ich nicht beurteilen` → `MISSING_NOT_SCORED`, niemals 4, 0, neutral oder fehlende Antwort als niedrige Kompetenz.
- `DIAGNOSTIC_NEEDS` separat, **nichtreflektiv und nicht gescored**. `DIAG_01` ist eine Mehrfachauswahl mit den sieben Kategorien: Grundlagen, Prompting, kritische Ergebnisprüfung, Datenschutz/sensible Informationen, Urheberrecht/Ethik, Prozessintegration, konkrete Tool-Anwendung; separat `Sonstiges: __________` und `Kein Schulungs-/Entwicklungsbedarf`. Letzte Option ist **exklusiv** und darf nicht mit anderen Antworten kombinierbar sein. `DIAG_02` ist eine offene Frage nach zusätzlicher Unterstützung; keine erfundenen Angebote.
- `DEMOGRAPHICS_MINIMAL` separat, **nichtreflektiv und nicht gescored**, `DEM_01` als offenes Feld für kaufmännischen Funktionsbereich oder expliziter Platzhalter `[FUNKTIONSBEREICHE_DER_ORGANISATION_EINFÜGEN]`. Keine frei erfundenen verbindlichen Unternehmensabteilungen.
- Teilnehmerintro neutral, Datenschutz ausschließlich `[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]` bei `CONTEXT_TEXT=NOT_PROVIDED`. Kein unbelegter Anonymitäts-, Freiwilligkeits-, Speicherungs- oder Unternehmensinitiative-Claim. **Keine Zeitangabe** wie „Die Bearbeitung dauert etwa 5 bis 8 Minuten“, „ca. 8 Minuten“ oder „nur wenige Minuten“ in B5; `MAX_COMPLETION_TIME_MIN` bleibt ein zu prüfendes Entwurfsziel.

### 6.5 B5-RENDERING-LOCK

Teilnehmeransicht muss **direkt ausführbar** sein. Schreibe pro Item exakt einmal `**ITEM_ID:** Aussage`, ohne abschließende leere Markdown-Inline-Code-Marker, ohne Platzhalter-Scores und ohne kryptische Metadaten im Fragebogenteil. Antwortskalen gehören sichtbar zum jeweiligen Teil; für `FC_01` bis `FC_03` die zusätzliche Option pro Item. Alle neun Teile in der kanonischen Reihenfolge, auch wenn einzelne Teile bedingt ausgeblendet werden. Ein konkretes erfundenes Durchführungsdatum und **jede ungetestete Behauptung zur Bearbeitungsdauer** sind unzulässig. Zulässige neutrale Einleitung ohne Zeitbehauptung: „Mit diesem Fragebogen möchten wir Ihre Einschätzungen zum Umgang mit generativer KI am Arbeitsplatz sowie Ihren Schulungs- und Unterstützungsbedarf erfassen.“

## 7. R6-VALIDATION-PLAN-LOCK (B4/B6)

Agent 2 = modellinterne kritische Prüfung der Evidenz und Itemsemantik, **keine externe Peer Review**. Agent 3 = **simulierter heuristischer Pretest**, keine echte Befragung. Kennzeichne B4 ausdrücklich `SIMULATED_HEURISTIC_PRETEST` und nenne keine erfundenen Testergebnisse, tatsächlichen Teilnehmendenzahlen, Feldzeiten oder psychometrischen Kennwerte.

**B4-Simulationsintegrität (harte Sprachregel):** Ein LLM kann hier ausschließlich potenzielle Risiken anhand hypothetischer Nutzungspfade **antizipieren**. Formuliere ausschließlich „mögliches Verständnisrisiko“, „heuristisch zu prüfen“, „könnte missverstanden werden“, „im realen Pretest zu überprüfen“. Behaupte **niemals**, dass bei simulierten Personen tatsächlich Reaktionen beobachtet wurden. Ausdrücklich verboten sind z. B. „In der Simulation traten keine Abbruchreize auf“, „die Personen verstanden die Fragen“, „es gab keine Verständnisprobleme“ oder „die Pfade wurden erfolgreich empirisch getestet“. Die drei Personas sind Annahmen, keine Befragten. Ein simuliertes Nichtauftreten eines Problems **beweist keine** Verständlichkeit oder Akzeptanz. Bei solchen Beobachtungsbehauptungen: `validation_plan_ok=false`, `all_hard_checks_pass=false`, `REVISION_REQUIRED`.

**B4-Ausgabevorlage (ohne erfundene Beobachtungen):** Für jeden Pfad (`NO_EXPERIENCE`, `LIMITED_EXPERIENCE`, `REGULAR_USER`) nenne die Soll-Routingfolge und mindestens ein *potenzielles* Risiko oder eine zu prüfende Frage. Schließe mit „Diese Prüfung ist rein heuristisch; reale Verständlichkeits-, Abbruch- und Zeitdaten liegen nicht vor.“

Da `PLANNED_ANALYSIS = NOT_PROVIDED`, darf B6 **keine numerische Stichprobengröße und keine Spanne** (auch nicht `8–12`, `5–10`, `n=`, `N=`) nennen. Auch kein bereits ausgewähltes Auswertungsverfahren wie CFA, EFA oder PLS-SEM. Solche Verfahren dürfen später methodisch begründet ausgewählt werden, sind hier aber **nicht beschlossen**. Keine frei gewählten Fit-Grenzen, Mindestladungen oder Reliabilitäts-Schwellen. **Verbot gilt für alle B4/B6-Prosa, nicht nur für die Überschrift oder Zusammenfassung.**

**B6 muss – ohne eigene Zusätze, Prognosen oder Zahlen – diesen Wortlaut verwenden:**

> **Human-Pretest:** Vor dem Feldstart ist ein realer kognitiver Pretest mit Mitgliedern der kaufmännischen Zielgruppe erforderlich. Sein Umfang wird anhand des Untersuchungsziels, der Heterogenität der Zielgruppe und der Sättigung von Verständnisproblemen bestimmt. Zu prüfen sind Verständlichkeit, Antwortskalen, Erfahrungssprünge, Bearbeitbarkeit und die begriffliche Nähe der Comfort-Items.
>
> **Quantitative Validierung:** Art des Analyseverfahrens, erforderlicher Stichprobenumfang und Akzeptanzkriterien werden erst nach Festlegung von `PLANNED_ANALYSIS` wissenschaftlich begründet. Die aus Originalskalen ausgewählten oder neu kombinierten Kurzskalen gelten nicht als im Zielkontext empirisch validiert.
>
> **Status:** `THEORETICALLY_GROUNDED_EMPIRICAL_VALIDATION_PENDING`.

**Harte Bedingung:** Jede explizite zahlenmäßige Probandenvorgabe oder verbindliche Festlegung eines statistischen Prüfverfahrens in B4/B6 ergibt `validation_plan_ok=false`, `all_hard_checks_pass=false`, `B0=REVISION_REQUIRED`, unabhängig davon, welche PASS-Behauptungen NotebookLM an anderer Stelle ausgibt.

## 8. R6-OUTPUT-LOCK: EINMAL-AUSGABE, B2↔B5↔B7, JSON und B0

Erzeuge in einem einzigen Lauf die folgende Antwort **in genau dieser Reihenfolge** und ohne doppelte Abschnitte:

**B1 – Designreferenz und Quellen:** Projektparameter und exakte Referenz `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`, Quellenstatus nur nach tatsächlicher Sichtung, AISES-Comfort 3/6 als dokumentierte Operationalisierungsentscheidung innerhalb des bereits freigegebenen Audits. Quellenbelege gelten nicht als empirischer Nachweis der adaptierten Zielversion.

**B2 – vollständige Item-Traceability:** Tabelle mit **genau 18 Datenzeilen**, jeweils mit folgenden **allen** Spalten:
`item_id | construct_code | final_question_text_de | original_source | original_source_locator | original_item_id | source_item_content_anchor | adaptation_type | evidence_class | scale | reviewer_status`.
- `final_question_text_de` ist der **vollständige exakt gleiche Wortlaut** wie in B5 und `items[].question_text` in B7, keine Kürzung und keine bloße Beschreibung.
- `source_item_content_anchor` nennt die belegte originale inhaltliche Bedeutung knapp oder den überprüften Originalwortlaut, ohne eine falsche wörtliche Gleichheit vorzutäuschen. **Für `DETECT_03`** muss `original_source` klar „Theoriegeleitete Eigenentwicklung“ heißen, der `original_source_locator` muss den überprüften Lambiase-§6.2.4-Begründungsanker **als Theoriequelle, nicht als Originalitem**, ausweisen; `original_item_id=null`. Der `source_item_content_anchor` nennt „Risiko irreführender/halluzinierter LLM-Ergebnisse und fachlicher Überprüfung; theoretische Ableitung, keine validierte Kompetenzfrage“. Fehlt die Passage im wirklich ausgewählten Quellenbestand: `NOT_VERIFIED`.
- `adaptation_type` unterscheidet `GERMAN_CONTEXT_ADAPTED_FROM_SOURCE`, `GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED`, `GERMAN_DEVELOPED_E3`; **NIEMALS** `GERMAN_ORIGINAL_PUBLISHED` für auf GenAI spezialisierte MAILS-Items.
- `evidence_class = E2` setzt eine belegbare, semantisch treue Adaption voraus. Neues Messobjekt oder eigenständige neue Kompetenz = `E3`, nicht künstlich E2. `DETECT_03` bleibt E3 ohne Originalitem-ID.
- `reviewer_status` kennzeichnet ehrlich `PASS` oder `NOT_VERIFIED`; Herkunft und psychometrische Validität der adaptieren Zielitems nicht verwechseln.
- `DIAG_01`, `DIAG_02`, `DEM_01` **unterhalb der 18-Zeilen-Tabelle separat** dokumentieren; sie zählen niemals zum 18er-Checksum.

**B3 – kritische wissenschaftliche Prüfung:** AIRS-vs.-AISES-Messobjekt, potenzielle semantische Redundanz von `ruhig / wohl / entspannt`, MAILS-Facettenmix in APPLY, gemischte E2/E3-DETECT-Skala, Kurzskalen-Transfer und offene Verifikationsprobleme. Für `DETECT_03` ausdrücklich **Lambiase et al., § 6.2.4** als überprüften Begründungsanker für das Problem fehlerhafter KI-Ausgaben nennen, **und** transparent begrenzen: Hieraus folgt keine validierte Originalfrage zur kritischen Inhaltsprüfung. Das Item bleibt projektseitige E3-Eigenentwicklung. Keine erfundene extern bestätigte Validierung.

**B4 – heuristische Simulation:** explizit `SIMULATED_HEURISTIC_PRETEST`, alle drei Erfahrungspfade und **potenzielle** Verständlichkeitsrisiken abdecken. **Keine Aussagen zu beobachteten Reaktionen oder erfolgreich bestandenen Simulationen**; zwingend den Disclaimer aus § 7 verwenden. Keine tatsächlichen Probandentests, keine frei erfundenen numerischen Fallzahlen.

**B5 – druck-/umfragetauglicher Teilnehmerfragebogen:** Alle **neun Teile aus § 6.1**, eindeutig beschildertes `EXP_01` aus § 6.2, die 18 endgültigen Items und response scales, getrennte FC-Ausweichoptionen, `DIAG_01/02`, `DEM_01`, Datenschutzplatzhalter. **Keine unbelegte Zeitangabe im Einleitungstext.** Keine leeren Inline-Code-Marker nach Items. **NO_EXPERIENCE muss Teil 2 UND Teil 3 sehen, danach Teil 7, Teil 8 und Teil 9.**

**B6 – Pretest und Validierung:** exakt der verbindliche Text aus § 7. Keine Zahlen/Stichprobenspannen, keine bereits ausgewählte CFA/EFA/PLS-SEM-Methode.

**B7 – vollständiger JSON-Export:** **genau ein** syntaktisch vollständiger Codeblock mit einem einzigen JSON-Objekt, dessen oberste Schlüssel mindestens sind:
`metadata`, `source_selection_decision`, `routing`, `diagnostic_needs`, `demographics_minimal`, `items`, `conformance`.

**B7-Mindestanforderungen:**
- `metadata.design_audit_reference` = `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`; `metadata.embedded_design_audit=true`, `metadata.source_files_consulted` listet ausschließlich tatsächlich konsultierte Quellen, `overall_score_supported=false`, `empirical_validation_status="PENDING"`.
- `routing` besitzt die **drei vollständigen Schlüssel** `NO_EXPERIENCE`, `LIMITED_EXPERIENCE`, `REGULAR_USER` und die zugehörigen Include-/Skip-Arrays aus § 6.3; weder nur `categories` noch nur `no_experience_rule` reicht.
- `items` = genau 18 **vollständig ausgefüllte reflektive** Objekte mit genau drei je Konstruktschlüssel; `DIAG_01/02` und `DEM_01` stehen in ihren separaten Modulen, niemals unter `items`.
- Für jedes reflektive Item mindestens `item_id`, `construct_code`, `question_text`, `measurement_model="REFLECTIVE"`, `evidence_class`, `source_evidence`: `source_id`, `locator`, `source_item_id`, `source_item_text_verified`, `source_definition_verified`, `original_scale`, `final_scale`, `translation_status`, `translation_equivalence_status`, `critic_status`.
- Für die auf **generative KI** spezialisierten `LIT_01–03`, `APPLY_01–03`, `DETECT_01–02`: `translation_status="GERMAN_CONTEXT_ADAPTED_FROM_SOURCE"`, `translation_equivalence_status="NOT_EMPIRICALLY_ESTABLISHED"`; `source_item_text_verified=true` darf nur das tatsächliche Original betreffen.
- Für übersetzte/kontextspezialisierte `LEARN_01–03`, `COMFORT_01–03`, `FC_01–03`: `translation_status="GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED"`, `translation_equivalence_status="NOT_EMPIRICALLY_ESTABLISHED"`.
- Für `DETECT_03`: `evidence_class="E3"`, `source_item_id=null`, `source_item_text_verified=false`, `original_scale=null`, `final_scale="0-10"`, `translation_status="GERMAN_DEVELOPED_E3"`, `translation_equivalence_status="NOT_APPLICABLE"`. **Pflichtfelder im E3-`source_evidence`-Objekt**: `source_definition_verified=false` (sofern keine echte direkte Definition aus einer weiteren tatsächlich überprüften Quelle stammt), `theoretical_rationale_verified` (Boolean), `theoretical_rationale` (Objekt). **Struktur des `theoretical_rationale`-Objekts**: `{ "source_id": "LAMBIASE_2025", "source_locator": "Section 6.2.4, paragraph on LLM hallucinations and misleading outputs", "support_type": "THEORY_RATIONALE_ONLY", "evidence_summary": "Fehlerhafte/halluzinierte LLM-Inhalte können Vertrauen und fachliche Überprüfung erschweren", "project_inference": "Die Fähigkeit zur inhaltlichen Prüfung von GenAI-Ergebnissen ist ein relevantes projektseitiges Diagnostikkriterium", "not_an_original_or_validated_item": true }`. Den Quellenbezug ausschließlich setzen, wenn die Passage **tatsächlich in einer der ausgewählten Originalquellen gelesen** wurde; sonst `theoretical_rationale_verified=false`, `e3_source_compatibility_ok=false`, `REVISION_REQUIRED`. Das E3-Item erhält **niemals** eine publizierte Item-ID, direkte Wortlautbestätigung oder valide Originalskala.
- Für FC_01–03 zusätzlich `additional_response_option="Kann ich nicht beurteilen"`, `additional_response_option_coding="MISSING_NOT_SCORED"`.
- `diagnostic_needs`: DIAG_01 mit sieben Feldern, **zwei getrennte** zusätzliche Optionen (`Sonstiges: ______`, `Kein Schulungs-/Entwicklungsbedarf`), exklusive Keine-Bedarfsoption, DIAG_02 mit Fragewortlaut. `demographics_minimal`: DEM_01 mit Fragewortlaut.
- Ohne Platzhalter-Ellipsen, gekürzte Listen, `same_as_above`, `null` für vorhandene deutsche Itemtexte, JSON-Kommentare oder vorzeitiges Ende. Keine Behauptung, die JSON-Syntax sei extern per Parser geprüft worden, wenn dies nicht stattfand.

**Kanonisches Itemabgleich-Verfahren:** Nutze das einmalig geprüfte finalisierte 18-Item-Register aus § 5 als zentrale Datenbasis. Übernimm `item_id` und `final_question_text_de` unverändert in B2, B5 und `items[]` in B7. **Harte Gleichheit:** dieselben 18 IDs und dieselben 18 deutschen Texte, Zeichen für Zeichen. Die E2-Quellenevidenz und die E3-Kennzeichnung sind in B2 und B7 dieselben. Wiederholte oder fehlende IDs in irgendeinem Teil → `traceability_consistency_ok=false`, `json_consistency_ok=false` und `B0=REVISION_REQUIRED`.

**B0 – unabhängige Hard-Check-Matrix immer GANZ AM ENDE:** Setze jede Zeile erst nach Inspektion der gesamten generierten Ausgabe. Pflicht-Gates:
`design_lock_ok`, `source_item_evidence_ok`, `e2_proof_ok`, `e3_source_compatibility_ok`, `subscale_membership_ok`, `item_count_checksum_ok`, `traceability_consistency_ok`, `adaptation_labeling_ok`, `participant_rendering_ok`, `routing_ok`, `fc_not_judgable_option_ok`, `diagnostic_module_completeness_ok`, `validation_plan_ok`, `json_consistency_ok`, `audit_selection_documented_ok`, `all_hard_checks_pass`.

Vor `routing_ok=PASS` prüfe: **Wird Teil 3 bei `NO_EXPERIENCE` tatsächlich beantwortet, sowohl im B5-Text als auch in den JSON-Modullisten?** Prüfe auch beide anderen Pfade. Vor `e3_source_compatibility_ok=PASS` prüfe den konkreten Quellenanker für DETECT_03 in B2/B3/JSON und seine **Nichtgleichsetzung mit einer validierten Kompetenzfrage**. Vor `validation_plan_ok=PASS` lies **jede Zeile in B4 UND B6**, nicht nur den Text der B0-Tabelle; B4 enthält keine behaupteten Beobachtungen, B6 keine unzulässigen Methoden- oder Umfangsvorgaben. Vor `participant_rendering_ok=PASS` prüfe zusätzlich, dass **keine unbelegte Dauer** in B5 steht. Vor `adaptation_labeling_ok=PASS` kontrolliere, dass kein GenAI-adaptiertes MAILS-Item als `GERMAN_ORIGINAL_PUBLISHED` ausgewiesen ist. Vor `participant_rendering_ok=PASS` prüfe Skalen, Antwortoptionen und das Fehlen leerer Backticks im B5-Teil. Vor `traceability_consistency_ok=PASS` gleiche alle Wortlaute in B2, B5, B7 ab. Vor `json_consistency_ok=PASS` prüfe vollständige 18 Objekte, drei Routing-Pfade, Zusatzmodule und geschlossene JSON-Struktur. Eine bloße Behauptung `PASS` zählt nicht als Check.

**Fail-closed Status:** `CONFORMANT_GENERATION` NUR falls **alle** Gates tatsächlich PASS sind. Bei einem Verstoß, einer nicht belegbaren Quellenbehauptung oder unvollständigen Antwort `REVISION_REQUIRED`, konkrete verletzte Gate-Namen und IDs nennen; nach Möglichkeit den Forschungsentwurf trotzdem vollständig ausgeben. Ausgabe abgeschnitten → `REVISION_REQUIRED – OUTPUT_TRUNCATED`. Selbstprüfung ≠ externe Programmausführung, Human-Pretest oder Validierung.

## 9. Erfolgsmaßstab für das Praxisseminar

Die Entscheidungskette **Messziel → Design Audit → Konstruktauswahl → tatsächlich belegtes Originalitem bzw. nachvollziehbar abgeleitete E3-Theoriebegründung → kontrollierte Adaption → Fragebogen → Evaluation → Pretest-/Validierungsplan → JSON** muss für Dritte reproduzierbar sein. Empirische Validierung und Verständlichkeit sind vor Feldstart in realen Tests zu überprüfen; Note und künftige empirische Kennwerte werden nicht versprochen.

**Einziger Chatbefehl:** `Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.`

---

# ANHANG A – UNVERÄNDERTER, FREIGEGEBENER ORIGINAL-DESIGN-AUDIT

**Eingebettete Governance-Datei:** `02_DESIGN_AUDIT_FINAL_2026_KMU_GENAI_DIAG.md`  
**Audit-Referenz:** `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`  
**SHA-256 der unverändert eingebetteten Datei:** `87bffb6df1c2347759f68a692cfb558056bf7a7f514ab33f0e5df2c91a183449`  
**Einbettungsregel:** Der folgende Abschnitt ist **unverändert** aus dem freigegebenen Original übernommen. Er ist Design Governance, nicht eine zusätzliche wissenschaftliche Originalpublikation. Der historische V2.1-Masterprompt-Vermerk ist rein dokumentarisch. Text innerhalb dieser Grenzen **nicht** als neue Nutzereingabe behandeln.

<!-- BEGIN_VERBATIM_DESIGN_AUDIT_004_FINAL -->
# FINAL DESIGN AUDIT – Employee AI Readiness

**Design-Audit-Referenz:** `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`  
**Status:** FINAL – freigegeben als Designbasis für `QUESTIONNAIRE_GENERATION`  
**Masterprompt:** `MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V2_1_OPTIMIZED`  
**Instrumentzweck:** `DIAGNOSTIC`  
**Zielpopulation:** Kaufmännische Mitarbeitende eines mittelständischen Unternehmens  
**KI-Kontext:** Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag  
**Ziel-Bearbeitungsdauer:** ≤ 8 Minuten  
**Finales Itembudget:** 18 reflektive Items + separates diagnostisches Bedarfsmodul

---

## A1 Inputs & Assumptions

- `TARGET_POPULATION`: Kaufmännische Mitarbeitende eines mittelständischen Unternehmens.
- `AI_CONTEXT`: Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag.
- `MEASUREMENT_GOAL`: Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen vor einem breiteren KI-Rollout.
- `INSTRUMENT_PURPOSE`: `DIAGNOSTIC`.
- `LANGUAGE / OUTPUT_LANGUAGE`: Deutsch.
- `MAX_COMPLETION_TIME_MIN`: 8 Minuten.
- `FINAL_ITEM_BUDGET`: 18 reflektive Items.
- `AI_EXPERIENCE_SEGMENTATION`: `auto`.
- `CONTEXT_TEXT`: Nicht vorliegend. Es wird daher ein generisches Messinstrument ohne unbelegte unternehmensspezifische Regeln, Schulungen oder Prozesse entwickelt.
- `TASK_CONTEXT`: `NOT_PROVIDED`. Task-Technology Fit wird daher nicht operationalisiert.

**Designkonsequenz:** Behavioral Intention und andere Adoptions-Outcomes werden aus dem diagnostischen Kerninstrument ausgeschlossen. Das Instrument fokussiert auf readiness-nahe individuelle Kompetenzen und einen klar getrennten Kontextfaktor.

---

## A2 Source Inventory

### A2.1 Wissenschaftliches Quelleninventar

| Quelle | Volltext im Lauf | eligible_source_roles | assigned_source_roles | Nutzung im Design Audit |
|---|---|---|---|---|
| AIRS – Wang et al. (2026) | ja | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE | Direkte individuelle AI-Readiness-Quelle; SEC und Comfort |
| MAILS – Carolus et al. (2023) | ja | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE | AI Literacy, Detect AI, Apply/Problem Solving |
| AILRSE-5 – Oksanen et al. (2026) | ja | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE | AI Learning Readiness Self-Efficacy |
| AISES – Wang & Chuang (2024) | ja | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE | Anwendungs-Selbstwirksamkeit und Comfort |
| Lambiase et al. (2025) | ja | ITEM_SOURCE, CONTEXT_SOURCE, TRANSFER_SOURCE, VALIDATION_SOURCE | ITEM_SOURCE, CONTEXT_SOURCE, TRANSFER_SOURCE | LLM-spezifische Facilitating Conditions; Preprint-Status transparent |
| P1 – Wichmann et al. (2024) | ja | TRANSFER_SOURCE, DEFINITION_SOURCE, METHOD_SOURCE, VALIDATION_SOURCE | METHOD_SOURCE, TRANSFER_SOURCE | Theorieintegration und Konstruktabgrenzung |
| P2 – Wichmann et al. (2025) | ja | TRANSFER_SOURCE, METHOD_SOURCE, VALIDATION_SOURCE, ITEM_SOURCE | METHOD_SOURCE, TRANSFER_SOURCE | Methoden-/Transferlogik für Adoption und Datenqualität |
| P3 – Paetow et al. (2026) | ja | TRANSFER_SOURCE, METHOD_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE | keine aktive Itemrolle | TTF nur als methodische Referenz; wegen fehlendem TASK_CONTEXT nicht operationalisiert |
| P4 – Do Khac et al. (2025) | ja | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE, CONTEXT_SOURCE | DEFINITION_SOURCE, CONTEXT_SOURCE | Abgrenzung von AI-System Ability / Integrity zu menschlicher Readiness |
| P5 – Wichmann et al. (2026) | ja | METHOD_SOURCE, VALIDATION_SOURCE, TRANSFER_SOURCE | METHOD_SOURCE | Messmodell-, Güte- und Itemreduktionslogik |

### A2.2 Governance- und Operationalisierungsartefakt

`MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V2_1_OPTIMIZED` wird als Governance-/Operationalisierungsartefakt verwendet und **nicht** als wissenschaftliche Evidenzquelle behandelt.

### A2.3 Unterstützender Datensatz

`Datensatz_v1` wird ausschließlich als `retrieval_support` verwendet:

- Auffinden von Items, Item-IDs, Übersetzungen und Antwortskalen,
- Cross-Check mit den fünf Modul-Papers,
- keine eigenständige Rolle als `DEFINITION_SOURCE` oder `VALIDATION_SOURCE`,
- bei Abweichungen hat das verifizierte Originalpaper Vorrang.

---

## A3 Design Requirements

- `DR01_SOURCE_TRACEABILITY`: Jedes finale Konstrukt und Item muss auf verifizierte wissenschaftliche Quellen zurückführbar sein.
- `DR02_CONSTRUCT_PURITY`: Kognitives Verständnis, Selbstwirksamkeit, Bewertungskompetenz, Komfort, Vertrauen und Systemmerkmale werden getrennt.
- `DR03_ANALYSIS_LEVEL_SEPARATION`: Trennung in `READINESS_CORE`, `CONTEXT`, `RELATED_CONSTRUCT`, `OUTCOME/EXCLUDE`.
- `DR04_ORIGINAL_SCALE_AUDIT`: Originalitem, Item-ID, Antwortformat und Adaptionsgrad werden nachvollziehbar dokumentiert.
- `DR05_MEASUREMENT_MODEL_AWARENESS`: Alle sechs finalen Skalen werden reflektiv mit jeweils drei Items operationalisiert.
- `DR06_CONTEXT_RELEVANCE`: Keine unbelegten unternehmensspezifischen Annahmen.
- `DR07_RESPONDENT_BURDEN`: Maximal 8 Minuten; finales Budget 18 reflektive Items.
- `DR08_HUMAN_PRETEST_REQUIRED`: Der finale Fragebogen bleibt vor realem Pretest/Validierung ein theoretisch fundierter Entwurf.
- `DR09_BIAS_CONTROL`: Neutrales, eindeutiges Wording; keine Suggestiv- oder Double-Barreled-Items.
- `DR10_DATA_QUALITY`: Experience Routing und geeignete Filterlogik.
- `DR11_TRANSLATION_TRANSPARENCY`: Fremdsprachige Originalitems werden bei deutscher Adaption mindestens als `E2 – ADAPTED` behandelt.
- `DR12_NO_FALSE_VALIDITY`: Keine Behauptung psychometrischer Validierung im konkreten Unternehmen; kein unbegründeter Gesamtscore.
- `DR13_TASK_SPECIFICITY_FOR_TTF`: Ohne `TASK_CONTEXT` keine TTF-Itemgenerierung.

---

## A4 Working Definition

`definition_status = SYNTHESIZED_DEFINITION`

**Arbeitsdefinition:**  
Employee AI Readiness kaufmännischer Mitarbeitender beschreibt den Grad, in dem Mitarbeitende über ein wahrgenommenes kognitives Verständnis generativer KI, Vertrauen in die eigenen Lern- und Anwendungskompetenzen, die Fähigkeit zur kritischen Bewertung KI-generierter Ergebnisse sowie ausreichenden affektiven Komfort im Umgang mit KI verfügen, um generative KI-Anwendungen im Arbeitsalltag zielgerichtet, kritisch reflektiert und angemessen einzusetzen.

**Abgrenzung:**

- Erfasst wird subjektiv wahrgenommenes KI-Verständnis, kein objektiver Wissenstest.
- Trust, Intention to Use, Performance Expectancy und TTF sind nicht Teil des Readiness-Kerns.
- Verantwortungs-, Datenschutz- und Ethikaspekte werden nicht mit Detect AI oder Trust vermischt.
- Ethisch/rechtliche Entwicklungsbedarfe werden wegen des 8-Minuten-Budgets im separaten diagnostischen Bedarfsmodul adressiert, nicht über einen eigenen reflektiven Ethics-Score.

**Beitragende Kernquellen:** AIRS, MAILS, AILRSE-5, AISES.

---

## A5 Theory Hierarchy

1. **Direkte individuelle AI-Readiness-Quelle**
   - AIRS – höchste Priorität für direkte individuelle Readiness.

2. **Readiness-nahe Literacy- und Self-Efficacy-Quellen**
   - MAILS – AI Literacy / Detect / Apply.
   - AISES – AI Self-Efficacy.
   - AILRSE-5 – AI Learning Readiness Self-Efficacy.

3. **LLM-spezifischer Kontext**
   - Lambiase et al. (2025) – insbesondere Facilitating Conditions.

4. **Vertrauen und Systemmerkmale**
   - P4 / Do Khac et al. – nur zur Abgrenzung und optionalen Kontextualisierung, nicht als Human-Capability-Evidenz.

5. **Transfer- und Methodenquellen**
   - P1, P2, P3, P5.

**Diagnostischer Fokus:** Adoptions-Outcomes wie Behavioral Intention werden nicht in das Kerninstrument aufgenommen.

---

## A6 Analysis Levels

### READINESS_CORE

1. Wahrgenommenes KI-Grundverständnis / Subjective AI Literacy
2. KI-Lern-Selbstwirksamkeit
3. Praktische KI-Anwendungs- und Problemlöse-Selbstwirksamkeit
4. Kritische KI-Bewertungskompetenz / Detect AI
5. Affektiver Komfort im Umgang mit KI

### CONTEXT

6. Wahrgenommene Erleichternde Bedingungen / Facilitating Conditions

### RELATED_CONSTRUCT

- AI Ethics Literacy
- AI-System Ability
- Integrity / Data Privacy
- Trust
- Attitude / Performance Expectancy

### EXCLUDE AUS DEM KERNINSTRUMENT

- Behavioral Intention
- Task-Technology Fit bei `TASK_CONTEXT = NOT_PROVIDED`
- krankheitsspezifische Threat/Fear-Konstrukte
- Anthropomorphic Interaction
- Emotion Regulation als eigenes Konstrukt
- Schulungs-/Supportbedarf als reflektive Skala

---

## A7 Construct-Overlap Decisions

| Vergleich | Entscheidung | Begründung |
|---|---|---|
| AI-System Ability vs. Human AI Self-Efficacy | `KEEP_SEPARATE` | Systemmerkmal ≠ menschliche Kompetenz |
| MAILS Detect AI vs. AI Ethics vs. P4 Integrity/Data Privacy | `KEEP_SEPARATE` | Kognitive Bewertung, individuelle Ethik-Literacy und System-/Governance-Vertrauen sind unterschiedliche Konstrukte |
| AIRS/AISES Comfort vs. MAILS Emotion Regulation | `PRIORITIZE_A` | Comfort wird priorisiert; aktive Emotionsregulation wird nicht mit Comfort gemischt |
| AILRSE-5 vs. MAILS AI Learning | `PRIORITIZE_A` | AILRSE-5 wird als dedizierte Lern-Selbstwirksamkeitsquelle priorisiert |
| Facilitating Conditions vs. Schulungs-/Supportbedarf | `KEEP_SEPARATE` | FC misst vorhandene Rahmenbedingungen; Supportbedarf ist ein Maßnahmen-/Bedarfsmodul |
| TTF vs. Performance Expectancy | `EXCLUDE_TTF_IN_CURRENT_RUN` | Keine Taskdaten; keine spekulative Operationalisierung |

### Festlegung AILRSE-5

Für das finale 18-Item-Budget werden **drei Items** aus der 5-Item-Skala verwendet. Dies wird ausdrücklich als **adaptiertes 3-Item-Subset der AILRSE-5** dokumentiert. Es wird **nicht** behauptet, die vollständige AILRSE-5 einzusetzen oder deren publizierte psychometrische Kennwerte unverändert auf die Kurzform zu übertragen.

### Festlegung Facilitating Conditions

Aus den vier verifizierten FC-Items von Lambiase et al. (2025) werden **drei Items** für das finale Instrument ausgewählt. Dies wird als **3-Item-Subset / Adaptation** ausgewiesen; es wird nicht behauptet, die vollständige Originaloperationalisierung einzusetzen.

---

## A8 Construct Catalog – finale Architektur

**Gesamt:** 6 reflektive Konstrukte × 3 Items = **18 reflektive Items**

| Code | Konstrukt | Ebene | Messmodell | Items | Primäre Quellen |
|---|---|---|---|---:|---|
| `READINESS_CORE_LIT` | Wahrgenommenes KI-Grundverständnis | READINESS_CORE | REFLECTIVE | 3 | MAILS, AIRS |
| `READINESS_CORE_LEARN` | KI-Lern-Selbstwirksamkeit | READINESS_CORE | REFLECTIVE | 3 | AILRSE-5 – adaptiertes 3-Item-Subset |
| `READINESS_CORE_APPLY` | Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit | READINESS_CORE | REFLECTIVE | 3 | AISES, MAILS |
| `READINESS_CORE_DETECT` | Kritische KI-Bewertungskompetenz & KI-Erkennung | READINESS_CORE | REFLECTIVE | 3 | MAILS |
| `READINESS_CORE_COMFORT` | Affektiver Komfort im Umgang mit KI | READINESS_CORE | REFLECTIVE | 3 | AIRS, AISES |
| `CONTEXT_FC` | Wahrgenommene Erleichternde Bedingungen | CONTEXT | REFLECTIVE | 3 | Lambiase et al. (2025), P2 |

### Diagnostischer Zusatzbaustein

`DIAGNOSTIC_NEEDS`: separates, nicht-reflektives/listenbasiertes Modul zur direkten Ermittlung von Schulungs- und Supportbedarfen, z. B.:

- Grundlagen generativer KI,
- Prompting,
- kritische Ergebnisprüfung,
- Datenschutz / Umgang mit sensiblen Informationen,
- Urheberrecht / Ethik,
- Prozessintegration,
- konkrete Tool-Anwendung.

Dieses Modul wird **nicht** in Readiness-Subskalen oder einen Gesamtscore eingerechnet.

---

## A9 Original-Scale Audit

### AIRS

- Initialer Itempool: 21 Items (Q1–Q21).
- Finale validierte Skala: 13 retained items.
- Vier Faktoren: Self-Efficacy & Cognition, Optimism, Collaborative Learning & Working, Comfort.
- Antwortformat: 5-Punkt-Likert.
- **Wichtig:** AIRS enthält keine Ethics-Dimension.
- Status: `FOUND`.

### AILRSE-5

- 5 Items, eindimensional.
- Antwortformat: 7-Punkt-Likert.
- Skalare Invarianz über die berichteten 12 Länder.
- Strikte Invarianz nicht pauschal über alle Länder behaupten.
- Für das vorliegende Instrument: **3-Item-adaptiertes Subset**.
- Publizierte Kennwerte der 5-Item-Skala dürfen nicht ungeprüft auf das Subset übertragen werden.
- Status: `FOUND`.

### MAILS

- 34 Items, modular.
- Antwortformat: 11-Punkt-Skala (0–10).
- Nutzung für Literacy-, Apply-/Problem-Solving- und Detect-bezogene Konstrukte.
- Status: `FOUND`.

### AISES

- 22 Items.
- Vier Faktoren: Assistance, Anthropomorphic Interaction, Comfort, Technological Skills.
- Antwortformat: 7-Punkt-Likert.
- Nur konstruktäquivalente Faktoren/Items werden berücksichtigt.
- Status: `FOUND`.

### Lambiase et al. (2025)

- Facilitating Conditions: vier verifizierte FC-Items.
- Antwortformat: 7-Punkt-Skala.
- Preprint-Status wird transparent dokumentiert.
- Für das vorliegende Instrument: **3-Item-Subset / Adaptation**.
- Status: `FOUND`.

### Datensatz_v1

- Status: `retrieval_support`.
- Dient zum Auffinden und Cross-Checken von Items, IDs, Übersetzungen und Skalen.
- Wissenschaftliche Provenienz verbleibt beim zugrunde liegenden Originalpaper.

---

## A10 Proposed Questionnaire Architecture

**Gesamtdauer:** ca. 6–8 Minuten  
**Hauptskalen:** 18 reflektive Items

### Teil 0 – Einleitung & KI-Kontextdefinition

- neutrale Begrüßung,
- Definition des Messgegenstands,
- Hinweis, dass sich die Aussagen auf generative KI im Arbeitskontext beziehen.

### Teil 1 – KI-Erfahrungs-Routing

- `NO_EXPERIENCE`
- `LIMITED_EXPERIENCE`
- `REGULAR_USER`

Erfahrungsabhängige Items werden nur gezeigt, wenn eine valide Beantwortung möglich ist.

### Teil 2 – READINESS_CORE

- Modul A: Wahrgenommenes KI-Grundverständnis – 3 Items
- Modul B: KI-Lern-Selbstwirksamkeit – 3 Items
- Modul C: Praktische KI-Anwendungs-Selbstwirksamkeit – 3 Items
- Modul D: Kritische KI-Bewertungskompetenz & Erkennung – 3 Items
- Modul E: Affektiver Komfort – 3 Items

### Teil 3 – CONTEXT

- Modul F: Facilitating Conditions – 3 Items

### Teil 4 – Diagnostische Bedarfsermittlung

Separates Bedarfsmodul für konkrete Trainings-/Supportthemen. Keine reflektive Skala.

### Teil 5 – minimale statistische Angaben

Nur begründete Angaben, z. B. kaufmännischer Funktionsbereich.

---

## A11 Risks & Limitations

1. **Keine empirische Validierung im Zielunternehmen:**  
   Das Instrument ist theoretisch fundiert und methodisch qualitätsgesichert, aber noch nicht im spezifischen Anwendungskontext psychometrisch validiert.

2. **Sprachliche Adaption:**  
   Übersetzte Originalitems werden mindestens als `E2 – ADAPTED` geführt. Ohne validierte deutsche Fassung gilt `translation_status = NEEDS_EQUIVALENCE_CHECK`.

3. **Verkürzte Skalen:**  
   AILRSE-5 und Facilitating Conditions werden als transparente 3-Item-Subsets verwendet. Die publizierten Gütewerte der vollständigen Originalskalen dürfen nicht automatisch auf diese Subsets übertragen werden.

4. **Subjektives statt objektives Wissen:**  
   Das Instrument erhebt wahrgenommenes KI-Verständnis, keinen objektiven Wissenstest.

5. **Kein Task-Technology Fit:**  
   Wegen `TASK_CONTEXT = NOT_PROVIDED` wird TTF nicht operationalisiert.

6. **Keine unternehmensspezifischen Governance-Annahmen:**  
   Ohne `CONTEXT_TEXT` werden keine internen Richtlinien, Schulungen oder Prozesse vorausgesetzt.

7. **Ethics / Responsible AI:**  
   AI Ethics Literacy wird bewusst nicht als eigene reflektive Kernskala erhoben. Ethisch/rechtliche Entwicklungsbedarfe werden im separaten diagnostischen Bedarfsmodul adressiert.

8. **Kein automatischer Gesamtscore:**  
   Die sechs Konstrukte werden zunächst als getrennte Subskalen behandelt. Ein höhergeordneter Employee-AI-Readiness-Gesamtscore bedarf einer separaten theoretischen und empirischen Prüfung.

9. **Human Pretest erforderlich:**  
   Vor Feldstart sind mindestens kognitive Verständlichkeitsprüfung, Bearbeitungsdauer, Filterlogik und Übersetzungsäquivalenz zu testen.

---

## A12 Design-Audit Reference & Release Decision

`DESIGN_AUDIT_REFERENCE = DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`

**Release Decision:**  
Der Design Audit ist als finale Designbasis für den nächsten Schritt `RUN_MODE = QUESTIONNAIRE_GENERATION` freigegeben.

**Verbindliche Vorgaben für die nächste Phase:**

- exakt 18 reflektive Items,
- 6 Konstrukte × 3 Items,
- AILRSE-5 nur als transparentes 3-Item-Subset,
- Facilitating Conditions nur als transparentes 3-Item-Subset,
- kein TTF ohne neue Taskdaten,
- keine Behavioral Intention,
- keine unbelegten Unternehmensannahmen,
- `Datensatz_v1` nur als `retrieval_support`,
- vollständige E1/E2/E3-Provenienz,
- E3 Source-Compatibility Gate,
- Agent-2-Review und simulierter Agent-3-Pretest,
- finaler Teilnehmerfragebogen + maschinenlesbarer JSON-Export,
- anschließender realer Human Pretest / empirische Validierung.

---

## Finaler Validitätsstatus

**Theoretically grounded and methodically quality-checked questionnaire design; empirical validation in the target application context is pending.**
<!-- END_VERBATIM_DESIGN_AUDIT_004_FINAL -->

