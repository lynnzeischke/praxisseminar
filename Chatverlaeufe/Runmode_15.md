# runmode 15

Quelle: https://notebook.google.com/notebook/ad19f3fc-0592-4426-bddc-f09272b2cbb4
Exportiert: 21.10.2026, 18:58:52

---

## Frage

führe das aus  MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V3_5_R1_SOURCE_BOUND_PRODUCTION_TEST_CANDIDATE.md

---

## Antwort

B0 – PROVISIONAL CONFORMANCE MATRIX (PHASE 1)

| Check / Hard Firewall Gate | Phase-1 Status | Evidence / Operational Rationale |
| --- | --- | --- |
| `design_lock_ok` | **PASS** | Locked architecture preserved: 6 constructs × 3 items = 18 reflective items; 3-item AILRSE-5 subset; 3-item Lambiase FC subset; TTF and Behavioral Intention excluded[1]. |
| `subset_source_lock_ok` | **PASS** | Subset source boundaries strictly respected: AILRSE-5 items from AILRSE-5[4][5]; FC items FC_1, FC_2, FC_3 from Lambiase et al.[6][7]. |
| `e2_proof_ok` | **PASS** | All E2 items linked to concrete verified source items, locators, and matching semantic fingerprints[5]. |
| `object_equivalence_ok` | **PASS** | Measurement objects preserved: capability → capability; org context → org context. No system property converted to human capability[11][12]. |
| `subscale_membership_ok` | **PASS** | Original subscales preserved: AIRS Comfort items drawn exclusively from published Comfort factor (COM1, COM2, COM3)[13][14]. |
| `construct_coverage_ok` | **PASS** | `READINESS_CORE_DETECT` covers both AI detection (origin recognition) and critical output evaluation[9][15]. |
| `apply_human_capability_ok` | **PASS** | All `READINESS_CORE_APPLY` items measure the respondent's own application capability (MAILS Use & Apply / Problem solving); productivity/time-saving items excluded[9][16]. |
| `e3_registry_closure_ok` | **PASS** | `DETECT_03` derived from verified active MAILS competency definitions; no unverified secondary sources used[9]. |
| `within_construct_scale_coherence_ok` | **PASS** | Exactly 1 response scale format per reflective construct (LIT 0–10, LEARN 1–7, APPLY 0–10, DETECT 0–10, COMFORT 1–5, FC 1–7)[19][20]. |
| `scale_instruction_semantics_ok` | **PASS** | Capability/intensity instructions used for 0–10 capability anchors; agreement instructions used for Likert agreement anchors[21][22]. |
| `design_audit_reference_ok` | **PASS** | Canonical identifier string matched exactly: `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`[1][17]. |
| `diagnostic_module_completeness_ok` | **PASS** | `DIAGNOSTIC_NEEDS` (DIAG_01, DIAG_02) and `DEMOGRAPHICS_MINIMAL` (DEM_01) present and excluded from 18-item checksum[23][24]. |
| `fc_not_judgable_option_ok` | **PASS** | "Kann ich nicht beurteilen" included on FC_01–FC_03, coded as `MISSING_NOT_SCORED`[25]. |
| `diag01_option_separation_ok` | **PASS** | "Sonstiges: ______" and "Kein Schulungs-/Entwicklungsbedarf" provided as separate choices in DIAG_01; exclusive selection configured[26]. |
| `item_count_checksum_ok` | **PASS** | Traceability item count = participant questionnaire item count = 18 reflective items (3 per construct)[2][27]. |
| `atomic_items_ok` | **PASS** | All final reflective items contain exactly 1 atomic proposition (e.g., DETECT_03 measures exclusively "inhaltliche Richtigkeit")[28][29]. |
| `retrieval_support_ok` | **PASS** | Scientific provenance mapped directly to verified primary papers; `retrieval_support` = `[]` for readiness core sources per exclusion map[30]. |
| `routing_ok` | **PASS** | Experience filter configured: `NO_EXPERIENCE` skips experience-dependent modules (APPLY, DETECT, COMFORT) without hypothetical score fabrication[31][32]. |
| `routing_cross_output_consistency_ok` | **PASS** | Identical routing definitions across trace, questionnaire, and scoring rules[33]. |
| `participant_claims_ok` | **PASS** | No unverified company policies, privacy guarantees, or organizational initiatives asserted; literal placeholder `[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]` used[3][34]. |
| `scale_decision_ok` | **PASS** | `SCALE_PREFERENCE` = `original_scales` applied per construct according to Audit 004_FINAL scale plan[19][35]. |
| `validation_plan_ok` | **PASS** | Non-numeric fallback template applied (`PLANNED_ANALYSIS` = `NOT_PROVIDED`); zero sample-size numerals, zero prescribed SEM/CFA methods[36][37]. |
| `json_consistency_ok` | **PENDING** | Machine-readable B7 export pending in Phase 2[38][39]. |
| **ALL_HARD_CHECKS_PASS** | **NOT_YET_DETERMINED** | Phase-1 check phase complete; final determination follows B7 JSON export[38][39]. |
| **OVERALL STATUS** | **PENDING_B7_EXPORT** | All Phase-1 inspectable gates passed. Ready for Phase-2 JSON export[38][39]. |

B1 – DESIGN-AUDIT REFERENCE, INPUTS & BOUNDED ASSUMPTIONS

**Design-Audit Reference:**  `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`[1]

**Target Population (** M1**):**  Kaufmännische Mitarbeitende eines mittelständischen Unternehmens[40].

**AI Context (** M2**):**  Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag[40].

**Measurement Goal (** M3**):**  Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen vor einem breiteren KI-Rollout[40].

**Instrument Purpose (** C1**):**  `DIAGNOSTIC`[40].

**Organizational Context (** C2**):**  `CONTEXT_TEXT` = `NOT_PROVIDED` (generisches Messinstrument ohne unbelegte unternehmensspezifische Regeln, Schulungen oder Prozesse)[40].

**Task Context (** C3**):**  `TASK_CONTEXT` = `NOT_PROVIDED` (Task-Technology Fit wird nicht operationalisiert)[40].

**Delivery & Output Configuration:**  `DELIVERY_MODE` = `TWO_PHASE_VERIFIABLE`, `OUTPUT_PHASE` = `PHASE_1_GENERATE`, `SCALE_PREFERENCE` = `original_scales`, `REPRODUCIBILITY_MODE` = `strict`, Language = Deutsch[19].

B2 – FULL ITEM TRACEABILITY (18 REFLECTIVE ITEMS + DIAGNOSTIC/DEMOGRAPHIC MODULES)

1. READINESS_CORE_LIT – Wahrgenommenes KI-Grundverständnis

*Construct Level:* `READINESS_CORE` | *Measurement Model:* `REFLECTIVE` | *Scale:* MAILS Original 0–10 Format (0 = gar nicht / kaum ausgeprägt, 10 = sehr gut / perfekt ausgeprägt)[2].

- **LIT_01** 
**Item Text:**  „Ich kenne die wichtigsten Grundbegriffe zum Thema generative KI.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `MAILS` (Carolus et al., 2023)[17][43]

**Source Locator:**  Appendix A, Item 7 ("Understand AI")[9]

**Source Item ID:**  `Understand_AI_7`

**Verified Source Meaning:**  Knowledge of the most important concepts of artificial intelligence[9].

**Target Semantic Fingerprint:**  Knowledge of core concepts regarding generative AI in business tasks.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **LIT_02** 
**Item Text:**  „Ich kenne grundlegende Definitionen und Funktionsweisen generativer KI.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `MAILS` (Carolus et al., 2023)[17][43]

**Source Locator:**  Appendix A, Item 8 ("Understand AI")[9]

**Source Item ID:**  `Understand_AI_8`

**Verified Source Meaning:**  Knowledge of definitions of artificial intelligence[9].

**Target Semantic Fingerprint:**  Knowledge of definitions and working principles of generative AI.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **LIT_03** 
**Item Text:**  „Ich kann die typischen Anwendungsmöglichkeiten generativer KI im kaufmännischen Alltag einschätzen.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `MAILS` (Carolus et al., 2023)[17][43]

**Source Locator:**  Appendix A, Item 9 ("Understand AI")[9]

**Source Item ID:**  `Understand_AI_9`

**Verified Source Meaning:**  Assessment of opportunities/applications of AI[9].

**Target Semantic Fingerprint:**  Ability to assess typical application possibilities of generative AI in business routine (atomic proposition: application scope)[46].

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`

2. READINESS_CORE_LEARN – KI-Lern-Selbstwirksamkeit

*Construct Level:* `READINESS_CORE` | *Measurement Model:* `REFLECTIVE` | *Scale:* AILRSE-5 Original 1–7 Format (1 = stimme gar nicht zu, 7 = stimme voll und ganz zu)[2].

- **LEARN_01** 
**Item Text:**  „Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen funktionieren.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `AILRSE-5` (Oksanen et al., 2026)[4][47]

**Source Locator:**  Table 2, Item 1[5]

**Source Item ID:**  `AILRSE5_1`

**Verified Source Meaning:**  Confidence in ability to understand how new AI technologies work[5].

**Target Semantic Fingerprint:**  Confidence in understanding the functionality of new generative AI tools.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **LEARN_02** 
**Item Text:**  „Ich bin zuversichtlich, dass ich lernen kann, wie man neue generative KI-Anwendungen bei Bedarf bedient.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `AILRSE-5` (Oksanen et al., 2026)[4][47]

**Source Locator:**  Table 2, Item 2[5]

**Source Item ID:**  `AILRSE5_2`

**Verified Source Meaning:**  Confidence in ability to learn how to use new AI technologies if necessary[5].

**Target Semantic Fingerprint:**  Confidence in learning to operate new generative AI applications when needed.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **LEARN_03** 
**Item Text:**  „Ich bin zuversichtlich, dass ich mir die Nutzung neuer generativer KI-Anwendungen eigenständig aneignen kann.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `AILRSE-5` (Oksanen et al., 2026)[4][47]

**Source Locator:**  Table 2, Item 5[48]

**Source Item ID:**  `AILRSE5_5`

**Verified Source Meaning:**  Confidence in ability to learn how to use new AI technologies independently[48].

**Target Semantic Fingerprint:**  Confidence in independently acquiring the skills to use new generative AI tools.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`

3. READINESS_CORE_APPLY – Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit

*Construct Level:* `READINESS_CORE` | *Measurement Model:* `REFLECTIVE` | *Scale:* MAILS Original 0–10 Format (0 = gar nicht / kaum ausgeprägt, 10 = sehr gut / perfekt ausgeprägt)[2].

- **APPLY_01** 
**Item Text:**  „Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag bedienen.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `MAILS` (Carolus et al., 2023)[17][43]

**Source Locator:**  Appendix A, Item 1 ("Use & Apply AI")[9]

**Source Item ID:**  `Apply_AI_1`

**Verified Source Meaning:**  Capability to operate AI applications in daily life[9].

**Target Semantic Fingerprint:**  Perceived capability to operate generative AI tools in office work.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **APPLY_02** 
**Item Text:**  „Ich kann generative KI gezielt einsetzen, um meine beruflichen Aufgaben zu bearbeiten.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `MAILS` (Carolus et al., 2023)[17][43]

**Source Locator:**  Appendix A, Item 3 ("Use & Apply AI")[9]

**Source Item ID:**  `Apply_AI_3`

**Verified Source Meaning:**  Capability to use AI meaningfully to achieve daily goals[9].

**Target Semantic Fingerprint:**  Perceived capability to apply generative AI targetedly for task completion.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **APPLY_03** 
**Item Text:**  „Ich kann auftretende Schwierigkeiten beim Umgang mit generativer KI weitgehend selbstständig bewältigen.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `MAILS` (Carolus et al., 2023)[17][43]

**Source Locator:**  Appendix A, Item 24 ("AI Problem solving")[9]

**Source Item ID:**  `Problem_solving_24`

**Verified Source Meaning:**  Capability to handle most problems in dealing with AI independently[9].

**Target Semantic Fingerprint:**  Perceived capability to independently solve difficulties when using generative AI.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`

4. READINESS_CORE_DETECT – Kritische KI-Bewertungskompetenz & KI-Erkennung

*Construct Level:* `READINESS_CORE` | *Measurement Model:* `REFLECTIVE` | *Scale:* MAILS Original 0–10 Format (0 = gar nicht / kaum ausgeprägt, 10 = sehr gut / perfekt ausgeprägt)[2].

- **DETECT_01** 
**Item Text:**  „Ich kann erkennen, ob eine digitale Anwendung auf generativer KI basiert.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `MAILS` (Carolus et al., 2023)[17][43]

**Source Locator:**  Appendix A, Item 13 ("Detect AI")[9]

**Source Item ID:**  `Detect_AI_13`

**Verified Source Meaning:**  Ability to tell if dealing with an application based on AI[9].

**Target Semantic Fingerprint:**  Capability to recognize whether a software application is based on generative AI.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **DETECT_02** 
**Item Text:**  „Ich kann unterscheiden, ob eine Rückmeldung von einer generativen KI oder von einer Person stammt.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `MAILS` (Carolus et al., 2023)[17][43]

**Source Locator:**  Appendix A, Item 15 ("Detect AI")[9]

**Source Item ID:**  `Detect_AI_15`

**Verified Source Meaning:**  Ability to distinguish interaction with AI versus a real human[9].

**Target Semantic Fingerprint:**  Capability to distinguish human-generated feedback from generative AI output.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **DETECT_03** 
**Item Text:**  „Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.“

**Evidence Class:**  `E3_THEORY_DERIVED` | **Adaptation Type:**  `THEORY_DERIVED`

**Source ID:**  `MAILS` (Carolus et al., 2023)[17][43]

**Source Locator:**  Definition & Competency Model Section 3.1 / Appendix A ("Evaluate AI" facet)[9][21]

**Source Item ID:**  `null` | **Source Item Text Verified:**  `false` | **Source Definition Verified:**  `true`[49]

**Substantive Sources:**  `["MAILS"]`[18] | **Contrast Sources:**  `["P4"]`[50]

**Target Semantic Fingerprint:**  Human capability to critically verify the factual correctness of AI-generated work outputs (atomic proposition: inhaltliche Richtigkeit)[28].

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NOT_NEEDED`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`

5. READINESS_CORE_COMFORT – Affektiver Komfort im Umgang mit KI

*Construct Level:* `READINESS_CORE` | *Measurement Model:* `REFLECTIVE` | *Scale:* AIRS Original 1–5 Format (1 = stimme gar nicht zu, 5 = stimme voll und ganz zu)[2].

- **COMFORT_01** 
**Item Text:**  „Es ist mir nicht unangenehm, wenn bei der Nutzung von generativer KI vor anderen Personen Fehler oder Probleme auftreten.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `AIRS` (Wang et al., 2026)[51][52]

**Source Locator:**  Appendix A, Item 9 (Comfort factor)[13][53]

**Source Item ID:**  `COM1` / `Q9`

**Verified Source Meaning:**  Absence of embarrassment when encountering AI problems in front of others[53][54].

**Target Semantic Fingerprint:**  Lack of embarrassment during public or peer-observed AI difficulties.

**Measurement Object:**  `HUMAN_ATTITUDE` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **COMFORT_02** 
**Item Text:**  „Ich bin überzeugt, dass die Nutzung generativer KI im Arbeitsalltag keine gesundheitlichen oder sicherheitsbezogenen Bedenken aufwirft.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `AIRS` (Wang et al., 2026)[51][52]

**Source Locator:**  Appendix A, Item 8 (Comfort factor)[13][53]

**Source Item ID:**  `COM2` / `Q8`

**Verified Source Meaning:**  Belief that AI technologies do not raise health or safety concerns[53][55].

**Target Semantic Fingerprint:**  Perceived absence of health/safety risks from generative AI use in daily office work[56].

**Measurement Object:**  `HUMAN_ATTITUDE` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **COMFORT_03** 
**Item Text:**  „Ich empfinde keine Angst oder Unbehagen bei der Interaktion mit generativen KI-Anwendungen.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `AIRS` (Wang et al., 2026)[51][52]

**Source Locator:**  Appendix A, Item 18 (Comfort factor)[8][13]

**Source Item ID:**  `COM3` / `Q18`

**Verified Source Meaning:**  Absence of fear toward interaction with AI entities[8][55].

**Target Semantic Fingerprint:**  Absence of personal fear/anxiety during direct interaction with generative AI tools[56].

**Measurement Object:**  `HUMAN_ATTITUDE` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`

6. CONTEXT_FC – Wahrgenommene Erleichternde Bedingungen

*Construct Level:* `CONTEXT` | *Measurement Model:* `REFLECTIVE` | *Scale:* Lambiase original 1–7 Format (1 = stimme gar nicht zu, 7 = stimme voll und ganz zu) + Zusätzliche Antwortoption „Kann ich nicht beurteilen“ (`MISSING_NOT_SCORED`)[6].

- **FC_01** 
**Item Text:**  „Mir stehen die notwendigen technischen Ressourcen für die Nutzung generativer KI zur Verfügung.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `Lambiase_et_al_2025`[57][58]

**Source Locator:**  Section 4.2 / UTAUT2 Facilitating Conditions Pool[6]

**Source Item ID:**  `FC_1`

**Verified Source Meaning:**  Possession of necessary resources to use the technology[6][59].

**Target Semantic Fingerprint:**  Perceived availability of technical resources required for generative AI use.

**Measurement Object:**  `ORG_CONTEXT` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **FC_02** 
**Item Text:**  „Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen zu nutzen.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `Lambiase_et_al_2025`[57][58]

**Source Locator:**  Section 4.2 / UTAUT2 Facilitating Conditions Pool[6]

**Source Item ID:**  `FC_2`

**Verified Source Meaning:**  Possession of necessary knowledge to use the technology[6][59].

**Target Semantic Fingerprint:**  Perceived possession of basic knowledge necessary for operating generative AI.

**Measurement Object:**  `HUMAN_CAPABILITY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`
- **FC_03** 
**Item Text:**  „Generative KI-Anwendungen sind kompatibel mit den anderen digitalen Werkzeugen, die ich bei der Arbeit nutze.“

**Evidence Class:**  `E2_ADAPTED` | **Adaptation Type:**  `LINGUISTIC_AND_CONTEXTUAL`

**Source ID:**  `Lambiase_et_al_2025`[57][58]

**Source Locator:**  Section 4.2 / UTAUT2 Facilitating Conditions Pool[6]

**Source Item ID:**  `FC_3`

**Verified Source Meaning:**  Compatibility of the technology with other technologies used[6][59].

**Target Semantic Fingerprint:**  Technical compatibility of generative AI applications with existing software tools.

**Measurement Object:**  `SYSTEM_PROPERTY` | **Translation Status:**  `NEEDS_EQUIVALENCE_CHECK`[44]

**Retrieval Support:**  `[]`[45] | **Context Verified:**  `false`[3]

**Critic Status:**  `PASS` | **Simulated Pretest:**  `PASS`

DIAGNOSTIC & DEMOGRAPHIC MODULES (SEPARATE NON-REFLECTIVE BLOCK)

- **DIAG_01 – Schulungs- und Entwicklungsbedarfe** 
**Purpose:**  Descriptive identification of specific training domains[60].

**Measurement Model:**  `NON_REFLECTIVE_DESCRIPTIVE` (Excluded from 18-item reflective checksum)[23][60].

  - **Format:**  Multi-Select with 7 required domain choices, plus 2 separate options[26][60]:
Grundlagen generativer KI

Prompting

kritische Ergebnisprüfung

Datenschutz / Umgang mit sensiblen Informationen

Urheberrecht / Ethik

Prozessintegration

konkrete Tool-Anwendung

Separate Option 8:* `Sonstiges: ______`

Separate Option 9 (Exclusive):* `Kein Schulungs-/Entwicklungsbedarf`
- **DIAG_02 – Allgemeiner Unterstützungsbedarf** 
**Purpose:**  Descriptive identification of qualitative support requirements[24][26].

**Measurement Model:**  `NON_REFLECTIVE_DESCRIPTIVE` (Excluded from 18-item reflective checksum)[23].

**Format:**  Open response / generic need formulation[24].

**Item Text:**  „Welche zusätzliche Unterstützung würde Ihnen bei der Nutzung von generativer KI am Arbeitsplatz am meisten helfen?“
- **DEM_01 – Kaufmännischer Funktionsbereich** 
**Purpose:**  Minimal control variable[24].

**Measurement Model:**  `DEMOGRAPHIC_CONTROL` (Excluded from 18-item reflective checksum)[23].

**Format:**  Open field or organizational insertion placeholder `[FUNKTIONSBEREICHE_DER_ORGANISATION_EINFÜGEN]`[24].

**Item Text:**  „Welchem kaufmännischen Funktionsbereich ordnen Sie sich überwiegend zu?“

B3 – INDEPENDENT CRITIC REVIEW (METHODOLOGICAL AUDIT)

**Audit Agent 2 Decision:**  `PASS` across all 18 reflective indicators and diagnostic modules[61][62].

- **Evaluated Gates & Verified Corrections:** 
**Atomic Item Gate:**  Item `DETECT_03` was checked for single-proposition compliance. Dual-criteria formulations combining "Richtigkeit und Plausibilität" were eliminated; the item strictly measures "inhaltliche Richtigkeit"[28][29]. `LIT_03` measures single application scope without combining limits and opportunities in one item[46].

**Construct Object Purity:**  Items under `READINESS_CORE_APPLY` were audited to ensure they measure `HUMAN_CAPABILITY`. AISES item AS6/Q16 (time-saving / system benefit) was rejected as primary evidence and excluded from APPLY[12].

**AIRS Comfort Subscale Lock:**  All items in `READINESS_CORE_COMFORT` were verified to originate strictly from the published AIRS Comfort factor (Q9, Q8, Q18). Cross-factor items (e.g., SEC4/Q16) were rejected[14].

**Lambiase FC Map & Response Lock:**  Facilitating Conditions items preserve exact mappings (FC_1 = resources, FC_2 = knowledge, FC_3 = compatibility). FC_4 (support) was excluded as a transparent subset decision and not merged into FC_3[7]. All FC items include the non-numeric response option "Kann ich nicht beurteilen"[25].

**No Unverified Privacy/Process Assurances:**  Participant text contains no fabricated promises regarding anonymity, data aggregation, or mandatory company training. Placeholder `[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]` is maintained[3][34].

B4 – SIMULATED COGNITIVE READ-THROUGH (HEURISTIC EVALUATION)

**Methodological Disclaimer:**  This section represents a simulated, heuristic cognitive walkthrough by artificial agent personas (low-experience employee vs. experienced user) to detect wording ambiguities and routing logic errors. It is an internal heuristic check and **must not be described as an empirical human pretest** [38][63].

**Perspective A (Low AI Experience):**  The introduction clearly defines generative KI in simple office terms[64]. Filtering directly directs non-users past experience-dependent questions (APPLY, DETECT, COMFORT), preventing frustration[32][65]. The response option "Kann ich nicht beurteilen" in Part 3 (FC) allows non-users to answer contextual questions without being forced into an ungrounded opinion[25][66].

**Perspective B (Regular User / Commercial Specialist):**  Item wordings feel realistic for modern office environments (e.g., Copilot / ChatGPT Enterprise context)[40]. The 0–10 scale for capability and 1–7 scale for agreement match standard survey expectations[19]. Completion time is estimated at 5–7 minutes, well within the 8-minute respondent burden ceiling[40][67].

B5 – FULL PARTICIPANT QUESTIONNAIRE

Teil 0 – Einleitung & KI-Kontextdefinition

**Befragung zur Nutzung von generativer KI im kaufmännischen Arbeitsalltag**

Sehr geehrte Damen und Herren,

vielen Dank, dass Sie sich die Zeit nehmen, an dieser Befragung teilzunehmen. Mit dieser Befragung möchten wir erfahren, wie Sie generative KI im kaufmännischen Arbeitsalltag einschätzen und welche Unterstützungsbedarfe bestehen[64].

**Was ist generative KI?**  Unter generativer Künstlicher Intelligenz (generativer KI) verstehen wir digitale Anwendungen, die selbstständig neue Inhalte wie Texte, Analysen, Tabellen oder Darstellungen erstellen können. Beispiele hierfür sind Sprachmodelle wie ChatGPT Enterprise oder Microsoft Copilot, die bei der täglichen Büro- und Verwaltungsarbeit unterstützen können[40].

Bitte beantworten Sie die folgenden Fragen zutreffend aus Ihrer persönlichen Sicht. Es gibt keine „richtigen“ oder „falschen“ Antworten.

`[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]`[34]

Teil 1 – KI-Erfahrungs-Routing

**Filterfrage F01:**  Wie häufig nutzen Sie generative KI-Anwendungen (z. B. ChatGPT, Microsoft Copilot) in Ihrer täglichen Arbeit?[65][68]

[ ] **NO_EXPERIENCE:**  Ich habe generative KI bisher noch nie genutzt.

[ ] **LIMITED_EXPERIENCE:**  Ich habe generative KI bisher selten oder gelegentlich genutzt (z. B. wenige Male ausprobiert).

[ ] **REGULAR_USER:**  Ich nutze generative KI regelmäßig (z. B. wöchentlich oder täglich).

Teil 2 – Messmodule (READINESS_CORE)

**HINWEIS ZUR AUTOMATISCHEN FILTERUNG (ROUTING):**

Befragte der Gruppe **NO_EXPERIENCE**  beantworten Modul A (KI-Grundverständnis) und Modul B (KI-Lern-Selbstwirksamkeit) sowie Teil 3 (Facilitating Conditions), Teil 4 (Diagnostik) und Teil 5 (Demographie). Die Module C, D und E werden übersprungen[31][32].

Befragte der Gruppen **LIMITED_EXPERIENCE**  und **REGULAR_USER**  beantworten alle Module (Modul A bis Modul F)[31].

Modul A: Wahrgenommenes KI-Grundverständnis (READINESS_CORE_LIT)

*Antwortskala: Bitte geben Sie auf einer Skala von 0 bis 10 an, wie stark die folgenden Kenntnisse bei Ihnen ausgeprägt sind (0 = gar nicht / kaum ausgeprägt bis 10 = sehr gut / perfekt ausgeprägt).*[19][22]

**LIT_01:**  Ich kenne die wichtigsten Grundbegriffe zum Thema generative KI. `[ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ]`

**LIT_02:**  Ich kenne grundlegende Definitionen und Funktionsweisen generativer KI. `[ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ]`

**LIT_03:**  Ich kann die typischen Anwendungsmöglichkeiten generativer KI im kaufmännischen Alltag einschätzen. `[ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ]`

Modul B: KI-Lern-Selbstwirksamkeit (READINESS_CORE_LEARN)

*Antwortskala: Bitte geben Sie an, wie sehr Sie den folgenden Aussagen zustimmen (1 = stimme gar nicht zu bis 7 = stimme voll und ganz zu).*[19][22]

**LEARN_01:**  Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen funktionieren. `[ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ]`

**LEARN_02:**  Ich bin zuversichtlich, dass ich lernen kann, wie man neue generative KI-Anwendungen bei Bedarf bedient. `[ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ]`

**LEARN_03:**  Ich bin zuversichtlich, dass ich mir die Nutzung neuer generativer KI-Anwendungen eigenständig aneignen kann. `[ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ]`

Modul C: Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit (READINESS_CORE_APPLY)

*(Wird für Befragte mit NO_EXPERIENCE automatisch übersprungen)*[32] *Antwortskala: Bitte geben Sie auf einer Skala von 0 bis 10 an, wie stark die folgenden Fähigkeiten bei Ihnen ausgeprägt sind (0 = gar nicht / kaum ausgeprägt bis 10 = sehr gut / perfekt ausgeprägt).*[19][22]

**APPLY_01:**  Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag bedienen. `[ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ]`

**APPLY_02:**  Ich kann generative KI gezielt einsetzen, um meine beruflichen Aufgaben zu bearbeiten. `[ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ]`

**APPLY_03:**  Ich kann auftretende Schwierigkeiten beim Umgang mit generativer KI weitgehend selbstständig bewältigen. `[ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ]`

Modul D: Kritische KI-Bewertungskompetenz & KI-Erkennung (READINESS_CORE_DETECT)

*(Wird für Befragte mit NO_EXPERIENCE automatisch übersprungen)*[32] *Antwortskala: Bitte geben Sie auf einer Skala von 0 bis 10 an, wie stark die folgenden Fähigkeiten bei Ihnen ausgeprägt sind (0 = gar nicht / kaum ausgeprägt bis 10 = sehr gut / perfekt ausgeprägt).*[19][22]

**DETECT_01:**  Ich kann erkennen, ob eine digitale Anwendung auf generativer KI basiert. `[ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ]`

**DETECT_02:**  Ich kann unterscheiden, ob eine Rückmeldung von einer generativen KI oder von einer Person stammt. `[ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ]`

**DETECT_03:**  Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen. `[ 0 ] [ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ] [ 6 ] [ 7 ] [ 8 ] [ 9 ] [ 10 ]`

Modul E: Affektiver Komfort im Umgang mit KI (READINESS_CORE_COMFORT)

*(Wird für Befragte mit NO_EXPERIENCE automatisch übersprungen)*[32] *Antwortskala: Bitte geben Sie an, wie sehr Sie den folgenden Aussagen zustimmen (1 = stimme gar nicht zu bis 5 = stimme voll und ganz zu).*[19][22]

**COMFORT_01:**  Es ist mir nicht unangenehm, wenn bei der Nutzung von generativer KI vor anderen Personen Fehler oder Probleme auftreten. `[ 1 ] [ 2 ] [ 3 ] [ 4 ] [ 5 ]`

**COMFORT_02:**  Ich bin überzeugt, dass die Nutzung generativer KI im Arbeitsalltag keine gesundheitlichen oder sicherheitsbezogenen### B0 – PROVISIONAL CONFORMANCE MATRIX (PHASE 1)

| Check / Hard Firewall Gate | Phase-1 Status | Evidence / Operational Rationale |
| --- | --- | --- |
| `design_lock_ok` | **PASS** | Locked architecture preserved: 6 constructs × 3 items = 18 reflective items; 3-item AILRSE-5 subset; 3-item Lambiase FC subset; TTF and Behavioral Intention excluded[1]. |
| `subset_source_lock_ok` | **PASS** | Subset source boundaries strictly respected: AILRSE-5 items from AILRSE-5[4][5]; FC items FC_1, FC_2, FC_3 from Lambiase et al.[6][7]. |
| `e2_proof_ok` | **PASS** | All E2 items linked to concrete verified source items, locators, and matching semantic fingerprints[5]. |
| `object_equivalence_ok` | **PASS** | Measurement objects preserved: capability → capability; org context → org context. No system property converted to human capability[11][12]. |
| `subscale_membership_ok` | **PASS** | Original subscales preserved: AIRS Comfort items drawn exclusively from published Comfort factor (COM1, COM2, COM3)[13][14]. |
| `construct_coverage_ok` | **PASS** | `READINESS_CORE_DETECT` covers both AI detection (origin recognition) and critical output evaluation[9][15]. |
| `apply_human_capability_ok` | **PASS** | All `READINESS_CORE_APPLY` items measure the respondent's own application capability (MAILS Use & Apply / Problem solving); productivity/time-saving items excluded[9][16]. |
| `e3_registry_closure_ok` | **PASS** | `DETECT_03` derived from verified active MAILS competency definitions; no unverified secondary sources used[9]. |
| `within_construct_scale_coherence_ok` | **PASS** | Exactly 1 response scale format per reflective construct (LIT 0–10, LEARN 1–7, APPLY 0–10, DETECT 0–10, COMFORT 1–5, FC 1–7)[19][20]. |
| `scale_instruction_semantics_ok` | **PASS** | Capability/intensity instructions used for 0–10 capability anchors; agreement instructions used for Likert agreement anchors[21][22]. |
| `design_audit_reference_ok` | **PASS** | Canonical identifier string matched exactly: `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`[1][17]. |
| `diagnostic_module_completeness_ok` | **PASS** | `DIAGNOSTIC_NEEDS` (DIAG_01, DIAG_02) and `DEMOGRAPHICS_MINIMAL` (DEM_01) present and excluded from 18-item checksum[23][24]. |
| `fc_not_judgable_option_ok` | **PASS** | "Kann ich nicht beurteilen" included on FC_01–FC_03, coded as `MISSING_NOT_SCORED`[25]. |
| `diag01_option_separation_ok` | **PASS** | "Sonstiges: ______" and "Kein Schulungs-/Entwicklungsbedarf" provided as separate choices in DIAG_01; exclusive selection configured[26]. |
| `item_count_checksum_ok` | **PASS** | Traceability item count = participant questionnaire item count = 18 reflective items (3 per construct)[2][27]. |
| `atomic_items_ok` | **PASS** | All final reflective items contain exactly 1 atomic proposition (e.g., DETECT_03 measures exclusively "inhaltliche Richtigkeit")[28][29]. |
| `retrieval_support_ok` | **PASS** | Scientific provenance mapped directly to verified primary papers; `retrieval_support` = `[]` for readiness core sources per exclusion map[30]. |
| `routing_ok` | **PASS** | Experience filter configured: `NO_EXPERIENCE` skips experience-dependent modules (APPLY, DETECT, COMFORT) without hypothetical score fabrication[31][32]. |
| `routing_cross_output_consistency_ok` | **PASS** | Identical routing definitions across trace, questionnaire, and scoring rules[33]. |
| `participant_claims_ok` | **PASS** | No unverified company policies, privacy guarantees, or organizational initiatives asserted; literal placeholder `[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]` used[3][34]. |
| `scale_decision_ok` | **PASS** | `SCALE_PREFERENCE` = `original_scales` applied per construct according to Audit 004_FINAL scale plan[19][35]. |
| `validation_plan_ok` | **PASS** | Non-numeric fallback template applied (`PLANNED_ANALYSIS` = `NOT_PROVIDED`); zero sample-size numerals, zero prescribed SEM/CFA methods[36][37]. |
| `json_consistency_ok` | **PENDING** | Machine-readable B7 export pending in Phase 2[38][39]. |
| **ALL_HARD_CHECKS_PASS** | **NOT_YET_DETERMINED** | Phase-1 check phase complete; final determination follows B7 JSON export[38][39]. |
| **OVERALL STATUS** | **PENDING_B7_EXPORT** | All Phase-1 inspectable gates passed. Ready for Phase-2 JSON export[38][39]. |

B1 – DESIGN-AUDIT REFERENCE, INPUTS & BOUNDED ASSUMPTIONS

**Design-Audit Reference:**  `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`[1]

**Target Population (** M1**):**  Kaufmännische Mitarbeitende eines mittelständischen Unternehmens[40].

**AI Context (** M2**):**  Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag[40].

**Measurement Goal (** M3**):**  Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen vor einem breiteren KI-Rollout[40].

**Instrument Purpose (** C1**):**  `DIAGNOSTIC`[40].

**Organizational Context (** C2**):**  `CONTEXT_TEXT` = `NOT_PROVIDED` (generisches Messinstrument ohne unbelegte unternehmensspezifische Regeln, Schulungen oder Prozesse)[40].

**Task Context (** C3**):**  `TASK_CONTEXT` = `NOT_PROVIDED` (Task-Technology Fit wird nicht operationalisiert)[40].

**Delivery & Output Configuration:**  `DELIVERY_MODE` = `TWO_PHASE_VERIFIABLE`, `OUTPUT_PHASE` = `PHASE_1_GENERATE`, `SCALE_PREFERENCE` = `original_scales`, `REPRODUCIBILITY_MODE` = `strict`, Language = Deutsch[19].

B2 – FULL ITEM TRACEABILITY (18 REFLECTIVE ITEMS + DIAGNOSTIC/DEMOGRAPHIC MODULES)

1. READINESS_CORE_LIT – Wahrgenommenes KI-Grundverständnis

*Construct Level:* `READINESS_CORE` | *Measurement Model:* `REFLECTIVE` | *Scale:* MAILS Original 0–10 Format (0 = gar nicht / kaum ausgeprägt, 10 = sehr gut / perfekt ausgeprägt)[2].

- **LIT_01:**  „Ich kenne die wichtigsten Grundbegriffe zum Thema generative KI.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `MAILS` (Carolus et al., 2023)[17][43]

*Source Locator:* Appendix A, Item 7 (`Understand_AI_7`)[9] | *Verified Source Meaning:* Knowledge of core concepts of AI[9].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **LIT_02:**  „Ich kenne grundlegende Definitionen und Funktionsweisen generativer KI.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `MAILS` (Carolus et al., 2023)[17][43]

*Source Locator:* Appendix A, Item 8 (`Understand_AI_8`)[9] | *Verified Source Meaning:* Knowledge of definitions of AI[9].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **LIT_03:**  „Ich kann die typischen Anwendungsmöglichkeiten generativer KI im kaufmännischen Alltag einschätzen.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `MAILS` (Carolus et al., 2023)[17][43]

*Source Locator:* Appendix A, Item 9 (`Understand_AI_9`)[9] | *Verified Source Meaning:* Assessment of opportunities/applications of AI[9].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]

2. READINESS_CORE_LEARN – KI-Lern-Selbstwirksamkeit

*Construct Level:* `READINESS_CORE` | *Measurement Model:* `REFLECTIVE` | *Scale:* AILRSE-5 Original 1–7 Format (1 = stimme gar nicht zu, 7 = stimme voll und ganz zu)[2].

- **LEARN_01:**  „Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen funktionieren.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `AILRSE-5` (Oksanen et al., 2026)[4][47]

*Source Locator:* Table 2, Item 1 (`AILRSE5_1`)[5] | *Verified Source Meaning:* Confidence in ability to understand how new AI technologies work[5].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **LEARN_02:**  „Ich bin zuversichtlich, dass ich lernen kann, wie man neue generative KI-Anwendungen bei Bedarf bedient.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `AILRSE-5` (Oksanen et al., 2026)[4][47]

*Source Locator:* Table 2, Item 2 (`AILRSE5_2`)[5] | *Verified Source Meaning:* Confidence in ability to learn how to use new AI technologies if necessary[5].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **LEARN_03:**  „Ich bin zuversichtlich, dass ich mir die Nutzung neuer generativer KI-Anwendungen eigenständig aneignen kann.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `AILRSE-5` (Oksanen et al., 2026)[4][47]

*Source Locator:* Table 2, Item 5 (`AILRSE5_5`)[48] | *Verified Source Meaning:* Confidence in ability to learn how to use new AI technologies independently[48].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]

3. READINESS_CORE_APPLY – Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit

*Construct Level:* `READINESS_CORE` | *Measurement Model:* `REFLECTIVE` | *Scale:* MAILS Original 0–10 Format (0 = gar nicht / kaum ausgeprägt, 10 = sehr gut / perfekt ausgeprägt)[2].

- **APPLY_01:**  „Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag bedienen.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `MAILS` (Carolus et al., 2023)[17][43]

*Source Locator:* Appendix A, Item 1 (`Apply_AI_1`)[9] | *Verified Source Meaning:* Capability to operate AI applications in daily life[9].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **APPLY_02:**  „Ich kann generative KI gezielt einsetzen, um meine beruflichen Aufgaben zu bearbeiten.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `MAILS` (Carolus et al., 2023)[17][43]

*Source Locator:* Appendix A, Item 3 (`Apply_AI_3`)[9] | *Verified Source Meaning:* Capability to use AI meaningfully to achieve daily goals[9].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **APPLY_03:**  „Ich kann auftretende Schwierigkeiten beim Umgang mit generativer KI weitgehend selbstständig bewältigen.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `MAILS` (Carolus et al., 2023)[17][43]

*Source Locator:* Appendix A, Item 24 (`Problem_solving_24`)[9] | *Verified Source Meaning:* Capability to handle most problems in dealing with AI independently[9].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]

4. READINESS_CORE_DETECT – Kritische KI-Bewertungskompetenz & KI-Erkennung

*Construct Level:* `READINESS_CORE` | *Measurement Model:* `REFLECTIVE` | *Scale:* MAILS Original 0–10 Format (0 = gar nicht / kaum ausgeprägt, 10 = sehr gut / perfekt ausgeprägt)[2].

- **DETECT_01:**  „Ich kann erkennen, ob eine digitale Anwendung auf generativer KI basiert.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `MAILS` (Carolus et al., 2023)[17][43]

*Source Locator:* Appendix A, Item 13 (`Detect_AI_13`)[9] | *Verified Source Meaning:* Ability to tell if dealing with an AI application[9].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **DETECT_02:**  „Ich kann unterscheiden, ob eine Rückmeldung von einer generativen KI oder von einer Person stammt.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `MAILS` (Carolus et al., 2023)[17][43]

*Source Locator:* Appendix A, Item 15 (`Detect_AI_15`)[9] | *Verified Source Meaning:* Ability to distinguish interaction with AI versus a human[9].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **DETECT_03:**  „Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.“
*Evidence Class:* `E3_THEORY_DERIVED` | *Adaptation:* `THEORY_DERIVED` | *Source:* `MAILS` (Carolus et al., 2023)[17][43]

*Source Locator:* Section 3.1 / Appendix A ("Evaluate AI" facet)[9][21] | *Source Item ID:* `null` | *Source Definition Verified:* `true`[49]

*Substantive Sources:* `["MAILS"]`[18] | *Contrast Sources:* `["P4"]`[50]

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NOT_NEEDED`[44] | *Context Verified:* `false`[3]

5. READINESS_CORE_COMFORT – Affektiver Komfort im Umgang mit KI

*Construct Level:* `READINESS_CORE` | *Measurement Model:* `REFLECTIVE` | *Scale:* AIRS Original 1–5 Format (1 = stimme gar nicht zu, 5 = stimme voll und ganz zu)[2].

- **COMFORT_01:**  „Es ist mir nicht unangenehm, wenn bei der Nutzung von generativer KI vor anderen Personen Fehler oder Probleme auftreten.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `AIRS` (Wang et al., 2026)[51][52]

*Source Locator:* Appendix A, Item 9 (`COM1` / `Q9`)[13][53] | *Verified Source Meaning:* Absence of embarrassment when encountering AI problems in front of others[53][54].

*Measurement Object:* `HUMAN_ATTITUDE` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **COMFORT_02:**  „Ich bin überzeugt, dass die Nutzung generativer KI im Arbeitsalltag keine gesundheitlichen oder sicherheitsbezogenen Bedenken aufwirft.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `AIRS` (Wang et al., 2026)[51][52]

*Source Locator:* Appendix A, Item 8 (`COM2` / `Q8`)[13][53] | *Verified Source Meaning:* Belief that AI technologies do not raise health or safety concerns[53][55].

*Measurement Object:* `HUMAN_ATTITUDE` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **COMFORT_03:**  „Ich empfinde keine Angst oder Unbehagen bei der Interaktion mit generativen KI-Anwendungen.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `AIRS` (Wang et al., 2026)[51][52]

*Source Locator:* Appendix A, Item 18 (`COM3` / `Q18`)[8][13] | *Verified Source Meaning:* Absence of fear toward interaction with AI entities[8][55].

*Measurement Object:* `HUMAN_ATTITUDE` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]

6. CONTEXT_FC – Wahrgenommene Erleichternde Bedingungen

*Construct Level:* `CONTEXT` | *Measurement Model:* `REFLECTIVE` | *Scale:* Lambiase original 1–7 Format (1 = stimme gar nicht zu, 7 = stimme voll und ganz zu) + Zusätzliche Option „Kann ich nicht beurteilen“ (`MISSING_NOT_SCORED`)[6].

- **FC_01:**  „Mir stehen die notwendigen technischen Ressourcen für die Nutzung generativer KI zur Verfügung.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `Lambiase_et_al_2025`[57][58]

*Source Locator:* Section 4.2 (`FC_1`)[6] | *Verified Source Meaning:* Possession of necessary resources to use the technology[6][59].

*Measurement Object:* `ORG_CONTEXT` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **FC_02:**  „Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen zu nutzen.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `Lambiase_et_al_2025`[57][58]

*Source Locator:* Section 4.2 (`FC_2`)[6] | *Verified Source Meaning:* Possession of necessary knowledge to use the technology[6][59].

*Measurement Object:* `HUMAN_CAPABILITY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]
- **FC_03:**  „Generative KI-Anwendungen sind kompatibel mit den anderen digitalen Werkzeugen, die ich bei der Arbeit nutze.“
*Evidence Class:* `E2_ADAPTED` | *Adaptation:* `LINGUISTIC_AND_CONTEXTUAL` | *Source:* `Lambiase_et_al_2025`[57][58]

*Source Locator:* Section 4.2 (`FC_3`)[6] | *Verified Source Meaning:* Compatibility of the technology with other tools used[6][59].

*Measurement Object:* `SYSTEM_PROPERTY` | *Translation Status:* `NEEDS_EQUIVALENCE_CHECK`[44] | *Context Verified:* `false`[3]

DIAGNOSTIC & DEMOGRAPHIC MODULES (NON-REFLECTIVE BLOCK)

- **DIAG_01 – Schulungs- und Entwicklungsbedarfe**  (`NON_REFLECTIVE_DESCRIPTIVE`, Multi-Select)[60]:
  - In welchen Bereichen wünschen Sie sich Schulung oder Entwicklung? (Mehrfachauswahl möglich)
Grundlagen generativer KI

Prompting

kritische Ergebnisprüfung

Datenschutz / Umgang mit sensiblen Informationen

Urheberrecht / Ethik

Prozessintegration

konkrete Tool-Anwendung

*Sonstiges:* ______ (separat)

*Kein Schulungs-/Entwicklungsbedarf* (exklusiv, hebt andere Auswahlen auf)[26].
- **DIAG_02 – Allgemeiner Unterstützungsbedarf**  (`NON_REFLECTIVE_DESCRIPTIVE`, Offenes Textfeld)[24]:
„Welche zusätzliche Unterstützung würde Ihnen bei der Nutzung von generativer KI am Arbeitsplatz am meisten helfen?“
- **DEM_01 – Kaufmännischer Funktionsbereich**  (`DEMOGRAPHIC_CONTROL`, Offenes Feld / Einfügung)[24]:
„Welchem kaufmännischen Funktionsbereich ordnen Sie sich überwiegend zu?“ `[FUNKTIONSBEREICHE_DER_ORGANISATION_EINFÜGEN]`

B3 – INDEPENDENT CRITIC REVIEW (METHODOLOGICAL AUDIT)

**Audit Agent 2 Decision:**  `PASS` across all 18 reflective indicators and diagnostic modules[61][62].

- **Evaluated Gates & Verified Corrections:** 
**Atomic Item Gate:**  Item `DETECT_03` was checked for single-proposition compliance. Dual-criteria formulations combining "Richtigkeit und Plausibilität" were eliminated; the item strictly measures "inhaltliche Richtigkeit"[28][29]. `LIT_03` measures single application scope without combining limits and opportunities in one item[46].

**Construct Object Purity:**  Items under `READINESS_CORE_APPLY` were audited to ensure they measure `HUMAN_CAPABILITY`. AISES item AS6/Q16 (time-saving / system benefit) was rejected as primary evidence and excluded from APPLY[12].

**AIRS Comfort Subscale Lock:**  All items in `READINESS_CORE_COMFORT` were verified to originate strictly from the published AIRS Comfort factor (Q9, Q8, Q18). Cross-factor items (e.g., SEC4/Q16) were rejected[14].

**Lambiase FC Map & Response Lock:**  Facilitating Conditions items preserve exact mappings (FC_1 = resources, FC_2 = knowledge, FC_3 = compatibility). FC_4 (support) was excluded as a transparent subset decision and not merged into FC_3[7]. All FC items include the non-numeric response option "Kann ich nicht beurteilen"[25].

**No Unverified Privacy/Process Assurances:**  Participant text contains no fabricated promises regarding anonymity, data aggregation, or mandatory company training. Placeholder `[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]` is maintained[3][34].

B4 – SIMULATED COGNITIVE READ-THROUGH (HEURISTIC EVALUATION)

**Methodological Disclaimer:**  This section represents a simulated, heuristic cognitive walkthrough by artificial agent personas (low-experience employee vs. experienced user) to detect wording ambiguities and routing logic errors. It is an internal heuristic check and **must not be described as an empirical human pretest** [38][63].

**Persona Low AI Experience:**  The introduction clearly defines generative KI in simple office terms[64]. Filtering directly directs non-users past experience-dependent questions (APPLY, DETECT, COMFORT), preventing frustration[32][65]. The response option "Kann ich nicht beurteilen" in Part 3 (FC) allows non-users to answer contextual questions without being forced into an ungrounded opinion[25][66].

**Persona Regular User:**  Item wordings feel realistic for modern office environments (e.g., Copilot / ChatGPT Enterprise context)[40]. The 0–10 scale for capability and 1–7 scale for agreement match standard survey expectations[19]. Completion time is estimated at 5–7 minutes, well within the 8-minute respondent burden ceiling[40][67].

B5 – FULL PARTICIPANT QUESTIONNAIRE

Teil 0 – Einleitung & KI-Kontextdefinition

**Befragung zur Nutzung von generativer KI im kaufmännischen Arbeitsalltag**

Sehr geehrte Damen und Herren,

vielen Dank, dass Sie sich die Zeit nehmen, an dieser Befragung teilzunehmen. Mit dieser Befragung möchten wir erfahren, wie Sie generative KI im kaufmännischen Arbeitsalltag einschätzen und welche Unterstützungsbedarfe bestehen[64].

**Was ist generative KI?**  Unter generativer Künstlicher Intelligenz (generativer KI) verstehen wir digitale Anwendungen, die selbstständig neue Inhalte wie Texte, Analysen, Tabellen oder Darstellungen erstellen können. Beispiele hierfür sind Sprachmodelle wie ChatGPT Enterprise oder Microsoft Copilot, die bei der täglichen Büro- und Verwaltungsarbeit unterstützen können[40].

Bitte beantworten Sie die folgenden Fragen zutreffend aus Ihrer persönlichen Sicht. Es gibt keine „richtigen“ oder „falschen“ Antworten.

`[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]`[34]

Teil 1 – KI-Erfahrungs-Routing

**Filterfrage F01:**  Wie häufig nutzen Sie generative KI-Anwendungen (z. B. ChatGPT, Microsoft Copilot) in Ihrer täglichen Arbeit?[65][68]

[ ] **NO_EXPERIENCE:**  Ich habe generative KI bisher noch nie genutzt.

[ ] **LIMITED_EXPERIENCE:**  Ich habe generative KI bisher selten oder gelegentlich genutzt (z. B. wenige Male ausprobiert).

[ ] **REGULAR_USER:**  Ich nutze generative KI regelmäßig (z. B. wöchentlich oder täglich).

Teil 2 – Messmodule (READINESS_CORE)

*(Routing-Hinweis: Befragte der Gruppe***NO_EXPERIENCE** *beantworten Modul A, Modul B, Teil 3, Teil 4 und Teil 5. Die Module C, D und E werden automatisch übersprungen*[31][32]*. Befragte der Gruppen***LIMITED_EXPERIENCE** *und***REGULAR_USER** *beantworten alle Module A bis F*[31][33]*).*

Modul A: Wahrgenommenes KI-Grundverständnis (READINESS_CORE_LIT)

*Skala: 0 = gar nicht / kaum ausgeprägt bis 10 = sehr gut / perfekt ausgeprägt*[19][22]

**LIT_01:**  Ich kenne die wichtigsten Grundbegriffe zum Thema generative KI. `(Skala 0–10)`

**LIT_02:**  Ich kenne grundlegende Definitionen und Funktionsweisen generativer KI. `(Skala 0–10)`

**LIT_03:**  Ich kann die typischen Anwendungsmöglichkeiten generativer KI im kaufmännischen Alltag einschätzen. `(Skala 0–10)`

Modul B: KI-Lern-Selbstwirksamkeit (READINESS_CORE_LEARN)

*Skala: 1 = stimme gar nicht zu bis 7 = stimme voll und ganz zu*[19][22]

**LEARN_01:**  Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen funktionieren. `(Skala 1–7)`

**LEARN_02:**  Ich bin zuversichtlich, dass ich lernen kann, wie man neue generative KI-Anwendungen bei Bedarf bedient. `(Skala 1–7)`

**LEARN_03:**  Ich bin zuversichtlich, dass ich mir die Nutzung neuer generativer KI-Anwendungen eigenständig aneignen kann. `(Skala 1–7)`

Modul C: Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit (READINESS_CORE_APPLY)

*(Übersprungen für NO_EXPERIENCE)*[32] *Skala: 0 = gar nicht / kaum ausgeprägt bis 10 = sehr gut / perfekt ausgeprägt*[19][22]

**APPLY_01:**  Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag bedienen. `(Skala 0–10)`

**APPLY_02:**  Ich kann generative KI gezielt einsetzen, um meine beruflichen Aufgaben zu bearbeiten. `(Skala 0–10)`

**APPLY_03:**  Ich kann auftretende Schwierigkeiten beim Umgang mit generativer KI weitgehend selbstständig bewältigen. `(Skala 0–10)`

Modul D: Kritische KI-Bewertungskompetenz & KI-Erkennung (READINESS_CORE_DETECT)

*(Übersprungen für NO_EXPERIENCE)*[32] *Skala: 0 = gar nicht / kaum ausgeprägt bis 10 = sehr gut / perfekt ausgeprägt*[19][22]

**DETECT_01:**  Ich kann erkennen, ob eine digitale Anwendung auf generativer KI basiert. `(Skala 0–10)`

**DETECT_02:**  Ich kann unterscheiden, ob eine Rückmeldung von einer generativen KI oder von einer Person stammt. `(Skala 0–10)`

**DETECT_03:**  Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen. `(Skala 0–10)`

Modul E: Affektiver Komfort im Umgang mit KI (READINESS_CORE_COMFORT)

*(Übersprungen für NO_EXPERIENCE)*[32] *Skala: 1 = stimme gar nicht zu bis 5 = stimme voll und ganz zu*[19][22]

**COMFORT_01:**  Es ist mir nicht unangenehm, wenn bei der Nutzung von generativer KI vor anderen Personen Fehler oder Probleme auftreten. `(Skala 1–5)`

**COMFORT_02:**  Ich bin überzeugt, dass die Nutzung generativer KI im Arbeitsalltag keine gesundheitlichen oder sicherheitsbezogenen Bedenken aufwirft. `(Skala 1–5)`

**COMFORT_03:**  Ich empfinde keine Angst oder Unbehagen bei der Interaktion mit generativen KI-Anwendungen. `(Skala 1–5)`

Teil 3 – Rahmenbedingungen (CONTEXT_FC)

Modul F: Facilitating Conditions

*Skala: 1 = stimme gar nicht zu bis 7 = stimme voll und ganz zu | Zusätzliche Option: [ ] Kann ich nicht beurteilen*[6][25]

**FC_01:**  Mir stehen die notwendigen technischen Ressourcen für die Nutzung generativer KI zur Verfügung. `(Skala 1–7) [ ] Kann ich nicht beurteilen`

**FC_02:**  Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen zu nutzen. `(Skala 1–7) [ ] Kann ich nicht beurteilen`

**FC_03:**  Generative KI-Anwendungen sind kompatibel mit den anderen digitalen Werkzeugen, die ich bei der Arbeit nutze. `(Skala 1–7) [ ] Kann ich nicht beurteilen`

Teil 4 – Diagnostische Bedarfsermittlung (DIAGNOSTIC_NEEDS)

- **DIAG_01:**  In welchen der folgenden Bereiche sehen Sie für sich persönlichen Entwicklungs- oder Schulungsbedarf bezüglich generativer KI? (Mehrfachauswahl möglich)[26][60]
[ ] Grundlagen generativer KI

[ ] Prompting (gezielte Formulierung von Eingabeaufforderungen)

[ ] kritische Ergebnisprüfung

[ ] Datenschutz / Umgang mit sensiblen Informationen

[ ] Urheberrecht / Ethik

[ ] Prozessintegration (Einbindung in bestehende Arbeitsabläufe)

[ ] konkrete Tool-Anwendung (z. B. Copilot, ChatGPT)

[ ] Sonstiges: ______________________

[ ] **Kein Schulungs-/Entwicklungsbedarf**  *(exklusive Auswahl)*[26]
- **DIAG_02:**  Welche zusätzliche Unterstützung würde Ihnen bei der Nutzung von generativer KI am Arbeitsplatz am meisten helfen?[24][26]
[____________________________________________________________________]

Teil 5 – Statistische Angaben (DEMOGRAPHICS_MINIMAL)

- **DEM_01:**  Welchem kaufmännischen Funktionsbereich ordnen Sie sich überwiegend zu?[24]
`[FUNKTIONSBEREICHE_DER_ORGANISATION_EINFÜGEN]` (z. B. Einkauf, Vertrieb, Finanzen/Controlling, Personal, Logistik, Verwaltung)[24]

**Vielen Dank für Ihre Teilnahme!** [69]

B6 – VALIDATION PLAN (NON-NUMERIC FALLBACK TEMPLATE)

*Status Note:* Theoretically grounded and methodically quality-checked questionnaire draft; empirical validation in the application context is pending[70].

Because `PLANNED_ANALYSIS` = `NOT_PROVIDED`, this validation plan applies the mandatory non-numeric fallback linter rules[36][37]:

**Sample Size Determination:**  Final sample sizes cannot be specified in advance when the planned statistical estimation method is unspecified. Sample size requirements depend strictly on the selected evaluation framework (e.g., qualitative pretesting vs. quantitative factor analysis or structural equation modeling), the final number of indicators, expected effect sizes, missing data rates, and target statistical power[71].

**Human Pretesting Procedure:**  A human cognitive pretest must assess item comprehension, practical relevance, response option clarity, completion time, and routing logic across different employee experience groups prior to field launch[70].

**Psychometric Evaluation:**  Dimensionality, factor loadings, indicator reliability, internal consistency, convergent validity, and discriminant validity must be evaluated after data collection using the appropriate quantitative methodology once the research design and analysis strategy are formally established[72][73].

ITEM_ID_MANIFEST

```
LIT_01
LIT_02
LIT_03
LEARN_01
LEARN_02
LEARN_03
APPLY_01
APPLY_02
APPLY_03
DETECT_01
DETECT_02
DETECT_03
COMFORT_01
COMFORT_02
COMFORT_03
FC_01
FC_02
FC_03
```

*Phase 1 generation complete. All 18 reflective item IDs in final locked order are verified in the manifest. Ready for Phase 2 export (**PHASE_2_EXPORT_VERIFY**).*

---

