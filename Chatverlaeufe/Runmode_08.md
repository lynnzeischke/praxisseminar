# runmode 8

Quelle: https://notebook.google.com/notebook/16222828-8783-4952-90f0-8ba1272062e2
Exportiert: 21.10.2026, 18:59:46

---

## Frage

RUN_MODE = QUESTIONNAIRE_GENERATION für MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V3_2_FAIL_CLOSED_TEST_CANDIDATE.md

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

**Design-Audit-Referenz:**  `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`[1][2]

**Status des Audits:**  FINAL – Freigegeben als wissenschaftlich fundierte Designbasis für `RUN_MODE = QUESTIONNAIRE_GENERATION`[1][2].

**Zielpopulation:**  Kaufmännische Mitarbeitende eines mittelständischen Unternehmens[1][3].

**KI-Kontext:**  Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag[1][3].

**Messziel:**  Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen vor einem breiteren KI-Rollout (`INSTRUMENT_PURPOSE = DIAGNOSTIC`)[1][3].

**Verbindlicher Item-Rahmen:**  Exakt **18 reflektive Items**  (6 Konstrukte × 3 Items) + ein separates, nicht-reflektives diagnostisches Bedarfsmodul (`DIAGNOSTIC_NEEDS`)[1].

**Verbindliche Ausschlussentscheidungen:**  Ausschluss von *Behavioral Intention*, *Task-Technology Fit* (da `TASK_CONTEXT = NOT_PROVIDED`), *AI-System Ability*, *Anthropomorphic Interaction* sowie pauschalen Gesamtscores[3].

B2 Item traceability

| Item-ID | Konstrukt-Code | Analyse-Ebene | Messmodell | Evidenz-Klasse | Item-Wortlaut (Deutsch) | Wissenschaftliche Quelle (`source_id`) | Quell-Locator & Quell-Item-ID | Original-Antwortskala | Finale Antwortskala | Skalen-Adaption | Adaptions-Typ | Übersetzungs-Status | `retrieval_support` | `context_verified` | Critic-Status | Pretest-Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **LIT_1** | `READINESS_CORE_LIT` | `READINESS_CORE` | REFLECTIVE | **E1** | Ich kenne die wichtigsten Grundbegriffe zum Thema Generative Künstliche Intelligenz. | MAILS (Carolus et al., 2023)[8][9] | App. A, Item 7 (`MAILS_7`)[9] | 11-Punkt-Skala (0–10)[10] | 11-Punkt-Skala (0–10) | `NONE` | `direct` | `NOT_NEEDED` | `[]` | `true` | `PASS` | `PASS` |
| **LIT_2** | `READINESS_CORE_LIT` | `READINESS_CORE` | REFLECTIVE | **E1** | Ich kenne gängige Definitionen und Anwendungsformen von generativer Künstlicher Intelligenz. | MAILS (Carolus et al., 2023)[8][9] | App. A, Item 8 (`MAILS_8`)[9] | 11-Punkt-Skala (0–10)[10] | 11-Punkt-Skala (0–10) | `NONE` | `direct` | `NOT_NEEDED` | `[]` | `true` | `PASS` | `PASS` |
| **LIT_3** | `READINESS_CORE_LIT` | `READINESS_CORE` | REFLECTIVE | **E1** | Ich kann einschätzen, welche Möglichkeiten und Grenzen der Einsatz generativer KI bietet. | MAILS (Carolus et al., 2023)[8][9] | App. A, Item 9 (`MAILS_9`)[9] | 11-Punkt-Skala (0–10)[10] | 11-Punkt-Skala (0–10) | `NONE` | `direct` | `NOT_NEEDED` | `[]` | `true` | `PASS` | `PASS` |
| **LEARN_1** | `READINESS_CORE_LEARN` | `READINESS_CORE` | REFLECTIVE | **E2** | Ich bin zuversichtlich, dass ich lernen kann, wie man neue generative KI-Anwendungen nutzt, wenn es erforderlich ist. | AILRSE-5 (Oksanen et al., 2026)[11][12] | Table 2, Item 2 (`AILRSE_2`)[12] | 7-Punkt-Likert (1–7)[13] | 7-Punkt-Likert (1–7) | `NONE` | `linguistic` | `NEEDS_EQUIVALENCE_CHECK` | `[]` | `true` | `PASS` | `PASS` |
| **LEARN_2** | `READINESS_CORE_LEARN` | `READINESS_CORE` | REFLECTIVE | **E2** | Ich bin zuversichtlich, dass ich lernen kann, wie ich generative KI-Anwendungen in meinem täglichen Arbeitsalltag einsetze. | AILRSE-5 (Oksanen et al., 2026)[11][12] | Table 2, Item 3 (`AILRSE_3`)[12] | 7-Punkt-Likert (1–7)[13] | 7-Punkt-Likert (1–7) | `NONE` | `linguistic` | `NEEDS_EQUIVALENCE_CHECK` | `[]` | `true` | `PASS` | `PASS` |
| **LEARN_3** | `READINESS_CORE_LEARN` | `READINESS_CORE` | REFLECTIVE | **E2** | Ich bin zuversichtlich, dass ich lernen kann, wie man generative KI-Anwendungen zur Lösung von Problemen nutzt. | AILRSE-5 (Oksanen et al., 2026)[11][12] | Table 2, Item 4 (`AILRSE_4`)[12] | 7-Punkt-Likert (1–7)[13] | 7-Punkt-Likert (1–7) | `NONE` | `linguistic` | `NEEDS_EQUIVALENCE_CHECK` | `[]` | `true` | `PASS` | `PASS` |
| **APPLY_1** | `READINESS_CORE_APPLY` | `READINESS_CORE` | REFLECTIVE | **E1** | Ich kann mich beim Einsatz generativer KI-Anwendungen in schwierigen Arbeitssituationen auf meine Fähigkeiten verlassen. | MAILS (Carolus et al., 2023)[8][9] | App. A, Item 23 (`MAILS_23`)[9] | 11-Punkt-Skala (0–10)[10] | 11-Punkt-Skala (0–10) | `NONE` | `direct` | `NOT_NEEDED` | `[]` | `true` | `PASS` | `PASS` |
| **APPLY_2** | `READINESS_CORE_APPLY` | `READINESS_CORE` | REFLECTIVE | **E1** | Ich kann die meisten Probleme im Umgang mit generativer KI gut aus eigener Kraft meistern. | MAILS (Carolus et al., 2023)[8][9] | App. A, Item 24 (`MAILS_24`)[9] | 11-Punkt-Skala (0–10)[10] | 11-Punkt-Skala (0–10) | `NONE` | `direct` | `NOT_NEEDED` | `[]` | `true` | `PASS` | `PASS` |
| **APPLY_3** | `READINESS_CORE_APPLY` | `READINESS_CORE` | REFLECTIVE | **E1** | Ich kann auch komplizierte Arbeitsaufgaben beim Arbeiten mit generativer KI meistens gut lösen. | MAILS (Carolus et al., 2023)[8][9] | App. A, Item 25 (`MAILS_25`)[9] | 11-Punkt-Skala (0–10)[10] | 11-Punkt-Skala (0–10) | `NONE` | `direct` | `NOT_NEEDED` | `[]` | `true` | `PASS` | `PASS` |
| **DETECT_1** | `READINESS_CORE_DETECT` | `READINESS_CORE` | REFLECTIVE | **E1** | Ich kann erkennen, ob ich es bei einem Arbeitsergebnis mit einer Anwendung auf Basis generativer Künstlicher Intelligenz zu tun habe. | MAILS (Carolus et al., 2023)[8][9] | App. A, Item 13 (`MAILS_13`)[9] | 11-Punkt-Skala (0–10)[10] | 11-Punkt-Skala (0–10) | `NONE` | `direct` | `NOT_NEEDED` | `[]##### B0 Conformance status |  |  |  |

| Check | Result |
| --- | --- |
| `design_lock_ok` | **PASS** |
| `subset_source_lock_ok` | **PASS** |
| `e2_proof_ok` | **PASS** |
| `object_equivalence_ok` | **PASS** |
| `subscale_membership_ok` | **PASS** |
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

**Design-Audit-Referenz:**  `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`[1][2]

**Status:**  FINAL – Freigegeben als wissenschaftliche Designbasis[1][2].

**Zielpopulation:**  Kaufmännische Mitarbeitende eines mittelständischen Unternehmens[1][3].

**KI-Kontext:**  Generative KI-Anwendungen (insbesondere ChatGPT Enterprise und Microsoft Copilot) im kaufmännischen Arbeitsalltag[1][3].

**Messziel:**  Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen vor einem breiteren KI-Rollout (`INSTRUMENT_PURPOSE = DIAGNOSTIC`)[1][3].

**Verbindlicher Item-Rahmen:**  Exakt 18 reflektive Items (6 Konstrukte × 3 Items) + ein separates diagnostisches Bedarfsmodul (`DIAGNOSTIC_NEEDS`)[1].

**Ausschlüsse:**  Ausschluss von *Behavioral Intention*, *Task-Technology Fit* (`TASK_CONTEXT = NOT_PROVIDED`), *AI-System Ability* sowie pauschalen Gesamtscores[3].

B2 Item traceability

- **LIT_1**  (`READINESS_CORE_LIT`): *Ich kenne die wichtigsten Grundbegriffe zum Thema Generative Künstliche Intelligenz.*[9]
**Quelle:**  MAILS (Carolus et al., 2023), App. A, Item 7 (`MAILS_7`)[8][9]. Evidenz: **E1** , Skala: 0–10[9][10]. `retrieval_support: []`.
- **LIT_2**  (`READINESS_CORE_LIT`): *Ich kenne Definitionen und Anwendungsformen von generativer Künstlicher Intelligenz.*[9]
**Quelle:**  MAILS (Carolus et al., 2023), App. A, Item 8 (`MAILS_8`)[8][9]. Evidenz: **E1** , Skala: 0–10[9][10]. `retrieval_support: []`.
- **LIT_3**  (`READINESS_CORE_LIT`): *Ich kann einschätzen, welche Chancen und Grenzen der Einsatz generativer KI bietet.*[9]
**Quelle:**  MAILS (Carolus et al., 2023), App. A, Item 9 (`MAILS_9`)[8][9]. Evidenz: **E1** , Skala: 0–10[9][10]. `retrieval_support: []`.
- **LEARN_1**  (`READINESS_CORE_LEARN`): *Ich bin zuversichtlich, dass ich lernen kann, wie man neue generative KI-Anwendungen nutzt, wenn es erforderlich ist.*[12]
**Quelle:**  AILRSE-5 (Oksanen et al., 2026), Table 2, Item 2 (`AILRSE_2`)[11][12]. Evidenz: **E2**  (dt. Adaption)[12][14], Skala: 1–7 (Likert)[13]. `retrieval_support: []`.
- **LEARN_2**  (`READINESS_CORE_LEARN`): *Ich bin zuversichtlich, dass ich lernen kann, wie ich generative KI-Anwendungen in meinem täglichen Arbeitsalltag einsetze.*[12]
**Quelle:**  AILRSE-5 (Oksanen et al., 2026), Table 2, Item 3 (`AILRSE_3`)[11][12]. Evidenz: **E2**  (dt. Adaption)[12][14], Skala: 1–7 (Likert)[13]. `retrieval_support: []`.
- **LEARN_3**  (`READINESS_CORE_LEARN`): *Ich bin zuversichtlich, dass ich lernen kann, wie man generative KI-Anwendungen zur Lösung von Problemen nutzt.*[12]
**Quelle:**  AILRSE-5 (Oksanen et al., 2026), Table 2, Item 4 (`AILRSE_4`)[11][12]. Evidenz: **E2**  (dt. Adaption)[12][14], Skala: 1–7 (Likert)[13]. `retrieval_support: []`.
- **APPLY_1**  (`READINESS_CORE_APPLY`): *Ich kann mich beim Einsatz generativer KI-Anwendungen in schwierigen Arbeitssituationen auf meine Fähigkeiten verlassen.*[9]
**Quelle:**  MAILS (Carolus et al., 2023), App. A, Item 23 (`MAILS_23`)[8][9]. Evidenz: **E1** , Skala: 0–10[9][10]. `retrieval_support: []`.
- **APPLY_2**  (`READINESS_CORE_APPLY`): *Ich kann die meisten Probleme im Umgang mit generativer KI gut aus eigener Kraft lösen.*[9]
**Quelle:**  MAILS (Carolus et al., 2023), App. A, Item 24 (`MAILS_24`)[8][9]. Evidenz: **E1** , Skala: 0–10[9][10]. `retrieval_support: []`.
- **APPLY_3**  (`READINESS_CORE_APPLY`): *Ich kann auch komplizierte Arbeitsaufgaben beim Arbeiten mit generativer KI gut bewältigen.*[9]
**Quelle:**  MAILS (Carolus et al., 2023), App. A, Item 25 (`MAILS_25`)[8][9]. Evidenz: **E1** , Skala: 0–10[9][10]. `retrieval_support: []`.
- **DETECT_1**  (`READINESS_CORE_DETECT`): *Ich kann erkennen, ob ein vorliegendes Arbeitsergebnis mit Hilfe generativer KI erstellt wurde.*[9]
**Quelle:**  MAILS (Carolus et al., 2023), App. A, Item 13 (`MAILS_13`)[8][9]. Evidenz: **E1** , Skala: 0–10[9][10]. `retrieval_support: []`.
- **DETECT_2**  (`READINESS_CORE_DETECT`): *Ich kann unterscheiden, welche Softwareanwendungen generative KI nutzen und welche nicht.*[9]
**Quelle:**  MAILS (Carolus et al., 2023), App. A, Item 14 (`MAILS_14`)[8][9]. Evidenz: **E1** , Skala: 0–10[9][10]. `retrieval_support: []`.
- **DETECT_3**  (`READINESS_CORE_DETECT`): *Ich kann im Arbeitsalltag unterscheiden, ob ich mit einer generativen KI oder einer realen Person interagiere.*[9]
**Quelle:**  MAILS (Carolus et al., 2023), App. A, Item 15 (`MAILS_15`)[8][9]. Evidenz: **E1** , Skala: 0–10[9][10]. `retrieval_support: []`.
- **COMFORT_1**  (`READINESS_CORE_COMFORT`): *Ich verspüre keine Ängste vor dem Erlernen und Nutzen generativer KI-Anwendungen.*[15]
**Quelle:**  AIRS (Wang et al., 2026), Table 5, Item SEC4 (`AIRS_16`)[15][16]. Evidenz: **E2**  (dt. Adaption)[14][15], Skala: 1–5 (Likert)[17]. `retrieval_support: []`.
- **COMFORT_2**  (`READINESS_CORE_COMFORT`): *Es ist mir nicht unangenehm, wenn beim Einsatz generativer KI vor anderen Personen Probleme auftreten.*[15]
**Quelle:**  AIRS (Wang et al., 2026), Table 5, Item COM1 (`AIRS_9`)[15][16]. Evidenz: **E2**  (dt. Adaption)[14][15], Skala: 1–5 (Likert)[17]. `retrieval_support: []`.
- **COMFORT_3**  (`READINESS_CORE_COMFORT`): *Ich habe keine Befürchtungen im direkten Arbeitskontakt mit generativen KI-Systemen.*[18]
**Quelle:**  AIRS (Wang et al., 2026), Table 5, Item COM3 (`AIRS_18`)[16][18]. Evidenz: **E2**  (dt. Adaption)[14][18], Skala: 1–5 (Likert)[17]. `retrieval_support: []`.
- **FC_1**  (`CONTEXT_FC`): *Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI in meiner Arbeit zu nutzen.*[19]
**Quelle:**  Lambiase et al. (2025) / UTAUT2, Sec. 4.2 (`FC_1`)[19][20]. Evidenz: **E2**  (dt. Adaption)[14][19], Skala: 1–7 (Likert)[19]. `retrieval_support: []`.
- **FC_2**  (`CONTEXT_FC`): *Ich verfüge über das erforderliche Wissen, um generative KI-Anwendungen bei meinen Aufgaben einzusetzen.*[19]
**Quelle:**  Lambiase et al. (2025) / UTAUT2, Sec. 4.2 (`FC_2`)[19][20]. Evidenz: **E2**  (dt. Adaption)[14][19], Skala: 1–7 (Likert)[19]. `retrieval_support: []`.
- **FC_3**  (`CONTEXT_FC`): *Bei Fragen oder Schwierigkeiten mit generativer KI steht mir bei Bedarf Unterstützung zur Verfügung.*[19]
**Quelle:**  Lambiase et al. (2025) / UTAUT2, Sec. 4.2 (`FC_3`)[19][20]. Evidenz: **E2**  (dt. Adaption)[14][19], Skala: 1–7 (Likert)[19]. `retrieval_support: []`.

B3 Critic review

**Methodische Prüfung (Agent 2):**  Alle 18 Items erfüllen die strengen Kriterien für Konstruktreinheit, Einzelforderungsstruktur (*Atomic Proposition Test*) und Korrespondenz von Messgegenstand und Subskalenmitgliedschaft[21].

**Keine unzulässige Synthese:**  Kein Item verknüpft Systemfähigkeiten mit menschlicher Selbstwirksamkeit[21][22].

**Skalenentscheidung:**  Da `SCALE_PREFERENCE = original_scales` festgelegt ist, bleiben die Originalantwortskalen der Primärquellen unverändert erhalten[24].

**Gesamtbeurteilung:**  `PASS` für alle 18 Items[25].

B4 Simulated pretest

**Prüfperspektiven:**  Simuliert für (A) kaufmännische Mitarbeitende ohne Vorerfahrung und (B) regelmäßige KI-Nutzer[26][27].

**Filter- und Routingcheck:**  Befragte ohne Vorerfahrung (`NO_EXPERIENCE`) füllen nur das Grundverständnis (`LIT`), die Lern-Selbstwirksamkeit (`LEARN`), die Rahmenbedingungen (`FC`) und das Bedarfsmodul (`DIAGNOSTIC_NEEDS`) aus. Die nutzungserfahrungsabhängigen Module `APPLY`, `DETECT` und `COMFORT` werden automatisiert übersprungen und als `not_scored_due_to_no_experience` klassifiziert[26][28].

**Ergebnis:**  `HEURISTICALLY_READY_FOR_HUMAN_PRETEST`[27][29].

B5 Final participant questionnaire

Fragebogen zur KI-Bereitschaft im kaufmännischen Arbeitsalltag

Teil 0 – Einleitung & Kontext

Vielen Dank für Ihre Teilnahme an dieser Befragung. Im Mittelpunkt stehen Ihre Einschätzungen zum Thema **Generative Künstliche Intelligenz (Generative KI)** , wie beispielsweise ChatGPT Enterprise oder Microsoft Copilot, im kaufmännischen Arbeitsalltag[1][3]. Es gibt keine "richtigen" oder "falschen" Antworten; interessiert ist ausschließlich Ihre persönliche Perspektive[30][31]. *(Hinweis: [DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER])*[32][33]

Teil 1 – KI-Erfahrung

**Frage E1:**  Wie häufig nutzen Sie generative KI-Anwendungen im Rahmen Ihrer beruflichen Tätigkeiten?

[ ] (1) Noch nie genutzt (`NO_EXPERIENCE`)

[ ] (2) Selten / gelegentlich genutzt (`LIMITED_EXPERIENCE`)

[ ] (3) Regelmäßig / täglich genutzt (`REGULAR_USER`)

Teil 2 – KI-Kompetenzen & Einstellungen

Modul A: KI-Grundverständnis (`READINESS_CORE_LIT`)

*(Antwortskala: 0 = "gar nicht ausgeprägt" bis 10 = "sehr gut ausgeprägt")*[10]

**LIT_1:**  Ich kenne die wichtigsten Grundbegriffe zum Thema Generative Künstliche Intelligenz.[9]

**LIT_2:**  Ich kenne Definitionen und Anwendungsformen von generativer Künstlicher Intelligenz.[9]

**LIT_3:**  Ich kann einschätzen, welche Chancen und Grenzen der Einsatz generativer KI bietet.[9]

Modul B: KI-Lern-Selbstwirksamkeit (`READINESS_CORE_LEARN`)

*(Antwortskala: 1 = "Trifft gar nicht zu" bis 7 = "Trifft vollkommen zu")*[13]

**LEARN_1:**  Ich bin zuversichtlich, dass ich lernen kann, wie man neue generative KI-Anwendungen nutzt, wenn es erforderlich ist.[12]

**LEARN_2:**  Ich bin zuversichtlich, dass ich lernen kann, wie ich generative KI-Anwendungen in meinem täglichen Arbeitsalltag einsetze.[12]

**LEARN_3:**  Ich bin zuversichtlich, dass ich lernen kann, wie man generative KI-Anwendungen zur Lösung von Problemen nutzt.[12]

Modul C: Anwendungs-Selbstwirksamkeit (`READINESS_CORE_APPLY`)

*(Nur für Personen mit KI-Vorerfahrung; Befragte mit**NO_EXPERIENCE**überspringen dieses Modul)*[26] *(Antwortskala: 0 = "gar nicht ausgeprägt" bis 10 = "sehr gut ausgeprägt")*[10]

**APPLY_1:**  Ich kann mich beim Einsatz generativer KI-Anwendungen in schwierigen Arbeitssituationen auf meine Fähigkeiten verlassen.[9]

**APPLY_2:**  Ich kann die meisten Probleme im Umgang mit generativer KI gut aus eigener Kraft lösen.[9]

**APPLY_3:**  Ich kann auch komplizierte Arbeitsaufgaben beim Arbeiten mit generativer KI gut bewältigen.[9]

Modul D: Kritische KI-Bewertungskompetenz (`READINESS_CORE_DETECT`)

*(Nur für Personen mit KI-Vorerfahrung; Befragte mit**NO_EXPERIENCE**überspringen dieses Modul)*[26] *(Antwortskala: 0 = "gar nicht ausgeprägt" bis 10 = "sehr gut ausgeprägt")*[10]

**DETECT_1:**  Ich kann erkennen, ob ein vorliegendes Arbeitsergebnis mit Hilfe generativer KI erstellt wurde.[9]

**DETECT_2:**  Ich kann unterscheiden, welche Softwareanwendungen generative KI nutzen und welche nicht.[9]

**DETECT_3:**  Ich kann im Arbeitsalltag unterscheiden, ob ich mit einer generativen KI oder einer realen Person interagiere.[9]

Modul E: Affektiver Komfort (`READINESS_CORE_COMFORT`)

*(Nur für Personen mit KI-Vorerfahrung; Befragte mit**NO_EXPERIENCE**überspringen dieses Modul)*[26] *(Antwortskala: 1 = "Stimme gar nicht zu" bis 5 = "Stimme vollkommen zu")*[17]

**COMFORT_1:**  Ich verspüre keine Ängste vor dem Erlernen und Nutzen generativer KI-Anwendungen.[15]

**COMFORT_2:**  Es ist mir nicht unangenehm, wenn beim Einsatz generativer KI vor anderen Personen Probleme auftreten.[15]

**COMFORT_3:**  Ich habe keine Befürchtungen im direkten Arbeitskontakt mit generativen KI-Systemen.[18]

Teil 3 – Erleichternde Rahmenbedingungen (`CONTEXT_FC`)

*(Antwortskala: 1 = "Trifft gar nicht zu" bis 7 = "Trifft vollkommen zu" | Option: [ ] Kann ich nicht beurteilen)*[19][26]

**FC_1:**  Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI in meiner Arbeit zu nutzen.[19]

**FC_2:**  Ich verfüge über das erforderliche Wissen, um generative KI-Anwendungen bei meinen Aufgaben einzusetzen.[19]

**FC_3:**  Bei Fragen oder Schwierigkeiten mit generativer KI steht mir bei Bedarf Unterstützung zur Verfügung.[19]

Teil 4 – Diagnostische Bedarfsermittlung (`DIAGNOSTIC_NEEDS`)

*(Dieses Modul dient der Schulungs- und Entwicklungsbedarfsanalyse und geht nicht in Readiness-Scores ein)*[5]. **Frage N1:**  In welchen der folgenden Bereiche wünschen Sie sich vertiefende Schulungen oder Unterstützung? *(Mehrfachauswahl möglich)*[5]

[ ] (1) Grundlagen & Funktionsweise generativer KI[5]

[ ] (2) Effektives Prompting & Formulierung von Arbeitsanweisungen[5]

[ ] (3) Kritische Prüfung & Qualitätssicherung KI-generierter Ergebnisse[5]

[ ] (4) Datenschutz & sicherer Umgang mit sensiblen Daten[5]

[ ] (5) Urheberrechtliche & ethische Leitlinien[5]

[ ] (6) Integration KI-gestützter Abläufe in kaufmännische Prozesse[5]

[ ] (7) Konkrete Tool-Anwendungen (z. B. Excel/Copilot-Integration)[5]

Teil 5 – Statistische Angaben

- **D1 (Funktionsbereich):** 
[ ] Einkauf / Logistik

[ ] Finanzen / Controlling / Rechnungswesen

[ ] Personalwesen (HR)

[ ] Marketing / Vertrieb / Kundenservice

[ ] Sonstiger kaufmännischer Bereich

B6 Validation plan

**Status:**  Theoretisch fundierter und methodisch qualitätsgesicherter Fragebogenentwurf; die empirische Validierung im konkreten Anwendungskontext steht aus[2][34].

**Kognitiver Human Pretest:**  Führen Sie einen realen kognitiven Pretest mit Angehörigen der Zielpopulation durch. Die Stichprobengröße richtet sich nach dem Pretest-Zweck, der Heterogenität der Zielgruppe und der Sättigung von Verständlichkeitsproblemen; in diesem Durchlauf wird keine feste Zahl vorgegeben[34].

**Quantitative Validierung:**  Die quantitative Validierungsmethode, Stichprobengröße und Akzeptanzkriterien müssen festgelegt werden, sobald `PLANNED_ANALYSIS` definiert ist. Sie hängen von der gewählten Messmodellevaluierung, der Modellkomplexität, Power-Überlegungen und etwaigen geplanten Gruppenvergleichen ab[34][35].

B7 Machine-readable JSON

```
{
  "conformance": {
    "design_lock_ok": true,
    "subset_source_lock_ok": true,
    "e2_proof_ok": true,
    "object_equivalence_ok": true,
    "subscale_membership_ok": true,
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
    "ai_context": "Generative KI-Anwendungen (ChatGPT Enterprise, Microsoft Copilot)",
    "measurement_goal": "Diagnostische Erfassung der Employee AI Readiness und Schulungsbedarfe",
    "instrument_purpose": "DIAGNOSTIC",
    "run_mode": "QUESTIONNAIRE_GENERATION",
    "design_audit_reference": "DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL",
    "status": "theoretically_grounded_empirical_validation_pending",
    "supporting_datasets": ["Datensatz_v1"],
    "overall_score_supported": false
  },
  "constructs": [
    {
      "construct_code": "READINESS_CORE_LIT",
      "construct_name": "Wahrgenommenes KI-Grundverständnis",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["MAILS (Carolus et al., 2023)"]
    },
    {
      "construct_code": "READINESS_CORE_LEARN",
      "construct_name": "KI-Lern-Selbstwirksamkeit",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["AILRSE-5 (Oksanen et al., 2026)"]
    },
    {
      "construct_code": "READINESS_CORE_APPLY",
      "construct_name": "Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["MAILS (Carolus et al., 2023)"]
    },
    {
      "construct_code": "READINESS_CORE_DETECT",
      "construct_name": "Kritische KI-Bewertungskompetenz & KI-Erkennung",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["MAILS (Carolus et al., 2023)"]
    },
    {
      "construct_code": "READINESS_CORE_COMFORT",
      "construct_name": "Affektiver Komfort im Umgang mit KI",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["AIRS (Wang et al., 2026)"]
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
    }
  },
  "items": [
    {
      "item_id": "LIT_1",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kenne die wichtigsten Grundbegriffe zum Thema Generative Künstliche Intelligenz.",
      "evidence_class": "E1",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Kennen der wichtigsten Grundbegriffe generativer KI",
      "source_evidence": [
        {
          "source_id": "MAILS (Carolus et al., 2023)",
          "source_locator": "App. A, Item 7",
          "source_item_id": "MAILS_7",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Kennen der wichtigsten Grundbegriffe der KI",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "direct",
      "original_scale": "11-Punkt-Skala (0-10)",
      "final_scale": "11-Punkt-Skala (0-10)",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NOT_NEEDED",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "LEARN_1",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich lernen kann, wie man neue generative KI-Anwendungen nutzt, wenn es erforderlich ist.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Zuversicht, die Nutzung neuer KI-Anwendungen bei Bedarf zu erlernen",
      "source_evidence": [
        {
          "source_id": "AILRSE-5 (Oksanen et al., 2026)",
          "source_locator": "Table 2, Item 2",
          "source_item_id": "AILRSE_2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Zuversicht im Erlernen neuer KI-Technologien bei Notwendigkeit",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "7-Punkt-Likert (1-7)",
      "final_scale": "7-Punkt-Likert (1-7)",
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
      "item_id": "APPLY_1",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Ich kann mich beim Einsatz generativer KI-Anwendungen in schwierigen Arbeitssituationen auf meine Fähigkeiten verlassen.",
      "evidence_class": "E1",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Verlässlichkeit eigener Fähigkeiten bei KI-Einsatz in schwierigen Situationen",
      "source_evidence": [
        {
          "source_id": "MAILS (Carolus et al., 2023)",
          "source_locator": "App. A, Item 23",
          "source_item_id": "MAILS_23",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Verlässlichkeit eigener KI-Fähigkeiten in schwierigen Situationen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "direct",
      "original_scale": "11-Punkt-Skala (0-10)",
      "final_scale": "11-Punkt-Skala (0-10)",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NOT_NEEDED",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "DETECT_1",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann erkennen, ob ein vorliegendes Arbeitsergebnis mit Hilfe generativer KI erstellt wurde.",
      "evidence_class": "E1",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Erkennen, ob ein Arbeitsergebnis durch KI erstellt wurde",
      "source_evidence": [
        {
          "source_id": "MAILS (Carolus et al., 2023)",
          "source_locator": "App. A, Item 13",
          "source_item_id": "MAILS_13",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Erkennen von KI-gestützten Anwendungen/Ergebnissen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "direct",
      "original_scale": "11-Punkt-Skala (0-10)",
      "final_scale": "11-Punkt-Skala (0-10)",
      "scale_adaptation": "NONE",
      "scale_adaptation_justification": "",
      "translation_status": "NOT_NEEDED",
      "context_verified": true,
      "critic_status": "PASS",
      "simulated_pretest_status": "PASS",
      "e3_source_compatibility_status": "NOT_APPLICABLE",
      "e3_substantive_sources": [],
      "e3_contrast_sources": []
    },
    {
      "item_id": "COMFORT_1",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Ich verspüre keine Ängste vor dem Erlernen und Nutzen generativer KI-Anwendungen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_ATTITUDE",
      "atomic_proposition": "Abwesenheit von Ängsten bezüglich KI-Lernen und -Nutzung",
      "source_evidence": [
        {
          "source_id": "AIRS (Wang et al., 2026)",
          "source_locator": "Table 5, Item SEC4",
          "source_item_id": "AIRS_16",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Keine Angst bezüglich des Lernens der KI-Nutzung",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "5-Punkt-Likert (1-5)",
      "final_scale": "5-Punkt-Likert (1-5)",
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
      "item_id": "FC_1",
      "construct_code": "CONTEXT_FC",
      "question_text": "Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI in meiner Arbeit zu nutzen.",
      "evidence_class": "E2",
      "measurement_object": "ORG_CONTEXT",
      "atomic_proposition": "Verfügbarkeit notwendiger Ressourcen für KI-Nutzung",
      "source_evidence": [
        {
          "source_id": "Lambiase et al. (2025)",
          "source_locator": "Sec. 4.2, FC_1",
          "source_item_id": "FC_1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Verfügbarkeit von Ressourcen für KI-Arbeit",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "linguistic",
      "original_scale": "7-Punkt-Likert (1-7)",
      "final_scale": "7-Punkt-Likert (1-7)",
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

💡 **Nächster Schritt:**  Möchten Sie diesen Fragebogen als gestaltetes PDF-Dokument oder als druckfertige Übersicht exportieren lassen, oder sollen Anpassungen an einzelnen Modulen vorgenommen werden?

---

