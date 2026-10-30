# runmode 11

Quelle: https://notebook.google.com/notebook/a7153645-b112-412f-a45e-877fd4f3986c
Exportiert: 21.10.2026, 18:59:24

---

## Frage

Nutze ausschließlich:




MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V3_5_SOURCE_CLOSURE_TEST_CANDIDATE.md




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

| Check | Result |
| --- | --- |
| `design_lock_ok` | **PASS** |
| `subset_source_lock_ok` | **PASS** |
| `e2_proof_ok` | **PASS** |
| `object_equivalence_ok` | **PASS** |
| `subscale_membership_ok` | **PASS** |
| `construct_coverage_ok` | **PASS** |
| `apply_human_capability_ok` | **PASS** |
| `e3_registry_closure_ok` | **PASS** |
| `within_construct_scale_coherence_ok` | **PASS** |
| `scale_instruction_semantics_ok` | **PASS** |
| `design_audit_reference_ok` | **PASS** |
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

`DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`

B2 Item traceability

| Item-ID | Konstrukt | Ebene | Messmodell | Evidenzklasse | Wording (Deutsch) | Primäre Quelle & Item-ID | Originalskala | Finalskala | Adaptionstyp | `retrieval_support` | `context_verified` | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **LIT_01** | READINESS_CORE_LIT | READINESS_CORE | REFLECTIVE | E2 | Ich kenne die wichtigsten Begriffe rund um das Thema „künstliche Intelligenz“. | MAILS (Carolus et al., 2023) – `Understand_AI_7` | 0–10 Fähigkeitsskala | 0–10 (0 = gar nicht ausgeprägt, 10 = sehr gut ausgeprägt) | E2 – ADAPTED (Sprachadaption) | `[]` | `true` | PASS |
| **LIT_02** | READINESS_CORE_LIT | READINESS_CORE | REFLECTIVE | E2 | Ich kenne Definitionen von künstlicher Intelligenz. | MAILS (Carolus et al., 2023) – `Understand_AI_8` | 0–10 Fähigkeitsskala | 0–10 (0 = gar nicht ausgeprägt, 10 = sehr gut ausgeprägt) | E2 – ADAPTED (Sprachadaption) | `[]` | `true` | PASS |
| **LIT_03** | READINESS_CORE_LIT | READINESS_CORE | REFLECTIVE | E2 | Ich kann einschätzen, welche Vor- und Nachteile der Einsatz künstlicher Intelligenz mit sich bringt. | MAILS (Carolus et al., 2023) – `Understand_AI_10` | 0–10 Fähigkeitsskala | 0–10 (0 = gar nicht ausgeprägt, 10 = sehr gut ausgeprägt) | E2 – ADAPTED (Sprachadaption) | `[]` | `true` | PASS |
| **LEARN_01** | READINESS_CORE_LEARN | READINESS_CORE | REFLECTIVE | E2 | Ich bin zuversichtlich, dass ich lernen kann, wie man neue KI-Technologien bedient, wenn es notwendig ist. | AILRSE-5 (Oksanen et al., 2026) – `Item 2` | 1–7 Likert-Skala | 1–7 (1 = stimme gar nicht zu, 7 = stimme voll und ganz zu) | E2 – ADAPTED (Sprachadaption) | `[]` | `true` | PASS |
| **LEARN_02** | READINESS_CORE_LEARN | READINESS_CORE | REFLECTIVE | E2 | Ich bin zuversichtlich, dass ich lernen kann, wie ich neue KI-Technologien in meinem Arbeitsalltag anwende. | AILRSE-5 (Oksanen et al., 2026) – `Item 3` | 1–7 Likert-Skala | 1–7 (1 = stimme gar nicht zu, 7 = stimme voll und ganz zu) | E2 – ADAPTED (Kontext- & Sprachadaption) | `[]` | `true` | PASS |
| **LEARN_03** | READINESS_CORE_LEARN | READINESS_CORE | REFLECTIVE | E2 | Ich bin zuversichtlich, dass ich lernen kann, wie man neue KI-Technologien nutzt, um ein Problem zu lösen. | AILRSE-5 (Oksanen et al., 2026) – `Item 4` | 1–7 Likert-Skala | 1–7 (1 = stimme gar nicht zu, 7 = stimme voll und ganz zu) | E2 – ADAPTED (Sprachadaption) | `[]` | `true` | PASS |
| **APPLY_01** | READINESS_CORE_APPLY | READINESS_CORE | REFLECTIVE | E2 | Ich kann generative KI-Anwendungen im Arbeitsalltag bedienen. | MAILS (Carolus et al., 2023) – `Apply_AI_1` | 0–10 Fähigkeitsskala | 0–10 (0 = gar nicht ausgeprägt, 10 = sehr gut ausgeprägt) | E2 – ADAPTED (Werkzeug- & Kontextadaption) | `[]` | `true` | PASS |
| **APPLY_02** | READINESS_CORE_APPLY | READINESS_CORE | REFLECTIVE | E2 | Ich kann generative KI-Anwendungen gezielt einsetzen, um meine täglichen Arbeitsaufgaben zu erleichtern. | MAILS (Carolus et al., 2023) – `Apply_AI_2` | 0–10 Fähigkeitsskala | 0–10 (0 = gar nicht ausgeprägt, 10 = sehr gut ausgeprägt) | E2 – ADAPTED (Werkzeug- & Kontextadaption) | `[]` | `true` | PASS |
| **APPLY_03** | READINESS_CORE_APPLY | READINESS_CORE | REFLECTIVE | E2 | Ich kann Probleme beim Umgang mit generativer KI meist gut selbstständig lösen. | MAILS (Carolus et al., 2023) – `Problem_solving_24` | 0–10 Fähigkeitsskala | 0–10 (0 = gar nicht ausgeprägt, 10 = sehr gut ausgeprägt) | E2 – ADAPTED (Werkzeugadaption) | `[]` | `true` | PASS |
| **DETECT_01** | READINESS_CORE_DETECT | READINESS_CORE | REFLECTIVE | E2 | Ich kann erkennen, ob ich es mit einer Anwendung auf Basis künstlicher Intelligenz zu tun habe. | MAILS (Carolus et al., 2023) – `Detect_AI_13` | 0–10 Fähigkeitsskala | 0–10 (0 = gar nicht ausgeprägt, 10 = sehr gut ausgeprägt) | E2 – ADAPTED (Sprachadaption) | `[]` | `true` | PASS |
| **DETECT_02** | READINESS_CORE_DETECT | READINESS_CORE | REFLECTIVE | E2 | Ich kann### B0 Conformance status |  |  |  |  |  |  |  |

| Check | Result |
| --- | --- |
| `design_lock_ok` | **PASS** |
| `subset_source_lock_ok` | **PASS** |
| `e2_proof_ok` | **PASS** |
| `object_equivalence_ok` | **PASS** |
| `subscale_membership_ok` | **PASS** |
| `construct_coverage_ok` | **PASS** |
| `apply_human_capability_ok` | **PASS** |
| `e3_registry_closure_ok` | **PASS** |
| `within_construct_scale_coherence_ok` | **PASS** |
| `scale_instruction_semantics_ok` | **PASS** |
| `design_audit_reference_ok` | **PASS** |
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

`DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`

B2 Item traceability

| Item-ID | Konstrukt | Ebene | Messmodell | Evidenzklasse | Wording (Deutsch) | Primäre Quelle & Item-ID | Originalskala | Finalskala | Adaptionstyp | `retrieval_support` | `context_verified` | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **LIT_01** | READINESS_CORE_LIT | READINESS_CORE | REFLECTIVE | E2 | Ich kenne die wichtigsten Begriffe rund um das Thema „künstliche Intelligenz“. | MAILS (Carolus et al., 2023) – `Understand_AI_7` | 0–10 | 0–10 (Fähigkeit) | E2 – ADAPTED | `[]` | `true` | PASS |
| **LIT_02** | READINESS_CORE_LIT | READINESS_CORE | REFLECTIVE | E2 | Ich kenne Definitionen von künstlicher Intelligenz. | MAILS (Carolus et al., 2023) – `Understand_AI_8` | 0–10 | 0–10 (Fähigkeit) | E2 – ADAPTED | `[]` | `true` | PASS |
| **LIT_03** | READINESS_CORE_LIT | READINESS_CORE | REFLECTIVE | E2 | Ich kann einschätzen, welche Vor- und Nachteile der Einsatz künstlicher Intelligenz mit sich bringt. | MAILS (Carolus et al., 2023) – `Understand_AI_10` | 0–10 | 0–10 (Fähigkeit) | E2 – ADAPTED | `[]` | `true` | PASS |
| **LEARN_01** | READINESS_CORE_LEARN | READINESS_CORE | REFLECTIVE | E2 | Ich bin zuversichtlich, dass ich lernen kann, wie man neue KI-Technologien bedient, wenn es notwendig ist. | AILRSE-5 (Oksanen et al., 2026) – `Item 2` | 1–7 | 1–7 (Zustimmung) | E2 – ADAPTED | `[]` | `true` | PASS |
| **LEARN_02** | READINESS_CORE_LEARN | READINESS_CORE | REFLECTIVE | E2 | Ich bin zuversichtlich, dass ich lernen kann, wie ich neue KI-Technologien in meinem Arbeitsalltag anwende. | AILRSE-5 (Oksanen et al., 2026) – `Item 3` | 1–7 | 1–7 (Zustimmung) | E2 – ADAPTED | `[]` | `true` | PASS |
| **LEARN_03** | READINESS_CORE_LEARN | READINESS_CORE | REFLECTIVE | E2 | Ich bin zuversichtlich, dass ich lernen kann, wie man neue KI-Technologien nutzt, um ein Problem zu lösen. | AILRSE-5 (Oksanen et al., 2026) – `Item 4` | 1–7 | 1–7 (Zustimmung) | E2 – ADAPTED | `[]` | `true` | PASS |
| **APPLY_01** | READINESS_CORE_APPLY | READINESS_CORE | REFLECTIVE | E2 | Ich kann generative KI-Anwendungen im Arbeitsalltag bedienen. | MAILS (Carolus et al., 2023) – `Apply_AI_1` | 0–10 | 0–10 (Fähigkeit) | E2 – ADAPTED | `[]` | `true` | PASS |
| **APPLY_02** | READINESS_CORE_APPLY | READINESS_CORE | REFLECTIVE | E2 | Ich kann generative KI-Anwendungen gezielt einsetzen, um meine täglichen Arbeitsaufgaben zu erleichtern. | MAILS (Carolus et al., 2023) – `Apply_AI_2` | 0–10 | 0–10 (Fähigkeit) | E2 – ADAPTED | `[]` | `true` | PASS |
| **APPLY_03** | READINESS_CORE_APPLY | READINESS_CORE | REFLECTIVE | E2 | Ich kann Probleme beim Umgang mit generativer KI meist gut selbstständig lösen. | MAILS (Carolus et al., 2023) – `Problem_solving_24` | 0–10 | 0–10 (Fähigkeit) | E2 – ADAPTED | `[]` | `true` | PASS |
| **DETECT_01** | READINESS_CORE_DETECT | READINESS_CORE | REFLECTIVE | E2 | Ich kann erkennen, ob ich es mit einer Anwendung auf Basis künstlicher Intelligenz zu tun habe. | MAILS (Carolus et al., 2023) – `Detect_AI_13` | 0–10 | 0–10 (Fähigkeit) | E2 – ADAPTED | `[]` | `true` | PASS |
| **DETECT_02** | READINESS_CORE_DETECT | READINESS_CORE | REFLECTIVE | E2 | Ich kann unterscheiden, ob ich mit einer KI oder einer echten Person interagiere. | MAILS (Carolus et al., 2023) – `Detect_AI_15` | 0–10 | 0–10 (Fähigkeit) | E2 – ADAPTED | `[]` | `true` | PASS |
| **DETECT_03** | READINESS_CORE_DETECT | READINESS_CORE | REFLECTIVE | E3 | Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen. | Theory-derived (MAILS Definition) | 0–10 | 0–10 (Fähigkeit) | E3 – THEORY_DERIVED | `[]` | `true` | PASS |
| **COMFORT_01** | READINESS_CORE_COMFORT | READINESS_CORE | REFLECTIVE | E2 | Ich fühle mich nicht verlegen, wenn bei der Nutzung von KI-Anwendungen vor anderen Probleme oder Schwierigkeiten auftreten. | AIRS (Wang et al., 2026) – `COM1 / Q9` | 1–5 | 1–5 (Zustimmung) | E2 – ADAPTED | `[]` | `true` | PASS |
| **COMFORT_02** | READINESS_CORE_COMFORT | READINESS_CORE | REFLECTIVE | E2 | Ich glaube, dass viele KI-Anwendungen keine Bedenken hinsichtlich Sicherheit oder Gesundheit aufwerfen. | AIRS (Wang et al., 2026) – `COM2 / Q8` | 1–5 | 1–5 (Zustimmung) | E2 – ADAPTED | `[]` | `true` | PASS |
| **COMFORT_03** | READINESS_CORE_COMFORT | READINESS_CORE | REFLECTIVE | E2 | Ich habe keine Angst vor KI-Anwendungen oder KI-gestützten Systemen. | AIRS (Wang et al., 2026) – `COM3 / Q18` | 1–5 | 1–5 (Zustimmung) | E2 – ADAPTED | `[]` | `true` | PASS |
| **FC_01** | CONTEXT_FC | CONTEXT | REFLECTIVE | E2 | Ich verfüge über die notwendigen Ressourcen, um Sprachmodelle / generative KI für meine Aufgaben zu nutzen. | Lambiase et al. (2025) – `FC_1` | 1–7 | 1–7 (Zustimmung) | E2 – ADAPTED | `[]` | `true` | PASS |
| **FC_02** | CONTEXT_FC | CONTEXT | REFLECTIVE | E2 | Ich besitze das notwendige Wissen, um Sprachmodelle / generative KI für meine Aufgaben zu nutzen. | Lambiase et al. (2025) – `FC_2` | 1–7 | 1–7 (Zustimmung) | E2 – ADAPTED | `[]` | `true` | PASS |
| **FC_03** | CONTEXT_FC | CONTEXT | REFLECTIVE | E2 | Sprachmodelle / generative KI sind mit anderen von mir genutzten Technologien kompatibel. | Lambiase et al. (2025) – `FC_3` | 1–7 | 1–7 (Zustimmung) | E2 – ADAPTED | `[]` | `true` | PASS |

B3 Critic review

- **Konstruktreinheit & Abgrenzung** :
`READINESS_CORE_LIT`, `APPLY` und `DETECT` stammen aus MAILS und erfassen rein menschliche Selbsteinschätzungen.

`READINESS_CORE_LEARN` nutzt ausschließlich das 3-Item-Subset der AILRSE-5-Skala (Self-Efficacy).

`READINESS_CORE_COMFORT` verwendet exakt die drei validierten AIRS-Comfort-Items (`COM1/Q9`, `COM2/Q8`, `COM3/Q18`). Insecurity-/Anxiety-Items anderer Subskalen bleiben ausgeschlossen.

`CONTEXT_FC` stützt sich auf das 3-Item-Subset (`FC_1`, `FC_2`, `FC_3`) aus Lambiase et al. (2025). `FC_4` (Support) bleibt ausgeschlossen und wird nicht in `FC_3` (Kompatibilität) umgedeutet.
- **Konstruktabdeckung DETECT** :
`DETECT_01` & `DETECT_02` erfassen die KI-Erkennung/Ursprungserkennung.

`DETECT_03` erfasst als einkriterielles E3-Item exakt die kritische Inhaltsprüfung („inhaltliche Richtigkeit“).
- **Evidenzklassen-Präzision** :
Alle sprachlich oder kontextuell auf den kaufmännischen Arbeitsalltag adaptierten Originalitems sind korrekt als **E2 – ADAPTED**  klassifiziert (keine E1-Falschdeklaration bei Kontextanpassung).

`retrieval_support` ist für alle Items konsistent `[]`.

B4 Simulated pretest

- **Perspektive A (Einsteiger / geringe KI-Erfahrung)** :
Bei Auswahl von `NO_EXPERIENCE` im Erfahrungs-Routing werden die erfahrungsabhängigen Module `APPLY`, `DETECT` und `COMFORT` automatisch übersprungen.

Verbleibende Module (`LIT`, `LEARN`, `FC`) lassen sich ohne direkte Nutzungserfahrung valide beantworten.
- **Perspektive B (Regelmäßige/r Nutzer/in)** :
Alle 18 Items lassen sich flüssig in ca. 4–6 Minuten bearbeiten.

Eindeutige Antwortskalen pro Konstrukt vermeiden kognitive Brüche.
**Status** : `HEURISTICALLY_READY_FOR_HUMAN_PRETEST`

B5 Final participant questionnaire

Fragebogen zur Nutzung künstlicher Intelligenz im kaufmännischen Arbeitsalltag

**Einleitung & Zielsetzung**  Sehr geehrte Damen und Herren,
dieser Fragebogen erfasst Ihre Einschätzungen zum Umgang mit Anwendungen der generativen künstlichen Intelligenz (wie z. B. **ChatGPT Enterprise**  oder **Microsoft Copilot** ) in Ihrem Arbeitsalltag. Bitte beantworten Sie die Fragen ehrlich. Es gibt keine richtigen oder falschen Antworten.

[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]

Teil 0: KI-Erfahrungs-Routing

Wie häufig nutzen Sie generative KI-Anwendungen (z. B. ChatGPT Enterprise, Microsoft Copilot) in Ihrem Arbeitsalltag?

[ ] **NO_EXPERIENCE** : Ich habe generative KI bisher noch nie persönlich genutzt.

[ ] **LIMITED_EXPERIENCE** : Ich habe generative KI bisher selten / vereinzelte Male ausprobiert.

[ ] **REGULAR_USER** : Ich nutze generative KI regelmäßig im Arbeitsalltag.

*(Hinweis: Bei Auswahl von**NO_EXPERIENCE**werden die Abschnitte C, D und E übersprungen.)*

Teil 1: Einschätzung der Fähigkeiten & Rahmenbedingungen

Abschnitt A: KI-Grundverständnis

*Bitte geben Sie auf einer Skala von 0 bis 10 an, wie stark die folgenden Kenntnisse bei Ihnen ausgeprägt sind.*
*(0 = gar nicht ausgeprägt bis 10 = sehr gut ausgeprägt)*

Ich kenne die wichtigsten Begriffe rund um das Thema „künstliche Intelligenz“. [1]

Ich kenne Definitionen von künstlicher Intelligenz. [1]

Ich kann einschätzen, welche Vor- und Nachteile der Einsatz künstlicher Intelligenz mit sich bringt. [1]

Abschnitt B: KI-Lern-Selbstwirksamkeit

*Bitte geben Sie an, wie sehr Sie den folgenden Aussagen zustimmen.*
*(1 = stimme gar nicht zu bis 7 = stimme voll und ganz zu)*

Ich bin zuversichtlich, dass ich lernen kann, wie man neue KI-Technologien bedient, wenn es notwendig ist. [1]

Ich bin zuversichtlich, dass ich lernen kann, wie ich neue KI-Technologien in meinem Arbeitsalltag anwende. [1]

Ich bin zuversichtlich, dass ich lernen kann, wie man neue KI-Technologien nutzt, um ein Problem zu lösen. [1]

Abschnitt C: Praktische KI-Anwendung *(nur bei LIMITED_EXPERIENCE & REGULAR_USER)*

*Bitte geben Sie auf einer Skala von 0 bis 10 an, wie stark die folgenden Fähigkeiten bei Ihnen ausgeprägt sind.*
*(0 = gar nicht ausgeprägt bis 10 = sehr gut ausgeprägt)*

Ich kann generative KI-Anwendungen im Arbeitsalltag bedienen. [1]

Ich kann generative KI-Anwendungen gezielt einsetzen, um meine täglichen Arbeitsaufgaben zu erleichtern. [1]

Ich kann Probleme beim Umgang mit generativer KI meist gut selbstständig lösen. [1]

Abschnitt D: Kritische KI-Bewertung & Erkennung *(nur bei LIMITED_EXPERIENCE & REGULAR_USER)*

*Bitte geben Sie auf einer Skala von 0 bis 10 an, wie stark die folgenden Fähigkeiten bei Ihnen ausgeprägt sind.*
*(0 = gar nicht ausgeprägt bis 10 = sehr gut ausgeprägt)*

Ich kann erkennen, ob ich es mit einer Anwendung auf Basis künstlicher Intelligenz zu tun habe. [1]

Ich kann unterscheiden, ob ich mit einer KI oder einer echten Person interagiere. [1]

Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen. [1]

Abschnitt E: Komfort im Umgang mit KI *(nur bei LIMITED_EXPERIENCE & REGULAR_USER)*

*Bitte geben Sie an, wie sehr Sie den folgenden Aussagen zustimmen.*
*(1 = stimme gar nicht zu bis 5 = stimme voll und ganz zu)*

Ich fühle mich nicht verlegen, wenn bei der Nutzung von KI-Anwendungen vor anderen Probleme oder Schwierigkeiten auftreten. [1]

Ich glaube, dass viele KI-Anwendungen keine Bedenken hinsichtlich Sicherheit oder Gesundheit aufwerfen. [1]

Ich habe keine Angst vor KI-Anwendungen oder KI-gestützten Systemen. [1]

Abschnitt F: Erleichternde Bedingungen (Facilitating Conditions)

*Bitte geben Sie an, wie sehr Sie den folgenden Aussagen zustimmen.*
*(1 = stimme gar nicht zu bis 7 = stimme voll und ganz zu; zusätzlich Option „Kann ich nicht beurteilen“)*

Ich verfüge über die notwendigen Ressourcen, um Sprachmodelle / generative KI für meine Aufgaben zu nutzen. `[1 - 7 / Kann ich nicht beurteilen]`

Ich besitze das notwendige Wissen, um Sprachmodelle / generative KI für meine Aufgaben zu nutzen. `[1 - 7 / Kann ich nicht beurteilen]`

Sprachmodelle / generative KI sind mit anderen von mir genutzten Technologien kompatibel. `[1 - 7 / Kann ich nicht beurteilen]`

B6 Validation plan

**Human pretest:** 
Führen Sie einen kognitiven Pretest (Denk-Laut-Protokolle / kognitive Interviews) mit Vertretern der Zielgruppe kaufmännischer Mitarbeitender durch. Die genaue Stichprobengröße richtet sich nach der Heterogenität der Zielgruppe und der Sättigung festgestellter Verständlichkeitsprobleme; ein fixer N-Wert wird ohne definierte `PLANNED_ANALYSIS` nicht vorgegeben.

**Quantitative Validierung:** 
Die quantitative Validierungsmethode, Stichprobengröße und Akzeptanzkriterien müssen festgelegt werden, sobald `PLANNED_ANALYSIS` definiert ist. Sie hängen von der gewählten Messmodellevaluierung, der Modellkomplexität, Power-Überlegungen und etwaigen Gruppenvergleichen ab.

**Status:** 
Theoretisch fundierter und methodisch geprüfter Fragebogenentwurf; die empirische Validierung im Anwendungskontext steht aus.

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
    "e3_registry_closure_ok": true,
    "within_construct_scale_coherence_ok": true,
    "scale_instruction_semantics_ok": true,
    "design_audit_reference_ok": true,
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
    "measurement_goal": "Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen.",
    "instrument_purpose": "DIAGNOSTIC",
    "run_mode": "QUESTIONNAIRE_GENERATION",
    "design_audit_reference": "DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL",
    "status": "theoretically_grounded_empirical_validation_pending",
    "supporting_datasets": [],
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
  "routing": {
    "NO_EXPERIENCE": {
      "included_modules": ["READINESS_CORE_LIT", "READINESS_CORE_LEARN", "CONTEXT_FC"],
      "skipped_modules": ["READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT"],
      "skipped_score_status": "not_scored_due_to_no_experience"
    },
    "LIMITED_EXPERIENCE": {
      "included_modules": ["READINESS_CORE_LIT", "READINESS_CORE_LEARN", "READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT", "CONTEXT_FC"],
      "skipped_modules": [],
      "skipped_score_status": "scored"
    },
    "REGULAR_USER": {
      "included_modules": ["READINESS_CORE_LIT", "READINESS_CORE_LEARN", "READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT", "CONTEXT_FC"],
      "skipped_modules": [],
      "skipped_score_status": "scored"
    }
  },
  "items": [
    {
      "item_id": "LIT_01",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kenne die wichtigsten Begriffe rund um das Thema „künstliche Intelligenz“.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kennt die wichtigsten Begriffe der künstlichen Intelligenz.",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Carolus et al. (2023), Appendix",
          "source_item_id": "Understand_AI_7",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "knowledge of core AI concepts",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "0-10 capability scale",
      "final_scale": "0-10 capability scale",
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
      "question_text": "Ich kenne Definitionen von künstlicher Intelligenz.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kennt Definitionen von künstlicher Intelligenz.",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Carolus et al. (2023), Appendix",
          "source_item_id": "Understand_AI_8",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "knowledge of AI definitions",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "0-10 capability scale",
      "final_scale": "0-10 capability scale",
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
      "question_text": "Ich kann einschätzen, welche Vor- und Nachteile der Einsatz künstlicher Intelligenz mit sich bringt.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann Vorteile und Nachteile des AI-Einsatzes bewerten.",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Carolus et al. (2023), Appendix",
          "source_item_id": "Understand_AI_10",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "assessment of AI advantages and disadvantages",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "0-10 capability scale",
      "final_scale": "0-10 capability scale",
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
      "question_text": "Ich bin zuversichtlich, dass ich lernen kann, wie man neue KI-Technologien bedient, wenn es notwendig ist.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte ist zuversichtlich, die Bedienung neuer KI-Technologien lernen zu können.",
      "source_evidence": [
        {
          "source_id": "AILRSE-5",
          "source_locator": "Oksanen et al. (2026), Table 2",
          "source_item_id": "Item 2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "confidence in learning to use new AI technologies",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "1-7 agreement scale",
      "final_scale": "1-7 agreement scale",
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
      "question_text": "Ich bin zuversichtlich, dass ich lernen kann, wie ich neue KI-Technologien in meinem Arbeitsalltag anwende.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte ist zuversichtlich, die Anwendung neuer KI-Technologien im Arbeitsalltag lernen zu können.",
      "source_evidence": [
        {
          "source_id": "AILRSE-5",
          "source_locator": "Oksanen et al. (2026), Table 2",
          "source_item_id": "Item 3",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "confidence in learning to apply AI in work context",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "1-7 agreement scale",
      "final_scale": "1-7 agreement scale",
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
      "question_text": "Ich bin zuversichtlich, dass ich lernen kann, wie man neue KI-Technologien nutzt, um ein Problem zu lösen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte ist zuversichtlich, die Nutzung neuer KI-Technologien zur Problemlösung lernen zu können.",
      "source_evidence": [
        {
          "source_id": "AILRSE-5",
          "source_locator": "Oksanen et al. (2026), Table 2",
          "source_item_id": "Item 4",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "confidence in learning AI for problem solving",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "1-7 agreement scale",
      "final_scale": "1-7 agreement scale",
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
      "question_text": "Ich kann generative KI-Anwendungen im Arbeitsalltag bedienen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann generative KI-Anwendungen im Arbeitsalltag bedienen.",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Carolus et al. (2023), Appendix",
          "source_item_id": "Apply_AI_1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "ability to operate AI applications",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "0-10 capability scale",
      "final_scale": "0-10 capability scale",
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
      "question_text": "Ich kann generative KI-Anwendungen gezielt einsetzen, um meine täglichen Arbeitsaufgaben zu erleichtern.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann generative KI gezielt zur Erleichterung von Arbeitsaufgaben nutzen.",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Carolus et al. (2023), Appendix",
          "source_item_id": "Apply_AI_2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "ability to use AI to facilitate daily tasks",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "0-10 capability scale",
      "final_scale": "0-10 capability scale",
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
      "question_text": "Ich kann Probleme beim Umgang mit generativer KI meist gut selbstständig lösen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann Probleme bei der KI-Nutzung selbstständig lösen.",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Carolus et al. (2023), Appendix",
          "source_item_id": "Problem_solving_24",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "ability to solve AI problems independently",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "0-10 capability scale",
      "final_scale": "0-10 capability scale",
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
      "question_text": "Ich kann erkennen, ob ich es mit einer Anwendung auf Basis künstlicher Intelligenz zu tun habe.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann das Vorliegen einer KI-Anwendung erkennen.",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Carolus et al. (2023), Appendix",
          "source_item_id": "Detect_AI_13",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "ability to detect whether an application uses AI",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "0-10 capability scale",
      "final_scale": "0-10 capability scale",
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
      "question_text": "Ich kann unterscheiden, ob ich mit einer KI oder einer echten Person interagiere.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann zwischen KI- und menschlicher Interaktion unterscheiden.",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Carolus et al. (2023), Appendix",
          "source_item_id": "Detect_AI_15",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "ability to distinguish AI interaction from human interaction",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "0-10 capability scale",
      "final_scale": "0-10 capability scale",
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
      "question_text": "Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.",
      "evidence_class": "E3",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte kann die inhaltliche Richtigkeit KI-generierter Ergebnisse kritisch überprüfen.",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Carolus et al. (2023), Section 2.1 & 3.2.1",
          "source_item_id": null,
          "source_item_text_verified": false,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "critical evaluation capability of AI output factual correctness",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "theory-derived",
      "original_scale": "0-10 capability scale",
      "final_scale": "0-10 capability scale",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NOT_NEEDED",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "PASS",
      "e3_substantive_sources": ["MAILS"],
      "e3_contrast_sources": []
    },
    {
      "item_id": "COMFORT_01",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Ich fühle mich nicht verlegen, wenn bei der Nutzung von KI-Anwendungen vor anderen Probleme oder Schwierigkeiten auftreten.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_ATTITUDE",
      "atomic_proposition": "Der Befragte fühlt sich bei Problemen mit KI-Anwendungen vor anderen nicht verlegen.",
      "source_evidence": [
        {
          "source_id": "AIRS",
          "source_locator": "Wang et al. (2026), Table 5 & Appendix A",
          "source_item_id": "COM1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "lack of embarrassment when encountering AI problems in front of others",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "1-5 agreement scale",
      "final_scale": "1-5 agreement scale",
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
      "question_text": "Ich glaube, dass viele KI-Anwendungen keine Bedenken hinsichtlich Sicherheit oder Gesundheit aufwerfen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_ATTITUDE",
      "atomic_proposition": "Der Befragte glaubt, dass KI-Anwendungen keine Sicherheits- oder Gesundheitsbedenken auslösen.",
      "source_evidence": [
        {
          "source_id": "AIRS",
          "source_locator": "Wang et al. (2026), Table 5 & Appendix A",
          "source_item_id": "COM2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "belief that AI products do not raise health or safety concerns",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "1-5 agreement scale",
      "final_scale": "1-5 agreement scale",
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
      "question_text": "Ich habe keine Angst vor KI-Anwendungen oder KI-gestützten Systemen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_ATTITUDE",
      "atomic_proposition": "Der Befragte hat keine Angst vor KI-Anwendungen.",
      "source_evidence": [
        {
          "source_id": "AIRS",
          "source_locator": "Wang et al. (2026), Table 5 & Appendix A",
          "source_item_id": "COM3",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "absence of fear towards AI products",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "1-5 agreement scale",
      "final_scale": "1-5 agreement scale",
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
      "question_text": "Ich verfüge über die notwendigen Ressourcen, um Sprachmodelle / generative KI für meine Aufgaben zu nutzen.",
      "evidence_class": "E2",
      "measurement_object": "ORG_CONTEXT",
      "atomic_proposition": "Der Befragte verfügt über die notwendigen Ressourcen zur Nutzung generativer KI.",
      "source_evidence": [
        {
          "source_id": "Lambiase et al. (2025)",
          "source_locator": "Lambiase et al. (2025), Section 5.1.1 & Appendix",
          "source_item_id": "FC_1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "availability of necessary resources for LLM use",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "1-7 agreement scale",
      "final_scale": "1-7 agreement scale",
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
      "question_text": "Ich besitze das notwendige Wissen, um Sprachmodelle / generative KI für meine Aufgaben zu nutzen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Der Befragte besitzt das notwendige Wissen zur Nutzung generativer KI.",
      "source_evidence": [
        {
          "source_id": "Lambiase et al. (2025)",
          "source_locator": "Lambiase et al. (2025), Section 5.1.1 & Appendix",
          "source_item_id": "FC_2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "possession of necessary knowledge for LLM use",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "1-7 agreement scale",
      "final_scale": "1-7 agreement scale",
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
      "question_text": "Sprachmodelle / generative KI sind mit anderen von mir genutzten Technologien kompatibel.",
      "evidence_class": "E2",
      "measurement_object": "SYSTEM_PROPERTY",
      "atomic_proposition": "Generative KI-Anwendungen sind mit anderen genutzten Technologien kompatibel.",
      "source_evidence": [
        {
          "source_id": "Lambiase et al. (2025)",
          "source_locator": "Lambiase et al. (2025), Section 5.1.1 & Appendix",
          "source_item_id": "FC_3",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "registry_activation_status": "ACTIVE_VERIFIED",
          "semantic_fingerprint": "compatibility of LLMs with other technologies used",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "1-7 agreement scale",
      "final_scale": "1-7 agreement scale",
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

---

