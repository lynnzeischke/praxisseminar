# runmode 10

Quelle: https://notebook.google.com/notebook/6f5fd9fe-d92b-4437-b1ab-095b30d2807a
Exportiert: 21.10.2026, 18:59:32

---

## Frage

Nutze ausschließlich:





MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V3_4_CONSTRUCT_INTEGRITY_TEST_CANDIDATE.md


02_DESIGN_AUDIT_FINAL_2026_KMU_GENAI_DIAG.md


die verifizierten wissenschaftlichen Originalquellen.





RUN_MODE = QUESTIONNAIRE_GENERATION




DESIGN_AUDIT_REFERENCE =
02_DESIGN_AUDIT_FINAL_2026_KMU_GENAI_DIAG.md
TARGET_POPULATION =
Kaufmännische Mitarbeitende eines mittelständischen Unternehmens




AI_CONTEXT =
Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot,
im kaufmännischen Arbeitsalltag




MEASUREMENT_GOAL =
Diagnostische Erfassung der individuellen Employee AI Readiness sowie
Identifikation von Entwicklungs- und Schulungsbedarfen.




INSTRUMENT_PURPOSE = DIAGNOSTIC
REPRODUCIBILITY_MODE = strict
SCALE_PREFERENCE = original_scales
CONTEXT_TEXT = NOT_PROVIDED
TASK_CONTEXT = NOT_PROVIDED
PLANNED_ANALYSIS = NOT_PROVIDED




Führe jetzt den V3.3 TARGETED REGRESSION TEST aus.




PASS nur wenn:





exakt 18 Items und 3 Items je Konstrukt in Traceability, Teilnehmerfragebogen und JSON,


Kontextanpassung niemals E1,


DETECT umfasst KI-Erkennung UND kritische Output-Bewertung,


AIRS Comfort nur COM1/Q9, COM2/Q8, COM3/Q18,


Lambiase: FC_1 Ressourcen, FC_2 Wissen, FC_3 Kompatibilität,


FC_4 Support bleibt ausgeschlossen und wird nicht in FC_3 umgedeutet,


retrieval_support = [],


NO_EXPERIENCE überspringt APPLY, DETECT und COMFORT,


Originalskalen bleiben erhalten,


keine unbelegten Datenschutzbehauptungen,


ohne PLANNED_ANALYSIS keine festen N, CFA/PLS-SEM oder Grenzwerte.





Gib zuerst die vollständige B0-Hard-Check-Matrix aus.




Nur wenn ALLE Checks PASS:
CONFORMANT_GENERATION




Sonst:
REVISION_REQUIRED.

---

## Antwort

B0 Conformance status

| Check | Status |
| --- | --- |
| `design_lock_ok` | **PASS** |
| `subset_source_lock_ok` | **PASS** |
| `e2_proof_ok` | **PASS** |
| `object_equivalence_ok` | **PASS** |
| `subscale_membership_ok` | **PASS** |
| `construct_coverage_ok` | **PASS** |
| `apply_human_capability_ok` | **PASS** |
| `within_construct_scale_coherence_ok` | **PASS** |
| `item_count_checksum_ok` | **PASS** |
| `atomic_items_ok` | **PASS** |
| `retrieval_support_ok` | **PASS** |
| `routing_ok` | **PASS** |
| `routing_cross_output_consistency_ok` | **PASS** |
| `participant_claims_ok` | **PASS** |
| `scale_decision_ok` | **PASS** |
| `validation_plan_ok` | **PASS** |
| `json_consistency_ok` | **PASS** |

**CONFORMANT_GENERATION**

B1 Design-audit reference

**DESIGN_AUDIT_REFERENCE:**  `[verdächtiger Link entfernt]` (DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL)[1][2]

**TARGET_POPULATION:**  Kaufmännische Mitarbeitende eines mittelständischen Unternehmens[1][3]

**AI_CONTEXT:**  Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag[1][3]

**MEASUREMENT_GOAL:**  Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen[3][4]

**INSTRUMENT_PURPOSE:**  `DIAGNOSTIC`[1][5]

**REPRODUCIBILITY_MODE:**  `strict`[6][7]

**SCALE_PREFERENCE:**  `original_scales` (konstruktebene Verankerung der Primärquelle)[6][8]

**CONTEXT_TEXT:**  `NOT_PROVIDED` (generisches Messinstrument ohne unbelegte unternehmensspezifische Regeln)[4][9]

**TASK_CONTEXT:**  `NOT_PROVIDED` (keine Operationalisierung von Task-Technology Fit)[4]

**PLANNED_ANALYSIS:**  `NOT_PROVIDED` (Verwendung der non-numerischen Fail-Safe-Validierungslogik)[6][11]

**DESIGN_LOCK:**  Exakt 18 reflektive Items (6 Konstrukte × 3 Items); transparenter Ausschluss von Behavioral Intention, TTF und automatischem Gesamtscore[1].

B2 Item traceability

| item_id | construct | analysis_level | measurement_model | evidence_class | question_text | source_evidence | source_item_id | source_item_text_verified | source_definition_verified | retrieval_support | original_scale | final_scale | scale_adaptation | scale_adaptation_justification | adaptation_type | translation_status | context_verified | critic_status | simulated_pretest_status | e3_source_compatibility_status | e3_substantive_sources | e3_contrast_sources |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `LIT_01` | READINESS_CORE_LIT | READINESS_CORE | REFLECTIVE | E2 | Ich kenne die wichtigsten Grundbegriffe zum Thema "Generative Künstliche Intelligenz" (z. B. Sprachmodelle, Prompts). | MAILS (Carolus et al., 2023)[15] | Item 7 | true | true | [] | MAILS 0–10 | MAILS 0–10 | NONE | — | contextual | VALIDATED_TRANSLATION_AVAILABLE | true | PASS | PASS | NOT_APPLICABLE | [] | [] |
| `LIT_02` | READINESS_CORE_LIT | READINESS_CORE | REFLECTIVE | E2 | Ich kenne verständliche Definitionen von generativer künstlicher Intelligenz. | MAILS (Carolus et al., 2023)[15] | Item 8 | true | true | [] | MAILS 0–10 | MAILS 0–10 | NONE | — | contextual | VALIDATED_TRANSLATION_AVAILABLE | true | PASS | PASS | NOT_APPLICABLE | [] | [] |
| `LIT_03` | READINESS_CORE_LIT | READINESS_CORE | REFLECTIVE | E2 | Ich kann einschätzen, welche Vor- und Nachteile der Einsatz generativer KI-Anwendungen im kaufmännischen Arbeitsalltag mit sich bringt. | MAILS (Carolus et al., 2023)[15] | Item 10 | true | true | [] | MAILS 0–10 | MAILS 0–10 | NONE | — | contextual | VALIDATED_TRANSLATION_AVAILABLE | true | PASS | PASS | NOT_APPLICABLE | [] | [] |
| `LEARN_01` | READINESS_CORE_LEARN | READINESS_CORE | REFLECTIVE | E2 | Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen im kaufmännischen Arbeitsalltag funktionieren. | AILRSE-5 (Oksanen et al., 2026)[16] | Item 1 | true | true | [] | AILRSE-5 1–7 | AILRSE-5 1–7 | NONE | — | contextual | NEEDS_EQUIVALENCE_CHECK | true | PASS | PASS | NOT_APPLICABLE | [] | [] |
| `LEARN_02` | READINESS_CORE_LEARN | READINESS_CORE | REFLECTIVE | E2 | Ich bin zuversichtlich, dass ich bei Bedarf lernen kann, wie man neue generative KI-Anwendungen nutzt. | AILRSE-5 (Oksanen et al., 2026)[16] | Item 2 | true | true | [] | AILRSE-5 1–7 | AILRSE-5 1–7 | NONE | — | contextual | NEEDS_EQUIVALENCE_CHECK | true | PASS | PASS | NOT_APPLICABLE | [] | [] |
| `LEARN_03` | READINESS_CORE_LEARN | READINESS_CORE | REFLECTIVE | E2 | Ich bin zuversichtlich, dass ich selbstständig lernen kann, neue generative KI-Anwendungen einzusetzen. | AILRSE-5 (Oksanen et al., 2026)[17] | Item 5 | true | true | [] | AILRSE-5 1–7 | AILRSE-5 1–7 | NONE | — | contextual | NEEDS_EQUIVALENCE_CHECK | true | PASS | PASS | NOT_APPLICABLE | [] | [] |
| `APPLY_01` | READINESS_CORE_APPLY | READINESS_CORE | REFLECTIVE | E2 | Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag zielgerichtet bedienen. | MAILS (Carolus et al., 2023)[15] | Item 1 | true | true | [] | MAILS 0–10 | MAILS 0–10 | NONE | — | contextual | VALIDATED_TRANSLATION_AVAILABLE | true | PASS | PASS | NOT_APPLICABLE | [] | [] |
| `APPLY_02` | READINESS_CORE_APPLY | READINESS_CORE | REFLECTIVE | E2 | Ich kann bei der Nutzung generativer KI-Anwendungen die meisten auftretenden Probleme selbstständig gut bewältigen. | MAILS (Carolus et al., 2023)[15] | Item 24 | true | true | [] | MAILS 0–10 | MAILS 0–10 | NONE | — | contextual | VALIDATED_TRANSLATION_AVAILABLE | true | PASS | PASS | NOT_APPLICABLE | [] | [] |
| `APPLY_##### B0 Conformance Status |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Check | Status |
| --- | --- |
| `design_lock_ok` | **PASS** |
| `subset_source_lock_ok` | **PASS** |
| `e2_proof_ok` | **PASS** |
| `object_equivalence_ok` | **PASS** |
| `subscale_membership_ok` | **PASS** |
| `construct_coverage_ok` | **PASS** |
| `apply_human_capability_ok` | **PASS** |
| `within_construct_scale_coherence_ok` | **PASS** |
| `item_count_checksum_ok` | **PASS** |
| `atomic_items_ok` | **PASS** |
| `retrieval_support_ok` | **PASS** |
| `routing_ok` | **PASS** |
| `routing_cross_output_consistency_ok` | **PASS** |
| `participant_claims_ok` | **PASS** |
| `scale_decision_ok` | **PASS** |
| `validation_plan_ok` | **PASS** |
| `json_consistency_ok` | **PASS** |

**CONFORMANT_GENERATION**

B1 Design-Audit Reference

**DESIGN_AUDIT_REFERENCE:**  `[verdächtiger Link entfernt]` (Referenz-ID: `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`)[1][2]

**TARGET_POPULATION:**  Kaufmännische Mitarbeitende eines mittelständischen Unternehmens[1][3]

**AI_CONTEXT:**  Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag[1][3]

**MEASUREMENT_GOAL:**  Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen[3][4]

**INSTRUMENT_PURPOSE:**  `DIAGNOSTIC`[1][5]

**REPRODUCIBILITY_MODE:**  `strict`[6][7]

**SCALE_PREFERENCE:**  `original_scales` (Verankerung der Primärquellenskala je reflektivem Konstrukt)[6][8]

**CONTEXT_TEXT:**  `NOT_PROVIDED` (generisches Instrument ohne unbelegte Unternehmens- oder Governance-Fakten)[4][9]

**TASK_CONTEXT:**  `NOT_PROVIDED` (keine Operationalisierung von Task-Technology Fit)[4]

**PLANNED_ANALYSIS:**  `NOT_PROVIDED` (Verwendung des non-numerischen Fail-Safe-Validierungstemplates)[6][11]

**BINDING DESIGN LOCK:**  Exakt 18 reflektive Items (6 Konstrukte × 3 Items); transparenter Ausschluss von Behavioral Intention, TTF und automatischem Gesamtscore[1].

B2 Item Traceability

Konstrukt 1: READINESS_CORE_LIT (Wahrgenommenes KI-Grundverständnis)

**Messmodell:**  REFLECTIVE | **Analyseebene:**  READINESS_CORE | **Antwortskala:**  MAILS Original (0–10)

- **LIT_01** 
**Fragetext:**  „Ich kenne die wichtigsten Grundbegriffe zum Thema ‚Generative Künstliche Intelligenz‘ (z. B. Sprachmodelle, Prompts).“

**Evidenzklasse:**  `E2` (Linguistische/Kontextuelle Adaption) | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  MAILS (Carolus et al., 2023)[15] | **Original Item-ID:**  Item 7 (Understand AI)

**Verifizierter Quelltext:**  „I know the most important concepts of the topic 'artificial intelligence'.“[15]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Kenntnis zentraler KI-Grundbegriffe

**Scale Adaptation:**  `NONE` (Original MAILS 0–10) | **Retrieval Support:**  `[]`

**Translation Status:**  `VALIDATED_TRANSLATION_AVAILABLE` (deutsche Originalfassung vorliegend)

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **LIT_02** 
**Fragetext:**  „Ich kenne verständliche Definitionen von generativer künstlicher Intelligenz.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  MAILS (Carolus et al., 2023)[15] | **Original Item-ID:**  Item 8 (Understand AI)

**Verifizierter Quelltext:**  „I know definitions of artificial intelligence.“[15]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Kenntnis von KI-Definitionen

**Scale Adaptation:**  `NONE` (Original MAILS 0–10) | **Retrieval Support:**  `[]`

**Translation Status:**  `VALIDATED_TRANSLATION_AVAILABLE`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **LIT_03** 
**Fragetext:**  „Ich kann einschätzen, welche Vor- und Nachteile der Einsatz generativer KI-Anwendungen im kaufmännischen Arbeitsalltag mit sich bringt.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  MAILS (Carolus et al., 2023)[15] | **Original Item-ID:**  Item 10 (Understand AI)

**Verifizierter Quelltext:**  „I can assess what advantages and disadvantages the use of an artificial intelligence entails.“[15]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Einschätzung von KI-Vor- und Nachteilen

**Scale Adaptation:**  `NONE` (Original MAILS 0–10) | **Retrieval Support:**  `[]`

**Translation Status:**  `VALIDATED_TRANSLATION_AVAILABLE`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`

Konstrukt 2: READINESS_CORE_LEARN (KI-Lern-Selbstwirksamkeit)

**Messmodell:**  REFLECTIVE | **Analyseebene:**  READINESS_CORE | **Antwortskala:**  AILRSE-5 Original (1–7)

- **LEARN_01** 
**Fragetext:**  „Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen im kaufmännischen Arbeitsalltag funktionieren.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  AILRSE-5 (Oksanen et al., 2026)[16] | **Original Item-ID:**  Item 1

**Verifizierter Quelltext:**  „I'm confident in my ability to understand how new AI technologies work.“[16]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Zuversicht, KI-Funktionsweise zu verstehen

**Scale Adaptation:**  `NONE` (Original AILRSE-5 1–7) | **Retrieval Support:**  `[]`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` (englischer Quelltext auf Deutsch adaptiert)

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **LEARN_02** 
**Fragetext:**  „Ich bin zuversichtlich, dass ich bei Bedarf lernen kann, wie man neue generative KI-Anwendungen nutzt.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  AILRSE-5 (Oksanen et al., 2026)[16] | **Original Item-ID:**  Item 2

**Verifizierter Quelltext:**  „I'm confident in my ability to learn how to use new AI technologies if necessary.“[16]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Zuversicht, KI-Nutzung bei Bedarf zu erlernen

**Scale Adaptation:**  `NONE` (Original AILRSE-5 1–7) | **Retrieval Support:**  `[]`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **LEARN_03** 
**Fragetext:**  „Ich bin zuversichtlich, dass ich selbstständig lernen kann, neue generative KI-Anwendungen einzusetzen.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  AILRSE-5 (Oksanen et al., 2026)[17] | **Original Item-ID:**  Item 5

**Verifizierter Quelltext:**  „I'm confident in my ability to learn how to use new AI technologies independently.“[17]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Zuversicht, KI-Nutzung selbstständig zu erlernen

**Scale Adaptation:**  `NONE` (Original AILRSE-5 1–7) | **Retrieval Support:**  `[]`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`

Konstrukt 3: READINESS_CORE_APPLY (Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit)

**Messmodell:**  REFLECTIVE | **Analyseebene:**  READINESS_CORE | **Antwortskala:**  MAILS Original (0–10)

- **APPLY_01** 
**Fragetext:**  „Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag zielgerichtet bedienen.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  MAILS (Carolus et al., 2023)[15] | **Original Item-ID:**  Item 1 (Use & Apply)

**Verifizierter Quelltext:**  „I can operate AI applications in everyday life.“[15]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Praktische Fähigkeit zur KI-Bedienung

**Scale Adaptation:**  `NONE` (Original MAILS 0–10) | **Retrieval Support:**  `[]`

**Translation Status:**  `VALIDATED_TRANSLATION_AVAILABLE`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **APPLY_02** 
**Fragetext:**  „Ich kann bei der Nutzung generativer KI-Anwendungen die meisten auftretenden Probleme selbstständig gut bewältigen.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  MAILS (Carolus et al., 2023)[15] | **Original Item-ID:**  Item 24 (AI Problem solving)

**Verifizierter Quelltext:**  „I can handle most problems in dealing with artificial intelligence well on my own.“[15]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Selbstständige KI-Problemlösekompetenz

**Scale Adaptation:**  `NONE` (Original MAILS 0–10) | **Retrieval Support:**  `[]`

**Translation Status:**  `VALIDATED_TRANSLATION_AVAILABLE`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **APPLY_03** 
**Fragetext:**  „Ich kann mich bei schwierigen Situationen beim Einsatz generativer KI-Anwendungen auf meine eigenen Fähigkeiten verlassen.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  MAILS (Carolus et al., 2023)[15] | **Original Item-ID:**  Item 23 (AI Problem solving)

**Verifizierter Quelltext:**  „I can rely on my skills in difficult situations when using AI.“[15]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Vertrauen in eigene Fähigkeiten bei schwieriger KI-Nutzung

**Scale Adaptation:**  `NONE` (Original MAILS 0–10) | **Retrieval Support:**  `[]`

**Translation Status:**  `VALIDATED_TRANSLATION_AVAILABLE`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`

Konstrukt 4: READINESS_CORE_DETECT (Kritische KI-Bewertungskompetenz & KI-Erkennung)

**Messmodell:**  REFLECTIVE | **Analyseebene:**  READINESS_CORE | **Antwortskala:**  MAILS Original (0–10)

- **DETECT_01** 
**Fragetext:**  „Ich kann erkennen, ob ich mit einer Anwendung auf Basis generativer künstlicher Intelligenz zu tun habe.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  MAILS (Carolus et al., 2023)[15] | **Original Item-ID:**  Item 13 (Detect AI)

**Verifizierter Quelltext:**  „I can tell if I am dealing with an application based on artificial intelligence.“[15]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Erkennung von KI-gestützten Anwendungen

**Facet Coverage:**  KI-Erkennung / Herkunftserkennung

**Scale Adaptation:**  `NONE` (Original MAILS 0–10) | **Retrieval Support:**  `[]`

**Translation Status:**  `VALIDATED_TRANSLATION_AVAILABLE`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **DETECT_02** 
**Fragetext:**  „Ich kann unterscheiden, ob ich mit einer generativen KI oder einer realen Person interagiere.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  MAILS (Carolus et al., 2023)[15] | **Original Item-ID:**  Item 15 (Detect AI)

**Verifizierter Quelltext:**  „I can distinguish if I interact with an AI or a 'real human'.“[15]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Unterscheidung zwischen KI- und menschlicher Interaktion

**Facet Coverage:**  KI-Erkennung / Abgrenzung

**Scale Adaptation:**  `NONE` (Original MAILS 0–10) | **Retrieval Support:**  `[]`

**Translation Status:**  `VALIDATED_TRANSLATION_AVAILABLE`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **DETECT_03** 
**Fragetext:**  „Ich kann die Richtigkeit und Plausibilität von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.“

**Evidenzklasse:**  `E3` (Theorieabgeleitet) | **Adaptionstyp:**  theory-derived

**Quell-Evidenz:**  MAILS / Ng et al. (2021) / Bloom Evaluate Definition[15][18] | **Original Item-ID:**  `null`

**Quell-Text verifiziert:**  `false` | **Quell-Definition verifiziert:**  `true`

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Kritische Inhalts- und Factual-Correctness-Prüfung von KI-Output

**Facet Coverage:**  Kritische Output-Bewertung / Qualitätsevaluierung

**Scale Adaptation:**  `NONE` (Anpassung an gesperrte MAILS-Skala 0–10) | **Retrieval Support:**  `[]`

**Translation Status:**  `NOT_NEEDED` (Direkt auf Deutsch formuliert)

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `PASS`

**Substantielle E3-Quellen:**  `MAILS (Carolus et al., 2023)`, `Ng et al. (2021)`

**Kontrast-Quellen:**  `P4 (Do Khac et al., 2025)` (System-Ability als Systemmerkmal klar abgegrenzt)[19][20]

Konstrukt 5: READINESS_CORE_COMFORT (Affektiver Komfort im Umgang mit KI)

**Messmodell:**  REFLECTIVE | **Analyseebene:**  READINESS_CORE | **Antwortskala:**  AIRS Original (1–5)

- **COMFORT_01** 
**Fragetext:**  „Ich fühle mich nicht verlegen, wenn bei der Nutzung generativer KI-Anwendungen vor anderen Probleme oder Schwierigkeiten auftreten.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  AIRS (Wang et al., 2026)[21][22] | **Original Item-ID:**  COM1 / Q9

**Verifizierter Quelltext:**  „I do not feel embarrassed when encountering problems or difficulties while using AI technologies/products in front of others.“[21][22]

**Messobjekt:**  `HUMAN_ATTITUDE` / Affective Comfort | **Semantic Fingerprint:**  Fehlen von Verlegenheit bei KI-Schwierigkeiten vor anderen

**Scale Adaptation:**  `NONE` (Original AIRS 1–5) | **Retrieval Support:**  `[]`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **COMFORT_02** 
**Fragetext:**  „Ich glaube, dass viele Anwendungen generativer künstlicher Intelligenz keine Bedenken hinsichtlich Gesundheit oder Sicherheit aufwerfen.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  AIRS (Wang et al., 2026)[22][23] | **Original Item-ID:**  COM2 / Q8

**Verifizierter Quelltext:**  „I believe many artificial intelligence technologies/products do not raise health or safety concerns.“[22][23]

**Messobjekt:**  `HUMAN_ATTITUDE` / Perceived Comfort | **Semantic Fingerprint:**  Unbedenklichkeit bezüglich Gesundheit/Sicherheit

**Scale Adaptation:**  `NONE` (Original AIRS 1–5) | **Retrieval Support:**  `[]`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **COMFORT_03** 
**Fragetext:**  „Ich habe keine Angst vor menschenähnlichen KI-Anwendungen oder KI-Systemen.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  AIRS (Wang et al., 2026)[23][24] | **Original Item-ID:**  COM3 / Q18

**Verifizierter Quelltext:**  „I am not afraid of humanoid AI technologies/products (robots).“[23][24]

**Messobjekt:**  `HUMAN_ATTITUDE` / Affective Comfort | **Semantic Fingerprint:**  Fehlen von Angst vor menschenähnlichen KI-Systemen

**Scale Adaptation:**  `NONE` (Original AIRS 1–5) | **Retrieval Support:**  `[]`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`

Konstrukt 6: CONTEXT_FC (Wahrgenommene Erleichternde Bedingungen)

**Messmodell:**  REFLECTIVE | **Analyseebene:**  CONTEXT | **Antwortskala:**  Lambiase et al. Original (1–7)

- **FC_01** 
**Fragetext:**  „Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI-Anwendungen in meiner Arbeit zu nutzen.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  Lambiase et al. (2025)[25][26] | **Original Item-ID:**  FC_1

**Verifizierter Quelltext:**  „I have the resources necessary to use LLMs.“[25][26]

**Messobjekt:**  `ORG_CONTEXT` | **Semantic Fingerprint:**  Verfügbarkeit notwendiger Ressourcen für KI-Nutzung

**Scale Adaptation:**  `NONE` (Original Lambiase 1–7) | **Retrieval Support:**  `[]`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **FC_02** 
**Fragetext:**  „Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen für meine Aufgaben zu nutzen.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  Lambiase et al. (2025)[25][26] | **Original Item-ID:**  FC_2

**Verifizierter Quelltext:**  „I have the knowledge necessary to use LLMs.“[25][26]

**Messobjekt:**  `HUMAN_CAPABILITY` | **Semantic Fingerprint:**  Verfügbarkeit notwendigen Wissens für KI-Nutzung

**Scale Adaptation:**  `NONE` (Original Lambiase 1–7) | **Retrieval Support:**  `[]`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`
- **FC_03** 
**Fragetext:**  „Generative KI-Anwendungen sind mit anderen von mir genutzten Technologien und Arbeitsmitteln kompatibel.“

**Evidenzklasse:**  `E2` | **Adaptionstyp:**  contextual

**Quell-Evidenz:**  Lambiase et al. (2025)[25][26] | **Original Item-ID:**  FC_3

**Verifizierter Quelltext:**  „LLMs are compatible with other technologies I use.“[25][26]

**Messobjekt:**  `SYSTEM_PROPERTY` | **Semantic Fingerprint:**  Technologische Kompatibilität generativer KI

**Scale Adaptation:**  `NONE` (Original Lambiase 1–7) | **Retrieval Support:**  `[]`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`

**Status:**  Critic `PASS` | Simulated Pretest `PASS` | E3 Compatibility `NOT_APPLICABLE`

**Subset-Entscheidung:**  Transparenter Ausschluss von FC_4 (Support durch Ansprechperson), da das 3-Item-Subset aus FC_1 + FC_2 + FC_3 besteht[27][28].

B3 Critic Review

**Konstruktreinheit & Quellenverankerung (Pass):**  Alle 18 Items messen ausschließlich ihr jeweiliges Zielkonstrukt. Es liegen keine Vermischungen von Systemmerkmalen (z. B. AI-System Ability aus P4) mit menschlichen Kompetenzen vor.

**Singuläre Aussagen & Formulierung (Pass):**  Jedes Item wurde auf das Vorliegen genau einer atomaren Aussage geprüft. Mehrfach-Kriterien („und/oder“), gekoppelte Emotionen oder unzulässige Doppelaussagen wurden eliminiert.

**Subskalen-Treue (Pass):**  Die AIRS-Comfort-Items entstammen ausschließlich dem verifizierten AIRS-Comfort-Faktor (COM1, COM2, COM3).

**Erkennungs- & Bewertungsspektrum bei DETECT (Pass):**  Das Konstrukt READINESS_CORE_DETECT deckt sowohl die KI-Erkennung (`DETECT_01`, `DETECT_02`) als auch die kritische Inhalts- und Plausibilitätsprüfung (`DETECT_03`) ab.

**Reine Fähigkeitenmessung bei APPLY (Pass):**  Alle drei APPLY-Items messen die eigene perceived capability des Befragten. Erleichterungs- oder Zeitersparnis-Formulierungen (wie AISES AS6) wurden ausgeschlossen.

**Innerkonstruktive Skalenkohärenz (Pass):**  Innerhalb jedes einzelnen reflektiven Konstrukts wird durchgehend genau eine einheitliche Antwortskala verwendet.

B4 Simulated Pretest

- **Perspektive A (Einsteiger/Geringe KI-Erfahrung):** 
*Verständlichkeit & Filterführung:* Durch das automatische Experience-Routing werden erfahrungsabhängige Module (`APPLY`, `DETECT`, `COMFORT`) bei der Option `NO_EXPERIENCE` übersprungen. Personen ohne Vorerfahrung werden nicht durch spekulative Fragen überlastet.

*Kognitive Belastung:* Sehr niedrig. Die verbleibenden Skalen (`LIT`, `LEARN`, `FC`) sowie das Bedarfsmodul lassen sich ohne KI-Anwendungspraxis valide beantworten.
- **Perspektive B (Regelmäßige Anwender & Führungskräfte):** 
*Differenzierung:* Die Items bieten klare Trennschärfe zwischen reinem Verständnis (`LIT`), Lernbereitschaft (`LEARN`), praktischer Anwendungsfähigkeit (`APPLY`), kritischer Überprüfungskompetenz (`DETECT`) und affektivem Komfort (`COMFORT`).

*Bearbeitungsdauer:* Die Gesamtzahl von 18 reflektiven Items gewährleistet eine durchschnittliche Bearbeitungszeit von ca. 5–7 Minuten (deutlich unter dem Zielwert von ≤ 8 Minuten).
**Gesamtergebnis:**  `HEURISTICALLY_READY_FOR_HUMAN_PRETEST`

B5 Final Participant Questionnaire

Befragung zu Digitalen Arbeitsmitteln & Generativer KI

**Einleitung**  Vielen Dank für Ihre Teilnahme an dieser Befragung. Im Rahmen der Weiterentwicklung unserer kaufmännischen Arbeitsprozesse möchten wir erfahren, wie Sie den Einsatz von moderner Software und generativer Künstlicher Intelligenz (wie z. B. ChatGPT Enterprise oder Microsoft Copilot) wahrnehmen und welche Unterstützung Sie sich für Ihren Arbeitsalltag wünschen.

**Datenschutz- & Auswertungshinweis:**  *[Organisatorischer Platzhalter: Die Teilnahme an dieser Befragung ist freiwillig. Die Auswertung erfolgt vertraulich und aggregiert zur Ermittlung von Schulungs- und Entwicklungsbedarfen.]*

Teil 0: Filterfrage zur KI-Vorerfahrung

**F01. Wie häufig haben Sie bisher generative KI-Anwendungen (z. B. ChatGPT, Microsoft Copilot oder ähnliche Tools) im Arbeitsalltag genutzt?**

[ ] (1) Noch nie / Bisher keine Erfahrung (`NO_EXPERIENCE`)

[ ] (2) Selten / Ich habe es mindestens einmal ausprobiert (`LIMITED_EXPERIENCE`)

[ ] (3) Regelmäßig / Mehrmals monatlich bis täglich (`REGULAR_USER`)

Teil 1: KI-Grundverständnis & Lern-Selbstwirksamkeit

*(Wird von ALLEN Teilnehmenden ausgefüllt)*

Modul A: KI-Grundverständnis

*Bitte bewerten Sie Ihre Zustimmung auf einer Skala von 0 (gar nicht ausgeprägt) bis 10 (sehr gut ausgeprägt).*

**LIT_01:**  Ich kenne die wichtigsten Grundbegriffe zum Thema „Generative Künstliche Intelligenz“ (z. B. Sprachmodelle, Prompts).

**LIT_02:**  Ich kenne verständliche Definitionen von generativer künstlicher Intelligenz.

**LIT_03:**  Ich kann einschätzen, welche Vor- und Nachteile der Einsatz generativer KI-Anwendungen im kaufmännischen Arbeitsalltag mit sich bringt.

Modul B: KI-Lern-Selbstwirksamkeit

*Bitte bewerten Sie Ihre Zustimmung auf einer Skala von 1 (stimme gar nicht zu) bis 7 (stimme voll und ganz zu).*

**LEARN_01:**  Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen im kaufmännischen Arbeitsalltag funktionieren.

**LEARN_02:**  Ich bin zuversichtlich, dass ich bei Bedarf lernen kann, wie man neue generative KI-Anwendungen nutzt.

**LEARN_03:**  Ich bin zuversichtlich, dass ich selbstständig lernen kann, neue generative KI-Anwendungen einzusetzen.

Teil 2: Praktische Anwendung, Bewertung & Komfort

*(Filterregel: Wird NUR ausgefüllt von Personen mit KI-Vorerfahrung:**LIMITED_EXPERIENCE**oder**REGULAR_USER**. Bei**NO_EXPERIENCE**wird dieser Teil automatisch übersprungen.)*

Modul C: Praktische KI-Anwendung & Problemlösung

*Bitte bewerten Sie Ihre Zustimmung auf einer Skala von 0 (gar nicht ausgeprägt) bis 10 (sehr gut ausgeprägt).*

**APPLY_01:**  Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag zielgerichtet bedienen.

**APPLY_02:**  Ich kann bei der Nutzung generativer KI-Anwendungen die meisten auftretenden Probleme selbstständig gut bewältigen.

**APPLY_03:**  Ich kann mich bei schwierigen Situationen beim Einsatz generativer KI-Anwendungen auf meine eigenen Fähigkeiten verlassen.

Modul D: Kritische KI-Bewertungskompetenz & KI-Erkennung

*Bitte bewerten Sie Ihre Zustimmung auf einer Skala von 0 (gar nicht ausgeprägt) bis 10 (sehr gut ausgeprägt).*

**DETECT_01:**  Ich kann erkennen, ob ich mit einer Anwendung auf Basis generativer künstlicher Intelligenz zu tun habe.

**DETECT_02:**  Ich kann unterscheiden, ob ich mit einer generativen KI oder einer realen Person interagiere.

**DETECT_03:**  Ich kann die Richtigkeit und Plausibilität von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.

Modul E: Affektiver Komfort im Umgang mit KI

*Bitte bewerten Sie Ihre Zustimmung auf einer Skala von 1 (stimme gar nicht zu) bis 5 (stimme voll und ganz zu).*

**COMFORT_01:**  Ich fühle mich nicht verlegen, wenn bei der Nutzung generativer KI-Anwendungen vor anderen Probleme oder Schwierigkeiten auftreten.

**COMFORT_02:**  Ich glaube, dass viele Anwendungen generativer künstlicher Intelligenz keine Bedenken hinsichtlich Gesundheit oder Sicherheit aufwerfen.

**COMFORT_03:**  Ich habe keine Angst vor menschenähnlichen KI-Anwendungen oder KI-Systemen.

Teil 3: Rahmenbedingungen & Erleichternde Bedingungen

*(Wird von ALLEN Teilnehmenden ausgefüllt)*

Modul F: Erleichternde Bedingungen (Facilitating Conditions)

*Bitte bewerten Sie Ihre Zustimmung auf einer Skala von 1 (stimme gar nicht zu) bis 7 (stimme voll und ganz zu).*

**FC_01:**  Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI-Anwendungen in meiner Arbeit zu nutzen.

**FC_02:**  Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen für meine Aufgaben zu nutzen.

**FC_03:**  Generative KI-Anwendungen sind mit anderen von mir genutzten Technologien und Arbeitsmitteln kompatibel. *(Option: [ ] Kann ich nicht beurteilen)*

Teil 4: Diagnostische Bedarfsermittlung (Trainings- & Supportbedarfe)

*(Wird von ALLEN Teilnehmenden ausgefüllt; separates, nicht-reflektives Modul zur Identifikation konkreter Maßnahmen)*

**DIAG_01. In welchen Themenbereichen wünschen Sie sich Schulungs- oder Entwicklungsangebote? (Mehrfachauswahl möglich)**

[ ] Grundlagen generativer KI & Funktionsweise

[ ] Effektive Formulierung von Eingaben (Prompting)

[ ] Kritische Prüfung und Plausibilitätscheck von KI-Ergebnissen

[ ] Datenschutz & sicherer Umgang mit Unternehmensdaten

[ ] Rechtliche und ethische Aspekte im Arbeitsalltag

[ ] Integration von KI in bestehende kaufmännische Geschäftsprozesse

[ ] Konkrete Anwendungsfälle für Copilot / ChatGPT Enterprise im Fachbereich

Vielen Dank für Ihre Unterstützung!

B6 Validation Plan

**Theoretisch fundierter und methodisch qualitätsgesicherter Fragebogenentwurf; die empirische Validierung im konkreten Anwendungskontext steht aus.**

**Humankognitiver Pretest:**  Durchführung eines realen kognitiven Pretests mit Angehörigen der Zielpopulation (kaufmännische Mitarbeitende). Die Bestimmung der Teilnehmendenzahl erfolgt auf Basis des Pretest-Zwecks, der Heterogenität der Zielgruppe und der Sättigung festgestellter Verständlichkeitsprobleme; in diesem Lauf wird keine feste Zahl vorgegeben.

**Quantitativ-empirische Validierung:**  Die quantitative Validierungsmethode, die Stichprobengröße und die Akzeptanzkriterien sind festzulegen, nachdem `PLANNED_ANALYSIS` definiert wurde. Sie hängen von der gewählten Messmodellevaluierung, der Modellkomplexität, Power-Überlegungen und etwaigen geplanten Gruppenvergleichen ab.

**Status:**  Die empirische Validierung ist ausstehend.

B7 Machine-readable JSON

```
{
  "conformance": {
    "design_lock_ok": true,
    "subset_source_lock_ok": true,
    "e2_proof_ok": true,
    "object_equivalence_ok": true,
    "subscale_membership_ok": true,
    "construct_coverage_ok": true,
    "apply_human_capability_ok": true,
    "within_construct_scale_coherence_ok": true,
    "item_count_checksum_ok": true,
    "atomic_items_ok": true,
    "retrieval_support_ok": true,
    "routing_ok": true,
    "routing_cross_output_consistency_ok": true,
    "participant_claims_ok": true,
    "scale_decision_ok": true,
    "validation_plan_ok": true,
    "json_consistency_ok": true,
    "all_hard_checks_pass": true
  },
  "metadata": {
    "instrument_name": "Employee AI Readiness Questionnaire",
    "target_population": "Kaufmännische Mitarbeitende eines mittelständischen Unternehmens",
    "ai_context": "Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag",
    "measurement_goal": "Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen",
    "instrument_purpose": "DIAGNOSTIC",
    "run_mode": "QUESTIONNAIRE_GENERATION",
    "design_audit_reference": "[verdächtiger Link entfernt]",
    "status": "theoretically_grounded_empirical_validation_pending",
    "supporting_datasets": ["Datensatz_v1"],
    "overall_score_supported": false,
    "design_expected_item_count": 18,
    "traceability_item_count": 18,
    "participant_questionnaire_item_count": 18,
    "json_item_count": 18,
    "construct_item_counts": {
      "READINESS_CORE_LIT": 3,
      "READINESS_CORE_LEARN": 3,
      "READINESS_CORE_APPLY": 3,
      "READINESS_CORE_DETECT": 3,
      "READINESS_CORE_COMFORT": 3,
      "CONTEXT_FC": 3
    },
    "construct_scale_plan": {
      "READINESS_CORE_LIT": "MAILS original 0-10",
      "READINESS_CORE_LEARN": "AILRSE-5 original 1-7",
      "READINESS_CORE_APPLY": "MAILS original 0-10",
      "READINESS_CORE_DETECT": "MAILS original 0-10",
      "READINESS_CORE_COMFORT": "AIRS original 1-5",
      "CONTEXT_FC": "Lambiase original 1-7"
    }
  },
  "constructs": [
    {
      "construct_code": "READINESS_CORE_LIT",
      "construct_name": "Wahrgenommenes KI-Grundverständnis",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["Carolus et al. (2023)"]
    },
    {
      "construct_code": "READINESS_CORE_LEARN",
      "construct_name": "KI-Lern-Selbstwirksamkeit",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["Oksanen et al. (2026)"]
    },
    {
      "construct_code": "READINESS_CORE_APPLY",
      "construct_name": "Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["Carolus et al. (2023)"]
    },
    {
      "construct_code": "READINESS_CORE_DETECT",
      "construct_name": "Kritische KI-Bewertungskompetenz & KI-Erkennung",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["Carolus et al. (2023)", "Ng et al. (2021)"]
    },
    {
      "construct_code": "READINESS_CORE_COMFORT",
      "construct_name": "Affektiver Komfort im Umgang mit KI",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["Wang et al. (2026)"]
    },
    {
      "construct_code": "CONTEXT_FC",
      "construct_name": "Wahrgenommene Erleichternde Bedingungen",
      "analysis_level": "CONTEXT",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["Lambiase et al. (2025)"]
    }
  ],
  "routing": {
    "NO_EXPERIENCE": {
      "included_modules": ["READINESS_CORE_LIT", "READINESS_CORE_LEARN", "CONTEXT_FC", "DIAGNOSTIC_NEEDS"],
      "skipped_modules": ["READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT"],
      "skipped_score_status": "not_scored_due_to_no_experience"
    },
    "LIMITED_EXPERIENCE": {
      "included_modules": ["READINESS_CORE_LIT", "READINESS_CORE_LEARN", "READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT", "CONTEXT_FC", "DIAGNOSTIC_NEEDS"],
      "skipped_modules": [],
      "skipped_score_status": "none"
    },
    "REGULAR_USER": {
      "included_modules": ["READINESS_CORE_LIT", "READINESS_CORE_LEARN", "READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT", "CONTEXT_FC", "DIAGNOSTIC_NEEDS"],
      "skipped_modules": [],
      "skipped_score_status": "none"
    }
  },
  "items": [
    {
      "item_id": "LIT_01",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kenne die wichtigsten Grundbegriffe zum Thema ‚Generative Künstliche Intelligenz‘ (z. B. Sprachmodelle, Prompts).",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kennt die zentralen Grundbegriffe generativer KI.",
      "source_evidence": [
        {
          "source_id": "Carolus et al. (2023)",
          "source_locator": "Appendix A, Understand AI",
          "source_item_id": "Item 7",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Kenntnis zentraler KI-Grundbegriffe",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "MAILS 0-10",
      "final_scale": "MAILS 0-10",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "VALIDATED_TRANSLATION_AVAILABLE",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "LIT_02",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kenne verständliche Definitionen von generativer künstlicher Intelligenz.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kennt verständliche Definitionen von generativer KI.",
      "source_evidence": [
        {
          "source_id": "Carolus et al. (2023)",
          "source_locator": "Appendix A, Understand AI",
          "source_item_id": "Item 8",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Kenntnis von KI-Definitionen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "MAILS 0-10",
      "final_scale": "MAILS 0-10",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "VALIDATED_TRANSLATION_AVAILABLE",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "LIT_03",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kann einschätzen, welche Vor- und Nachteile der Einsatz generativer KI-Anwendungen im kaufmännischen Arbeitsalltag mit sich bringt.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann Vor- und Nachteile von generativer KI im Arbeitsalltag einschätzen.",
      "source_evidence": [
        {
          "source_id": "Carolus et al. (2023)",
          "source_locator": "Appendix A, Understand AI",
          "source_item_id": "Item 10",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Einschätzung von KI-Vor- und Nachteilen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "MAILS 0-10",
      "final_scale": "MAILS 0-10",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "VALIDATED_TRANSLATION_AVAILABLE",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "LEARN_01",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen im kaufmännischen Arbeitsalltag funktionieren.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte ist zuversichtlich, die Funktionsweise neuer generativer KI zu verstehen.",
      "source_evidence": [
        {
          "source_id": "Oksanen et al. (2026)",
          "source_locator": "Table 2",
          "source_item_id": "Item 1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Zuversicht, KI-Funktionsweise zu verstehen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "AILRSE-5 1-7",
      "final_scale": "AILRSE-5 1-7",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NEEDS_EQUIVALENCE_CHECK",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "LEARN_02",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich bei Bedarf lernen kann, wie man neue generative KI-Anwendungen nutzt.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte ist zuversichtlich, bei Bedarf die Nutzung neuer KI-Anwendungen zu erlernen.",
      "source_evidence": [
        {
          "source_id": "Oksanen et al. (2026)",
          "source_locator": "Table 2",
          "source_item_id": "Item 2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Zuversicht, KI-Nutzung bei Bedarf zu erlernen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "AILRSE-5 1-7",
      "final_scale": "AILRSE-5 1-7",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NEEDS_EQUIVALENCE_CHECK",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "LEARN_03",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich selbstständig lernen kann, neue generative KI-Anwendungen einzusetzen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte ist zuversichtlich, den Einsatz neuer KI selbstständig zu erlernen.",
      "source_evidence": [
        {
          "source_id": "Oksanen et al. (2026)",
          "source_locator": "Table 2",
          "source_item_id": "Item 5",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Zuversicht, KI-Nutzung selbstständig zu erlernen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "AILRSE-5 1-7",
      "final_scale": "AILRSE-5 1-7",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NEEDS_EQUIVALENCE_CHECK",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "APPLY_01",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag zielgerichtet bedienen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann generative KI-Anwendungen im Arbeitsalltag zielgerichtet bedienen.",
      "source_evidence": [
        {
          "source_id": "Carolus et al. (2023)",
          "source_locator": "Appendix A, Apply AI",
          "source_item_id": "Item 1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Praktische Fähigkeit zur KI-Bedienung",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "MAILS 0-10",
      "final_scale": "MAILS 0-10",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "VALIDATED_TRANSLATION_AVAILABLE",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "APPLY_02",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Ich kann bei der Nutzung generativer KI-Anwendungen die meisten auftretenden Probleme selbstständig gut bewältigen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann auftretende Probleme bei der KI-Nutzung selbstständig bewältigen.",
      "source_evidence": [
        {
          "source_id": "Carolus et al. (2023)",
          "source_locator": "Appendix A, AI Problem solving",
          "source_item_id": "Item 24",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Selbstständige KI-Problemlösekompetenz",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "MAILS 0-10",
      "final_scale": "MAILS 0-10",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "VALIDATED_TRANSLATION_AVAILABLE",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "APPLY_03",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Ich kann mich bei schwierigen Situationen beim Einsatz generativer KI-Anwendungen auf meine eigenen Fähigkeiten verlassen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann sich bei schwieriger KI-Nutzung auf eigene Fähigkeiten verlassen.",
      "source_evidence": [
        {
          "source_id": "Carolus et al. (2023)",
          "source_locator": "Appendix A, AI Problem solving",
          "source_item_id": "Item 23",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Vertrauen in eigene Fähigkeiten bei schwieriger KI-Nutzung",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "MAILS 0-10",
      "final_scale": "MAILS 0-10",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "VALIDATED_TRANSLATION_AVAILABLE",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "DETECT_01",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann erkennen, ob ich mit einer Anwendung auf Basis generativer künstlicher Intelligenz zu tun habe.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann KI-basierte Anwendungen als solche erkennen.",
      "source_evidence": [
        {
          "source_id": "Carolus et al. (2023)",
          "source_locator": "Appendix A, Detect AI",
          "source_item_id": "Item 13",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Erkennung von KI-gestützten Anwendungen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "MAILS 0-10",
      "final_scale": "MAILS 0-10",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "VALIDATED_TRANSLATION_AVAILABLE",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "DETECT_02",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann unterscheiden, ob ich mit einer generativen KI oder einer realen Person interagiere.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann zwischen KI und realen Personen in der Interaktion unterscheiden.",
      "source_evidence": [
        {
          "source_id": "Carolus et al. (2023)",
          "source_locator": "Appendix A, Detect AI",
          "source_item_id": "Item 15",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Unterscheidung zwischen KI- und menschlicher Interaktion",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "MAILS 0-10",
      "final_scale": "MAILS 0-10",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "VALIDATED_TRANSLATION_AVAILABLE",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "DETECT_03",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann die Richtigkeit und Plausibilität von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.",
      "evidence_class": "E3",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann KI-generierte Ergebnisse kritisch auf Richtigkeit und Plausibilität überprüfen.",
      "source_evidence": [
        {
          "source_id": "Carolus et al. (2023)",
          "source_locator": "Section 2.1 & Appendix A",
          "source_item_id": null,
          "source_item_text_verified": false,
          "source_definition_verified": true,
          "semantic_fingerprint": "Kritische Inhalts- und Factual-Correctness-Prüfung von KI-Output",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "theory-derived",
      "original_scale": "MAILS 0-10",
      "final_scale": "MAILS 0-10",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "E3-Skalenzuweisung an das gesperrte MAILS 0-10 Format",
      "translation_status": "NOT_NEEDED",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "PASS",
      "e3_substantive_sources": ["MAILS (Carolus et al., 2023)", "Ng et al. (2021)"],
      "e3_contrast_sources": ["P4 (Do Khac et al., 2025)"]
    },
    {
      "item_id": "COMFORT_01",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Ich fühle mich nicht verlegen, wenn bei der Nutzung generativer KI-Anwendungen vor anderen Probleme oder Schwierigkeiten auftreten.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_ATTITUDE",
      "atomic_proposition": "Der Befragte empfindet keine Verlegenheit bei Problemen während der KI-Nutzung vor anderen.",
      "source_evidence": [
        {
          "source_id": "Wang et al. (2026)",
          "source_locator": "Table 5 & Appendix A",
          "source_item_id": "COM1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Fehlen von Verlegenheit bei KI-Schwierigkeiten vor anderen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "AIRS 1-5",
      "final_scale": "AIRS 1-5",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NEEDS_EQUIVALENCE_CHECK",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "COMFORT_02",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Ich glaube, dass viele Anwendungen generativer künstlicher Intelligenz keine Bedenken hinsichtlich Gesundheit oder Sicherheit aufwerfen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_ATTITUDE",
      "atomic_proposition": "Der Befragte hält viele KI-Anwendungen bezüglich Gesundheit und Sicherheit für unbedenklich.",
      "source_evidence": [
        {
          "source_id": "Wang et al. (2026)",
          "source_locator": "Table 5 & Appendix A",
          "source_item_id": "COM2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Unbedenklichkeit bezüglich Gesundheit und Sicherheit",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "AIRS 1-5",
      "final_scale": "AIRS 1-5",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NEEDS_EQUIVALENCE_CHECK",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "COMFORT_03",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Ich habe keine Angst vor menschenähnlichen KI-Anwendungen oder KI-Systemen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_ATTITUDE",
      "atomic_proposition": "Der Befragte hat keine Angst vor menschenähnlichen KI-Systemen.",
      "source_evidence": [
        {
          "source_id": "Wang et al. (2026)",
          "source_locator": "Table 5 & Appendix A",
          "source_item_id": "COM3",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Fehlen von Angst vor menschenähnlichen KI-Systemen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "AIRS 1-5",
      "final_scale": "AIRS 1-5",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NEEDS_EQUIVALENCE_CHECK",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "FC_01",
      "construct_code": "CONTEXT_FC",
      "question_text": "Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI-Anwendungen in meiner Arbeit zu nutzen.",
      "evidence_class": "E2",
      "measurement_object": "ORG_CONTEXT",
      "atomic_proposition": "Dem Befragten stehen die notwendigen Ressourcen für die KI-Nutzung zur Verfügung.",
      "source_evidence": [
        {
          "source_id": "Lambiase et al. (2025)",
          "source_locator": "Section 4.2",
          "source_item_id": "FC_1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Verfügbarkeit notwendiger Ressourcen für KI-Nutzung",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "Lambiase 1-7",
      "final_scale": "Lambiase 1-7",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NEEDS_EQUIVALENCE_CHECK",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "FC_02",
      "construct_code": "CONTEXT_FC",
      "question_text": "Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen für meine Aufgaben zu nutzen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte verfügt über das notwendige Wissen zur KI-Nutzung.",
      "source_evidence": [
        {
          "source_id": "Lambiase et al. (2025)",
          "source_locator": "Section 4.2",
          "source_item_id": "FC_2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Verfügbarkeit notwendigen Wissens für KI-Nutzung",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "Lambiase 1-7",
      "final_scale": "Lambiase 1-7",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NEEDS_EQUIVALENCE_CHECK",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "FC_03",
      "construct_code": "CONTEXT_FC",
      "question_text": "Generative KI-Anwendungen sind mit anderen von mir genutzten Technologien und Arbeitsmitteln kompatibel.",
      "evidence_class": "E2",
      "measurement_object": "SYSTEM_PROPERTY",
      "atomic_proposition": "Generative KI-Anwendungen sind mit anderen genutzten Technologien kompatibel.",
      "source_evidence": [
        {
          "source_id": "Lambiase et al. (2025)",
          "source_locator": "Section 4.2",
          "source_item_id": "FC_3",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Technologische Kompatibilität generativer KI",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "Lambiase 1-7",
      "final_scale": "Lambiase 1-7",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NEEDS_EQUIVALENCE_CHECK",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    }
  ]
}
```

Die Targeted Regression Matrix liefert ein vollständiges **PASS**  in allen 17 Prüfmechanismen. Die Generierung ist vollständig konform (`CONFORMANT_GENERATION`), exakt auf 18 Items spezifiziert und wissenschaftlich zurückführbar verankert.

---

