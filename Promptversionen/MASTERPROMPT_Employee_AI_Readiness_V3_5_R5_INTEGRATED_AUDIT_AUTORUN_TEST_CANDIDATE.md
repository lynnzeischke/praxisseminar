# MASTERPROMPT – Employee AI Readiness | V3.5-R5 INTEGRATED-AUDIT AUTORUN

**Status:** `TEST_CANDIDATE` – quellentreue Produktionsfassung für genau **einen** neuen NotebookLM-Fragebogenlauf. Der originale `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL` steht am Ende dieser Datei wortgetreu in **Anhang A**. Der Audit wird nicht nochmals als separate NotebookLM-Quelle benötigt. Die Qualität der tatsächlichen NotebookLM-Ausgabe ist vor einer FINAL-Freigabe unabhängig zu prüfen.

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

**Harte Beweisregel E2:** Überprüfe bei jedem Item **vor dem PASS** anhand der wirklich verfügbaren Primärpublikation die Itemnummer/ID oder Originalposition, den Wortlaut bzw. die überprüfte präzise Semantik, die Faktorzugehörigkeit, Messobjekt, Skala und Adaptionsart. In B2 und JSON Quellen-Locator und Prüfstatus pro Item festhalten. Aus alter KI-Ausgabe, einem Entwurfs-Manifest oder einem ähnlich klingenden Satz entstehen keine Originalbelege. Mögliche deutsche MAILS-Originalitems nicht fälschlich als englisch übersetzte Originalitems ausgeben. Übersetzung aus dem Englischen → `NEEDS_EQUIVALENCE_CHECK`, wenn keine validierte Übersetzung vorliegt. Bei fehlendem Volltext, abweichendem Itemwortlaut oder Inhaltswechsel: `E2_NOT_VERIFIED` und `e2_proof_ok=false`, auch wenn andere Checks PASS wären.

**MAILS Original-Positionsregel:** Die publizierte englische Appendix-A-Paginierung/Nummerierung ordnet `Use & Apply` Pos. 1–6, `Understand` Pos. 7–12, `Detect` Pos. 13–15 und `AI Problem solving` Pos. 23–25 zu. **Diese Positionsnummern sind Referenzpositionen, keine erfundenen Original-Variablennamen**. Akzeptiere nur Originalinhalte, die an dieser Position tatsächlich belegbar sind. AI-Erkennung von Anwendung oder Interaktionspartner ist nicht gleich Faktenprüfung eines generierten Textes.

**DETECT_03 – fester E3-Kandidat (keine doppelte Eigenschaft):** „Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.“ Dies ist eine **eigens entwickelte Prüfkompetenzfrage**, kein Originalitem der MAILS-Detect-Skala. Die Quellen müssen das kritische Bewerten von KI-Ergebnissen und die Möglichkeit inhaltlich falscher Ausgaben inhaltlich stützen; ausschließlich allgemeine KI-Erkennung genügt nicht. Ohne belegte, konkrete Theorieanbindung `e3_source_compatibility_ok=false`. **Nie** eine Originalitem-ID erfinden. Die Skala 0–10 ist das projektspezifische Endformat, keine publizierte Originalskala dieses E3-Items.

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
| `DETECT_03` | `READINESS_CORE_DETECT` | Originaldefinition für E3 verifizieren, Pos./ID `NOT_APPLICABLE` | `E3` | `0-10` | Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen. |
| `COMFORT_01` | `READINESS_CORE_COMFORT` | Wang & Chuang (2024), AISES, Pos./ID `CF1/Q25` | `E2` | `1-7` | Wenn ich mit generativer KI interagiere, fühle ich mich ruhig. |
| `COMFORT_02` | `READINESS_CORE_COMFORT` | Wang & Chuang (2024), AISES, Pos./ID `CF3/Q24` | `E2` | `1-7` | Wenn ich mit generativer KI interagiere, fühle ich mich wohl. |
| `COMFORT_03` | `READINESS_CORE_COMFORT` | Wang & Chuang (2024), AISES, Pos./ID `CF5/Q22` | `E2` | `1-7` | Wenn ich mit generativer KI interagiere, fühle ich mich entspannt. |
| `FC_01` | `CONTEXT_FC` | Lambiase et al. (2025), Pos./ID `FC_1` | `E2` | `1-7` | Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI-Anwendungen bei meiner Arbeit zu nutzen. |
| `FC_02` | `CONTEXT_FC` | Lambiase et al. (2025), Pos./ID `FC_2` | `E2` | `1-7` | Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen bei meiner Arbeit zu nutzen. |
| `FC_03` | `CONTEXT_FC` | Lambiase et al. (2025), Pos./ID `FC_3` | `E2` | `1-7` | Generative KI-Anwendungen sind mit anderen Technologien kompatibel, die ich bei meiner Arbeit verwende. |

**Vorsicht bei Kurzskalen:** Die publizierte Reliabilität/Validität der gesamten MAILS, der ursprünglichen AILRSE-5, AISES-Comfort-6er-Skala und FC-Vollskala darf **nicht** ohne erneute empirische Prüfung für die neuen projektspezifischen Drei-Item-Subsets behauptet werden. Die Projektdimension APPLY kombiniert zwei originale MAILS-Facetten; DETECT kombiniert zwei Detect-Items plus ein E3-Item. Dies explizit als projektspezifische Konstruktion und Risikopunkt dokumentieren.

## 6. Fragebogen-Routing und nichtreflektive Zusatzmodule

- Erfahrungsfilter `EXP_01`: `NO_EXPERIENCE` / `LIMITED_EXPERIENCE` / `REGULAR_USER`. Die Kategorien eindeutig und auf berufliche Nutzung beziehen.
- `NO_EXPERIENCE` erhält **LIT, LEARN, FC, DIAGNOSTIC_NEEDS, DEMOGRAPHICS_MINIMAL**; **APPLY, DETECT, COMFORT** werden übersprungen (`NOT_SCORED_DUE_TO_NO_EXPERIENCE`, kein Nullpunkt, keine fiktive Ersatzantwort).
- `LIMITED_EXPERIENCE` und `REGULAR_USER` erhalten alle sechs Skalen und die beiden Zusatzmodule. Bei sporadischen Nutzern nur Items erfassen, für die tatsächliche Erfahrung zur Beantwortung vorliegt; falls zusätzliche Filterregel verwendet, konsistent in B5 und JSON erläutern.
- Alle drei FC-Items behalten 1–7 **und** separat `Kann ich nicht beurteilen`, Kodierung `MISSING_NOT_SCORED`; weder neutraler Skalenmittelpunkt noch Nullwert.
- `DIAGNOSTIC_NEEDS` NICHT-reflektiv, NICHT scored, NICHT im 18er-Checksum: `DIAG_01` sieben Bedarfsfelder (Grundlagen, Prompting, kritische Ergebnisprüfung, Datenschutz/sensible Informationen, Urheberrecht/Ethik, Prozessintegration, konkrete Tool-Anwendung), dazu getrennt `Sonstiges: ____` und `Kein Schulungs-/Entwicklungsbedarf` (**exklusiv**); `DIAG_02` offene Frage nach zusätzlicher Hilfe/Unterstützung, keine erfundenen betrieblichen Leistungen.
- `DEMOGRAPHICS_MINIMAL` nichtreflektiv, nicht gescored, nur `DEM_01` kaufmännischer Funktionsbereich, **offenes Feld** oder `[FUNKTIONSBEREICHE_DER_ORGANISATION_EINFÜGEN]`; keine erfundenen Firmenabteilungen.
- Neutraler Teilnehmertext, Arbeitskontext klar; Datenschutz/Studieninformation ausschließlich wörtlich `[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]`, solange `CONTEXT_TEXT=NOT_PROVIDED`. Keine Behauptung von Anonymität, Freiwilligkeit, Datenspeicherung oder genehmigten Schulungen.

## 7. Pretest und spätere Validierung

Agent 2 prüft die reale Itemquellen-Zuordnung als **modellinterne kritische Evaluation**, aber behauptet keine unabhängige menschliche Prüfung. Agent 3 simuliert nur eine **heuristische** Verständlichkeits- und Routing-Prüfung aus Nutzerperspektiven; das ersetzt keinen echten kognitiven Human-Pretest.

Wenn `PLANNED_ANALYSIS = NOT_PROVIDED`: in B4/B6 keine feste numerische Teilnehmerzahl, keine behauptete getestete Bearbeitungszeit und kein bereits gewähltes Verfahren (etwa EFA/CFA/PLS-SEM), keine frei erfundenen Gütegrenzen. Keine vorgeschriebene quantitative Methode. **B6 Fallback:** Ein echter kognitiver Pretest ist nötig; sein Umfang wird von Ziel, Zielgruppenheterogenität und Verständnissättigung abhängig bestimmt. Analysestrategie, Stichprobe und Prüfkriterien werden erst nach Konkretisierung der Forschungsplanung begründet. Status: `THEORETICALLY_GROUNDED_EMPIRICAL_VALIDATION_PENDING`.

## 8. EINMAL-AUSGABE: verbindliches Format und technische Konsistenz

Erstelle aus dem einzigen Startbefehl die folgende Ausgabe **in exakt dieser Reihenfolge**:

**B1** Projektwerte, eingebettete Design-Audit-Referenz, Liste tatsächlich ausgewählter Quellen (einschließlich FC-Originalfrage-Datei) und dokumentierte Auswahlentscheidung `AISES-Comfort 3/6 im Rahmen von Audit 004_FINAL` (nicht als auditfremd behaupten); Quellenstatus.
**B2** Tabelle aller 18 reflektiven Items mit finalem identischem Wortlaut, primärer Originalquelle, Originalpositionsbeweis, Quellenevidenz E2/E3, Skala und Validierungsstatus, plus DIAG/DEM gesondert.
**B3** tatsächlich kritische Prüfung einschließlich möglicher nicht äquivalenter Adaptionen (AIRS vs AISES), redundanter Comfort-Items, gemischter MAILS-Facetten, E3 und fehlender Primärquellen.
**B4** als `SIMULATED_HEURISTIC_PRETEST` gekennzeichneter Durchgang ohne künstlich geschätzte Bearbeitungszeit.
**B5** vollständig lesbarer, direkt einsetzbarer Teilnehmerfragebogen (nicht nur Itemliste): neutraler Intro-/Datenschutzplatzhalter, EXP_01, 18 Items, sämtliche Antwortskalen, FC-Ausweichoption, DIAG_01/02, DEM_01, korrektes Routing.
**B6** nichtnumerischer Human-Pretest-/Validierungsplan (siehe Abschnitt 7).
**B7** **ein einziger vollständig syntaktisch gültiger JSON-Codeblock** mit dieser Grundstruktur:
```json
{
  "metadata": {"design_audit_reference":"DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL","run_mode":"QUESTIONNAIRE_GENERATION","overall_score_supported":false,"empirical_validation_status":"PENDING"},
  "source_selection_decision": {"comfort_source":"AISES","comfort_original_pool_items":6,"comfort_selected_items":3,"audit_amendment_required":false,"selection_justification":"documented within Audit 004_FINAL"},
  "routing": {},
  "diagnostic_needs": {},
  "demographics_minimal": {},
  "items": [],
  "conformance": {}
}
```
**Diese Struktur ist nur ein Schema**: Niemals die leeren `{}` oder `[]` als fertiges JSON übernehmen. Im echten B7 muss `items` **18 tatsächlich vollständig ausgefüllte reflektive Item-Objekte** enthalten, `routing` alle drei Erfahrungsgruppen und beide Zusatzmodule als separate Objekte. Jeder Eintrag in `items` mindestens: `item_id`, `construct_code`, `question_text`, `measurement_model`, `evidence_class`, `source_evidence` mit `source_id`, `locator`, `source_item_id`/Position, `source_item_text_verified`, `source_definition_verified`, `original_scale`, `final_scale`, `translation_status`, `critic_status`, sowie bei FC `additional_response_option`, `additional_response_option_coding`. Für E3: `source_item_id=null`, `source_item_text_verified=false`, `original_scale=null`. Für AISES: `source_item_id` mit echten CF/Q-Codes. `metadata.design_audit_reference` exakt wie oben; `metadata.embedded_design_audit = true` und `metadata.source_files_consulted` mit tatsächlich verwendeten Quellen. Für jeden E2-Item, dessen Original nicht überprüfbar war, `critic_status="NOT_VERIFIED"` statt ausgedachter PASS-Werte.

**B0 ERST GANZ AM ENDE** (vollständige Ausgabe zuerst, Status erst danach): Hard-Check-Matrix, unabhängig von vorherigen hypothetischen Statusannahmen. Mindestens `design_lock_ok`, `source_item_evidence_ok`, `e2_proof_ok`, `e3_source_compatibility_ok`, `subscale_membership_ok`, `item_count_checksum_ok`, `routing_ok`, `fc_not_judgable_option_ok`, `diagnostic_module_completeness_ok`, `validation_plan_ok`, `json_consistency_ok`, `audit_selection_documented_ok`, `all_hard_checks_pass`. PASS nur bei tatsächlich plausibel überprüften Bedingungen. Beim endgültigen Vergleich der Zeichenfolgen müssen die 18 Item-IDs und deutschen Fragewortlaute in B2/B5/B7 identisch sein; Sondermodule zählen nie mit. Kein zweiter B0/B1/B2-Start, keine duplizierten Sektionen, keine abgeschnittenen Tabellen oder JSON-Arrays.

**Fail-closed Entscheidung:** `CONFORMANT_GENERATION` nur wenn ALLE Bedingungen nachweisbar PASS, das komplette B7 nicht abgeschnitten ist und keine wissenschaftlich entscheidenden E2/E3-Verifikationen fehlen. Sonst `REVISION_REQUIRED` und konkret betroffene Item-IDs + fehlende Primärbelege/Regelfehler nennen; den Forschungsentwurf dennoch nach Möglichkeit vollständig zeigen. Bei Tokenlimit: `REVISION_REQUIRED – OUTPUT_TRUNCATED`, nicht behaupten dass JSON vollständig geprüft wurde. Erfolgreiche modellinterne Formalkontrolle ist keine externe technische Validierung und keine psychometrische Validierung.

## 9. Erfolgsmaßstab für das Praxisseminar

Die Entscheidungskette **Messziel → Design Audit → Konstruktauswahl → tatsächlich belegtes Originalitem → kontrollierte Adaption → Fragebogen → Evaluation → Pretest-/Validierungsplan → JSON** muss für Dritte reproduzierbar sein. Empirische Validierung und Verständlichkeit sind vor Feldstart in realen Tests zu überprüfen; Note und künftige empirische Kennwerte werden nicht versprochen.

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

