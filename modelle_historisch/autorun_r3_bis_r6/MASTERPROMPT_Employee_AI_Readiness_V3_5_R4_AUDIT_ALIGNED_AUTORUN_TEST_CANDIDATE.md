# MASTERPROMPT – Employee AI Readiness | V3.5-R4 AUDIT-ALIGNED AUTORUN

**Status:** `TEST_CANDIDATE` – zur unabhängigen Quellenevaluation und zum NotebookLM-Regressionstest. **Designbasis bleibt unverändert** `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`; keine ungeprüfte Nachtragsfreigabe und keine empirische Validitätsbehauptung.

## 1. Einzige Nutzereingabe / Start

`Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.`

Wenn dieser exakte Befehl eingegeben wird: sofort **einen vollständigen neuen Fragebogenlauf in einer einzigen Antwort** durchführen. Keine zusätzlichen Angaben, keinen zweiten Startprompt, keinen Folgeaufruf und keinen zweiten JSON-Export anfordern. Der Masterprompt selbst gilt **nicht** als wissenschaftliche Evidenzquelle.

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

**Prioritätsregel:** Der beigefügte, als `004_FINAL` freigegebene **Original-Design-Audit** ist die maßgebliche Designbasis. Frühere Masterprompts, NotebookLM-Ausgaben und ein separat **vorgeschlagener** Nachtrag dürfen die Aussagen des Audits nicht überschreiben. Eine im Audit bereits ausdrücklich zugelassene Quellenauswahl ist **keine** Änderung des Audits. Der Audit nennt bei `READINESS_CORE_COMFORT` sowohl `AIRS` als auch `AISES` (Abschnitt A8); für `AISES` dokumentiert er die Originalskala 1–7 (A9). Die Auswahl von **drei AISES-Comfort-Items** ist daher eine **dokumentationspflichtige Operationalisierungsentscheidung innerhalb des bestehenden Audits**, nicht automatisch ein genehmigungspflichtiger Nachtrag. Andere Designänderungen müssen gesondert ausgewiesen und dürfen nicht als bereits freigegeben gelten.

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

**DETECT_03 – fester E3-Kandidat (keine doppelte Eigenschaft):** „Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.“ Die ursprüngliche MAILS Detect-Skala belegt diesen Satz **nicht als empirisch validiertes Detect-Originalitem**. Leite ihn nur mit einer wirklich nachweisbar passenden Definition kritischer Bewertung ab; wenn die Quelle nur KI-Erkennung oder generalisierte Literacy stützt, `e3_source_compatibility_ok=false`. Kennzeichne den Score 0–10 als **projektspezifisch zugewiesenes Format**, nicht als „Originalskala“ dieses E3-Items.

**AIRS-Verwechslungsblock:** Q9/COM1: Verlegenheit bei Problemen in Anwesenheit anderer; Q8/COM2: gesundheits-/sicherheitsbezogene Bedenken; Q18/COM3: humanoide Roboter. KEINES davon automatisch als semantisch identisches Office-GenAI-Comfort-Item behandeln. AISES-Comfort-Originalitems stammen dagegen aus der veröffentlichten AISES-Faktorgruppe: `CF1/Q25` Ruhe, `CF3/Q24` Wohlbefinden, `CF5/Q22` Entspanntheit. Vor E2-Freigabe Quellenvolltext, originale Labels, zugehörige Itemformulierungen und tatsächliche 1–7-Skala überprüfen. Die drei nahe verwandten affektiven Formulierungen sind eine **potenzielle Redundanz**, im echten Pretest und bei der empirischen Messmodellprüfung gezielt zu überprüfen.

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
| `FC_01` | `CONTEXT_FC` | Lambiase et al. (2025), Pos./ID `FC_1` | `E2` | `1-7` | Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI-Anwendungen zu nutzen. |
| `FC_02` | `CONTEXT_FC` | Lambiase et al. (2025), Pos./ID `FC_2` | `E2` | `1-7` | Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen zu nutzen. |
| `FC_03` | `CONTEXT_FC` | Lambiase et al. (2025), Pos./ID `FC_3` | `E2` | `1-7` | Generative KI-Anwendungen sind mit den anderen von mir verwendeten Technologien kompatibel. |

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

**B1** Projektwerte, Design-Audit-Referenz und dokumentierte Auswahlentscheidung `AISES-Comfort 3/6 im Rahmen von Audit 004_FINAL` (nicht als auditfremd behaupten); Quellenstatus.
**B2** Tabelle aller 18 reflektiven Items mit finalem identischem Wortlaut, primärer Originalquelle, Originalpositionsbeweis, Quellenevidenz E2/E3, Skala und Validierungsstatus, plus DIAG/DEM gesondert.
**B3** tatsächlich kritische Prüfung einschließlich möglicher nicht äquivalenter Adaptionen (AIRS vs AISES), redundanter Comfort-Items, gemischter MAILS-Facetten, E3 und fehlender Primärquellen.
**B4** als `SIMULATED_HEURISTIC_PRETEST` gekennzeichneter Durchgang ohne künstlich geschätzte Bearbeitungszeit.
**B5** vollständig lesbarer Teilnehmerfragebogen: neutraler Intro-/Datenschutzplatzhalter, EXP_01, 18 Items, sämtliche Antwortskalen, FC-Ausweichoption, DIAG_01/02, DEM_01, korrektes Routing.
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
**Diese Struktur ist nur ein Schema**: Niemals die leeren `{}` oder `[]` als fertiges JSON übernehmen. Im echten B7 muss `items` **18 tatsächlich vollständig ausgefüllte reflektive Item-Objekte** enthalten, `routing` alle drei Erfahrungsgruppen und beide Zusatzmodule als separate Objekte. Jeder Eintrag in `items` mindestens: `item_id`, `construct_code`, `question_text`, `measurement_model`, `evidence_class`, `source_evidence` mit `source_id`, `locator`, `source_item_id`/Position, `source_item_text_verified`, `source_definition_verified`, `original_scale`, `final_scale`, `translation_status`, `critic_status`, sowie bei FC `additional_response_option`, `additional_response_option_coding`. Für E3: `source_item_id=null`, `source_item_text_verified=false`, `original_scale=null`. Für AISES: `source_item_id` mit echten CF/Q-Codes. `metadata.design_audit_reference` exakt wie oben. Für jeden E2-Item, dessen Original nicht überprüfbar war, `critic_status="NOT_VERIFIED"` statt ausgedachter PASS-Werte.

**B0 ERST GANZ AM ENDE**: Hard-Check-Matrix, unabhängig von vorherigen hypothetischen Statusannahmen. Mindestens `design_lock_ok`, `source_item_evidence_ok`, `e2_proof_ok`, `e3_source_compatibility_ok`, `subscale_membership_ok`, `item_count_checksum_ok`, `routing_ok`, `fc_not_judgable_option_ok`, `diagnostic_module_completeness_ok`, `validation_plan_ok`, `json_consistency_ok`, `audit_selection_documented_ok`, `all_hard_checks_pass`. PASS nur bei tatsächlich plausibel überprüften Bedingungen. Beim endgültigen Vergleich der Zeichenfolgen müssen die 18 Item-IDs und deutschen Fragewortlaute in B2/B5/B7 identisch sein; Sondermodule zählen nie mit. Kein zweiter B0/B1/B2-Start, keine duplizierten Sektionen, keine abgeschnittenen Tabellen oder JSON-Arrays.

**Fail-closed Entscheidung:** `CONFORMANT_GENERATION` nur wenn ALLE Bedingungen nachweisbar PASS, das komplette B7 nicht abgeschnitten ist und keine wissenschaftlich entscheidenden E2/E3-Verifikationen fehlen. Sonst `REVISION_REQUIRED` und konkret betroffene Item-IDs + fehlende Primärbelege/Regelfehler nennen; den Forschungsentwurf dennoch nach Möglichkeit vollständig zeigen. Bei Tokenlimit: `REVISION_REQUIRED – OUTPUT_TRUNCATED`, nicht behaupten dass JSON vollständig geprüft wurde. Erfolgreiche modellinterne Formalkontrolle ist keine externe technische Validierung und keine psychometrische Validierung.

## 9. Erfolgsmaßstab für das Praxisseminar

Die Entscheidungskette **Messziel → Design Audit → Konstruktauswahl → tatsächlich belegtes Originalitem → kontrollierte Adaption → Fragebogen → Evaluation → Pretest-/Validierungsplan → JSON** muss für Dritte reproduzierbar sein. Empirische Validierung und Verständlichkeit sind vor Feldstart in realen Tests zu überprüfen; Note und künftige empirische Kennwerte werden nicht versprochen.

**Einziger Chatbefehl:** `Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.`
