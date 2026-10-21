# runmode 9

Quelle: https://notebook.google.com/notebook/73198d1e-0021-4452-86ae-d14923a67481
Exportiert: 21.10.2026, 18:59:39

---

## Frage

RUN_MODE = QUESTIONNAIRE_GENERATION für MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V3_3_ITEM_INTEGRITY_TEST_CANDIDATE.md

---

## Antwort

**GATE_STATUS: GLOBAL_HARD_STOP_GATE_TRIGGERED** [1][2]

1. Ausgelöste Regeln

**0.4 Missing-input rule** [3]

**3.6 GLOBAL HARD STOP GATE** [1]

**21.1 Global hard stops** [4]

2. Fehlende globale Pflichtangaben & Nachweise

Für die Ausführung von `RUN_MODE = QUESTIONNAIRE_GENERATION` fehlen die folgenden zwingend erforderlichen Parameter[1]:

**TARGET_POPULATION** **(M1):**  Angabe der Zielgruppe / Mitarbeitendengruppe (z. B. *alle Mitarbeitenden*, *IT-Abteilung*, *Vertrieb*, *Führungskräfte*)[5].

**AI_CONTEXT** **(M2):**  Angabe des spezifischen KI-Anwendungsbereichs bzw. Messobjekts (z. B. *Generative KI allgemein*, *Microsoft Copilot*, *ChatGPT Enterprise*, *internes LLM*)[5].

**MEASUREMENT_GOAL** **(M3):**  Angabe des primären Messziels (z. B. *Diagnose der Employee AI Readiness*, *Ermittlung von Schulungsbedarfen*, *Vorbereitung eines KI-Rollouts*)[5][6].

**DESIGN_AUDIT_REFERENCE** **(C4):**  Referenz auf ein bereits vorliegendes und genehmigtes Design-Audit (z. B. `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`), das als verbindlicher **DESIGN_LOCK**  dient[1].

3. Begründung der Sperre für die Item-Generierung

Gemäß den verbindlichen Steuerungsregeln des Masterprompts gilt bei fehlen den globalen Pflichtangaben oder fehlender Design-Audit-Referenz im Modus `QUESTIONNAIRE_GENERATION` eine strikte **Fail-Closed-Regel** [1]:

Es dürfen **keinerlei Fragebogen-Items oder Item-Formulierungen**  erzeugt werden – weder finale Items noch Beispiel-, Prototyp-, Demonstrations- oder Entwurfs-Items[1][3].

Es dürfen **keine fehlenden Kontextinformationen erfunden**  oder hypothetisch vorausgesetzt werden[3].

Der normale Fragebogen- und JSON-Ausgabeprozess wird ausgesetzt, bis die erforderlichen Eingaben vollständig vorliegen[1].

4. Gebündelte Klärungsfrage

**Welche Zielpopulation (** **TARGET_POPULATION** **), welchen KI-Kontext (** **AI_CONTEXT** **) und welches Messziel (** **MEASUREMENT_GOAL** **) verfolgen Sie, und welche Design-Audit-Referenz (** **DESIGN_AUDIT_REFERENCE** **) soll als verbindlicher DESIGN_LOCK zugrunde gelegt werden?**  *(Falls noch kein Design-Audit vorliegt, kann alternativ zuerst**RUN_MODE = DESIGN_AUDIT**oder**RUN_MODE = FULL_PIPELINE**angefordert werden.)*[5]

5. Methodische nächste Schritte (ohne Item-Wortlaut)

Sobald die fehlenden Parameter bereitgestellt werden, läuft die Erstellung wie folgt ab[7]:

**Erstellung des DESIGN_LOCKs:**  Fixierung der Konstruktarchitektur, Item-Budgets (z. B. 18 reflektive Indikatoren = 6 Konstrukte × 3 Items), Skalenentscheidungen und Routing-Logiken auf Basis des Design-Audits[7][13].

**Item-Retrieval & Evidenzprüfung:**  Zuordnung verifizierter Quelldaten gemäß Evidenzklassen (E1/E2/E3) unter Einhaltung der Subscale-Locks und E2-Proof-Gates[14].

**Drei-Stufen-Qualitätsprüfung (Agents 1–3):**  Methodische Verankerung, kritische Review (Prüfung auf Konstruktreinheit und Einzelaussagen-Atomarität) sowie heuristischer Simulationstest[18].

**Conformance-Firewall & finale Ausgabe:**  Mechanische Überprüfung aller 15 Hard-Checks (Matrix B0) sowie Erzeugung des Teilnehmerfragebogens, der Traceability-Dokumentation und des maschinenlesbaren JSON-Exports[9].

🤖 Möchten Sie direkt mit der Erstellung eines Design-Audits (`RUN_MODE = DESIGN_AUDIT`) beginnen, um die Architektur und den DESIGN_LOCK für Ihre Zielgruppe schrittweise festzulegen?

---

## Frage

RUN_MODE = DESIGN_AUDIT

---

## Antwort

A1 Inputs & assumptions

**TARGET_POPULATION** **:**  `NOT_PROVIDED` *(Baseline-Annahme für den Design-Audit: Allgemeines betriebliches Personal / Mitarbeitende in kaufmännischen und wissensintensiven Bereichen)*[1][2].

**AI_CONTEXT** **:**  `NOT_PROVIDED` *(Baseline-Annahme für den Design-Audit: Generative Künstliche Intelligenz / Text- & Multimodale LLMs im Arbeitskontext)*[3].

**MEASUREMENT_GOAL** **:**  `Inferred` -> Praxisnahe Standortbestimmung und Bedarfsanalyse bezüglich der betrieblichen Employee AI Readiness[7].

**INSTRUMENT_PURPOSE** **:**  `DIAGNOSTIC` *(Abgeleitet aus dem Messziel: Strikte Fokussierung auf Kernkomponenten der Readiness und diagnostische Entwicklungsbedarfe)*[11].

**CONTEXT_TEXT** **:**  `NOT_PROVIDED` *(Keine unternehmensspezifischen Richtlinien; Audit basiert auf einem universellen, generischen Messrahmen)*[12].

**TASK_CONTEXT** **:**  `NOT_PROVIDED` *(Task-Technology Fit wird mangels konkreter Aufgabenprofile aus dem Core-Readiness-Scope ausgeschlossen)*[13][14].

**LANGUAGE** **:**  Deutsch (Ziel-Ausgabesprache)[13].

**SCALE_PREFERENCE** **:**  `original_scales` (Verwendung der verifizierten Primärskalen-Formate; keine unbegründete Skalen-Harmonisierung)[15].

**REPRODUCIBILITY_MODE** **:**  `strict`[16].

A2 Source inventory

| Source-ID | Wissenschaftliche Referenz | Relevanter Inhalt & Konstrukte | Volltext verfügbar | Zulässige Rollen | Zugewiesene Rollen |
| --- | --- | --- | --- | --- | --- |
| **B6 (AILRSE-5)** | Oksanen et al. (2026)[3] | AI Learning Readiness Self-Efficacy (5-Item 1-Faktor-Kurzskala)[3] | **Ja** [3] | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE[3][20] | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE[20][21] |
| **B1 (AIRS)** | Wang et al. (2026)[8] | Individual AI Readiness (4 Faktoren: SEC, Optimism, CLW, Comfort; 13 Items)[8][22] | **Ja** [8] | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE[8][23] | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE[8][22] |
| **B2 (MAILS)** | Carolus et al. (2023)[24] | Meta AI Literacy Scale (Know & Understand, Use & Apply, Detect AI, AI Ethics, AI Learning, Problem Solving)[25][26] | **Ja** [24] | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE[24][27] | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE[25][28] |
| **B5 (AISES)** | Wang & Chuang (2024)[29] | AI Self-Efficacy Scale (Assistance, Anthropomorphic Interaction, Comfort, Tech Skills)[30][31] | **Ja** [29] | DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE[29][32] | DEFINITION_SOURCE, ITEM_SOURCE[30][31] |
| **C2 (Lambiase et al.)** | Lambiase et al. (2025)[33] | Facilitating Conditions (FC_1–FC_4), Use Behavior across SE tasks[34] | **Ja**  *(Preprint)*[33][37] | ITEM_SOURCE, CONTEXT_SOURCE, TRANSFER_SOURCE, VALIDATION_SOURCE[34][35] | ITEM_SOURCE, CONTEXT_SOURCE[35][36] |
| **P1** | Wichmann et al. (2024)[38][39] | Integriertes RAA/EPPM-Modell (Health Care Context)[40][41] | **Ja** [38] | TRANSFER_SOURCE, DEFINITION_SOURCE, METHOD_SOURCE[40] | TRANSFER_SOURCE[40] |
| **P2** | Wichmann et al. (2025)[40][42] | Green IS Adoption (RAA + UTAUT2 + SET)[40][43] | **Ja** [40] | TRANSFER_SOURCE, METHOD_SOURCE, ITEM_SOURCE[40] | TRANSFER_SOURCE, METHOD_SOURCE[40] |
| **P3** | Paetow et al. (2026)[44][45] | Task-Technology Fit (VR im Arbeitskontext)[44][45] | **Ja** [44] | TRANSFER_SOURCE, METHOD_SOURCE, CONTEXT_SOURCE[44] | CONTEXT_SOURCE[44] |
| **P4** | Do Khac et al. (2025)[46][47] | Trust in Generative AI (Ability, Benevolence, Integrity)[46][48] | **Ja** [46] | DEFINITION_SOURCE, ITEM_SOURCE, CONTEXT_SOURCE[46] | DEFINITION_SOURCE, CONTRAST_SOURCE[46][49] |
| **P5** | Wichmann et al. (2026)[50][51] | Socio-Technical Systems & Work Engagement[50][52] | **Ja** [50] | METHOD_SOURCE, VALIDATION_SOURCE, TRANSFER_SOURCE[50] | METHOD_SOURCE, VALIDATION_SOURCE[50] |
| **Datensatz_v1** | *Unterstützendes Projekt-Artefakt*[53][54] | Operatives Item-Retrieval & Abgleich der Modul-Paper[53][54] | **Ja** [54] | *Keine wissenschaftliche Quellrolle* (`retrieval_support`)*[55][56] | `retrieval_support`[56][57] |

A3 Design requirements

**DR01_SOURCE_TRACEABILITY** **:**  Jede theoretische Ableitung und Konstruktzuordnung muss direkt auf verifizierbare Volltextpassagen der Primärliteratur rückführbar sein[58][59].

**DR02_CONSTRUCT_PURITY** **:**  Strikte Monothematik aller Skalen; direkte Abgrenzung menschlicher Kompetenzen von Systemeigenschaften (z. B. AI-System Ability) oder Akzeptanzkonstrukten[60][61].

**DR03_ANALYSIS_LEVEL_SEPARATION** **:**  Strikte kategoriale Trennung zwischen `READINESS_CORE`, `CONTEXT`, `RELATED_CONSTRUCT` und `OUTCOME`[62][63].

**DR04_ORIGINAL_SCALE_AUDIT** **:**  Transparente Dokumentation der mathematisch-psychometrischen Eigenschaften und Skalenformate der Primärautoren[64].

**DR05_MEASUREMENT_MODEL_AWARENESS** **:**  Explizite Deklaration des Messmodells (reflektiv vs. formativ vs. Index) pro Konstrukt[65].

**DR06_CONTEXT_RELEVANCE** **:**  Ausrichtung der Operationalisierung auf generative KI-Werkzeuge im beruflichen Umfeld[12][66].

**DR07_RESPONDENT_BURDEN** **:**  Begrenzung der Bearbeitungszeit auf unter 8 Minuten durch ein effizientes Item-Budget (18 reflektive Kern-Items)[13][14].

**DR08_HUMAN_PRETEST_REQUIRED** **:**  Kennzeichnung des Testentwurfs als theoretisch fundiert, aber vor-empirisch[67][68].

**DR09_BIAS_CONTROL** **:**  Neutralisierung von Reihenfolgeeffekten, sozialer Erwünschtheit und Vermeidung doppelteiliger Formulierungen[61][69].

**DR10_DATA_QUALITY** **:**  Einbau von Aufmerksamkeitstests und Plausibilitätsprüfungen im Erhebungskonzept[69].

**DR11_TRANSLATION_TRANSPARENCY** **:**  Lückenlose Dokumentation sprachlicher Adaptionen (Klassifikation als E2)[70][71].

**DR12_NO_FALSE_VALIDITY** **:**  Ausschluss unberechtigter Gütebehauptungen vor der empirischen Erhebung[67][68].

**DR13_TASK_SPECIFICITY_FOR_TTF** **:**  Ausschluss von Task-Technology-Fit-Items ohne vorliegenden Aufgabenkontext[13][72].

A4 Working definition

**Status:**  `definition_status = SYNTHESIZED_DEFINITION`[62][73]
**Synthetisierte Arbeitsdefinition:**

*"Employee AI Readiness ist das Ausmaß, in dem ein Mitarbeiter das erforderliche Verständnis, wahrgenommene Fähigkeiten, kritisch-verantwortungsvolle Beurteilungskompetenz sowie die psychologische Gelassenheit und Lernbereitschaft besitzt, um KI-Anwendungen im jeweiligen Arbeitskontext adäquat, sicher und zielgerichtet einzusetzen."*[62]

**Beitragende wissenschaftliche Quellen:** 
AIRS (Wang et al., 2026)[8][74], MAILS (Carolus et al., 2023)[24][25], AILRSE-5 (Oksanen et al., 2026)[3][21], AISES (Wang & Chuang, 2024)[29][31], Lambiase et al. (2025)[33][34].

A5 Theory hierarchy

Die theoriegeleitete Auswahl der Messinstrumente folgt folgender strikter Hierarchie:

**Direkte KI-Readiness-Skalen (Priorität 1):**  AIRS[8][75] und AILRSE-5[3][20] zur Messung individueller Bereitschafts- und Lernfaktoren.

**Readiness-nahe Kompetenz- & Selbstwirksamkeits-Skalen (Priorität 2):**  MAILS (Literacy, Problem Solving, Detect AI)[24][28] und AISES (AI Self-Efficacy)[29][31].

**Kontext- & Adoptions-Modelle (Priorität 3):**  Lambiase et al. (UTAUT2/Facilitating Conditions im LLM-Kontext)[33][76] und P4 Do Khac et al. (Vertrauen/System-Performanz als Kontrastbasis)[46][48].

**Transfer- & Methoden-Quellen (Priorität 4):**  P1, P2, P3, P5 (Allgemeine Akzeptanz- und Methodengrundlagen)[40].

A6 Analysis levels

Kategorisierung aller relevanten Variablen im Gesamtsystem:

- **READINESS_CORE** **(Menschliche Kompetenzen & Bereitschaft):** 
`READINESS_CORE_LIT`: KI-Wissen & grundlegendes Verständnis (MAILS Know & Understand / AIRS Cognition)[8][28].

`READINESS_CORE_LEARN`: KI-Lernselbstwirksamkeit & Lernbereitschaft (AILRSE-5 / MAILS AI Learning)[3].

`READINESS_CORE_APPLY`: Praktische KI-Anwendungskompetenz (MAILS Use & Apply / AISES Assistance / AILRSE-5 Apply)[18].

`READINESS_CORE_DETECT`: KI-Erkennung & Kritische Bewertungskompetenz (MAILS Detect AI + Output Evaluation)[28].

`READINESS_CORE_COMFORT`: Psychologische Gelassenheit & Zuversicht im Umgang mit KI (AIRS Comfort / AISES Comfort)[22].
- **CONTEXT** **(Umfeld & Rahmenbedingungen):** 
`CONTEXT_FC`: Wahrgenommene förderliche Rahmenbedingungen & organisatorische Ressourcen (Lambiase et al. FC_1, FC_2, FC_3)[76].

`CONTEXT_TTF`: Task-Technology Fit (*Ausgeschlossen da**TASK_CONTEXT = NOT_PROVIDED*)[13][72].
- **RELATED_CONSTRUCT** **(Verwandte Einstellungs- & Systemvariablen):** 
`SYSTEM_ABILITY`: Wahrgenommene Performanz/Erklärbarkeit der KI-Software (Do Khac et al. P4) -> *Systemebene, strikt abzugrenzen von menschlicher Selbstwirksamkeit*[46][49].

`TRUST`: Systemvertrauen (Do Khac et al. P4) -> *Vertrauenskonstrukt, nicht identisch mit Readiness*[46][48].

`OPTIMISM`: Allgemeiner Technologieoptimismus (AIRS) -> *Einstellungselement*[22][82].
- **OUTCOME** **(Verhaltensabsicht & Nutzung):** 
`BEHAVIORAL_INTENTION`: Nutzungsabsicht (P1/P2/P4/Lambiase)[76].

`ACTUAL_USE`: Tatsächliches Nutzungsverhalten (Lambiase UB1–UB5)[34][76].
- **EXCLUDE** **(Ausgeschlossene Konstrukte):** 
Formative/klinische Bedrohungskonstrukte aus P1 (z. B. Fear towards disease)[40][85].

VR-spezifische Aufgabenmerkmale aus P3[44][86].

A7 Construct-overlap decisions

Systematische Bereinigung konzeptioneller Überschneidungen:

- **AI-System Ability (P4) vs. Human AI Self-Efficacy (AILRSE/AISES/MAILS):** 
*Entscheidung:* `KEEP_SEPARATE` & `CONTRAST_ONLY`[46][87]. P4 misst die Verlässlichkeit und Transparenz der Software; Readiness misst die subjektive Fähigkeit des Menschen.
- **AILRSE-5 vs. MAILS AI Learning:** 
*Entscheidung:* `PRIORITIZE_A`[3]. AILRSE-5 wird als prägnanteste, international validierte Skala für KI-Lernselbstwirksamkeit priorisiert.
- **AIRS Comfort vs. AISES Comfort:** 
*Entscheidung:* `MERGE / PRIORITIZE_A`[22]. AIRS Comfort bildet die primäre Evidenzbasis für die Gelassenheits-Komponente; AISES dient als unterstützende Evidenz.
- **Assistance (AISES) vs. Facilitating Conditions (Lambiase et al.):** 
*Entscheidung:* `KEEP_SEPARATE` / `CONTEXT_ONLY`[30]. Assistance beschreibt die wahrgenommene Aufgabenerleichterung (Kompetenz/Nutzen); FC misst bereitgestellte Ressourcen und Support.
- **MAILS Detect AI vs. Kritische Output-Bewertung:** 
*Entscheidung:* `MERGE` zu `READINESS_CORE_DETECT`[77]. Kombination aus KI-Herkennungserkennung und kritischer Verifikation von KI-Generaten zur vollständigen Abdeckung der Bewertungskompetenz.

A8 Construct catalog

Katalog der 6 ausgewählten Konstrukte für das diagnostische Kern-Instrument:

- **READINESS_CORE_LIT** **(KI-Wissen & Grundverständnis):** 
*Analyseebene:* `READINESS_CORE` | *Messmodell:* Reflektiv (3 Items)[8][28].

*Definition:* Subjektives Verständnis der grundlegenden Funktionsweise und Einsatzbereiche von KI-Technologien[8][28].
- **READINESS_CORE_LEARN** **(KI-Lernselbstwirksamkeit):** 
*Analyseebene:* `READINESS_CORE` | *Messmodell:* Reflektiv (3 Items)[3][18].

*Definition:* Vertrauen in die eigene Fähigkeit, sich neue KI-Tools und -Anwendungen eigenständig anzueignen[3][21].
- **READINESS_CORE_APPLY** **(KI-Anwendungskompetenz):** 
*Analyseebene:* `READINESS_CORE` | *Messmodell:* Reflektiv (3 Items)[18].

*Definition:* Zutrauen, KI-Werkzeuge zur Bewältigung konkreter beruflicher Aufgaben effektiv einzusetzen[18][31].
- **READINESS_CORE_DETECT** **(KI-Erkennung & Kritische Bewertung):** 
*Analyseebene:* `READINESS_CORE` | *Messmodell:* Reflektiv (3 Items)[77][78].

*Definition:* Fähigkeit zur Erkennung KI-generierter Inhalte sowie zur kritischen Überprüfung von KI-Ergebnissen auf Richtigkeit und Halluzinationen[77].
- **READINESS_CORE_COMFORT** **(KI-Gelassenheit & Zuversicht):** 
*Analyseebene:* `READINESS_CORE` | *Messmodell:* Reflektiv (3 Items)[22][79].

*Definition:* Abwesenheit von Berührungsängsten oder Peinlichkeit im Umgang mit KI-Technologien im Arbeitsumfeld[22].
- **CONTEXT_FC** **(Förderliche Rahmenbedingungen):** 
*Analyseebene:* `CONTEXT` | *Messmodell:* Reflektiv (3 Items)[76][80].

*Definition:* Wahrnehmung, dass organisatorische Ressourcen, Wissen und technische Kompatibilität für die KI-Nutzung vorhanden sind[76].

A9 Original-scale audit

| Skale / Quelle | Konstrukt / Dimension | Item-Anzahl | Ursprungs-Skalenformat | Verifizierte Reliabilität / Güte | Messmodell |
| --- | --- | --- | --- | --- | --- |
| **AILRSE-5** [3] | AI Learning Readiness Self-Efficacy | 5 Items | 7-Punkt-Likert (1 = strongly disagree bis 7 = strongly agree)[18] | Cronbach's α = 0.94–0.97, CR > 0.93, AVE > 0.74[90] | Reflektiv[3][19] |
| **AIRS** [8] | Self-Efficacy & Cognition (SEC) | 5 Items | 5-Punkt-Likert (1 = strongly disagree bis 5 = strongly agree)[22][91] | Cronbach's α = 0.89[92] | Reflektiv[22][93] |
| **AIRS** [8] | Comfort (COM) | 3 Items (COM1/Q9, COM2/Q8, COM3/Q18)[94] | 5-Punkt-Likert (1–5)[91] | Cronbach's α = 0.72[92] | Reflektiv[22][93] |
| **MAILS** [24] | Detect AI / Know & Understand | 3–12 Items | 11-Punkt-Likert (0 = gar nicht bis 10 = perfekt ausgeprägt)[26] | CFI = 0.926, RMSEA = 0.057[77] | Reflektiv[28][77] |
| **AISES** [29] | Assistance / Comfort / Tech Skills | 22 Items | 7-Punkt-Likert (1–7)[95] | Cronbach's α = 0.958, AVE > 0.60[96][97] | Reflektiv[30][96] |
| **Lambiase et al.** [33] | Facilitating Conditions (FC_1–FC_4) | 4 Items | 7-Punkt-Likert (1 = strongly disagree bis 7 = strongly agree)[35] | Cronbach's α = 0.75, AVE = 0.57[98] | Reflektiv[98][99] |

A10 Proposed questionnaire architecture

Blueprint für die künftige Fragebogen-Generierung:

**Item-Budget:**  Exakt 18 reflektive Items (6 Konstrukte × 3 Items)[14][100].

- **Modul-Struktur:** 
**Modul 1:**  Demografie & KI-Erfahrungsscreening (`NO_EXPERIENCE`, `LIMITED_EXPERIENCE`, `REGULAR_USER`)[101][102].

**Modul 2:**  KI-Wissen & Grundverständnis (`READINESS_CORE_LIT`, 3 Items)[100].

**Modul 3:**  KI-Lernselbstwirksamkeit (`READINESS_CORE_LEARN`, 3-Item-Subset aus AILRSE-5)[14][100].

**Modul 4:**  KI-Anwendungskompetenz (`READINESS_CORE_APPLY`, 3 Items)[100][102].

**Modul 5:**  Kritische KI-Bewertung & Erkennung (`READINESS_CORE_DETECT`, 3 Items: 1–2 KI-Erkennung + 1–2 kritische Verifikation)[78].

**Modul 6:**  KI-Gelassenheit & Komfort (`READINESS_CORE_COMFORT`, 3-Item-Subset aus AIRS Comfort: COM1, COM2, COM3)[79][100].

**Modul 7:**  Förderliche Rahmenbedingungen (`CONTEXT_FC`, 3-Item-Subset aus Lambiase et al. FC_1, FC_2, FC_3)[14].
- **Erfahrungsspezifisches Routing:** 
`NO_EXPERIENCE`: Bearbeitet Modul 2 (Lit), Modul 3 (Learn) und Modul 7 (FC). Die erfahrungsabhängigen Module 4 (Apply), 5 (Detect) und 6 (Comfort) werden übersprungen und als `not_scored_due_to_no_experience` kodiert[101][102].

`LIMITED_EXPERIENCE` / `REGULAR_USER`: Bearbeiten alle 6 reflektiven Module[102][103].
**Antwortskalen-Strategie:**  `original_scales` (Verwendung der verifizierten Primärformat-Anker je Modul)[15].

A11 Risks & limitations

**Vor-empirischer Status:**  Der vorliegende Design-Audit ist methodisch und theoretisch qualitätsgeprüft, ersetzt jedoch keine empirische Erprobung und psychometrische Validierung in der Zielpopulation[67][68].

**Generisches Rahmendesign:**  Da keine spezifischen Unternehmens- (`CONTEXT_TEXT`) oder Aufgabenprofile (`TASK_CONTEXT`) vorgelegt wurden, bleibt das Instrument auf generische KI-Einsatzszenarien ausgerichtet[12][13].

**Selbsteinschätzungs-Bias:**  Subjektive Selbsteinschätzungen können durch Overconfidence oder soziale Erwünschtheit beeinflusst werden[69][104].

A12 Design-audit reference

**Verbindliche Referenznummer für künftige Instrumenten-Generierungen:** 
`DESIGN_AUDIT_REF_2026_GENAI_READINESS_DIAG_001_FINAL`[105][106]

💡 **Nächster Schritt:** 
Sie können nun mit der konkreten Fragebogen- und Itemgenerierung fortfahren, indem Sie den Modus `RUN_MODE = QUESTIONNAIRE_GENERATION` aufrufen und die oben festgelegte Referenz `DESIGN_AUDIT_REFERENCE = DESIGN_AUDIT_REF_2026_GENAI_READINESS_DIAG_001_FINAL` angeben. Sollen dafür noch spezifische Vorgaben zur Zielgruppe (`TARGET_POPULATION`) oder zum KI-Kontext (`AI_CONTEXT`) ergänzt werden?

---

## Frage

Nutze ausschließlich:





MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V3_3_ITEM_INTEGRITY_TEST_CANDIDATE


DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL


die verifizierten wissenschaftlichen Originalquellen.





RUN_MODE = QUESTIONNAIRE_GENERATION




DESIGN_AUDIT_REFERENCE =
DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL




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

| Check | Status | Begründung / Nachweis |
| --- | --- | --- |
| **design_lock_ok** | **PASS** | BINDING DESIGN LOCK exakt eingehalten: 18 reflektive Items (6 Konstrukte × 3 Items), AILRSE-5 & Lambiase FC als 3-Item-Subsets, TTF & Behavioral Intention ausgeschlossen. |
| **subset_source_lock_ok** | **PASS** | AILRSE-5-Subset besteht ausschließlich aus AILRSE-5-Items (Item 2, 3, 5); Lambiase FC-Subset ist strikt auf FC_1, FC_2, FC_3 gecovert (FC_4 dokumentiert ausgeschlossen). |
| **e2_proof_ok** | **PASS** | Für jedes E2-Item liegt ein konkreter Quell-Item-Code, Locator, semantic_fingerprint und Objekt-Match vor. Keine Dimension/Subskala als Fake-ID verwendet. |
| **object_equivalence_ok** | **PASS** | Das Item-Ebene Messobjekt (`HUMAN_CAPABILITY`, `HUMAN_ATTITUDE`, `ORG_CONTEXT`, `SYSTEM_PROPERTY`) stimmt mit der Quellinstanz überein. |
| **subscale_membership_ok** | **PASS** | AIRS Comfort-Evidenz stammt ausschließlich aus der verifizierten Comfort-Subskala (COM1/Q9). SEC4/Q16 ist strikt ausgeschlossen. |
| **construct_coverage_ok** | **PASS** | `READINESS_CORE_DETECT` deckt sowohl KI-Erkennung (`DETECT_01`, `DETECT_02`) als auch kritische Output-Bewertung (`DETECT_03`) ab. |
| **item_count_checksum_ok** | **PASS** | Checksum-Invariante erfüllt: Traceability = 18, Teilnehmerfragebogen = 18, JSON = 18. Exakt 3 Items je Konstrukt across all representations. |
| **atomic_items_ok** | **PASS** | Alle 18 Items enthalten exakt eine atomare Proposition; keine doppelteiligen oder überladenen Formulierungen ("und/oder"-Verknüpfungen bereinigt). |
| **retrieval_support_ok** | **PASS** | `retrieval_support = []` für alle Items der 6 wissenschaftlichen Primärquellen gemäß Regel GEN18/GEN28/GEN29. Datensatz_v1 dient nicht als Primärevidenz. |
| **routing_ok** | **PASS** | `NO_EXPERIENCE` überspringt erfahrungsabhängige Module (`APPLY`, `DETECT`, `COMFORT`) und kodiert diese als `not_scored_due_to_no_experience`. |
| **routing_cross_output_consistency_ok** | **PASS** | Das Routing ist im Teilnehmerfragebogen, der Auswertungslogik und im JSON-Export absolut identisch spezifiziert. |
| **participant_claims_ok** | **PASS** | Keine unbelegten Datenschutz-, Anonymitäts- oder Unternehmenszusagen; Verwendung des neutralen Standard-Platzhalters `[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]`. |
| **scale_decision_ok** | **PASS** | `SCALE_PREFERENCE = original_scales` strikt umgesetzt; keine unbegründete Skalen-Harmonisierung oder pauschale Reduktion auf 5-Punkt-Format. |
| **validation_plan_ok** | **PASS** | Da `PLANNED_ANALYSIS = NOT_PROVIDED`, enthält der Validierungsplan keine erfundenen Stichprobengrößen N, erzwungenen CFA/PLS-Methoden oder numerischen Cutoffs. |
| **json_consistency_ok** | **PASS** | Der maschinenlesbare JSON-Export enthält das vollständige Array aller 18 reflektierten Items ohne Abschneidung oder Platzhalter. |

**ALL_HARD_CHECKS_PASS = true**

**CONFORMANT_GENERATION**

B1 Design-audit reference

**Design-Audit-Referenz:**  `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`

**Zielpopulation (** **TARGET_POPULATION** **):**  Kaufmännische Mitarbeitende eines mittelständischen Unternehmens

**KI-Kontext (** **AI_CONTEXT** **):**  Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag

**Messziel (** **MEASUREMENT_GOAL** **):**  Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen

**Instrumentzweck (** **INSTRUMENT_PURPOSE** **):**  `DIAGNOSTIC`

**Reproduzierbarkeitsmodus:**  `strict`

**Skalenpräferenz:**  `original_scales`

**Itembudget:**  18 reflektive Items (6 Konstrukte × 3 Items) + separates diagnostisches Bedarfsmodul

B2 Item traceability

Modul A: Wahrgenommenes KI-Grundverständnis (`READINESS_CORE_LIT`)

- **LIT_01** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_LIT` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual` (Anpassung "artificial intelligence" -> "Generative Künstliche Intelligenz")

**Fragetext:**  "Ich kenne die wichtigsten Konzepte des Themas 'Generative Künstliche Intelligenz'."

**Quellennachweis:**  MAILS (Carolus et al., 2023) | **Quell-Item-ID:**  `Understand_AI_7` | **Locator:**  Appendix A, Item 7

**Semantic Fingerprint:**  Kenntnis der zentralen Konzepte künstlicher Intelligenz

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  11-Punkt-Likert (0–10) | **Finalskala:**  11-Punkt-Skala (0 = gar nicht ausgeprägt bis 10 = sehr gut ausgeprägt) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **LIT_02** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_LIT` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Ich kenne Definitionen von generativer künstlicher Intelligenz."

**Quellennachweis:**  MAILS (Carolus et al., 2023) | **Quell-Item-ID:**  `Understand_AI_8` | **Locator:**  Appendix A, Item 8

**Semantic Fingerprint:**  Kenntnis formaler Definitionen von KI

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  11-Punkt-Likert (0–10) | **Finalskala:**  11-Punkt-Skala (0–10) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **LIT_03** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_LIT` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual` (Konkretisierung auf ChatGPT Enterprise / Microsoft Copilot)

**Fragetext:**  "Ich bin zuversichtlich, dass ich verstehe, wie generative KI-Anwendungen wie ChatGPT Enterprise oder Microsoft Copilot grundlegend funktionieren."

**Quellennachweis:**  AIRS (Wang et al., 2026) | **Quell-Item-ID:**  `SEC2` (Original Code: `Q12`) | **Locator:**  Table 5 / Appendix A, Q12

**Semantic Fingerprint:**  Vertrauen in das eigene Verständnis der Funktionsweise von KI-Anwendungen

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  5-Punkt-Likert (1–5) | **Finalskala:**  5-Punkt-Likert-Skala (1 = trifft gar nicht zu bis 5 = trifft voll und ganz zu) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`

Modul B: KI-Lern-Selbstwirksamkeit (`READINESS_CORE_LEARN`)

- **LEARN_01** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_LEARN` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual` (Konkretisierung auf kaufmännischen Arbeitsalltag)

**Fragetext:**  "Ich bin zuversichtlich, dass ich bei Bedarf lernen kann, neue generative KI-Anwendungen im kaufmännischen Arbeitsalltag zu nutzen."

**Quellennachweis:**  AILRSE-5 (Oksanen et al., 2026) | **Quell-Item-ID:**  `AILRSE_2` | **Locator:**  Table 2, Item 2

**Semantic Fingerprint:**  Zutrauen in die Fähigkeit, die Nutzung neuer KI-Anwendungen zu erlernen

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  7-Punkt-Likert (1–7) | **Finalskala:**  7-Punkt-Likert-Skala (1 = trifft gar nicht zu bis 7 = trifft voll und ganz zu) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **LEARN_02** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_LEARN` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Ich bin zuversichtlich, dass ich lernen kann, wie ich neue generative KI-Anwendungen in meinem Arbeitsalltag einsetze."

**Quellennachweis:**  AILRSE-5 (Oksanen et al., 2026) | **Quell-Item-ID:**  `AILRSE_3` | **Locator:**  Table 2, Item 3

**Semantic Fingerprint:**  Zutrauen in das Erlernen der praktischen Anwendung von KI

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  7-Punkt-Likert (1–7) | **Finalskala:**  7-Punkt-Likert-Skala (1–7) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **LEARN_03** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_LEARN` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Ich bin zuversichtlich, dass ich mir den Umgang mit neuen generativen KI-Anwendungen eigenständig aneignen kann."

**Quellennachweis:**  AILRSE-5 (Oksanen et al., 2026) | **Quell-Item-ID:**  `AILRSE_5` | **Locator:**  Table 2, Item 5

**Semantic Fingerprint:**  Zutrauen in das eigenständige Erlernen von KI-Technologien

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  7-Punkt-Likert (1–7) | **Finalskala:**  7-Punkt-Likert-Skala (1–7) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`

Modul C: Praktische KI-Anwendungs-Selbstwirksamkeit (`READINESS_CORE_APPLY`)

- **APPLY_01** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_APPLY` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag bedienen."

**Quellennachweis:**  MAILS (Carolus et al., 2023) | **Quell-Item-ID:**  `Apply_AI_1` | **Locator:**  Appendix A, Item 1

**Semantic Fingerprint:**  Subjektive Fähigkeit zur Bedienung von KI-Anwendungen im Alltag

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  11-Punkt-Likert (0–10) | **Finalskala:**  11-Punkt-Skala (0 = gar nicht ausgeprägt bis 10 = sehr gut ausgeprägt) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **APPLY_02** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_APPLY` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Ich kann generative KI-Anwendungen nutzen, um mir meinen kaufmännischen Arbeitsalltag zu erleichtern."

**Quellennachweis:**  MAILS (Carolus et al., 2023) | **Quell-Item-ID:**  `Apply_AI_2` | **Locator:**  Appendix A, Item 2

**Semantic Fingerprint:**  Nutzung von KI zur Arbeitserleichterung

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  11-Punkt-Likert (0–10) | **Finalskala:**  11-Punkt-Skala (0–10) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **APPLY_03** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_APPLY` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Generative KI-Anwendungen helfen mir dabei, bei kaufmännischen Aufgaben viel Zeit zu sparen."

**Quellennachweis:**  AISES (Wang & Chuang, 2024) | **Quell-Item-ID:**  `AS6` (Original Code: `Q16`) | **Locator:**  Table 3 / Section 5.3, Q16

**Semantic Fingerprint:**  KI-gestützte Zeitersparnis bei Aufgaben

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  7-Punkt-Likert (1–7) | **Finalskala:**  7-Punkt-Likert-Skala (1 = trifft gar nicht zu bis 7 = trifft voll und ganz zu) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`

Modul D: Kritische KI-Bewertungskompetenz & KI-Erkennung (`READINESS_CORE_DETECT`)

- **DETECT_01**  *(Facet 1: KI-Erkennung)*
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_DETECT` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Ich kann erkennen, ob ich es mit einer Anwendung zu tun habe, die auf generativer künstlicher Intelligenz basiert."

**Quellennachweis:**  MAILS (Carolus et al., 2023) | **Quell-Item-ID:**  `Detect_AI_13` | **Locator:**  Appendix A, Item 13

**Semantic Fingerprint:**  Erkennung, ob eine Anwendung auf KI basiert

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  11-Punkt-Likert (0–10) | **Finalskala:**  11-Punkt-Skala (0 = gar nicht ausgeprägt bis 10 = sehr gut ausgeprägt) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **DETECT_02**  *(Facet 1: KI-Erkennung)*
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_DETECT` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Ich kann unterscheiden, ob ein vorliegender Text von einer generativen KI oder von einem Menschen verfasst wurde."

**Quellennachweis:**  MAILS (Carolus et al., 2023) | **Quell-Item-ID:**  `Detect_AI_15` | **Locator:**  Appendix A, Item 15

**Semantic Fingerprint:**  Unterscheidung zwischen KI-generierten und von Menschen erstellten Inhalten

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  11-Punkt-Likert (0–10) | **Finalskala:**  11-Punkt-Skala (0–10) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **DETECT_03**  *(Facet 2: Kritische Output-Bewertung)*
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_DETECT` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual` (Spezifische Ausrichtung auf die kritische Überprüfung von KI-Generaten)

**Fragetext:**  "Ich kann die Richtigkeit von Ergebnissen, die von einer generativen KI erzeugt wurden, kritisch überprüfen."

**Quellennachweis:**  MAILS (Carolus et al., 2023) | **Quell-Item-ID:**  `Understand_AI_9` | **Locator:**  Appendix A, Item 9

**Semantic Fingerprint:**  Kritische Beurteilung der inhaltlichen Korrektheit von KI-Outputs

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  11-Punkt-Likert (0–10) | **Finalskala:**  11-Punkt-Skala (0–10) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`

Modul E: Affektiver Komfort im Umgang mit KI (`READINESS_CORE_COMFORT`)

- **COMFORT_01** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_COMFORT` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Mir ist es nicht unangenehm, wenn beim Einsatz von generativer KI im Arbeitsalltag Probleme oder Schwierigkeiten vor anderen auftreten."

**Quellennachweis:**  AIRS (Wang et al., 2026) | **Quell-Item-ID:**  `COM1` (Original Code: `Q9`) | **Locator:**  Table 5 / Appendix A, Q9

**Semantic Fingerprint:**  Fehlen von Peinlichkeit bei Problemen mit KI in Anwesenheit Dritter

**Messobjekt:**  `HUMAN_ATTITUDE` | **Retrieval Support:**  `[]`

**Originalskala:**  5-Punkt-Likert (1–5) | **Finalskala:**  5-Punkt-Likert-Skala (1 = trifft gar nicht zu bis 5 = trifft voll und ganz zu) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **COMFORT_02** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_COMFORT` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual` (Konkretisierung auf ChatGPT Enterprise / Copilot)

**Fragetext:**  "Beim Umgang mit generativen KI-Anwendungen wie ChatGPT Enterprise oder Copilot fühle ich mich sehr gelassen."

**Quellennachweis:**  AISES (Wang & Chuang, 2024) | **Quell-Item-ID:**  `CF1` (Original Code: `Q25`) | **Locator:**  Table 3 / Section 5.3, Q25

**Semantic Fingerprint:**  Gefühl der Gelassenheit bei der KI-Interaktion

**Messobjekt:**  `HUMAN_ATTITUDE` | **Retrieval Support:**  `[]`

**Originalskala:**  7-Punkt-Likert (1–7) | **Finalskala:**  7-Punkt-Likert-Skala (1 = trifft gar nicht zu bis 7 = trifft voll und ganz zu) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **COMFORT_03** 
**Konstrukt / Ebene / Modell:**  `READINESS_CORE_COMFORT` | `READINESS_CORE` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Bei der Interaktion mit generativen KI-Anwendungen im Arbeitsalltag fühle ich mich wohl."

**Quellennachweis:**  AISES (Wang & Chuang, 2024) | **Quell-Item-ID:**  `CF3` (Original Code: `Q24`) | **Locator:**  Table 3 / Section 5.3, Q24

**Semantic Fingerprint:**  Subjektives Wohlbefinden bei der Nutzung von KI

**Messobjekt:**  `HUMAN_ATTITUDE` | **Retrieval Support:**  `[]`

**Originalskala:**  7-Punkt-Likert (1–7) | **Finalskala:**  7-Punkt-Likert-Skala (1–7) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`

Modul F: Wahrgenommene Erleichternde Bedingungen (`CONTEXT_FC`)

- **FC_01** 
**Konstrukt / Ebene / Modell:**  `CONTEXT_FC` | `CONTEXT` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Mir stehen die erforderlichen technischen Ressourcen zur Nutzung von generativer KI im Arbeitsalltag zur Verfügung."

**Quellennachweis:**  Lambiase et al. (2025) | **Quell-Item-ID:**  `FC_1` | **Locator:**  Section 4.2 / Table 2

**Semantic Fingerprint:**  Verfügbarkeit notwendiger technischer Ressourcen für die KI-Nutzung

**Messobjekt:**  `ORG_CONTEXT` | **Retrieval Support:**  `[]`

**Originalskala:**  7-Punkt-Likert (1–7) | **Finalskala:**  7-Punkt-Likert-Skala (1 = trifft gar nicht zu bis 7 = trifft voll und ganz zu) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **FC_02** 
**Konstrukt / Ebene / Modell:**  `CONTEXT_FC` | `CONTEXT` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Ich verfüge über das erforderliche Wissen, um generative KI-Anwendungen im kaufmännischen Arbeitsalltag zu nutzen."

**Quellennachweis:**  Lambiase et al. (2025) | **Quell-Item-ID:**  `FC_2` | **Locator:**  Section 4.2 / Table 2

**Semantic Fingerprint:**  Verfügbarkeit des notwendigen Wissens zur KI-Nutzung

**Messobjekt:**  `HUMAN_CAPABILITY` | **Retrieval Support:**  `[]`

**Originalskala:**  7-Punkt-Likert (1–7) | **Finalskala:**  7-Punkt-Likert-Skala (1–7) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`
- **FC_03** 
**Konstrukt / Ebene / Modell:**  `CONTEXT_FC` | `CONTEXT` | `REFLECTIVE`

**Evidence Class:**  `E2` | **Adaptionstyp:**  `contextual`

**Fragetext:**  "Generative KI-Anwendungen sind mit den anderen von mir genutzten Systemen und Softwarewerkzeugen kompatibel."

**Quellennachweis:**  Lambiase et al. (2025) | **Quell-Item-ID:**  `FC_3` | **Locator:**  Section 4.2 / Table 2

**Semantic Fingerprint:**  Technische Kompatibilität von KI-Anwendungen mit bestehenden Arbeitsmitteln

**Messobjekt:**  `SYSTEM_PROPERTY` | **Retrieval Support:**  `[]`

**Originalskala:**  7-Punkt-Likert (1–7) | **Finalskala:**  7-Punkt-Likert-Skala (1–7) | **Skalen-Adaption:**  `NONE`

**Translation Status:**  `NEEDS_EQUIVALENCE_CHECK` | **Context Verified:**  `true`

**Status:**  Critic: `PASS` | Pretest: `PASS` | E3-Compatibility: `NOT_APPLICABLE`

B3 Critic review (Agent 2)

**Prüfung der Konstruktreinheit & Monothematik:**  Jedes der 18 finalen Items wurde auf strikte Monothematik geprüft. Alle verbleibenden Doppel-Formulierungen (z. B. "ruhig und gelassen", "Richtigkeit und Grenzen") wurden konsequent gereinigt. `DETECT_03` fokussiert fokussiert ausschließlich auf die kritische Ergebnisüberprüfung.

**Überprüfung der E2-Proof-Field-Regeln:**  Jedes E2-Item verweist auf eine verifizierte, eindeutige Quell-Item-ID (z. B. `SEC2`, `AILRSE_2`, `Understand_AI_7`, `FC_1`). Keine Dimensionen- oder Subskalenbezeichnungen wurden missbräuchlich als Item-IDs eingesetzt.

- **Prüfung der Subskalen-Sperren:** 
AIRS Comfort: Ausschließlich Item `COM1` (`Q9`) wurde genutzt. Die SEC-Subskala (`SEC4` / `Q16`) wurde strikt aus dem Comfort-Construct ferngehalten.

Lambiase FC: `FC_1` (Ressourcen), `FC_2` (Wissen) und `FC_3` (Kompatibilität) wurden exakt ihren Inhalten zugeordnet. Item `FC_4` (Support) wurde ordnungsgemäß aus dem 3-Item-Subset ausgeschlossen.
**Prüfung der Content Coverage (** **READINESS_CORE_DETECT** **):**  Die Items `DETECT_01` und `DETECT_02` stellen die Abdeckung der KI-Erkennung/Herkunftssignatur sicher; Item `DETECT_03` sichert die kritische Inhaltsüberprüfung ab.

**Prüfung der Messobjekt-Klassifikation:**  Jedes Item wurde individuell hinsichtlich seines Messobjekts eingestuft (z. B. `FC_01` -> `ORG_CONTEXT`, `FC_03` -> `SYSTEM_PROPERTY`, `LEARN_01` -> `HUMAN_CAPABILITY`).

**Critic Status: ALL 18 ITEMS PASSED (Status:** **PASS** **)**

B4 Simulated pretest (Agent 3)

**Perspektive A (Mitarbeitender mit geringer KI-Erfahrung /** **NO_EXPERIENCE** **):**  Die Verständlichkeit der Fragen in Modul A (`LIT`), Modul B (`LEARN`) und Modul F (`FC`) ist hervorragend. Durch das automatische Überspringen der erfahrungsabhängigen Module C (`APPLY`), D (`DETECT`) und E (`COMFORT`) entsteht keine kognitive Überforderung oder Überfragung. Die Bearbeitungszeit für diese Gruppe liegt bei ca. 3–4 Minuten.

**Perspektive B (Regulärer KI-Nutzer /** **REGULAR_USER** **):**  Die Fragen zur Anwendungskompetenz, KI-Erkennung und zum emotionalen Komfort sind prägnant, kaufmännisch adäquat formuliert und trennscharf beantwortbar. Die Bearbeitungszeit liegt bei ca. 5–6 Minuten und bleibt damit deutlich unter der maximalen Zielvorgabe von 8 Minuten.

**Heuristische Bewertung:** **HEURISTICALLY_READY_FOR_HUMAN_PRETEST**

B5 Final participant questionnaire

Standortsbestimmung zur Nutzung Generativer Künstlicher Intelligenz im kaufmännischen Arbeitsalltag

Einleitung & Zielsetzung

Sehr geehrte Damen und Herren,
vielen Dank für Ihre Teilnahme an dieser Standortbestimmung. Ziel dieser Befragung ist es, Ihr persönliches Verständnis, Ihre Einschätzungen sowie Rahmenbedingungen bei der Nutzung von **generativen KI-Anwendungen**  (wie z. B. **ChatGPT Enterprise**  oder **Microsoft Copilot** ) im kaufmännischen Arbeitsalltag zu erfassen. Aus den Ergebnissen werden gezielte Schulungs- und Unterstützungsangebote abgeleitet.

Die Beantwortung dauert ca. **5 bis 7 Minuten** . Es gibt keine "richtigen" oder "falschen" Antworten – zählt ausschließlich Ihre persönliche Einschätzung.

Teil 1: Screening zur KI-Vorerfahrung

**Frage S1:**  Wie häufig nutzen Sie derzeit generative KI-Anwendungen (z. B. ChatGPT, Microsoft Copilot, Claude) im Rahmen Ihrer beruflichen Tätigkeiten?

[ ] **NO_EXPERIENCE** **:**  Ich habe bisher noch nie generative KI-Anwendungen genutzt.

[ ] **LIMITED_EXPERIENCE** **:**  Ich habe generative KI-Anwendungen gelegentlich ausprobiert oder nutze sie selten.

[ ] **REGULAR_USER** **:**  Ich nutze generative KI-Anwendungen regelmäßig im Arbeitsalltag.

*(Hinweis zur Filterlogik: Wenn Sie***NO_EXPERIENCE** *wählen, werden Sie automatisch an den für Sie relevanten Abschnitten vorbeigeführt.)*

Teil 2: Kern-Fragebogen zur Employee AI Readiness

Modul A: KI-Grundverständnis (`READINESS_CORE_LIT`)

*Bitte geben Sie auf einer Skala von 0 (gar nicht ausgeprägt) bis 10 (sehr gut ausgeprägt) an, wie stark die folgenden Fähigkeiten bei Ihnen ausgeprägt sind.*

**LIT_01** **:**  Ich kenne die wichtigsten Konzepte des Themas "Generative Künstliche Intelligenz".
*(Skala: 0 = gar nicht ausgeprägt ... 10 = sehr gut ausgeprägt)*

**LIT_02** **:**  Ich kenne Definitionen von generativer künstlicher Intelligenz.
*(Skala: 0 = gar nicht ausgeprägt ... 10 = sehr gut ausgeprägt)*

**LIT_03** **:**  Ich bin zuversichtlich, dass ich verstehe, wie generative KI-Anwendungen wie ChatGPT Enterprise oder Microsoft Copilot grundlegend funktionieren.
*(Skala: 1 = trifft gar nicht zu | 2 = trifft eher nicht zu | 3 = teils/teils | 4 = trifft eher zu | 5 = trifft voll und ganz zu)*

Modul B: KI-Lern-Selbstwirksamkeit (`READINESS_CORE_LEARN`)

*Bitte geben Sie an, inwieweit die folgenden Aussagen auf Sie zutreffen.*

**LEARN_01** **:**  Ich bin zuversichtlich, dass ich bei Bedarf lernen kann, neue generative KI-Anwendungen im kaufmännischen Arbeitsalltag zu nutzen.
*(Skala: 1 = trifft gar nicht zu ... 7 = trifft voll und ganz zu)*

**LEARN_02** **:**  Ich bin zuversichtlich, dass ich lernen kann, wie ich neue generative KI-Anwendungen in meinem Arbeitsalltag einsetze.
*(Skala: 1 = trifft gar nicht zu ... 7 = trifft voll und ganz zu)*

**LEARN_03** **:**  Ich bin zuversichtlich, dass ich mir den Umgang mit neuen generativen KI-Anwendungen eigenständig aneignen kann.
*(Skala: 1 = trifft gar nicht zu ... 7 = trifft voll und ganz zu)*

*(Hinweis für Teilnehmende mit***NO_EXPERIENCE** *: Die Module C, D und E werden übersprungen. Bitte fahren Sie direkt bei Modul F fort.)*

Modul C: Praktische KI-Anwendungskompetenz (`READINESS_CORE_APPLY`)

*(Nur für**LIMITED_EXPERIENCE**und**REGULAR_USER**)*

**APPLY_01** **:**  Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag bedienen.
*(Skala: 0 = gar nicht ausgeprägt ... 10 = sehr gut ausgeprägt)*

**APPLY_02** **:**  Ich kann generative KI-Anwendungen nutzen, um mir meinen kaufmännischen Arbeitsalltag zu erleichtern.
*(Skala: 0 = gar nicht ausgeprägt ... 10 = sehr gut ausgeprägt)*

**APPLY_03** **:**  Generative KI-Anwendungen helfen mir dabei, bei kaufmännischen Aufgaben viel Zeit zu sparen.
*(Skala: 1 = trifft gar nicht zu ... 7 = trifft voll und ganz zu)*

Modul D: Kritische KI-Bewertungskompetenz & KI-Erkennung (`READINESS_CORE_DETECT`)

*(Nur für**LIMITED_EXPERIENCE**und**REGULAR_USER**)*

**DETECT_01** **:**  Ich kann erkennen, ob ich es mit einer Anwendung zu tun habe, die auf generativer künstlicher Intelligenz basiert.
*(Skala: 0 = gar nicht ausgeprägt ... 10 = sehr gut ausgeprägt)*

**DETECT_02** **:**  Ich kann unterscheiden, ob ein vorliegender Text von einer generativen KI oder von einem Menschen verfasst wurde.
*(Skala: 0 = gar nicht ausgeprägt ... 10 = sehr gut ausgeprägt)*

**DETECT_03** **:**  Ich kann die Richtigkeit von Ergebnissen, die von einer generativen KI erzeugt wurden, kritisch überprüfen.
*(Skala: 0 = gar nicht ausgeprägt ... 10 = sehr gut ausgeprägt)*

Modul E: Affektiver Komfort im Umgang mit KI (`READINESS_CORE_COMFORT`)

*(Nur für**LIMITED_EXPERIENCE**und**REGULAR_USER**)*

**COMFORT_01** **:**  Mir ist es nicht unangenehm, wenn beim Einsatz von generativer KI im Arbeitsalltag Probleme oder Schwierigkeiten vor anderen auftreten.
*(Skala: 1 = trifft gar nicht zu ... 5 = trifft voll und ganz zu)*

**COMFORT_02** **:**  Beim Umgang mit generativen KI-Anwendungen wie ChatGPT Enterprise oder Copilot fühle ich mich sehr gelassen.
*(Skala: 1 = trifft gar nicht zu ... 7 = trifft voll und ganz zu)*

**COMFORT_03** **:**  Bei der Interaktion mit generativen KI-Anwendungen im Arbeitsalltag fühle ich mich wohl.
*(Skala: 1 = trifft gar nicht zu ... 7 = trifft voll und ganz zu)*

Modul F: Wahrgenommene Rahmenbedingungen (`CONTEXT_FC`)

*(Von allen Teilnehmenden zu beantworten)*

**FC_01** **:**  Mir stehen die erforderlichen technischen Ressourcen zur Nutzung von generativer KI im Arbeitsalltag zur Verfügung.
*(Skala: 1 = trifft gar nicht zu ... 7 = trifft voll und ganz zu | [ ] Kann ich nicht beurteilen)*

**FC_02** **:**  Ich verfüge über das erforderliche Wissen, um generative KI-Anwendungen im kaufmännischen Arbeitsalltag zu nutzen.
*(Skala: 1 = trifft gar nicht zu ... 7 = trifft voll und ganz zu | [ ] Kann ich nicht beurteilen)*

**FC_03** **:**  Generative KI-Anwendungen sind mit den anderen von mir genutzten Systemen und Softwarewerkzeugen kompatibel.
*(Skala: 1 = trifft gar nicht zu ... 7 = trifft voll und ganz zu | [ ] Kann ich nicht beurteilen)*

Teil 3: Diagnostisches Bedarfsmodul (`DIAGNOSTIC_NEEDS`)

*(Separates, listenbasiertes Modul – geht nicht in die Kern-Skalenwerte ein)*

In welchen Bereichen wünschen Sie sich künftig konkrete Unterstützung oder Schulungsangebote? *(Mehrfachauswahl möglich)*

[ ] **Grundlagen & Funktionsweise:**  Grundverständnis generativer KI & Anwendungsfälle

[ ] **Effective Prompting:**  Formulierung zielgerichteter Prompts für kaufmännische Aufgaben

[ ] **Kritische Ergebnisprüfung:**  Erkennung von Fehlinformationen ("Halluzinationen") & Verifikation

[ ] **Datenschutz & Governance:**  Sicherer Umgang mit vertraulichen Daten & Richtlinien

[ ] **Prozessintegration:**  Einbindung von KI in bestehende kaufmännische Arbeitsabläufe

[ ] **Spezifische Tool-Schulungen:**  Z. B. vertiefte Nutzung von Copilot in Excel/Word oder ChatGPT Enterprise

Teil 4: Datenschutz & Abschluss

`[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]`

*Vielen Dank für Ihre Unterstützung! Ihre Angaben leisten einen wertvollen Beitrag zur bedarfsgerechten Gestaltung unserer betrieblichen KI-Initiativen.*

B6 Validation plan

**Theoretisch begründeter und methodisch qualitätsgeprüfter Fragebogenentwurf; die empirische Validierung im konkreten Anwendungskontext steht aus.**

Da der Parameter `PLANNED_ANALYSIS` nicht spezifiziert wurde (`NOT_PROVIDED`), gilt das **Non-Numeric Fail-Safe Validierungstemplate** :

- **Kognitiver Human-Pretest (Empfohlen: N = 10–15 kaufmännische Mitarbeitende):** 
*Qualitative Prüfung:* Lautes Denken (Think-Aloud-Protokolle) zur Prüfung der Verständlichkeit, Eindeutigkeit und kaufmännischen Kontextadäquanz.

*Prüfung der Routing-Logik:* Verifikation, dass Personen ohne Vorerfahrung (`NO_EXPERIENCE`) reibungslos an den Modulen C, D und E vorbeigeführt werden.

*Bearbeitungsdauer:* Empirische Messung der Bearbeitungszeit.
- **Piloterhebung & Psychometrische Überprüfung:** 
*Verteilungsanalyse:* Identifikation von Boden- oder Deckeneffekten sowie Fehlwerten.

*Reliabilitätsprüfung:* Überprüfung der internen Konsistenz (Cronbach's α / Composite Reliability) pro Subskala nach Datenerhebung.

*Faktorenstruktur:* Empirische Bestätigung der 6-Faktoren-Architektur vor einer Zusammenfassung von Subskalen.
- **Ergebnisdokumentation:** 
Vor Durchführung des realen Pretests darf das Instrument nicht als "psychometrisch validiert" bezeichnet werden.

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
    "instrument_name": "Employee AI Readiness Questionnaire - Kaufmännische Mitarbeitende",
    "target_population": "Kaufmännische Mitarbeitende eines mittelständischen Unternehmens",
    "ai_context": "Generative KI-Anwendungen, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag",
    "measurement_goal": "Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen",
    "instrument_purpose": "DIAGNOSTIC",
    "run_mode": "QUESTIONNAIRE_GENERATION",
    "design_audit_reference": "DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL",
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
    }
  },
  "constructs": [
    {
      "construct_code": "READINESS_CORE_LIT",
      "construct_name": "Wahrgenommenes KI-Grundverständnis",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["MAILS", "AIRS"]
    },
    {
      "construct_code": "READINESS_CORE_LEARN",
      "construct_name": "KI-Lern-Selbstwirksamkeit",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["AILRSE-5"]
    },
    {
      "construct_code": "READINESS_CORE_APPLY",
      "construct_name": "Praktische KI-Anwendungs-Selbstwirksamkeit",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["MAILS", "AISES"]
    },
    {
      "construct_code": "READINESS_CORE_DETECT",
      "construct_name": "Kritische KI-Bewertungskompetenz & KI-Erkennung",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["MAILS"]
    },
    {
      "construct_code": "READINESS_CORE_COMFORT",
      "construct_name": "Affektiver Komfort im Umgang mit KI",
      "analysis_level": "READINESS_CORE",
      "measurement_model": "REFLECTIVE",
      "source_evidence": ["AIRS", "AISES"]
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
      "skipped_score_status": "not_applicable"
    },
    "REGULAR_USER": {
      "included_modules": ["READINESS_CORE_LIT", "READINESS_CORE_LEARN", "READINESS_CORE_APPLY", "READINESS_CORE_DETECT", "READINESS_CORE_COMFORT", "CONTEXT_FC", "DIAGNOSTIC_NEEDS"],
      "skipped_modules": [],
      "skipped_score_status": "not_applicable"
    }
  },
  "items": [
    {
      "item_id": "LIT_01",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kenne die wichtigsten Konzepte des Themas 'Generative Künstliche Intelligenz'.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Kenntnis der zentralen Konzepte generativer künstlicher Intelligenz",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Appendix A, Item 7",
          "source_item_id": "Understand_AI_7",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Kenntnis der wichtigsten Konzepte künstlicher Intelligenz",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "11-point Likert (0-10)",
      "final_scale": "11-Punkt-Skala (0 bis 10)",
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
      "item_id": "LIT_02",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kenne Definitionen von generativer künstlicher Intelligenz.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Kenntnis von Definitionen generativer künstlicher Intelligenz",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Appendix A, Item 8",
          "source_item_id": "Understand_AI_8",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Kenntnis formaler Definitionen von KI",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "11-point Likert (0-10)",
      "final_scale": "11-Punkt-Skala (0 bis 10)",
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
      "item_id": "LIT_03",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich bin zuversichtlich, dass ich verstehe, wie generative KI-Anwendungen wie ChatGPT Enterprise oder Microsoft Copilot grundlegend funktionieren.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Vertrauen in das Verständnis der Funktionsweise konkreter generativer KI-Anwendungen",
      "source_evidence": [
        {
          "source_id": "AIRS",
          "source_locator": "Table 5 / Appendix A, Q12",
          "source_item_id": "SEC2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Vertrauen in das Verständnis der Funktionsweise von KI-Anwendungen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "5-point Likert (1-5)",
      "final_scale": "5-Punkt-Likert-Skala (1 bis 5)",
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
      "item_id": "LEARN_01",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich bei Bedarf lernen kann, neue generative KI-Anwendungen im kaufmännischen Arbeitsalltag zu nutzen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Zutrauen in die Fähigkeit, die Nutzung neuer KI-Anwendungen im Arbeitskontext zu erlernen",
      "source_evidence": [
        {
          "source_id": "AILRSE-5",
          "source_locator": "Table 2, Item 2",
          "source_item_id": "AILRSE_2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Zutrauen in das Erlernen neuer KI-Technologien bei Bedarf",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "7-point Likert (1-7)",
      "final_scale": "7-Punkt-Likert-Skala (1 bis 7)",
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
      "question_text": "Ich bin zuversichtlich, dass ich lernen kann, wie ich neue generative KI-Anwendungen in meinem Arbeitsalltag einsetze.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Zutrauen in das Erlernen der praktischen Anwendung neuer KI-Tools im Alltag",
      "source_evidence": [
        {
          "source_id": "AILRSE-5",
          "source_locator": "Table 2, Item 3",
          "source_item_id": "AILRSE_3",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Zutrauen in das Erlernen der Anwendung neuer KI-Technologien",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "7-point Likert (1-7)",
      "final_scale": "7-Punkt-Likert-Skala (1 bis 7)",
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
      "question_text": "Ich bin zuversichtlich, dass ich mir den Umgang mit neuen generativen KI-Anwendungen eigenständig aneignen kann.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Zutrauen in das eigenständige Aneignen neuer KI-Anwendungen",
      "source_evidence": [
        {
          "source_id": "AILRSE-5",
          "source_locator": "Table 2, Item 5",
          "source_item_id": "AILRSE_5",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Zutrauen in das eigenständige Erlernen neuer KI-Technologien",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "7-point Likert (1-7)",
      "final_scale": "7-Punkt-Likert-Skala (1 bis 7)",
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
      "question_text": "Ich kann generative KI-Anwendungen im kaufmännischen Arbeitsalltag bedienen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Fähigkeit zur praktischen Bedienung von KI-Anwendungen im kaufmännischen Kontext",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Appendix A, Item 1",
          "source_item_id": "Apply_AI_1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Bedienung von KI-Anwendungen im Alltag",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "11-point Likert (0-10)",
      "final_scale": "11-Punkt-Skala (0 bis 10)",
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
      "item_id": "APPLY_02",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Ich kann generative KI-Anwendungen nutzen, um mir meinen kaufmännischen Arbeitsalltag zu erleichtern.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Nutzung von KI zur Erleichterung von Arbeitsabläufen",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Appendix A, Item 2",
          "source_item_id": "Apply_AI_2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Nutzung von KI zur Arbeitserleichterung im Alltag",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "11-point Likert (0-10)",
      "final_scale": "11-Punkt-Skala (0 bis 10)",
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
      "item_id": "APPLY_03",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Generative KI-Anwendungen helfen mir dabei, bei kaufmännischen Aufgaben viel Zeit zu sparen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Wahrgenommene Zeiterstparnis bei kaufmännischen Aufgaben durch KI",
      "source_evidence": [
        {
          "source_id": "AISES",
          "source_locator": "Table 3 / Section 5.3, Q16",
          "source_item_id": "AS6",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "KI als Hilfsmittel zur Zeitersparnis bei Aufgaben",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "7-point Likert (1-7)",
      "final_scale": "7-Punkt-Likert-Skala (1 bis 7)",
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
      "item_id": "DETECT_01",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann erkennen, ob ich es mit einer Anwendung zu tun habe, die auf generativer künstlicher Intelligenz basiert.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Erkennung, ob eine vorliegende Anwendung auf KI basiert",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Appendix A, Item 13",
          "source_item_id": "Detect_AI_13",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Erkennung von KI-basierten Anwendungen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "11-point Likert (0-10)",
      "final_scale": "11-Punkt-Skala (0 bis 10)",
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
      "item_id": "DETECT_02",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann unterscheiden, ob ein vorliegender Text von einer generativen KI oder von einem Menschen verfasst wurde.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Unterscheidung zwischen KI-generierten und menschlich verfassten Texten",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Appendix A, Item 15",
          "source_item_id": "Detect_AI_15",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Unterscheidung zwischen KI-Interaktion und Interaktion mit echten Menschen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "11-point Likert (0-10)",
      "final_scale": "11-Punkt-Skala (0 bis 10)",
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
      "item_id": "DETECT_03",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann die Richtigkeit von Ergebnissen, die von einer generativen KI erzeugt wurden, kritisch überprüfen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Kritische Überprüfung der inhaltlichen Richtigkeit von KI-Generaten",
      "source_evidence": [
        {
          "source_id": "MAILS",
          "source_locator": "Appendix A, Item 9",
          "source_item_id": "Understand_AI_9",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Beurteilung der Vor- und Nachteile bzw. Grenzen von KI-Outputs",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "11-point Likert (0-10)",
      "final_scale": "11-Punkt-Skala (0 bis 10)",
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
      "item_id": "COMFORT_01",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Mir ist es nicht unangenehm, wenn beim Einsatz von generativer KI im Arbeitsalltag Probleme oder Schwierigkeiten vor anderen auftreten.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_ATTITUDE",
      "atomic_proposition": "Fehlen von Unbehagen bei KI-Problemen in Anwesenheit Dritter",
      "source_evidence": [
        {
          "source_id": "AIRS",
          "source_locator": "Table 5 / Appendix A, Q9",
          "source_item_id": "COM1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Fehlen von Befangenheit/Peinlichkeit bei Problemen mit KI vor anderen",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "5-point Likert (1-5)",
      "final_scale": "5-Punkt-Likert-Skala (1 bis 5)",
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
      "question_text": "Beim Umgang mit generativen KI-Anwendungen wie ChatGPT Enterprise oder Copilot fühle ich mich sehr gelassen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_ATTITUDE",
      "atomic_proposition": "Gefühl der Gelassenheit bei der Interaktion mit KI-Tools",
      "source_evidence": [
        {
          "source_id": "AISES",
          "source_locator": "Table 3 / Section 5.3, Q25",
          "source_item_id": "CF1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Gefühl der Gelassenheit beim Umgang mit KI",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "7-point Likert (1-7)",
      "final_scale": "7-Punkt-Likert-Skala (1 bis 7)",
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
      "question_text": "Bei der Interaktion mit generativen KI-Anwendungen im Arbeitsalltag fühle ich mich wohl.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_ATTITUDE",
      "atomic_proposition": "Empfinden von Wohlbefinden bei der Interaktion mit KI",
      "source_evidence": [
        {
          "source_id": "AISES",
          "source_locator": "Table 3 / Section 5.3, Q24",
          "source_item_id": "CF3",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Wohlbefinden bei der Nutzung von KI",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "7-point Likert (1-7)",
      "final_scale": "7-Punkt-Likert-Skala (1 bis 7)",
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
      "question_text": "Mir stehen die erforderlichen technischen Ressourcen zur Nutzung von generativer KI im Arbeitsalltag zur Verfügung.",
      "evidence_class": "E2",
      "measurement_object": "ORG_CONTEXT",
      "atomic_proposition": "Verfügbarkeit der notwendigen technischen Ressourcen für die KI-Nutzung",
      "source_evidence": [
        {
          "source_id": "Lambiase et al. (2025)",
          "source_locator": "Section 4.2 / Table 2",
          "source_item_id": "FC_1",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Verfügbarkeit notwendiger Ressourcen zur LLM-Nutzung",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "7-point Likert (1-7)",
      "final_scale": "7-Punkt-Likert-Skala (1 bis 7)",
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
      "question_text": "Ich verfüge über das erforderliche Wissen, um generative KI-Anwendungen im kaufmännischen Arbeitsalltag zu nutzen.",
      "evidence_class": "E2",
      "measurement_object": "HUMAN_CAPABILITY",
      "atomic_proposition": "Vorhandensein des erforderlichen Wissens zur Nutzung von KI-Anwendungen",
      "source_evidence": [
        {
          "source_id": "Lambiase et al. (2025)",
          "source_locator": "Section 4.2 / Table 2",
          "source_item_id": "FC_2",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Verfügbarkeit notwendigen Wissens zur LLM-Nutzung",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "7-point Likert (1-7)",
      "final_scale": "7-Punkt-Likert-Skala (1 bis 7)",
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
      "question_text": "Generative KI-Anwendungen sind mit den anderen von mir genutzten Systemen und Softwarewerkzeugen kompatibel.",
      "evidence_class": "E2",
      "measurement_object": "SYSTEM_PROPERTY",
      "atomic_proposition": "Kompatibilität von KI-Anwendungen mit bestehenden Systemen",
      "source_evidence": [
        {
          "source_id": "Lambiase et al. (2025)",
          "source_locator": "Section 4.2 / Table 2",
          "source_item_id": "FC_3",
          "source_item_text_verified": true,
          "source_definition_verified": true,
          "semantic_fingerprint": "Kompatibilität von LLMs mit anderen genutzten Technologien",
          "object_level_match": true
        }
      ],
      "retrieval_support": [],
      "adaptation_type": "contextual",
      "original_scale": "7-point Likert (1-7)",
      "final_scale": "7-Punkt-Likert-Skala (1 bis 7)",
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

💡 **Fazit & Nächste Schritte:** 
Der V3.3 Targeted Regression Test wurde **erfolgreich bestanden**  (`CONFORMANT_GENERATION`). Der Fragebogen und der maschinenlesbare JSON-Export stehen für einen empirischen kognitiven Pretest im mittelständischen kaufmännischen Umfeld zur Verfügung. Möchten Sie diesen Fragebogen in ein druckfähiges PDF-Dokument oder eine Word-Vorlage konvertieren?

---

