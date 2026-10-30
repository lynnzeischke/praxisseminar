# MASTERPROMPT — Employee AI Readiness | V3.5-R3 QUELLENTREU AUTORUN

**Status: TEST_CANDIDATE / A1_DESIGN_AMENDMENT_PROPOSED.** Keine Behauptung einer empirisch validierten Skala; eine Note kann nicht garantiert werden.

## 1. Einziger notwendiger NotebookLM-Befehl

`Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.`

Führe daraufhin **sofort einen neuen vollständigen Fragebogenlauf** aus. Niemals einen zweiten Startprompt, eine zweite Phase oder einen separaten JSON-Export anfordern. Lade als Quellen in NotebookLM diesen Masterprompt, das ursprüngliche Design Audit, den vorgeschlagenen Nachtrag A1 sowie die Primärquellen, die für die jeweilige Itemfamilie relevant sind.

## 2. Feste Projektwerte

```text
RUN_MODE = QUESTIONNAIRE_GENERATION
TARGET_POPULATION = Kaufmännische Mitarbeitende mittelständischer Unternehmen
AI_CONTEXT = generative KI im kaufmännischen Alltag, insbesondere ChatGPT Enterprise und Microsoft Copilot
MEASUREMENT_GOAL = subjektive Employee AI Readiness und Entwicklungs-/Schulungsbedarf diagnostizieren
INSTRUMENT_PURPOSE = DIAGNOSTIC
LANGUAGE = German
DESIGN_AUDIT_BASE = DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL
DESIGN_AUDIT_ADDENDUM = DESIGN_AUDIT_ADDENDUM_004_A1_PROPOSED
DESIGN_AMENDMENT_STATUS = PENDING_HUMAN_APPROVAL
MAX_REFLECTIVE_ITEMS = 18
MAX_COMPLETION_TIME_MIN = 8
SCALE_PREFERENCE = original_scales_per_selected_family
CONTEXT_TEXT = NOT_PROVIDED
TASK_CONTEXT = NOT_PROVIDED
PLANNED_ANALYSIS = NOT_PROVIDED
REPRODUCIBILITY_MODE = strict
DELIVERY_MODE = AUTORUN_SINGLE_COMMAND
SOURCE_POLICY = ACTUAL_ORIGINAL_ITEM_EVIDENCE
```

Wenn der Nutzer später den Nachtrag A1 ausdrücklich freigibt, darf nur dann `DESIGN_AMENDMENT_STATUS = APPROVED` verwendet werden. Die bloße Existenz des Nachtrags ist **keine** Freigabe. Selbst ein korrekt generierter Entwurf bleibt ohne empirischen Pretest methodisch unvalidiert.

## 3. Aufgabenstellung und bindende Architektur

Generiere einen vollständigen, nachvollziehbaren und einsatznahen Fragebogen: **sechs Konstrukte × drei reflektive Items = 18**. Die fünf individuellen Subskalen werden getrennt von `CONTEXT_FC` interpretiert. Niemals einen Gesamt-Readiness-Score ohne gesondert bestätigtes Messmodell berechnen. Bei fehlendem `TASK_CONTEXT` keine TTF-Items und keine Behavioral-Intention-Skala.

Nicht-reflektive Zusatzmodule außerhalb der 18er-Zählung: `DIAGNOSTIC_NEEDS` mit `DIAG_01` und `DIAG_02` sowie `DEMOGRAPHICS_MINIMAL` mit `DEM_01`.

Routing: `NO_EXPERIENCE` zeigt nur LIT, LEARN, FC, DIAG, DEM; überspringt APPLY, DETECT und COMFORT. `LIMITED_EXPERIENCE` und `REGULAR_USER` sehen alle sechs Konstrukte plus Zusatzmodule. Übersprungene Module werden als `NOT_SCORED_NO_EXPERIENCE` und **niemals** mit Nullwert kodiert.

Skalen:
- LIT, APPLY, DETECT: wahrgenommene Fähigkeit 0–10 (0 = kaum/gar nicht ausgeprägt, 10 = sehr gut/nahezu perfekt ausgeprägt);
- LEARN, COMFORT, FC: Zustimmung 1–7 (1 = stimme gar nicht zu, 7 = stimme voll und ganz zu);
- FC_01–FC_03 haben jeweils `Kann ich nicht beurteilen` als separat codierten Wert `MISSING_NOT_SCORED`;
- `DIAG_01` Mehrfachauswahl mit eigenständigem offenen `Sonstiges` und **exklusiver** Option `Kein Schulungs-/Entwicklungsbedarf`.

Die Comfort-Skalenänderung gegenüber Audit `004_FINAL` ist **A1-provisorisch**. Wenn das Audit A1 nicht genehmigt wird, setze `design_amendment_ok=false` und zwingend `REVISION_REQUIRED`. Gib keinen Anschein, A1 sei bereits der Originalbeschluss.

## 4. Originalquellen-Governance: absolute Priorität

**Ein E2-Item braucht nachweisbar:** Primärpublikation, nachvollziehbaren Locator, eine existierende Original-Item-ID bzw. Positionsangabe, überprüften Originalinhalt (vorzugsweise semantische Paraphrase), dieselbe Kompetenz und denselben Gegenstand, Originalskala und dokumentierte Übersetzung/Kontextänderung. Übersetzungen selbst sind nicht validiert (`NEEDS_EQUIVALENCE_CHECK`). Nicht allein aus ähnlich klingendem Itemtext oder aus einer früheren NotebookLM-Ausgabe auf eine Quelle schließen. Erfundene Originalzitate und Bezeichnungen wie `Know_AI_1`, `Use_AI_2` oder `Detect_AI_14` dürfen nicht als Belege erscheinen, wenn sie sich im Original nicht nachweisen lassen.

**MAILS** (Carolus et al. 2023) ist direkt auf der offiziellen Würzburger Seite **auf Deutsch** erhältlich. Die Itemnummern unten sind numerische Positionen im publizierten 34-Item-Instrument; sie sind keine erfundenen Original-Variablennamen. Entsprechend sind für diese deutschsprachigen Ursprungsitems ggf. nur Kontextadaptionen, nicht erfundene Rückübersetzungen, zu kennzeichnen. Keine `source_item_original_text_excerpt`-Felder mit nicht verifizierten englischen Zitaten.

**AIRS-Transfer ausgeschlossen:** AIRS-COM1/Q9 = Verlegenheit bei AI-Problemen **vor anderen**; AIRS-COM2/Q8 = Auffassung zu gesundheitlichen/sicherheitsbezogenen Bedenken; AIRS-COM3/Q18 = Angst vor **humanoiden KI-Technologien / Robotern**. Ein Büro-GenAI-Komfortitem darf aus Q18 nicht als semantisch äquivalentes E2 konstruiert werden. Die ursprüngliche AIRS-Faktorzugehörigkeit allein beweist nicht die Inhaltsäquivalenz nach Kontextwechsel.

**Für den vorgeschlagenen Nachtrag A1** wird der source-bounded Comfort-Faktor aus AISES (Wang & Chuang 2024) benutzt. Für diese Skala: tatsächliche Primärquelle, CF-Faktor- und Q-IDs, Antwortskala 1–7 und semantische Nähe unabhängig verifizieren. Falls die Primärquelle/Items nicht vorliegen, E2 nicht freigeben, sondern `e2_proof_ok=false` und `REVISION_REQUIRED`. Das Belegzitat darf **nicht** aus dem hier enthaltenen semantischen Fingerprint erfunden werden.

**E3** ist ein *selbst entwickeltes* Item mit `source_item_id = null`, `source_item_text_verified = false`, `original_scale = null`. `source_definition_verified = true` **nur** wenn die Originaldefinition die spezifische Fähigkeit tatsächlich trägt. Quelle für generische KI-Erkennung beweist nicht automatisch Faktenprüfung. E3 benötigt eine echte, aktive, konzeptuell passende Primärquelle und transparent benannte inhaltliche Herleitung; andernfalls `e3_registry_closure_ok=false`.

## 5. Bindende Kandidaten-Itemkarte (ausschließlich unter Originalbeweis)

Diese Karte enthält **Entwurfsformulierungen**, keine fiktiv validierten Originalitems. Sie ist die Vergleichsbasis für B2/B5/B7, solange Quelle und A1-Status wie angegeben geprüft werden. Alle Texte exakt gleich in B2/B5/B7 nutzen. Die Herkunftsnachweise werden mit Originalpublikation validiert; niemals blind kopieren.

| item_id | Konstrukt | Quelle | Original-Position/ID | Evidenzkandidat | Skala | Entwurfsformulierung DE |
|---|---|---|---|---|---|---|
| `LIT_01` | `READINESS_CORE_LIT` | `MAILS` | `7` | `E2` | `0-10` | Ich kenne die wichtigsten Grundbegriffe generativer KI. |
| `LIT_02` | `READINESS_CORE_LIT` | `MAILS` | `8` | `E2` | `0-10` | Ich kenne die Bedeutung des Begriffs generative KI. |
| `LIT_03` | `READINESS_CORE_LIT` | `MAILS` | `12` | `E2` | `0-10` | Ich kann mir mögliche zukünftige Anwendungen generativer KI vorstellen. |
| `LEARN_01` | `READINESS_CORE_LEARN` | `AILRSE-5` | `1` | `E2` | `1-7` | Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen funktionieren. |
| `LEARN_02` | `READINESS_CORE_LEARN` | `AILRSE-5` | `2` | `E2` | `1-7` | Ich bin zuversichtlich, dass ich bei Bedarf die Nutzung neuer generativer KI-Anwendungen erlernen kann. |
| `LEARN_03` | `READINESS_CORE_LEARN` | `AILRSE-5` | `5` | `E2` | `1-7` | Ich bin zuversichtlich, dass ich mir die Nutzung neuer generativer KI-Anwendungen selbstständig aneignen kann. |
| `APPLY_01` | `READINESS_CORE_APPLY` | `MAILS` | `1` | `E2` | `0-10` | Ich kann generative KI-Anwendungen bedienen. |
| `APPLY_02` | `READINESS_CORE_APPLY` | `MAILS` | `3` | `E2` | `0-10` | Ich kann generative KI sinnvoll einsetzen, um meine Arbeitsziele zu erreichen. |
| `APPLY_03` | `READINESS_CORE_APPLY` | `MAILS` | `24` | `E2` | `0-10` | Die meisten Probleme im Umgang mit generativer KI kann ich aus eigener Kraft meistern. |
| `DETECT_01` | `READINESS_CORE_DETECT` | `MAILS` | `13` | `E2` | `0-10` | Ich kann erkennen, ob eine Anwendung auf generativer KI basiert. |
| `DETECT_02` | `READINESS_CORE_DETECT` | `MAILS` | `15` | `E2` | `0-10` | Ich kann unterscheiden, ob ich mit einer generativen KI oder einer Person interagiere. |
| `DETECT_03` | `READINESS_CORE_DETECT` | `THEORY` | `NOT_APPLICABLE` | `E3` | `0-10` | Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen. |
| `COMFORT_01` | `READINESS_CORE_COMFORT` | `AISES` | `CF1/Q25` | `E2` | `1-7` | Wenn ich mit generativer KI interagiere, fühle ich mich ruhig. |
| `COMFORT_02` | `READINESS_CORE_COMFORT` | `AISES` | `CF3/Q24` | `E2` | `1-7` | Wenn ich mit generativer KI interagiere, fühle ich mich wohl. |
| `COMFORT_03` | `READINESS_CORE_COMFORT` | `AISES` | `CF5/Q22` | `E2` | `1-7` | Wenn ich mit generativer KI interagiere, fühle ich mich entspannt. |
| `FC_01` | `CONTEXT_FC` | `LAMBIASE` | `FC_1` | `E2` | `1-7` | Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI-Anwendungen zu nutzen. |
| `FC_02` | `CONTEXT_FC` | `LAMBIASE` | `FC_2` | `E2` | `1-7` | Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen zu nutzen. |
| `FC_03` | `CONTEXT_FC` | `LAMBIASE` | `FC_3` | `E2` | `1-7` | Generative KI-Anwendungen sind mit den anderen von mir verwendeten Technologien kompatibel. |

**Quellenkompatibilitätskontrollen:**
- MAILS LIT 7/8/12 aus originaler Knowledge/Understand-AI-Teilskala; Item 12 erfasst vorgestellte künftige Anwendungsmöglichkeiten. Dieses Teilkonstrukt misst kein objektives AI-Wissen und nicht ausschließlich Funktionsverständnis: präzise Konstruktbezeichnung verwenden.
- MAILS APPLY Originalpositionen 1 und 3 = `Use & Apply`; 24 = `AI Problem Solving`. Unterschiedliche veröffentlichte Teilfacetten im projektspezifischen Anwendungskompetenz-Konstrukt transparent deklarieren; keine unveränderte psychometrische Originalskala behaupten.
- MAILS DETECT 13 und 15 messen KI-Anwendungen/Interaktionspartner, nicht KI-generierte Textursprünge oder Faktenprüfung. `DETECT_03` ist E3.
- AISES COMFORT `CF1/Q25`, `CF3/Q24`, `CF5/Q22` liegen zwar in derselben veröffentlichten Comfort-Subskala, bilden aber nur ein 3-von-6-Subset. Psychometrische Kennwerte der ursprünglichen 6er-Subskala **nicht** auf das Subset übertragen. Überlappung von „ruhig“, „wohl“ und „entspannt“ im menschlichen Pretest überprüfen.
- AILRSE-5: nur Items 1/2/5. Inhalt von Item 5 muss bei der Originalpublikation nachweisbar sein; bei Nichtnachweis kein PASS.
- FC: `FC_1`=Ressourcen, `FC_2`=eigenes Wissen (measurement_object HUMAN_CAPABILITY), `FC_3`=Technologiekompatibilität (SYSTEM_PROPERTY), nicht Support. Support `FC_4` bewusst ausgeschlossen.

## 6. Separate Bedarfs- und Demografiemodule

`DIAG_01`: „In welchen Bereichen wünschen Sie sich Weiterbildung oder Unterstützung zu generativer KI?“ Mehrfachauswahl: Grundlagen; Prompting; kritische Ergebnisprüfung; Datenschutz und Umgang mit sensiblen Informationen; Urheberrecht/Ethik; Prozessintegration; konkrete Tool-Anwendung; `Sonstiges: ____`; `Kein Schulungs-/Entwicklungsbedarf` (exklusiv; darf nicht mit anderen gewählt werden).

`DIAG_02`: „Welche zusätzliche Unterstützung würde Ihnen die Nutzung generativer KI bei der Arbeit erleichtern?“ (offenes Feld). Keine nicht belegten Angebote des Unternehmens erfinden.

`DEM_01`: „Welchem kaufmännischen Funktionsbereich ordnen Sie sich überwiegend zu?“ (offenes Feld oder `[FUNKTIONSBEREICHE_DER_ORGANISATION_EINFÜGEN]`; keine fiktiven Abteilungsnamen).

`CONTEXT_TEXT = NOT_PROVIDED`: Teilnehmerinformation/Datenschutz-Platzhalter **exakt** `[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]`. Keine erfundenen Versprechen zu Anonymität, Freiwilligkeit, vertraulichen Auswertungen oder Unternehmensmaßnahmen. Einleitung sachlich und neutral.

## 7. Prüfworkflow ohne Scheinaudit

Vor Ausgabefreigabe:
1. Primärquellen wirklich suchen/lesen. Für jede der 17 E2-Kandidaten einzelne Quelle, Locator, publizierte ID/Position, semantische Äquivalenz, Skaleneignung protokollieren. Nicht verfügbare Itemtexte mit `NOT_VERIFIED` markieren, nie mit erfundenem Wortlaut ersetzen. Für E3 kompatible originale Definition prüfen.
2. Einzelaussage, keine suggestiven Fragen; speziell `DETECT_03` ausschließlich inhaltliche Richtigkeit. Hinterfragen, ob LIT_03 und das Comfort-Subset fachlich angemessen sind.
3. B2/B5/B7 auf 18 identische Item-IDs und wortgleiche Entwurfsformulierungen prüfen.
4. Alle drei FC-Items müssen zusätzliche Antwortoption `Kann ich nicht beurteilen` / `MISSING_NOT_SCORED` haben.
5. Nur heuristische simulierte Pretest-Rückmeldung; keine erfundene Ausfüllzeit oder empirische Stichprobe. `PLANNED_ANALYSIS = NOT_PROVIDED`: kein numerisches Pretest-N, keine festgelegte Schätzmethode, keine frei erfundenen psychometrischen Grenzwerte. Menschlicher Pretest, methodisch begründete Planung und empirische Prüfung sind erforderlich.
6. **Design-Audit-Abweichung explizit ausweisen**: A1 bei Quellenwechsel AIRS → AISES, Skala COMFORT 1–5 → 1–7 und MAILS Itemselektion. Ohne dokumentierte fachliche A1-Freigabe kein `CONFORMANT_GENERATION`.

## 8. Ausgabeformat: ein Durchlauf und genau ein B7-JSON

In **einer einzigen NotebookLM-Antwort** und genau dieser Reihenfolge:

- **B1** Projektwerte, `004_FINAL` plus vorgeschlagener Nachtrag A1 (status offen), Quellenstatus.
- **B2** 18-Zeilen-Traceability mit Itemtext, Konstrukten, Quelle/Original-Position, überprüfbarem Locator, Evidenz E2/E3, Originalskala, angepasster Skala, Übersetzungs-/Transferstatus; plus DIAG/DEM separat.
- **B3** Kritische Quellen-/Konstruktevaluation und spezifische Risiken statt pauschalem „alle Items PASS“.
- **B4** Simulierter kognitiver Durchgang (klar als Simulation deklariert, niemals Human-Pretest).
- **B5** Vollständiger lesbarer Teilnehmerfragebogen mit Filter, 18 Items, Skalen, FC-Option, DIAG und DEM.
- **B6** Nichtnumerischer Plan für kognitiven Human-Pretest und spätere empirische Validierung, keine fixe Fallzahl/Schätzmethode.
- **B7** **Ein vollständiger valider JSON-Codeblock**. Datenmodell: `{ "metadata": {...}, "conformance": {...}, "constructs": [...], "routing": {...}, "diagnostic_needs": {...}, "demographics_minimal": {...}, "items": [18 echte, vollständige reflektive Items] }`. Für jedes Item mindestens `item_id`, `construct_code`, `question_text`, `evidence_class`, `measurement_object`, `source_evidence` (mit realer Quelle und Locator; bei E3 `source_item_id:null`), `original_scale`, `final_scale`, `translation_status`, `critic_status`. Für FC zusätzlich `additional_response_option` und `additional_response_option_coding`.
- **B0** erst **nach B7**: nachprüfbare Hard-Check-Matrix. `json_consistency_ok` nur wahr bei tatsächlich 18 Item-Objekten im JSON und wortgleichen B2/B5/B7-Items. `e2_proof_ok` und `design_amendment_ok` müssen unabhängig geprüft werden.

**Statuslogik:** Wenn Item-Provenienz, E3 oder A1-Freigabe fehlen, Ausgabe dennoch als klar gekennzeichneter **Forschungsentwurf**, aber `REVISION_REQUIRED` mit Fehlern und Handlungsempfehlung. Niemals behaupten, das vom Modell ausgegebene JSON sei technisch extern geparst oder es hätte einen echten Human-Pretest gegeben. Wenn Ausgabe zu lang ist: `REVISION_REQUIRED – OUTPUT_TRUNCATED`, statt `CONFORMANT_GENERATION`.

Die einzige Nutzereingabe bleibt: `Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.`
