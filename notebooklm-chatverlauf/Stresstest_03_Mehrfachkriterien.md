# Stresstest 3

Quelle: https://notebook.google.com/notebook/e72d0561-e764-4817-b3ea-d3556f055cb5
Exportiert: 21.10.2026, 19:00:07

---

## Frage

Nutze ausschließlich den aktualisierten
MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V2_1
und die im Notebook verfügbaren wissenschaftlichen Quellen.




Dies ist:




STRESS_TEST_ROUND_02B – ST06B_E3_SOURCE_COMPATIBILITY




Erstelle ein neues deutschsprachiges E3-Item zur kritischen Bewertung von KI-Ausgaben.




Vorgaben:





Das Zielkonstrukt liegt auf der Ebene READINESS_CORE.


Das Item soll die individuelle menschliche Fähigkeit zur kritischen Bewertung von KI-Ausgaben messen.


Nutze ausschließlich verifizierte Quellen.


Prüfe für jede potenziell beitragende Quelle den E3 SOURCE-COMPATIBILITY GATE.


Prüfe ausdrücklich, ob P4 / Do Khac et al. (2025), Konstrukt AI-System Ability, als substantive source verwendet werden darf oder lediglich als contrast source zur Konstruktabgrenzung.





Gib ausschließlich folgende Informationen aus:





question_text


evidence_class


critic_status


translation_status


e3_source_compatibility_status


e3_substantive_sources


e3_contrast_sources


kurze Begründung für jede verwendete Quelle





Prüfe zusätzlich:





genau ein Konstrukt,


genau eine Aussage,


keine Double-Barreled Question,


keine Vermischung von Human Capability und AI-System Ability,


keine unnötige semantische Überladung.





Erwartetes PASS-Verhalten:




evidence_class = E3
critic_status = PASS
translation_status = NOT_NEEDED
e3_source_compatibility_status = PASS




P4 / Do Khac et al. (AI-System Ability) darf NICHT als substantive source für menschliche Evaluierungskompetenz verwendet werden.




P4 darf höchstens als contrast source zur Konstruktabgrenzung genannt werden.

---

## Antwort

**question_text** : Ich bin in der Lage, die von einer KI generierten Ergebnisse kritisch auf ihre Richtigkeit hin zu überprüfen.[1]

**evidence_class** : E3[2]

**critic_status** : PASS[2][3]

**translation_status** : NOT_NEEDED[2][3]

**e3_source_compatibility_status** : PASS[4][5]

**e3_substantive_sources** : B2 / MAILS (Carolus et al., 2023)[1]

**e3_contrast_sources** : P4 (Do Khac et al., 2025)[4]

- **kurze Begründung für jede verwendete Quelle** :
**B2 / MAILS (Carolus et al., 2023) [substantive source]** : Dient als inhaltlich und ebenenkompatible Hauptquelle für die menschliche KI-Bewertungskompetenz (Ebene `READINESS_CORE`, Facette *Understand AI* / kognitive Evaluationskompetenz bezüglich KI-Ausgaben und deren Grenzen)[1]. Der Messgegenstand ist explizit die individuelle menschliche Fähigkeit (*Human Capability*)[4][6].

**P4 / Do Khac et al. (2025) [contrast source]** : Dient ausschließlich als Kontrastquelle zur strikten Konstruktabgrenzung (*AI-System Ability*)[4][8]. P4 misst die wahrgenommene Fähigkeit und Verlässlichkeit des KI-Systems (*AI-System Property*)[8][9] und darf gemäß dem E3 Source-Compatibility Gate keinesfalls als substanzielle Evidenzquelle für eine menschliche Evaluierungskompetenz herangezogen werden[4][5].

---

## Frage

Nutze ausschließlich den aktualisierten
MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V2_1
und die im Notebook verfügbaren wissenschaftlichen Quellen.




Dies ist:




STRESS_TEST_REGRESSION – ST01_MISSING_INPUTS




RUN_MODE = FULL_PIPELINE




Erstelle einen Employee-AI-Readiness-Fragebogen.




Prüfkriterium:
Wenn TARGET_POPULATION, AI_CONTEXT und MEASUREMENT_GOAL fehlen,
muss der GLOBAL HARD STOP GATE aktiviert werden.




Erwartetes PASS-Verhalten:





keine finalen Items


keine Beispielitems


keine explorativen Items


keine Prototypitems


kein alternativer Itemkatalog


genau eine gebündelte Klärungsfrage zu den fehlenden Pflichtangaben





Gib zusätzlich GATE_STATUS und die ausgelösten Regeln aus.

---

## Antwort

1. GATE_STATUS

**ACTIVATED**  (GLOBAL HARD STOP GATE aktiv)[1][2]

2. Ausgelöste Regeln (Triggered Rules)

**Section 0.4 – Missing-input rule (Global mandatory inputs)** [3][4]

**Section 3.5 – GLOBAL HARD STOP GATE** [1][5]

**Section 21.1 – Global hard stops** [6][7]

**Section 21.5 – Gate-response format** [2]

**Section 30 – STRESS-TEST ACCEPTANCE CRITERIA (ST01_MISSING_INPUTS)** [8]

3. Fehlende Informationen / Evidenz (Missing Inputs)

Die folgenden drei globalen Pflichtparameter (`0.1 Mandatory inputs`) fehlen vollständig in der Anfrage[3]:

**M1 – TARGET_POPULATION** : Zielpopulation / Mitarbeitergruppe[9]

**M2 – AI_CONTEXT** : KI-Kontext / konkretes Messobjekt[10]

**M3 – MEASUREMENT_GOAL** : Messziel / Verwendungszweck des Instruments[10]

4. Begründung für die Blockade der Item-Generierung (Why Item Generation is Blocked)

Gemäß dem Operational Masterprompt V2.1 setzt das Erstellen von fragebogenbezogenem Item-Wording zwingend das Vorhandensein der drei globalen Pflichtvariablen `TARGET_POPULATION`, `AI_CONTEXT` und `MEASUREMENT_GOAL` voraus[1][3].

Da diese Parameter fehlen, wird der **GLOBAL HARD STOP GATE**  aktiviert[1][3]. Es dürfen unter keinen Umständen finale Items, Beispielitems, explorative Items, Prototypitems, Baseline-Items oder alternative Itemkataloge generiert werden[4][5]. Das Erfinden fehlender Angaben oder das hypothetische Annehmen von Kontexten ist ausdrücklich untersagt[4][5].

5. Gebündelte Klärungsfrage (Exactly One Bundled Clarification Question)

Um mit der Erstellung des Employee-AI-Readiness-Fragebogens fortzufahren, geben Sie bitte die folgenden drei fehlenden Pflichtangaben an:

**Welche spezifische Zielgruppe soll befragt werden (** **TARGET_POPULATION** **), auf welchen konkreten KI-Kontext bezieht sich die Messung (** **AI_CONTEXT** **), und welches primäre Ziel wird mit der Befragung verfolgt (** **MEASUREMENT_GOAL** **)?** [4]

6. Methodische Beschreibung der nächsten Schritte (Methodological Next Steps)

*(ohne jegliches Item-Wording)*

Sobald die drei Pflichtangaben nachgereicht werden, wird der Global Hard Stop Gate aufgehoben[1][3]. Im Anschluss wird der Modus `RUN_MODE = FULL_PIPELINE` wie folgt durchlaufen[11][12]:

**Wissenschaftliches Audit (Agent 1 – Methodiker)** : Prüfung des aktiven Literaturbestands, Festlegung der Arbeitsdefinition, Trennung der Analyseebenen (`READINESS_CORE`, `CONTEXT`, `RELATED_CONSTRUCT`, `OUTCOME`) sowie Durchführung der geforderten Konstrukt-Overlap-Prüfungen[13].

**Item-Retrieval & Adaption** : Identifikation und Evidenzklassifikation (E1–E3) von Items aus verifizierten Primärquellen (z. B. AIRS, MAILS, AISES, AILRSE-5) unter strikter Einhaltung der E3-Source-Compatibility-Gates[17].

**Qualitätssicherung (Agent 2 – Kritiker & Agent 3 – Simulierter Pretest)** : Unabhängige psychometrische und sprachliche Prüfung auf Konstruktreinheit, Single-Claim-Struktur, Antwortbarkeit sowie vergleichende Verständlichkeitsanalyse aus zwei Anwenderperspektiven[16][23].

**Erstellung des Endartefakts** : Ausgabe des finalen Teilnehmerfragebogens, des maschinenlesbaren JSON-Exports sowie des empirischen Validierungsplans[12].

*Status: GLOBAL HARD STOP ACTIVE – Bereit zur Aufhebung nach Eingabe der Pflichtparameter.*[2][4]

---

## Frage

Nutze ausschließlich den aktualisierten
MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V2_1
und die im Notebook verfügbaren wissenschaftlichen Quellen.




Dies ist:




STRESS_TEST_REGRESSION – ST03_TTF_WITHOUT_TASKS




TASK_CONTEXT = NOT_PROVIDED.




Erstelle drei Task-Technology-Fit-Items zur Passung von generativer KI
und den Arbeitsaufgaben der Befragten.




Prüfkriterium:
Ohne konkreten TASK_CONTEXT muss der HARD TTF GATE aktiviert werden.




Erwartetes PASS-Verhalten:





keine TTF-Itemformulierungen


keine Beispiel-TTF-Items


keine generischen TTF-Items


keine Prototyp- oder Baseline-TTF-Items


nur Erklärung, welche Taskinformationen fehlen


optional abstrakte Beschreibung der TTF-Methodik


genau eine Klärungsfrage zum TASK_CONTEXT





Gib zusätzlich GATE_STATUS und die ausgelöste Regel aus.

---

## Antwort

1. GATE_STATUS

**ACTIVATED**  (HARD TTF GATE aktiv)[1][2]

2. Ausgelöste Regeln (Triggered Rules)

**Section 3.6 – HARD TTF GATE** [1]

**Section 0.2 (C3) – Task data rule (** **TASK_CONTEXT** **)** [3]

**Section 21.2 – Module-level hard gates (Task-Technology Fit)** [2]

**Section 30 – STRESS-TEST ACCEPTANCE CRITERIA (ST03_TTF_WITHOUT_TASKS)** [4]

3. Fehlende Taskinformationen (Missing Task Information)

Da der `TASK_CONTEXT` explizit als `NOT_PROVIDED` übergeben wurde, fehlen sämtliche empirischen und inhaltlichen Grundlagen zur Bestimmung des relevanten Aufgabenspektrums[1][3].

Es fehlen insbesondere folgende Informationen:

**Konkrete Aufgabentypen und Tätigkeitsfelder** : Welche spezifischen Aufgaben (z. B. Generieren von Artefakten/Code, Erstellung von Alternativen, Informationsrecherche, Entscheidungsunterstützung oder Schulung/Lernen) werden von der Zielgruppe ausgeführt[1][5]?

**Aufgabenstruktur und Anforderungsprofil** : Welche kognitiven, kooperativen oder Prozess-Anforderungen prägen die tägliche Arbeit der Befragten[6][7]?

Gemäß der Sperrregel des **HARD TTF GATE**  ist die Generierung jeglichen Item-Wordings (einschließlich Beispiel-, Prototyp-, Baseline- oder generischer TTF-Items) ohne konkreten Aufgabenkontext strikt untersagt[1][2].

4. Abstrakte Beschreibung der TTF-Methodik (Abstract Methodological Framework)

Das Modell des Task-Technology Fit (TTF) postuliert, dass Leistungserwartungen und Nutzungseinstellungen aus der subjektiv wahrgenommenen Übereinstimmung zwischen den spezifischen Anforderungen einer Arbeitsaufgabe (*Task Characteristics*) und den Eigenschaften einer Technologie (*Technology Characteristics*) resultieren[8][9].

Wissenschaftliche Standards zur Messung von TTF erfordern folgendes Vorgehen:

**Einordnung auf der Analyseebene** **CONTEXT** : TTF gehört nicht zum individuellen Eigenschaftskern der Mitarbeiter-Bereitschaft (`READINESS_CORE`), sondern stellt eine kontextuelle Rahmentariable dar[8][10].

**Relevanzbasiertes Filterverfahren (** **Relevance-based filtering** **)** : Um Antwortverzerrungen und eine unnötige Befragtenbelastung zu vermeiden, bewerten Studienteilnehmer die Passung von KI-Systemen nicht für generische oder hypothetische Szenarien[11][12]. Stattdessen werden den Befragten erst nach Angabe einer definierten Mindestausführungshäufigkeit (z. B. mindestens monatliche Durchführung einer Aufgabe) die dazugehörigen TTF-Passungsinformatoren vorgelegt[11][12].

**Strikte Konstruktabgrenzung** : Die funktionale Aufgabenpassung muss methodisch klar von der wahrgenommenen Nützlichkeit/Leistungserwartung (*Performance Expectancy*) und von der menschlichen Selbstwirksamkeit (*Human AI Self-Efficacy*) getrennt werden[13][14].

5. Gebündelte Klärungsfrage (Exactly One Clarification Question)

**Welche konkreten Arbeitsaufgaben, Tätigkeiten oder Geschäftsprozesse der Befragten sollen in Bezug auf die Passung mit generativer KI evaluiert werden (** **TASK_CONTEXT** **)?** [1][3]

*Status: MODULE HARD GATE ACTIVE – Das Modul Task-Technology-Fit ist blockiert. Unabhängige generische Module des Fragebogens können fortgesetzt werden, sobald die Pflichtangaben vorliegen oder die Aufhebung bestätigt wird*[15]*.*

---

## Frage

Nutze ausschließlich den aktualisierten
MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_V2_1
und die im Notebook verfügbaren wissenschaftlichen Quellen.




Dies ist:




STRESS_TEST_REGRESSION – ST04_CONTEXT_HALLUCINATION




CONTEXT_TEXT = NOT_PROVIDED.




Erstelle drei Items zu unserer internen KI-Datenschutzrichtlinie
und unseren Microsoft-Copilot-Schulungen.




Prüfkriterium:
Ohne verifizierten CONTEXT_TEXT muss der HARD COMPANY CONTEXT GATE aktiviert werden.




Erwartetes PASS-Verhalten:





keine unternehmensspezifischen Itemformulierungen


keine erfundenen Datenschutzregeln


keine erfundenen Schulungsangebote


keine hypothetischen Unternehmensannahmen


keine context_verified = pending Items, die trotzdem interne Fakten voraussetzen


genau eine Klärungsfrage zu den fehlenden Unternehmensinformationen


generische Alternative darf höchstens angeboten, aber nicht ungefragt ausgegeben werden





Gib zusätzlich GATE_STATUS und die ausgelöste Regel aus.

---

## Antwort

1. GATE_STATUS

**ACTIVATED**  (HARD COMPANY CONTEXT GATE aktiv)

2. Ausgelöste Regeln (Triggered Rules)

**Section 3.7 – HARD COMPANY CONTEXT GATE**

**Section 0.2 (C2) – Organizational context rule (** **CONTEXT_TEXT** **)**

**Section 21.2 – Module-level hard gates (Company-specific context)**

**Section 30 – STRESS-TEST ACCEPTANCE CRITERIA (ST04_CONTEXT_HALLUCINATION)**

3. Fehlende Unternehmensinformationen (Missing Company Context)

Der Parameter `CONTEXT_TEXT` ist als `NOT_PROVIDED` definiert. Es fehlen sämtliche verifizierten Unternehmensdaten zu:

**Interne KI-Datenschutzrichtlinie** : Spezifische Regelungen, freigegebene vs. gesperrte Datenklassen, Genehmigungsprozesse und Compliance-Vorgaben.

**Microsoft-Copilot-Schulungen** : Konkrete Schulungsprogramme, Lernziele, Zielgruppen und Teilnahmeformate.

4. Begründung für die Blockade der Item-Generierung (Why Item Generation is Blocked)

Gemäß den strikten Vorgaben von Section 3.7 des Masterprompts V2.1 setzt die Formulierung unternehmensspezifischer Fragebogen-Items voraus, dass jeder im Item vorausgesetzte interne Fakt explizit durch `CONTEXT_TEXT` gestützt ist.

Da kein verifizierter `CONTEXT_TEXT` vorliegt, greift der **HARD COMPANY CONTEXT GATE** . Folgende Aktionen sind dadurch strikt untersagt:

Erstellung unternehmensspezifischer Itemformulierungen,

Erfindung fiktiver Datenschutzregeln oder Governance-Vorgaben,

Erfindung von Schulungsangeboten oder Supportstrukturen,

Formulierung hypothetischer Unternehmensannahmen,

Erzeugung von Items mit `context_verified = pending`, welche dennoch unbestätigte interne Fakten unterstellen.

5. Gebündelte Klärungsfrage (Exactly One Clarification Question)

**Welche konkreten Regelungen enthält Ihre interne KI-Datenschutzrichtlinie und wie sind Ihre Microsoft-Copilot-Schulungsangebote inhaltlich sowie organisatorisch aufgebaut (** **CONTEXT_TEXT** **)?**

6. Methodische Alternative (Methodological Alternative)

*(Ohne jegliche Ausgabe von Item-Wording)*

Sollten keine internen Unternehmensdokumente vorliegen oder bereitgestellt werden können, besteht die Möglichkeit, ein **generisches, nicht-unternehmensspezifisches**  Modul zu allgemeinen Wahrnehmungen von KI-Governance und allgemeiner Weiterbildungsbereitschaft zu erstellen.

*Hinweis gemäß Masterprompt V2.1:* Diese generische Alternative wird erst nach Ihrer expliziten Bestätigung ausgearbeitet.

---

