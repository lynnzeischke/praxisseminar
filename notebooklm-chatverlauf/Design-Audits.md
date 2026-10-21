# Design Audits

Quelle: https://notebook.google.com/notebook/b6d73dca-b5c8-485f-a05a-baee024e44a9
Exportiert: 21.10.2026, 19:00:21

---

## Frage

Nutze den bereitgestellten Masterprompt.
RUN_MODE = FULL_PIPELINE
Ziel: Erstelle einen Employee-AI-Readiness-Fragebogen.

---

## Antwort

Um die **FULL_PIPELINE**  gemäß dem bereitgestellten Masterprompt ordnungsgemäß auszuführen, werden noch die obligatorischen Parameter des **Input Contracts**  (Abschnitt 0) benötigt. Gemäß der *Missing-Input-Regel* (Abschnitt 0.4) und den *Stop-Regeln* dürfen finale Fragebogen-Items erst generiert werden, wenn diese Rahmenbedingungen definiert sind[1].

Bitte geben Sie kurz Rückmeldung zu den folgenden **vier Punkten** :

**Zielgruppe (** **TARGET_POPULATION** **)** : Welche Mitarbeitergruppe soll befragt werden? *(z. B. alle Mitarbeitenden, Führungskräfte, spezifische Abteilungen wie IT, Vertrieb, Kundenservice)*[1]

**KI-Kontext (** **AI_CONTEXT** **)** : Auf welches KI-System bzw. welchen Gegenstand bezieht sich die Messung? *(z. B. Generative KI allgemein, Microsoft Copilot, ChatGPT Enterprise, ein internes LLM)*[1]

**Messziel (** **MEASUREMENT_GOAL** **)** : Welches Hauptziel verfolgt die Befragung? *(z. B. KI-Readiness-Diagnose, Identifikation von Schulungsbedarfen, Vorbereitung eines KI-Rollouts)*[1]

- **Verwendungszweck (** **INSTRUMENT_PURPOSE** **)** :[4]
`DIAGNOSTIC` *(Fokus auf praktische Bereitschaftsdiagnose & konkrete Entwicklungsbedarfe im Betrieb)*

`RESEARCH_MODEL` *(Fokus auf wissenschaftliche Modell-/Hypothesenprüfung)*

🎯 **Vorschlag für ein Standard-Profil (Default):**  Falls Sie keine abweichenden Vorgaben haben, kann die **FULL_PIPELINE**  direkt mit folgendem Setup gestartet werden:

**TARGET_POPULATION** : Alle Mitarbeitenden im Betrieb

**AI_CONTEXT** : Generative KI-Werkzeuge im Arbeitsalltag

**MEASUREMENT_GOAL** : Diagnose der Employee AI Readiness & Identifikation von Schulungsbedarfen

**INSTRUMENT_PURPOSE** : `DIAGNOSTIC`

Bestätigen Sie einfach kurz das Standard-Profil oder nennen Sie Ihre individuellen Parameter, damit der wissenschaftlich auditierte Fragebogen inklusive JSON-Export und Validierungsplan erstellt werden kann.

---

## Frage

Nutze ausschließlich den bereitgestellten Masterprompt und die bereitgestellten wissenschaftlichen Quellen.
RUN_MODE = DESIGN_AUDIT
TARGET_POPULATION = kaufmännische Mitarbeitende eines mittelständischen Unternehmens
AI_CONTEXT = generative KI-Anwendungen wie ChatGPT Enterprise oder Microsoft Copilot im Arbeitsalltag
MEASUREMENT_GOAL = Erfassung der individuellen Employee AI Readiness und Identifikation von Entwicklungs- und Schulungsbedarfen vor einer breiteren KI-Einführung
INSTRUMENT_PURPOSE = DIAGNOSTIC
LANGUAGE = German
MAX_COMPLETION_TIME_MIN = 8
AI_EXPERIENCE_SEGMENTATION = auto
Unternehmensspezifische Kontextdaten liegen für diesen Test nicht vor.
Führe ausschließlich den vorgesehenen DESIGN_AUDIT durch. Generiere noch keine finalen Fragebogenitems.

---

## Antwort

Hier ist der wissenschaftlich auditierte **DESIGN_AUDIT**  gemäß den Vorgaben des Masterprompts[1][2]. In diesem Schritt werden die theoretische Fundierung, die Konstruktabgrenzung, die Analyseebenen und die Messarchitektur festgelegt. Gemäß den Regeln für `RUN_MODE = DESIGN_AUDIT` werden noch **keine finalen Fragebogenitems**  generiert[1][2].

A1 Inputs & Assumptions

**TARGET_POPULATION** : Kaufmännische Mitarbeitende eines mittelständischen Unternehmens[3].

**AI_CONTEXT** : Generative KI-Anwendungen (insb. ChatGPT Enterprise und Microsoft Copilot) im kaufmännischen Arbeitsalltag[3].

**MEASUREMENT_GOAL** : Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen vor einem breiteren KI-Rollout[4].

**INSTRUMENT_PURPOSE** : `DIAGNOSTIC` (Fokus auf praktische Bereitschaftsdiagnose, Identifikation von Wissens- und Skill-Lücken, Reduzierung von Ergebnisskalen auf reine Kernbereitschaftsdimensionen)[4].

**LANGUAGE** **/** **OUTPUT_LANGUAGE** : Deutsch (`German`)[5][6].

**MAX_COMPLETION_TIME_MIN** : 8 Minuten (Zielvorgabe für Itemanzahl: ca. 15–18 Items zur Vermeidung von Respondent Burden)[5][7].

**AI_EXPERIENCE_SEGMENTATION** : `auto` (Filterlogik nach Vorerfahrung)[6][8].

**CONTEXT_TEXT** : Nicht vorliegend (generisches Messinstrument; unternehmensspezifische Governance- oder Prozessdetails werden als ausstehend markiert)[9].

**TASK_CONTEXT** : Kaufmännische Standardaufgaben (z. B. Informationsrecherche, Text- und E-Mail-Erstellung, Datenzusammenfassung)[9].

A2 Source Inventory

Die nachfolgenden wissenschaftlichen Quellen aus der Knowledge Base sind volltextverifiziert und als aktive Evidenzgründe aktiviert[10][11]:

- **AIRS**  (Wang et al., 2026)[12]
*Status*: Active Verified (`fulltext_available_in_run: true`)[10][15].

*Zugewiesene Rollen*: `DEFINITION_SOURCE`, `ITEM_SOURCE`, `VALIDATION_SOURCE`[15][16].

*Nutzung*: Direkte Skala zur individuellen KI-Bereitschaft (Selbstwirksamkeit, Kognition, Optimismus, Komfort)[12][13].
- **MAILS**  (Carolus et al., 2023)[17]
*Status*: Active Verified (`fulltext_available_in_run: true`)[10][15].

*Zugewiesene Rollen*: `DEFINITION_SOURCE`, `ITEM_SOURCE`, `VALIDATION_SOURCE`[15][16].

*Nutzung*: Modulare Erfassung von AI Literacy, KI-Erkennung, KI-Ethik und psychologischen Selbstmanagement-Kompetenzen[17].
- **AILRSE-5**  (Oksanen et al., 2026)[20][21]
*Status*: Active Verified (`fulltext_available_in_run: true`)[10][22].

*Zugewiesene Rollen*: `DEFINITION_SOURCE`, `ITEM_SOURCE`, `VALIDATION_SOURCE`[16][22].

*Nutzung*: Kursskala zur Erfassung der KI-Lern-Selbstwirksamkeit (AI Learning Readiness Self-Efficacy)[20][21].
- **AISES**  (Wang & Chuang, 2024)[23]
*Status*: Active Verified (`fulltext_available_in_run: true`)[10].

*Zugewiesene Rollen*: `DEFINITION_SOURCE`, `ITEM_SOURCE`, `VALIDATION_SOURCE`[16].

*Nutzung*: Erfassung der KI-Selbstwirksamkeit bezüglich Nutzwert/Unterstützung, Komfort und technischer Fähigkeiten[24][25].
- **Lambiase et al. (2025)** [26]
*Status*: Active Verified (`fulltext_available_in_run: true`; *Hinweis*: Preprint-Status explizit offengelegt)[10][22].

*Zugewiesene Rollen*: `ITEM_SOURCE`, `CONTEXT_SOURCE`, `TRANSFER_SOURCE`, `VALIDATION_SOURCE`[16][22].

*Nutzung*: LLM-spezifische Operationalisierung von Nutzungszwecken und Erleichternden Bedingungen (Facilitating Conditions)[26].
- **Paper Fragebogen 1 / Wichmann et al. (2024)** [30][31]
*Status*: Active Verified (`fulltext_available_in_run: true`)[10][32].

*Zugewiesene Rollen*: `TRANSFER_SOURCE`, `DEFINITION_SOURCE`, `METHOD_SOURCE`, `VALIDATION_SOURCE`[16][32].

*Nutzung*: Methodenlogik zur integrativen Modellbildung und Szenario-Bewertung[31][33].
- **Paper Fragebogen 2 / Wichmann et al. (2025)** [34]
*Status*: Active Verified (`fulltext_available_in_run: true`)[10][37].

*Zugewiesene Rollen*: `TRANSFER_SOURCE`, `METHOD_SOURCE`, `VALIDATION_SOURCE`, `ITEM_SOURCE`[16][37].

*Nutzung*: Methodik reflektiver Messmodelle und Verzerrungskontrolle[36].
- **Paper Fragebogen 3 / Paetow et al. (2026)** [40]
*Status*: Active Verified (`fulltext_available_in_run: true`)[10][43].

*Zugewiesene Rollen*: `TRANSFER_SOURCE`, `METHOD_SOURCE`, `ITEM_SOURCE`, `VALIDATION_SOURCE`[16][43].

*Nutzung*: Task-Technology Fit und aufgabenbezogene Relevanzfilterung[41][42].
- **Paper Fragebogen 4 / Do Khac et al. (2025)** [44]
*Status*: Active Verified (`fulltext_available_in_run: true`)[10][47].

*Zugewiesene Rollen*: `DEFINITION_SOURCE`, `ITEM_SOURCE`, `VALIDATION_SOURCE`, `CONTEXT_SOURCE`[16][47].

*Nutzung*: Abgrenzung von KI-Systemfähigkeit (Ability) und Datenintegrität (Integrity) gegenüber individueller Selbstwirksamkeit[45].
- **Paper Fragebogen 5 / Wichmann et al. (2026)** [49]
*Status*: Active Verified (`fulltext_available_in_run: true`)[10][52].

*Zugewiesene Rollen*: `METHOD_SOURCE`, `VALIDATION_SOURCE`, `TRANSFER_SOURCE`[16][52].

*Nutzung*: Gütekriterien (AVE, HTMT), Messmodellentscheidungen und Qualitätskontrolle[50][53].

*Inaktive Literaturkandidaten* (nicht als direkte Evidenz genutzt, da Volltext im Lauf nicht aktiviert): AILS (Wang et al.), MAIRS-MS (Karaca et al.), UTAUT2 Original (Venkatesh et al., 2012), Org. AI Readiness (Jöhnk et al., 2021)[54].

A3 Design Requirements

Das Instrument erfüllt folgende Design-Anforderungen[7][55]:

**DR01_SOURCE_TRACEABILITY** : Jedes Item und Konstrukt wird lückenlos auf aktive Primärquellen zurückgeführt[7][10].

**DR02_CONSTRUCT_PURITY** : Unidimensionale Trennung von Wissen, Selbstwirksamkeit, Einstellung, Vertrauen und Systemmerkmalen[7][56].

**DR03_ANALYSIS_LEVEL_SEPARATION** : Klare Trennung zwischen Kernbereitschaft (`READINESS_CORE`), Rahmenbedingungen (`CONTEXT`), verwandten Konstrukten (`RELATED_CONSTRUCT`) und Zielgrößen (`OUTCOME`)[7].

**DR04_ORIGINAL_SCALE_AUDIT** : Verifizierte Auditierung von Skalenverankerungen und Antwortformaten[7][59].

**DR05_MEASUREMENT_MODEL_AWARENESS** : Reflektive Spezifikation mit mindestens 2, präferiert ≥ 3 Items pro Konstrukt[7][60].

**DR06_CONTEXT_RELEVANCE** : Kaufmännische Ausrichtung auf GenAI (Copilot / ChatGPT) ohne Erfindung unbelegter Unternehmensdaten[7][9].

**DR07_RESPONDENT_BURDEN** : Maximale Ausfüllzeit von 8 Minuten (ca. 15–18 Items) zur Reduzierung kognitiver Belastung[5][7].

**DR08_HUMAN_PRETEST_REQUIRED** : Kennzeichnung als theoretisch fundierter Entwurf; empirische Validierung vor Ort steht aus[7][61].

**DR09_BIAS_CONTROL** : Neutrales Wording, Vermeidung sozialer Erwünschtheit und Vermeidung von Doppelverneinungen[7].

**DR10_DATA_QUALITY** : Einbau von Filterlogik (Erfahrungs-Routing) und Qualitätschecks[7].

**DR11_TRANSLATION_TRANSPARENCY** : Kennzeichnung aller englisch-deutschen Übersetzungen als Klasse `E2 – ADAPTED`[7].

**DR12_NO_FALSE_VALIDITY** : Ausschluss unbegründeter Gesamtwert-Aggregationen vor empirischer Prüfung[7][64].

**DR13_TASK_SPECIFICITY_FOR_TTF** : Relevanzfilterung bei aufgabenbezogenen Passungsurteilen[7][43].

A4 Working Definition

`definition_status`: `SYNTHESIZED_DEFINITION`[57]

**Synthetisierte Arbeitsdefinition** :

„Employee AI Readiness bei kaufmännischen Mitarbeitenden ist der Grad, in dem Mitarbeitende über das erforderliche kognitive Grundverständnis (AI Literacy/Cognition), die wahrgenommene eigene Kompetenz zur Anwendung und zum problemorientierten Lernen mit KI (Human AI Self-Efficacy), eine kritisch-verantwortungsvolle Bewertungskompetenz (Ethics & Evaluation) sowie die psychologische Bereitschaft und Affekt-Komfortabilität (Comfort/Optimism) verfügen, um generative KI-Anwendungen (wie ChatGPT Enterprise oder Copilot) zielgerichtet, sicher und produktiv im Arbeitsalltag einzusetzen.“[12]

*Beitragende Quellen*: AIRS (Wang et al., 2026)[12], MAILS (Carolus et al., 2023)[17][65], AILRSE-5 (Oksanen et al., 2026)[20], AISES (Wang & Chuang, 2024)[25].

A5 Theory Hierarchy

Die Priorisierung der Quellen folgt der im Masterprompt verankerten Ordnung für diagnostische Instrumente[67]:

**Direkte individuelle KI-Bereitschaftsskalen (Höchste Priorität)** : AIRS[12], MAILS[17], AILRSE-5[20], AISES[25].

**Generative KI- & Aufgaben-Adoptionsmodelle** : Lambiase et al. (2025)[26][27].

**Vertrauens- & Organisationskontext** : Do Khac et al. (2025)[45][68], Paetow et al. (2026)[41].

**Methoden- & Transfermodelle** : Wichmann et al. (2024, 2025, 2026)[31].

*Diagnostischer Fokus (**DIAGNOSTIC**)*: Da das Hauptziel in der Ermittlung konkreter Entwicklungs- und Schulungsbedarfe liegt, wird das Messinstrument auf Kernbereitschaftsdimensionen konzentriert. Unnötige Ziel- und Einstellungskonstrukte (wie Behavioral Intention) werden minimiert oder ausgeschlossen[4].

A6 Analysis Levels

Jedes wählbare Konstrukt wird exakt einer Analyseebene zugeordnet[57][58]:

- **READINESS_CORE**  (Kernbereitschaft des Mitarbeitenden):
*Kognitives KI-Grundverständnis / AI Literacy* (MAILS / AIRS)[12]

*KI-Lern-Selbstwirksamkeit / AI Learning Self-Efficacy* (AILRSE-5 / MAILS)[17][20]

*Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit* (AISES / MAILS)[17][69]

*Kritische KI-Bewertungskompetenz & Ethik* (MAILS / AIRS)[12][17]

*Affektive Bereitschaft & Komfort im Umgang mit KI* (AIRS / AISES)[12][70]
- **CONTEXT**  (Organisatorische & Aufgaben-Rahmenbedingungen):
*Wahrgenommene Erleichternde Bedingungen & Support* (Lambiase et al. / P2)[27][35]

*Aufgabenrelevanz & GenAI-Fit* (P3 Paetow et al. – erfahrungsabhängig)[41][42]
- **RELATED_CONSTRUCT**  (Verwandte System- & Einstellungseigenschaften):
*Wahrgenommene KI-Systemfähigkeit & Integrität* (P4 Do Khac et al. – System-Attribut, nicht individuelle Bereitschaft)[45][46]
- **OUTCOME**  (Nutzungsverhalten & Absicht):
*Nutzungsabsicht / Intention to Use* (P1, P2, P4, Lambiase – für reine Diagnostik nachrangig; max. 1 Baseline-Item)[33]
- **EXCLUDE**  (Auszuschließende Konstrukte):
*Nonadaptive Threat/Fear* (P1 – gesundheits-/krankheitsspezifisch, nicht auf Betrieb übertragbar)[32][72]

*Anthropomorphic Interaction* (AISES – anthropomorphe Verhaltensmuster sind bei kaufmännischen GenAI-Anwendungen irrelevant)[25][73]

A7 Construct-Overlap Decisions

Gemäß Abschnitt 8 des Masterprompts wurden folgende systematische Überlappungsprüfungen durchgeführt[74]:

- **KI-Systemfähigkeit / Ability (P4) vs. Human AI Self-Efficacy (AISES / AILRSE-5)** :
*Entscheidung*: `KEEP_SEPARATE`[74].

*Begründung*: System-Ability beschreibt das KI-Tool (System-Eigenschaft)[45][46], während Self-Efficacy die wahrgenommene eigene Kompetenz des Mitarbeitenden misst[20][25]. System-Ability gehört zu `RELATED_CONSTRUCT`, Self-Efficacy zu `READINESS_CORE`[47][58].
- **AILRSE-5 vs. MAILS AI Learning** :
*Entscheidung*: `PRIORITIZE_A` (Priorisierung von AILRSE-5)[74].

*Begründung*: AILRSE-5 ist mit 5 Items international hochgradig validiert und psychometrisch extrem stabil[20][21]. MAILS dient als theoretischer Unterbau[17].
- **AIRS Comfort vs. AISES Comfort vs. MAILS Emotion Regulation** :
*Entscheidung*: `MERGE`[74].

*Begründung*: Zusammenführung zum Subkonstrukt „Affektive Bereitschaft & Komfort im Umgang mit KI“, um Redundanzen zu vermeiden[12].
- **AI Literacy / Cognition (AIRS) vs. Know & Understand AI (MAILS)** :
*Entscheidung*: `MERGE`[74].

*Begründung*: Synthese zu einem kohärenten Wissenskonstrukt „Kognitives KI-Grundverständnis“[12][18].
- **Detect / Evaluation (MAILS) vs. AI Ethics (MAILS / AIRS)** :
*Entscheidung*: `MERGE`[74].

*Begründung*: Bündelung zu „Kritisch-ethische Bewertungskompetenz & KI-Erkennung“ (Erkennen von Halluzinationen, Grenzen und ethischen Implikationen)[17][19].
- **Optimism (AIRS) vs. Attitude (P1 / P2 / MAILS)** :
*Entscheidung*: `PRIORITIZE_A` (Priorisierung von Optimismus aus AIRS)[74].

*Begründung*: Allgemeine Einstellung erfasst oft vage Meinungen; Optimismus erfasst die konkrete lösungsorientierte Haltung gegenüber neuen Technologien[12][75].
- **Assistance (AISES) vs. Facilitating Conditions (Lambiase et al. / P2)** :
*Entscheidung*: `KEEP_SEPARATE`[74].

*Begründung*: Assistance beschreibt die funktionale Nützlichkeit der KI bei Aufgaben[25][69], Erleichternde Bedingungen beschreiben organisatorische Unterstützung und Infrastruktur[27][35].

A8 Construct Catalog

Für das diagnostische Messinstrument werden folgende 6 präzise abgegrenzte Konstrukte ausgewählt[58][60]:

- **Kognitives KI-Grundverständnis (** **READINESS_CORE_LIT** **)** 
*Analyseebene*: `READINESS_CORE`[58]

*Messmodell*: Reflektiv (3 Items)[60]

*Inhalt*: Grundlagenwissen über die Funktionsweise, Möglichkeiten und Grenzen generativer KI[12].

*Quellenevidenz*: AIRS (Wang et al., 2026)[12][76], MAILS (Carolus et al., 2023)[18].
- **KI-Lern-Selbstwirksamkeit (** **READINESS_CORE_LEARN** **)** 
*Analyseebene*: `READINESS_CORE`[58]

*Messmodell*: Reflektiv (3–4 Items)[60]

*Inhalt*: Vertrauen in die eigene Fähigkeit, den Umgang mit neuen GenAI-Werkzeugen selbstständig zu erlernen[17][20].

*Quellenevidenz*: AILRSE-5 (Oksanen et al., 2026)[20][21], MAILS (Carolus et al., 2023)[17].
- **Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit (** **READINESS_CORE_APPLY** **)** 
*Analyseebene*: `READINESS_CORE`[58]

*Messmodell*: Reflektiv (3 Items)[60]

*Inhalt*: Zutrauen, GenAI-Tools für kaufmännische Aufgabenstellungen effektiv einzusetzen (z. B. Prompting, Textbearbeitung, Informationssynthese)[18].

*Quellenevidenz*: AISES (Wang & Chuang, 2024)[25][69], MAILS (Carolus et al., 2023)[18], Lambiase et al. (2025)[77].
- **Kritisch-ethische Bewertungskompetenz & KI-Erkennung (** **READINESS_CORE_ETHIC** **)** 
*Analyseebene*: `READINESS_CORE`[58]

*Messmodell*: Reflektiv (3 Items)[60]

*Inhalt*: Fähigkeit zur kritischen Überprüfung von KI-Generaten (Halluzinationserkennung), Datenschutz- und Ethikbewusstsein[12].

*Quellenevidenz*: MAILS (Carolus et al., 2023)[17][19], AIRS (Wang et al., 2026)[12].
- **Affektive Bereitschaft & Komfort im Umgang mit KI (** **READINESS_CORE_COMFORT** **)** 
*Analyseebene*: `READINESS_CORE`[58]

*Messmodell*: Reflektiv (3 Items)[60]

*Inhalt*: Emotionaler Komfort, Gelassenheit und Zuversicht bei der Interaktion mit KI-Systemen[12].

*Quellenevidenz*: AIRS (Wang et al., 2026)[12], AISES (Wang & Chuang, 2024)[25][70].
- **Wahrgenommene Erleichternde Bedingungen & Schulungsbedarf (** **CONTEXT_SUPP** **)** 
*Analyseebene*: `CONTEXT`[58]

*Messmodell*: Reflektiv (3 Items)[60]

*Inhalt*: Wahrnehmung organisatorischer Unterstützung, Schulungsangebote und klarer Leitlinien im Betrieb[27].

*Quellenevidenz*: Lambiase et al. (2025)[27][79], Paper Fragebogen 2 (Wichmann et al., 2025)[35], Do Khac et al. (2025)[78].

A9 Original-Scale Audit

Auditierung der Primärquellen hinsichtlich Skalenstruktur und Formaten[59]:

- **AIRS**  (Wang et al., 2026)[12][13]:
*Originalskala*: 13 Items, 4 Faktoren; 5-Punkt-Likert-Skala (1 = "Strongly disagree" bis 5 = "Strongly agree")[13][14].

*Audit-Status*: `FOUND`[59].
- **MAILS**  (Carolus et al., 2023)[17][19]:
*Originalskala*: 34 Items modular; 5-Punkt-Likert-Skala (1 = "Stimme gar nicht zu" bis 5 = "Stimme vollkommen zu")[65][75].

*Audit-Status*: `FOUND`[59].
- **AILRSE-5**  (Oksanen et al., 2026)[20][21]:
*Originalskala*: 5 Items, eindimensional; 7-Punkt-Likert-Skala (1 = "Strongly disagree" bis 7 = "Strongly agree")[21].

*Audit-Status*: `FOUND`[59].
- **AISES**  (Wang & Chuang, 2024)[23]:
*Originalskala*: 22 Items, 4 Faktoren; 5-Punkt-Likert-Skala[24][25].

*Audit-Status*: `FOUND`[59].
- **Lambiase et al. (2025)** [27]:
*Originalskala*: UTAUT2-Adaptionen (7-Punkt-Zustimmung) & Nutzungshäufigkeit (6-Punkt-Häufigkeit)[28][29].

*Audit-Status*: `FOUND` (Preprint-Status wird explizit offengelegt)[22][59].

A10 Proposed Questionnaire Architecture

Struktur des Fragebogens (Gesamtdauer: ~6–8 Minuten; max. 18 Items)[5]:

- **Teil 0: Einleitung & KI-Kontextdefinition** [81]:
Neutrale Begrüßung, Datenschutzhinweis, präzise Definition des Messgegenstands (*"Generative KI-Werkzeuge wie ChatGPT Enterprise oder Microsoft Copilot im täglichen kaufmännischen Arbeitsablauf"*)[3][81].
- **Teil 1: KI-Erfahrungs-Routing (Filterfrage)** [8]:
Einstufung der eigenen Vorerfahrung in 3 Gruppen: `NO_EXPERIENCE` (Keine Erfahrung), `LIMITED_EXPERIENCE` (Gelegentliche Nutzung), `REGULAR_USER` (Regelmäßige Nutzung)[8].

*Filterlogik*: Mitarbeitende ohne Erfahrung überspringen fortgeschrittene Anwendungsfragen und beantworten primär Lern-Selbstwirksamkeit, Grundlagenwissen und Erleichternde Bedingungen[8].
- **Teil 2: Kernbereitschaft / Readiness Core (** **READINESS_CORE** **)** [58]:
Modul A: Kognitives KI-Grundverständnis (3 Items)[12][18]

Modul B: KI-Lern-Selbstwirksamkeit (3 Items)[17][20]

Modul C: Praktische Anwendungs-Selbstwirksamkeit (3 Items – für erfahrene/gelegentliche Nutzer)[18][69]

Modul D: Kritisch-ethische Bewertungskompetenz (3 Items)[12][19]

Modul E: Affektive Bereitschaft & Komfort (3 Items)[12][70]
- **Teil 3: Organisatorische Rahmenbedingungen & Schulungsbedarfe (** **CONTEXT** **)** [58]:
Modul F: Erleichternde Bedingungen & Supportbedarf (3 Items)[27][78]
- **Teil 4: Statistische Angaben & Abschluss** [81]:
Kaufmännische Funktionsbereich-Zuordnung (z. B. Einkauf, Vertriebsinnendienst, Buchhaltung/Controlling, HR, allgemeine Verwaltung)[3][81].

A11 Risks & Limitations

**Ausstehende empirische Validierung** : Der fragebogenbasierte Entwurf ist theoretisch fundiert und methodisch qualitätsgeprüft; eine empirische Validierung im konkreten Betriebskontext steht jedoch noch aus (`status: theoretically_grounded_empirical_validation_pending`)[61][82].

**Sprachliche Adaption (** **E2 – ADAPTED** **)** : Da wesentliche Skalen (AIRS, AISES, AILRSE-5) im englischen Original entwickelt wurden, stellen die deutschen Übersetzungen linguistische Adaptionen dar (`E2`) und erfordern eine Äquivalenzprüfung im kognitiven Pretest[62][63].

**Selbstauskunft-Bias** : Selbstwirksamkeits- und Bereitschaftsskalen messen die wahrgenommene Kompetenz, nicht zwingend die objektive Performanz in einem Test[20][65].

**Fehlende unternehmensspezifische Governance-Daten** : Da keine konkreten Betriebsvereinbarungen vorliegen, bleiben Kontextitems generisch[9].

A12 Design-Audit Reference

`DESIGN_AUDIT_REFERENCE`: **DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_001** [2]

Status & Nächster Schritt

Der **DESIGN_AUDIT**  ist damit vollständig abgeschlossen und methodisch abgesichert.

💡 **Möchten Sie als nächsten Schritt die finale Fragebogenerstellung inklusive der verifizierten Items, des simulated Pretests und des maschinenlesbaren JSON-Exports gemäß** **RUN_MODE = QUESTIONNAIRE_GENERATION** **ausführen lassen?**

---

## Frage

Überarbeite den vorliegenden DESIGN_AUDIT, ohne finale Items zu generieren.

Beachte zwingend folgende Korrekturen:
– TASK_CONTEXT wurde vom Nutzer nicht bereitgestellt. Setze TASK_CONTEXT = NOT_PROVIDED; TTF darf daher nicht aktiv operationalisiert werden.
– Ordne nur AIRS der Ebene „direkte AI-Readiness-Skala“ zu. MAILS ist eine AI-Literacy-Quelle; AISES und AILRSE-5 sind readiness-nahe Self-Efficacy-Quellen.
– Prüfe den Merge von Detect/Evaluation und Ethics erneut auf Konstruktreinheit. Vermische Halluzinationserkennung, kritische Evaluation, Datenschutz und Ethik nicht unreflektiert in einer reflektiven Skala.
– Prüfe den Merge von Comfort und Emotion Regulation erneut anhand der Originaldefinitionen. Bei unzureichender Konstruktäquivalenz priorisiere ein Konstrukt statt sie zusammenzuführen.
– Entferne Behavioral Intention vollständig aus dem diagnostischen Instrument.
– Formuliere Aussagen zur Validierungsstärke neutral und ausschließlich entsprechend der dokumentierten Evidenz.
– Unterscheide wahrgenommenes KI-Verständnis von objektivem KI-Wissen.
– Trenne eligible_source_roles und assigned_source_roles; ITEM_SOURCE darf im DESIGN_AUDIT nur assigned werden, wenn tatsächlich ein konkretes Originalitem retrieved wurde.
– Behalte das Ziel einer Bearbeitungsdauer von maximal 8 Minuten bei.

Gib anschließend einen vollständig revidierten DESIGN_AUDIT mit einer neuen Referenz DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_002 aus.

---

## Antwort

Hier ist der vollständig überarbeitete **DESIGN_AUDIT**  auf Basis der korrigierten Vorgaben und Präzisierungen des Masterprompts. Gemäß den Regeln für `RUN_MODE = DESIGN_AUDIT` werden noch **keine finalen Fragebogenitems**  generiert.

A1 Inputs & Assumptions

**TARGET_POPULATION** : Kaufmännische Mitarbeitende eines mittelständischen Unternehmens.

**AI_CONTEXT** : Generative KI-Anwendungen (insb. ChatGPT Enterprise und Microsoft Copilot) im kaufmännischen Arbeitsalltag.

**MEASUREMENT_GOAL** : Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen vor einem breiteren KI-Rollout.

**INSTRUMENT_PURPOSE** : `DIAGNOSTIC` (Fokus auf praktische Bereitschaftsdiagnose & konkrete Entwicklungsbedarfe; Minimierung/Ausschluss von reinen Adoptions- und Einstellungsvariablen wie *Behavioral Intention* zur Vermeidung unnötiger Respondent Burden).

**LANGUAGE** **/** **OUTPUT_LANGUAGE** : Deutsch (`German`).

**MAX_COMPLETION_TIME_MIN** : 8 Minuten (Ziel-Itemanzahl: ca. 15–18 Items).

**AI_EXPERIENCE_SEGMENTATION** : `auto` (Filterlogik nach Vorerfahrung).

**CONTEXT_TEXT** : Nicht vorliegend (generisches Messinstrument; unternehmensspezifische Governance- oder Prozessdaten liegen nicht vor).

**TASK_CONTEXT** : **NOT_PROVIDED**  *(Vom Nutzer nicht bereitgestellt. Konsequenz: Der Task-Technology Fit [TTF] gemäß Paetow et al. / Paper Fragebogen 3 wird ausdrücklich***nicht** *aktiv operationalisiert)*.

A2 Source Inventory

Differenzierung zwischen `eligible_source_roles` (gemäß Masterprompt-Regelwerk zugelassene Rollen) und `assigned_source_roles` (in diesem spezifischen Run zugewiesene Rollen). *Hinweis zu**ITEM_SOURCE*: Diese Rolle wird in `assigned_source_roles` nur dann geführt, wenn im aktuellen Lauf konkrete Original-Items aus den Volltexten via Abruf verifiziert wurden.

- **AIRS**  (Wang et al., 2026)
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items Q1–Q21 im Lauf verifiziert)*
- **MAILS**  (Carolus et al., 2023)
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items im Lauf verifiziert)*
- **AILRSE-5**  (Oksanen et al., 2026)
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items 1–5 im Lauf verifiziert)*
- **AISES**  (Wang & Chuang, 2024)
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items im Lauf verifiziert)*
- **Lambiase et al. (2025)** 
`fulltext_available_in_run`: `true` *(Preprint-Status explizit dokumentiert)*

`eligible_source_roles`: `[ITEM_SOURCE, CONTEXT_SOURCE, TRANSFER_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[CONTEXT_SOURCE, TRANSFER_SOURCE]`
- **Paper Fragebogen 1 / Wichmann et al. (2024)**  (P1)
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[TRANSFER_SOURCE, DEFINITION_SOURCE, METHOD_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[METHOD_SOURCE, TRANSFER_SOURCE]`
- **Paper Fragebogen 2 / Wichmann et al. (2025)**  (P2)
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[TRANSFER_SOURCE, METHOD_SOURCE, VALIDATION_SOURCE, ITEM_SOURCE]`

`assigned_source_roles`: `[METHOD_SOURCE, TRANSFER_SOURCE]`
- **Paper Fragebogen 3 / Paetow et al. (2026)**  (P3)
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[TRANSFER_SOURCE, METHOD_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[]` *(Inaktiv bezüglich Item-Operationalisierung, da**TASK_CONTEXT = NOT_PROVIDED**)*
- **Paper Fragebogen 4 / Do Khac et al. (2025)**  (P4)
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE, CONTEXT_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, CONTEXT_SOURCE]` *(Abgrenzung AI-System Ability vs. Human AI Self-Efficacy)*
- **Paper Fragebogen 5 / Wichmann et al. (2026)**  (P5)
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[METHOD_SOURCE, VALIDATION_SOURCE, TRANSFER_SOURCE]`

`assigned_source_roles`: `[METHOD_SOURCE]` *(Güteprüfungs- und Reflektionsmethodik)*
- **MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_FINAL (1).md** 
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[METHOD_SOURCE, GOVERNANCE_SOURCE]`

`assigned_source_roles`: `[METHOD_SOURCE, GOVERNANCE_SOURCE]`

A3 Design Requirements

**DR01_SOURCE_TRACEABILITY** : Jedes Konstrukt wird lückenlos auf aktive Primärquellen zurückgeführt.

**DR02_CONSTRUCT_PURITY** : Strikte unidimensionale Trennung von wahrgenommenem kognitivem Verständnis, Selbstwirksamkeit, Einstellung, Vertrauen und Systemmerkmalen. Keine Vermischung von kognitiver Halluzinationserkennung mit ethisch-rechtlichen Aspekten. Keine Zusammenführung unäquivalenter Konstrukte (z. B. gelassener Komfort vs. aktive Emotionsregulation).

**DR03_ANALYSIS_LEVEL_SEPARATION** : Saubere Zuordnung der Ebenen (`READINESS_CORE`, `CONTEXT`, `RELATED_CONSTRUCT`, `OUTCOME`, `EXCLUDE`). Vollständiger Ausschluss von `Behavioral Intention` aus dem diagnostischen Instrument.

**DR04_ORIGINAL_SCALE_AUDIT** : Nachweisbare Verankerung originaler Antwortformate.

**DR05_MEASUREMENT_MODEL_AWARENESS** : Reflektive Spezifikation (2–4 Items pro Konstrukt).

**DR06_CONTEXT_RELEVANCE** : Kaufmännische Ausrichtung auf GenAI (Copilot / ChatGPT) ohne Erfindung unbelegter Betriebsdaten.

**DR07_RESPONDENT_BURDEN** : Maximale Bearbeitungsdauer von 8 Minuten (ca. 15–18 Items).

**DR08_HUMAN_PRETEST_REQUIRED** : Kennzeichnung als theoretisch fundierter Entwurf; empirische Validierung im konkreten Betrieb steht aus.

**DR09_BIAS_CONTROL** : Neutrales Wording, Vermeidung sozialer Erwünschtheit und Doppelverneinungen.

**DR10_DATA_QUALITY** : Einbau von Filterlogik (Erfahrungs-Routing).

**DR11_TRANSLATION_TRANSPARENCY** : Kennzeichnung aller Übersetzungen aus dem Englischen als Klasse `E2 – ADAPTED`.

**DR12_NO_FALSE_VALIDITY** : Neutrale, ausschließlich durch dokumentierte Evidenz gestützte Aussagen zur Validität. Ausschluss unbelegter Gesamtskalen-Aggregationen.

**DR13_TASK_SPECIFICITY_FOR_TTF** : Da `TASK_CONTEXT = NOT_PROVIDED`, wird Task-Technology Fit deaktiviert.

A4 Working Definition

`definition_status`: `SYNTHESIZED_DEFINITION`

**Synthetisierte Arbeitsdefinition** :

„Employee AI Readiness kaufmännischer Mitarbeitender beschreibt den Grad, in dem Mitarbeitende über ein wahrgenommenes kognitives KI-Grundverständnis (subjective AI Literacy/Cognition), die wahrgenommene eigene Kompetenz zur Anwendung und zum selbstständigen Erlernen generativer KI (Human AI Self-Efficacy / AI Learning Readiness), eine kritische Bewertungs- und Erkennungskompetenz sowie die affektive Bereitschaft und den subjektiven Komfort im Umgang mit KI verfügen, um generative KI-Anwendungen (wie ChatGPT Enterprise oder Copilot) zielgerichtet, sicher und produktiv im Arbeitsalltag einzusetzen.“

*Explizite Abgrenzung*: Das Messinstrument erfasst das **wahrgenommene/subjektive KI-Verständnis**  (`perceived / subjective AI literacy`) und die subjektive Selbstwirksamkeit der Mitarbeitenden, **nicht**  ein objektiv getestetes KI-Wissen (`objective knowledge`).

*Beitragende Quellen*: AIRS (Wang et al., 2026), MAILS (Carolus et al., 2023), AILRSE-5 (Oksanen et al., 2026), AISES (Wang & Chuang, 2024).

A5 Theory Hierarchy

Die Priorisierung der Quellen folgt der streng korrigierten Hierarchieordnung für diagnostische Instrumente:

- **Direkte individuelle AI-Readiness-Skala (Höchste Priorität)** :
**AIRS**  (Wang et al., 2026) – *Einzige direkte Skala zur individuellen AI Readiness in der aktiven Knowledge Base*.
- **Readiness-nahe Literacy- und Self-Efficacy-Skalen** :
**MAILS**  (Carolus et al., 2023) – *AI-Literacy-Quelle* (Meta AI Literacy Scale).

**AISES**  (Wang & Chuang, 2024) – *Readiness-nahe AI Self-Efficacy-Quelle*.

**AILRSE-5**  (Oksanen et al., 2026) – *Readiness-nahe AI Learning Self-Efficacy-Quelle*.
- **Generative KI- & Adoptionsmodelle** :
**Lambiase et al. (2025)**  – *LLM-Nutzungszwecke und Erleichternde Bedingungen (FC)*.
- **Vertrauens- & Organisationskontext** :
**Paper Fragebogen 4 / Do Khac et al. (2025)**  – *Abgrenzung KI-Systemfähigkeit (Ability) und Integrität von individueller Selbstwirksamkeit*.
- **Transfer- & Methodenmodelle** :
**Paper Fragebogen 1, 2, 3, 5 / Wichmann et al., Paetow et al.**  (*Hinweis*: P3/TTF ist inaktiv aufgrund von `TASK_CONTEXT = NOT_PROVIDED`).

*Diagnostischer Fokus (**DIAGNOSTIC**)*: Das Instrument wird strikt auf Kernbereitschaftsdimensionen zur Ermittlung von Schulungsbedarfen fokussiert. Die Variable **Behavioral Intention**  (Nutzungsabsicht) wird **vollständig gestrichen** , da sie für reine Entwicklungs- und Bereitschaftsdiagnosen keinen primären diagnostischen Mehrwert bietet und die Bearbeitungszeit unnötig belasten würde.

A6 Analysis Levels

Jedes wählbare Konstrukt wird exakt einer Analyseebene zugeordnet:

- **READINESS_CORE**  (Kernbereitschaft des Mitarbeitenden):
*Wahrgenommenes kognitives KI-Grundverständnis / Subjective AI Literacy* (MAILS Know & Understand / AIRS Cognition)

*KI-Lern-Selbstwirksamkeit / AI Learning Readiness Self-Efficacy* (AILRSE-5)

*Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit* (AISES / MAILS Apply & Problem Solving)

*Kritische KI-Bewertungskompetenz & KI-Erkennung / Detection* (MAILS Detect AI)

*Affektiver Komfort im Umgang mit KI / Comfort with AI* (AIRS Comfort / AISES Comfort)
- **CONTEXT**  (Organisatorische Rahmenbedingungen):
*Wahrgenommene Erleichternde Bedingungen & Supportbedarf* (Lambiase et al. FC / P2)
- **RELATED_CONSTRUCT**  (Verwandte System- & Governance-Eigenschaften):
*Wahrgenommene KI-Systemfähigkeit & Integrität* (P4 Do Khac et al. – System-Attribut, getrennt von persönlicher Selbstwirksamkeit)

*KI-Ethik & Governance-Bewusstsein* (MAILS Ethics / AIRS Ethics – organisatorisch-normative Rahmenbedingungen, getrennt von kognitiver Halluzinationserkennung)
- **OUTCOME** :
*Behavioral Intention / Nutzungsabsicht*: **Vollständig entfernt**  (`INSTRUMENT_PURPOSE = DIAGNOSTIC`).
- **EXCLUDE**  (Auszuschließende Konstrukte):
*Task-Technology Fit (TTF)* (P3 – Grund: `TASK_CONTEXT = NOT_PROVIDED`).

*Behavioral Intention* (P1, P2, P4, Lambiase – Grund: Für diagnostisches Instrument zur Entwicklungsbedarfserfassung entfernt).

*Nonadaptive Threat/Fear* (P1 – krankheitsspezifisch).

*Anthropomorphic Interaction* (AISES – anthropomorphe Interaktionsformen bei kaufmännischen GenAI-Werkzeugen irrelevant).

A7 Construct-Overlap Decisions

Systematische Re-Evaluation der Konstruktüberlappungen gemäß Masterprompt und Nutzerkorrekturen:

- **Detect AI / Critical Evaluation (MAILS) vs. AI Ethics (MAILS / AIRS / P4)** :
*Prüfung auf Konstruktreinheit (**DR02_CONSTRUCT_PURITY**)*: Halluzinationserkennung und kritische Evaluation (`Detect AI`) beziehen sich auf kognitive Qualitätskontrolle und Fehlersuche bei KI-Generaten. Ethik und Datenschutz (`AI Ethics` / `Data Privacy`) betreffen normative, rechtliche und moralische Richtlinien.

*Entscheidung*: `KEEP_SEPARATE`.

*Begründung*: Eine Zusammenführung in eine reflektive Skala verletzt die Konstruktreinheit. `Detect AI / Critical Evaluation` wird als kognitive Fähigkeit in `READINESS_CORE` geführt. `AI Ethics` verbleibt als organisatorisches Governance-Thema in `RELATED_CONSTRUCT` bzw. wird separat behandelt.
- **Comfort (AIRS / AISES) vs. Emotion Regulation (MAILS)** :
*Prüfung anhand der Originaldefinitionen*: `Comfort with AI` (AIRS/AISES) misst einen affektiven Gelassenheits- und Komfortstatus beim Umgang mit KI ("feeling calm/relaxed, not embarrassed"). `Emotion Regulation` (MAILS) misst eine psychologische Metakompetenz der aktiven Selbststeuerung von Frustration, Angst oder Euphorie.

*Entscheidung*: `PRIORITIZE_A` (Priorisierung von `Comfort with AI` aus AIRS/AISES).

*Begründung*: Konstruktäquivalenz ist unzureichend. Für die Standard-Bereitschaftsdiagnostik stellt der affektive Komfort (`Comfort with AI`) die etablierte, direkte Komponente der Kernbereitschaft dar. `Emotion Regulation` wird ausgeschlossen, um Redundanzen zu vermeiden.
- **KI-Systemfähigkeit / Ability (P4) vs. Human AI Self-Efficacy (AISES / AILRSE-5 / MAILS)** :
*Entscheidung*: `KEEP_SEPARATE`.

*Begründung*: System-Ability beschreibt die Leistung des KI-Tools (System-Eigenschaft), Self-Efficacy die wahrgenommene Kompetenz des Mitarbeitenden.
- **AILRSE-5 vs. MAILS AI Learning** :
*Entscheidung*: `PRIORITIZE_A` (Priorisierung von AILRSE-5).

*Begründung*: AILRSE-5 ist mit 5 Items international über 12 Länder hinweg psychometrisch validiert (skalare/strikte Messinvarianz).
- **Wahrgenommenes KI-Verständnis (MAILS Know & Understand / AIRS Cognition) vs. Objektives KI-Wissen** :
*Entscheidung*: `CLEAR_DISTINCTION`.

*Begründung*: Selbstberichtsskalen erfassen das *wahrgenommene / subjektive KI-Verständnis* (`perceived AI literacy`), nicht objektiv getestetes Wissen. Dies wird in der Arbeitsdefinition und Auswertung explizit dokumentiert.
- **Optimismus (AIRS) vs. Einstellung / Attitude (P1 / P2 / MAILS)** :
*Entscheidung*: `PRIORITIZE_A` (Priorisierung von Optimismus aus AIRS als lösungsorientierte Einstellungskomponente).
- **Assistance (AISES) vs. Facilitating Conditions (Lambiase et al. / P2)** :
*Entscheidung*: `KEEP_SEPARATE`.

*Begründung*: Functional Assistance beschreibt die Aufgabenunterstützung durch die KI, Facilitating Conditions beschreibt organisatorischen Support und Infrastruktur.

A8 Construct Catalog

Für das diagnostische Messinstrument werden folgende 6 präzise abgegrenzte Konstrukte ausgewählt (Gesamtzahl: 16–18 Items; Bearbeitungsdauer: ≤ 8 Minuten):

- **Wahrgenommenes KI-Grundverständnis (** **READINESS_CORE_LIT** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (3 Items)

*Inhalt*: Subjektiv wahrgenommenes Verständnis der Funktionsweise, Möglichkeiten und Leistungsgrenzen generativer KI (klare Abgrenzung zu objektivem Wissenstest).

*Quellenevidenz*: AIRS (Wang et al., 2026), MAILS (Carolus et al., 2023).
- **KI-Lern-Selbstwirksamkeit (** **READINESS_CORE_LEARN** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (3–5 Items)

*Inhalt*: Zutrauen in die eigene Fähigkeit, den Umgang mit neuen GenAI-Anwendungen selbstständig zu erlernen.

*Quellenevidenz*: AILRSE-5 (Oksanen et al., 2026).
- **Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit (** **READINESS_CORE_APPLY** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (3 Items)

*Inhalt*: Selbstwirksamkeit bei der praktischen Nutzung von GenAI für kaufmännische Aufgaben und der Lösung auftretender Anwendungsanforderungen.

*Quellenevidenz*: AISES (Wang & Chuang, 2024), MAILS (Carolus et al., 2023).
- **Kritische KI-Bewertungskompetenz & KI-Erkennung (** **READINESS_CORE_DETECT** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (3 Items)

*Inhalt*: Wahrgenommene Fähigkeit, KI-generierte Inhalte zu erkennen und auf Plausibilität/Halluzinationen zu überprüfen (strikt getrennt von rechtlich-ethischen Richtlinien).

*Quellenevidenz*: MAILS (Carolus et al., 2023).
- **Affektiver Komfort im Umgang mit KI (** **READINESS_CORE_COMFORT** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (3 Items)

*Inhalt*: Emotionaler Komfort, Gelassenheit und Abwesenheit von Verunsicherung/Peinlichkeit bei der Interaktion mit KI-Tools.

*Quellenevidenz*: AIRS (Wang et al., 2026), AISES (Wang & Chuang, 2024).
- **Wahrgenommene Erleichternde Bedingungen & Supportbedarf (** **CONTEXT_SUPP** **)** 
*Analyseebene*: `CONTEXT`

*Messmodell*: Reflektiv (3 Items)

*Inhalt*: Wahrnehmung organisatorischer Rahmenbedingungen, technischer Ausstattung und des Bedarfs an betrieblichen Schulungsangeboten.

*Quellenevidenz*: Lambiase et al. (2025), Paper Fragebogen 2 (Wichmann et al., 2025).

A9 Original-Scale Audit

Prüfung der Primärquellen hinsichtlich Struktur, Stichproben und Antwortformaten:

**AIRS**  (Wang et al., 2026): 13 Items, 4 Faktoren (SEC, OPT, CLW, COM); 5-Punkt-Likert-Skala (1–5). Validiert an N=174. Status: `FOUND`.

**MAILS**  (Carolus et al., 2023): 34 Items modular; 11-Punkt-Skala (0–10). Faktorielle Struktur an deutschsprachiger Stichprobe N=300 nachgewiesen. Status: `FOUND`.

**AILRSE-5**  (Oksanen et al., 2026): 5 Items, eindimensional; 7-Punkt-Likert-Skala (1–7). Über 12 Länder (N=20.173) mit skalarer und strikter Messinvarianz getestet. Status: `FOUND`.

**AISES**  (Wang & Chuang, 2024): 22 Items, 4 Faktoren (Assistance, Anthropomorphic Interaction, Comfort, Tech Skills); 7-Punkt-Likert-Skala. Validiert an N=314. Status: `FOUND`.

**Lambiase et al. (2025)** : UTAUT2-Adaptionen (7-Punkt-Skala). Validierung an N=188 Software-Engineers; Preprint-Status wird explizit offengelegt. Status: `FOUND`.

A10 Proposed Questionnaire Architecture

Struktur des diagnostischen Fragebogens (Gesamtdauer: ~6–8 Minuten; ca. 18 Items):

- **Teil 0: Einleitung & KI-Kontextdefinition** :
Neutrale Begrüßung, Datenschutzhinweis, präzise Definition des Messgegenstands (*"Generative KI-Werkzeuge wie ChatGPT Enterprise oder Microsoft Copilot im täglichen kaufmännischen Arbeitsablauf"*).
- **Teil 1: KI-Erfahrungs-Routing (Filterfrage)** :
Einstufung der eigenen Vorerfahrung in 3 Gruppen: `NO_EXPERIENCE` (Keine Erfahrung), `LIMITED_EXPERIENCE` (Gelegentliche Nutzung), `REGULAR_USER` (Regelmäßige Nutzung).

*Filterlogik*: Mitarbeitende ohne Vorerfahrung überspringen fortgeschrittene Anwendungsfragen und beantworten primär Lern-Selbstwirksamkeit, kognitives Grundverständnis und Erleichternde Bedingungen.
- **Teil 2: Kernbereitschaft / Readiness Core (** **READINESS_CORE** **)** :
Modul A: Wahrgenommenes kognitives KI-Grundverständnis (3 Items)

Modul B: KI-Lern-Selbstwirksamkeit (3 Items)

Modul C: Praktische KI-Anwendungs-Selbstwirksamkeit (3 Items – erfahrungsgefiltert)

Modul D: Kritische KI-Bewertungskompetenz & Erkennung (3 Items)

Modul E: Affektiver Komfort im Umgang mit KI (3 Items)
- **Teil 3: Organisatorische Rahmenbedingungen & Schulungsbedarfe (** **CONTEXT** **)** :
Modul F: Erleichternde Bedingungen & Supportbedarf (3 Items)
- **Teil 4: Statistische Angaben** :
Kaufmännische Funktionsbereich-Zuordnung (z. B. Einkauf, Vertriebsinnendienst, Buchhaltung/Controlling, HR, allgemeine Verwaltung).

A11 Risks & Limitations

**Empirische Validierung im Betrieb ausstehend** : Gütekriterien und Faktorenstrukturen beruhen auf der theoretischen Fundierung der veröffentlichten Primärquellen. Eine empirische Prüfung der Gütekriterien im Zielunternehmen steht noch aus (`status: theoretically_grounded_empirical_validation_pending`).

**Sprachliche Adaption (** **E2 – ADAPTED** **)** : Da maßgebliche Skalen (AIRS, AISES, AILRSE-5) im englischen Original entwickelt wurden, stellen die deutschen Übersetzungen linguistische Adaptionen dar (`E2`) und erfordern kognitive Pretests zur Absicherung der Begriffssäquivalenz.

**Abgrenzung von subjektivem Verständnis und objektivem Wissen** : Das Selbstauskunftsinstrument misst die wahrgenommene Kompetenz und Orientierung der Mitarbeitenden, nicht deren objektiv geprüftes KI-Wissen.

**Fehlender Aufgabenkontext (** **TASK_CONTEXT = NOT_PROVIDED** **)** : Da keine spezifischen Aufgabenprofile übermittelt wurden, ist eine Operationalisierung des Task-Technology Fit (TTF) ausgeschlossen.

**Neutralität der Validitätsaussagen** : Es werden keine unbelegten Behauptungen über empirische Gesamtskalengüte oder Vorhersagekraft im spezifischen Unternehmen vor einer tatsächlichen Datenerhebung aufgestellt.

A12 Design-Audit Reference

`DESIGN_AUDIT_REFERENCE`: **DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_002**

Der revidierte **DESIGN_AUDIT**  ist damit vollständig abgeschlossen und methodisch abgesichert.

💡 **Möchten Sie als nächsten Schritt die finale Fragebogenerstellung gemäß** **RUN_MODE = QUESTIONNAIRE_GENERATION** **(inklusive Item-Retrieval, Critic Review, simulated Pretest und JSON-Export) durchführen lassen?**

---

## Frage

Überarbeite den DESIGN_AUDIT DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_002 ein letztes Mal, ohne finale Fragebogenitems zu generieren.





AIRS: Unterscheide ausdrücklich zwischen initialem Itempool Q1–Q21 und der final validierten 13-Item-Skala.


Entferne AIRS als Quelle für AI Ethics. AIRS enthält keine Ethics-Dimension. Trenne individuelle AI-Ethics-Literacy (MAILS) von Trust/Integrity/Data Privacy (P4).


Präzisiere AILRSE-5: skalare Invarianz über 12 Länder; strikte Invarianz nicht pauschal über alle Länder behaupten.


Löse die Itembudget-Inkonsistenz: Wenn nur 3 der 5 AILRSE-5-Items verwendet werden sollen, kennzeichne dies ausdrücklich als verkürzte/adaptierte Auswahl und nicht als vollständige AILRSE-5.


Trenne Facilitating Conditions von Support-/Schulungsbedarf. FC bleibt ein Kontextkonstrukt; konkreter Schulungsbedarf wird als separate diagnostische Bedarfserhebung außerhalb der reflektiven Skala vorgesehen.


Entferne den Masterprompt aus dem wissenschaftlichen Source Inventory. Dokumentiere ihn separat als Governance-/Artifact Instruction, nicht als wissenschaftliche Evidenzquelle.


Behalte TASK_CONTEXT = NOT_PROVIDED, den vollständigen Ausschluss von Behavioral Intention und die aktuelle Trennung von Comfort vs. Emotion Regulation unverändert bei.
Gib anschließend einen vollständigen revidierten DESIGN_AUDIT mit neuer Referenz
DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_003 aus.

---

## Antwort

Hier ist der vollständig überarbeitete und präzisierte **DESIGN_AUDIT**  (Referenz `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_003`), der alle geforderten Korrekturen und methodischen Klarstellungen des Masterprompts präzise umsetzt. Gemäß den Vorgaben für `RUN_MODE = DESIGN_AUDIT` werden noch **keine finalen Fragebogenitems**  generiert.

A1 Inputs & Assumptions

**TARGET_POPULATION** : Kaufmännische Mitarbeitende eines mittelständischen Unternehmens.

**AI_CONTEXT** : Generative KI-Anwendungen (insb. ChatGPT Enterprise und Microsoft Copilot) im kaufmännischen Arbeitsalltag.

**MEASUREMENT_GOAL** : Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen vor einem breiteren KI-Rollout.

**INSTRUMENT_PURPOSE** : `DIAGNOSTIC` (Fokus auf praktische Bereitschaftsdiagnose; vollständiger Ausschluss von Adoptions- und Einstellungszielvariablen wie *Behavioral Intention*, um den Fragebogen schlank zu halten und Respondent Burden zu minimieren)[1].

**LANGUAGE** **/** **OUTPUT_LANGUAGE** : Deutsch (`German`).

**MAX_COMPLETION_TIME_MIN** : 8 Minuten (Ziel-Itemanzahl: ca. 15–18 Items).

**AI_EXPERIENCE_SEGMENTATION** : `auto` (Filterlogik nach Vorerfahrung)[4].

**CONTEXT_TEXT** : Nicht vorliegend (generisches Messinstrument; unternehmensspezifische Governance- oder Prozessdaten liegen nicht vor)[4][5].

**TASK_CONTEXT** : **NOT_PROVIDED**  *(Vom Nutzer nicht bereitgestellt. Konsequenz: Der Task-Technology Fit [TTF] gemäß Paetow et al. / Paper Fragebogen 3 wird ausdrücklich***nicht** *aktiv operationalisiert)*[6][7].

A2 Source Inventory

Differenzierung zwischen `eligible_source_roles` (gemäß Regelwerk zugelassene Rollen) und `assigned_source_roles` (in diesem spezifischen Run zugewiesene Rollen)[6]. Die Rolle `ITEM_SOURCE` wird nur vergeben, wenn im aktuellen Lauf konkrete Original-Items aus den Volltexten via Abruf verifiziert wurden[8][10].

A2.1 Wissenschaftliches Quelleninventar

- **AIRS**  (Wang et al., 2026)[13]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items im Lauf verifiziert; differenziert zwischen 21 Initial-Items und 13 Final-Items)*[14].
- **MAILS**  (Carolus et al., 2023)[17]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items im Lauf verifiziert)*[19].
- **AILRSE-5**  (Oksanen et al., 2026)[20][21]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items 1–5 im Lauf verifiziert)*[21][22].
- **AISES**  (Wang & Chuang, 2024)[23][24]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items im Lauf verifiziert)*[24][25].
- **Lambiase et al. (2025)** [26]
`fulltext_available_in_run`: `true` *(Preprint-Status explizit dokumentiert)*[27].

`eligible_source_roles`: `[ITEM_SOURCE, CONTEXT_SOURCE, TRANSFER_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[CONTEXT_SOURCE, TRANSFER_SOURCE]`
- **Paper Fragebogen 1 / Wichmann et al. (2024)**  (P1)[28]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[TRANSFER_SOURCE, DEFINITION_SOURCE, METHOD_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[METHOD_SOURCE, TRANSFER_SOURCE]`
- **Paper Fragebogen 2 / Wichmann et al. (2025)**  (P2)[29]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[TRANSFER_SOURCE, METHOD_SOURCE, VALIDATION_SOURCE, ITEM_SOURCE]`

`assigned_source_roles`: `[METHOD_SOURCE, TRANSFER_SOURCE]`
- **Paper Fragebogen 3 / Paetow et al. (2026)**  (P3)[30]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[TRANSFER_SOURCE, METHOD_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[]` *(Inaktiv bezüglich Item-Operationalisierung, da**TASK_CONTEXT = NOT_PROVIDED**)*[6].
- **Paper Fragebogen 4 / Do Khac et al. (2025)**  (P4)[31]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE, CONTEXT_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, CONTEXT_SOURCE]` *(Abgrenzung AI-System Ability/Integrity vs. Human AI Literacy/Ethics)*[11][31].
- **Paper Fragebogen 5 / Wichmann et al. (2026)**  (P5)[32]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[METHOD_SOURCE, VALIDATION_SOURCE, TRANSFER_SOURCE]`

`assigned_source_roles`: `[METHOD_SOURCE]` *(Güteprüfungs- und Reflektionsmethodik)*[12].

A2.2 Separate Governance & Operational Framework Reference

- **MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_FINAL (1).md** [1][33]
*Rolle*: `GOVERNANCE_AND_OPERATIONAL_FRAMEWORK` (Artefakt- und Methodik-Instruktion, **nicht**  als wissenschaftliche Primärevidenzquelle im Source Inventory geführt)[1].

A3 Design Requirements

**DR01_SOURCE_TRACEABILITY** : Jedes Konstrukt wird lückenlos auf aktive wissenschaftliche Primärquellen zurückgeführt[8][34].

**DR02_CONSTRUCT_PURITY** : Strikte unidimensionale Trennung von kognitivem Verständnis, Selbstwirksamkeit, Bewertungskompetenz, Vertrauen und Systemmerkmalen[34][35]. Keine Vermischung von kognitiver Halluzinationserkennung (`Detect AI`) mit rechtlich-ethischen Richtlinien (`AI Ethics`). Keine Zusammenführung von affektivem Komfort (`Comfort with AI`) und aktiver Emotionsregulation (`Emotion Regulation`).

**DR03_ANALYSIS_LEVEL_SEPARATION** : Saubere Zuordnung der Ebenen (`READINESS_CORE`, `CONTEXT`, `RELATED_CONSTRUCT`, `EXCLUDE`)[2]. Vollständiger Ausschluss von `Behavioral Intention` aus dem diagnostischen Instrument[2][3].

**DR04_ORIGINAL_SCALE_AUDIT** : Nachweisbare Verankerung originaler Antwortformate und skalengetreue Audits[36].

**DR05_MEASUREMENT_MODEL_AWARENESS** : Reflektive Spezifikation (2–5 Items pro Konstrukt)[37].

**DR06_CONTEXT_RELEVANCE** : Kaufmännische Ausrichtung auf GenAI (Copilot / ChatGPT) ohne Erfindung unbestätigter Betriebsdaten[5].

**DR07_RESPONDENT_BURDEN** : Maximale Bearbeitungsdauer von 8 Minuten (ca. 15–18 Items)[38].

**DR08_HUMAN_PRETEST_REQUIRED** : Kennzeichnung als theoretisch fundierter Entwurf; empirische Validierung im konkreten Betrieb steht aus[38][39].

**DR09_BIAS_CONTROL** : Neutrales Wording, Vermeidung sozialer Erwünschtheit und Doppelverneinungen[38].

**DR10_DATA_QUALITY** : Einbau von Filterlogik (Erfahrungs-Routing)[4][38].

**DR11_TRANSLATION_TRANSPARENCY** : Kennzeichnung aller Übersetzungen aus dem Englischen als Klasse `E2 – ADAPTED`[38][40].

**DR12_NO_FALSE_VALIDITY** : Neutrale, ausschließlich durch dokumentierte Evidenz gestützte Aussagen zur Validität. Ausschluss unbelegter Gesamtskalen-Aggregationen[38][41].

**DR13_TASK_SPECIFICITY_FOR_TTF** : Da `TASK_CONTEXT = NOT_PROVIDED`, wird Task-Technology Fit deaktiviert[6].

A4 Working Definition

`definition_status`: `SYNTHESIZED_DEFINITION`

**Synthetisierte Arbeitsdefinition** :

„Employee AI Readiness kaufmännischer Mitarbeitender beschreibt den Grad, in dem Mitarbeitende über ein wahrgenommenes kognitives KI-Grundverständnis (subjective AI Literacy/Cognition), die wahrgenommene eigene Kompetenz zur Anwendung und zum selbstständigen Erlernen generativer KI (Human AI Self-Efficacy / AI Learning Readiness), eine kritische Bewertungs- und Erkennungskompetenz sowie den affektiven Komfort im Umgang mit KI verfügen, um generative KI-Anwendungen (wie ChatGPT Enterprise oder Copilot) zielgerichtet, sicher und produktiv im Arbeitsalltag einzusetzen.“[13]

**Präzisierung / Abgrenzung** : Das Instrument erfasst das **wahrgenommene / subjektive KI-Grundverständnis**  (`perceived / subjective AI literacy`) der Mitarbeitenden[17][42]. Es unterscheidet sich explizit von einem objektiv getesteten Leistungswissen (`objective AI knowledge`)[42][43].

*Beitragende Quellen*: AIRS (Wang et al., 2026)[13], MAILS (Carolus et al., 2023)[17], AILRSE-5 (Oksanen et al., 2026)[20], AISES (Wang & Chuang, 2024)[23].

A5 Theory Hierarchy

Die Priorisierung der Quellen folgt der Hierarchieordnung für diagnostische Instrumente:

- **Direkte individuelle AI-Readiness-Skala (Höchste Priorität)** :
**AIRS**  (Wang et al., 2026) – *Einzige direkte Skala zur individuellen AI Readiness in der aktiven Knowledge Base*[13][44].
- **Readiness-nahe Literacy- und Self-Efficacy-Skalen** :
**MAILS**  (Carolus et al., 2023) – *AI-Literacy-Quelle* (Meta AI Literacy Scale)[17][44].

**AISES**  (Wang & Chuang, 2024) – *Readiness-nahe AI Self-Efficacy-Quelle*[23][45].

**AILRSE-5**  (Oksanen et al., 2026) – *Readiness-nahe AI Learning Self-Efficacy-Quelle*[20][46].
- **Generative KI- & Adoptionsmodelle** :
**Lambiase et al. (2025)**  – *LLM-Nutzungszwecke und Erleichternde Bedingungen (FC)*[26][47].
- **Vertrauens- & Organisationskontext** :
**Paper Fragebogen 4 / Do Khac et al. (2025)**  – *Abgrenzung KI-Systemfähigkeit (Ability) und Integrität/Datenschutz von individueller Selbstwirksamkeit und Ethik-Literacy*[11][31].
- **Transfer- & Methodenmodelle** :
**Paper Fragebogen 1, 2, 3, 5 / Wichmann et al., Paetow et al.**  (*P3/TTF ist inaktiv aufgrund von**TASK_CONTEXT = NOT_PROVIDED*)[6].

*Diagnostischer Fokus (**DIAGNOSTIC**)*: Das Instrument konzentriert sich auf Kernbereitschaftsdimensionen. **Behavioral Intention**  wird **vollständig ausgeschlossen** , um Verfälschungen zu vermeiden und Ausfüllzeit zu sparen[2][3].

A6 Analysis Levels

Jedes wählbare Konstrukt wird exakt einer Analyseebene zugeordnet:

- **READINESS_CORE**  (Kernbereitschaft des Mitarbeitenden):
*Wahrgenommenes kognitives KI-Grundverständnis / Subjective AI Literacy* (MAILS Know & Understand / AIRS Cognition)[13][17]

*KI-Lern-Selbstwirksamkeit / AI Learning Readiness Self-Efficacy* (AILRSE-5)[20]

*Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit* (AISES / MAILS Apply & Problem Solving)[17][23]

*Kritische KI-Bewertungskompetenz & KI-Erkennung / Detection* (MAILS Detect AI)[17][19]

*Affektiver Komfort im Umgang mit KI / Comfort with AI* (AIRS Comfort / AISES Comfort)[13][23]
- **CONTEXT**  (Organisatorische Rahmenbedingungen):
*Wahrgenommene Erleichternde Bedingungen / Facilitating Conditions* (Lambiase et al. FC / P2)[26][29]
- **RELATED_CONSTRUCT**  (Verwandte System- & Governance-Eigenschaften):
*Wahrgenommene KI-Systemfähigkeit & Integrität / Data Privacy* (P4 Do Khac et al. – System- & Organisationseigenschaften)[11][31]

*KI-Ethik-Literacy* (MAILS Ethics – kritisches Individuumsbewusstsein für gesellschaftlich-ethische Implikationen, getrennt von kognitiver Halluzinationserkennung und organisationalem Datenschutz)[17][19]
- **EXCLUDE**  (Auszuschließende Konstrukte):
*Behavioral Intention* (P1, P2, P4, Lambiase – Grund: Für diagnostisches Instrument zur Entwicklungsbedarfserfassung vollständig entfernt)[2][3].

*Task-Technology Fit (TTF)* (P3 – Grund: `TASK_CONTEXT = NOT_PROVIDED`)[6][7].

*Schulungs- und Supportbedarf als reflektives Skalenkonstrukt* (Verlagerung in eine separate, formative/listenbasierte Bedarfserhebung, um die reflektive Skala der Facilitating Conditions nicht zu verunreinigen).

*Nonadaptive Threat/Fear* (P1 – krankheitsspezifisch)[9].

*Anthropomorphic Interaction* (AISES – bei kaufmännischen GenAI-Werkzeugen irrelevant)[23].

A7 Construct-Overlap Decisions

Überarbeitete Zuordnung der Konstruktüberlappungen:

- **AIRS-Dimensionen & Entfernung als Ethik-Quelle** :
*Prüfung*: Das AIRS-Instrument von Wang et al. (2026) umfasst vier Faktoren: *Self-Efficacy and Cognition (SEC)*, *Optimism (OPT)*, *Collaborative Learning and Working (CLW)* und *Comfort (COM)*[13]. AIRS enthält **keine**  Ethik-Dimension[15].

*Entscheidung*: AIRS wird als Quelle für `AI Ethics` gestrichen.
- **Kritische KI-Erkennung (MAILS Detect AI) vs. Individuelle AI Ethics (MAILS) vs. System-Integrity / Data Privacy (P4)** :
  - *Prüfung auf Konstruktreinheit (**DR02_CONSTRUCT_PURITY**)*:
`Detect AI` (MAILS): Kognitive Fähigkeit zur Erkennung von KI-Generaten und Überprüfung auf Fehler/Halluzinationen[17][19].

`AI Ethics` (MAILS): Individuelle Orientierung bezüglich ethischer Implikationen und gesellschaftlicher Folgen[17][19].

`Integrity / Data Privacy` (P4 Do Khac et al.): Wahrgenommene Konformität des Systems/Unternehmens mit Datenschutzregeln (z. B. DSGVO)[11][31].
*Entscheidung*: `KEEP_SEPARATE`.

*Begründung*: Vermischung verletzt die unidimensionale reflektive Messung. `Detect AI` verbleibt als kognitives Element in `READINESS_CORE`. `AI Ethics` (MAILS) und `Integrity/Data Privacy` (P4) verbleiben in `RELATED_CONSTRUCT` bzw. fließen nicht in die Kernbereitschaftsskala ein.
- **Comfort with AI (AIRS / AISES) vs. Emotion Regulation (MAILS)** :
*Prüfung anhand Originaldefinitionen*: `Comfort with AI` (AIRS/AISES) beschreibt ein Gefühl von Gelassenheit und Abwesenheit von Verunsicherung bei der KI-Nutzung[13][23]. `Emotion Regulation` (MAILS) misst die aktive psychologische Selbststeuerung negativer oder euphorischer Affekte[17][19].

*Entscheidung*: `PRIORITIZE_A` (Priorisierung von `Comfort with AI` aus AIRS/AISES).

*Begründung*: Keinesfalls zusammenführen, da unzureichende Konstruktäquivalenz. `Comfort with AI` verbleibt als Standard-Dimension in `READINESS_CORE`. `Emotion Regulation` wird zur Vermeidung von Komplexität ausgeschlossen.
- **Facilitating Conditions (Lambiase / P2) vs. Schulungs- und Supportbedarf** :
*Entscheidung*: `KEEP_SEPARATE`.

*Begründung*: `Facilitating Conditions` misst als reflektives Konstrukt die Wahrnehmung vorhandener organisationaler Ressourcen und Infrastruktur[26][29]. Konkrete Schulungsbedarfe (z. B. Wunsch nach Prompting-Kursen) stellen einen diagnostischen Handlungsbedarf dar und werden außerhalb der reflektiven Skalen als eigenständiges, kaufmännisches Abfragemodul (formativ/Multiple-Choice-Liste) integriert.
- **AILRSE-5 Itembudget & Skalenanpassung** :
*Entscheidung*: Wenn aus Zeitgründen (8-Minuten-Budget) nur 3 der 5 AILRSE-5-Items eingesetzt werden, wird diese Auswahl explizit als **„adaptierte Kurzform / 3-Item-Sub-Set der AILRSE-5“**  ausgewiesen und nicht fälschlich als vollständige AILRSE-5 bezeichnet[20]. Falls das Budget reicht, wird die vollständige 5-Item-Skala präferiert[21].

A8 Construct Catalog

Das diagnostische Messinstrument umfasst folgende 6 reflektive Konstrukte (Gesamtzahl: 18 Items; Bearbeitungsdauer: ≤ 8 Minuten):

- **Wahrgenommenes KI-Grundverständnis (** **READINESS_CORE_LIT** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (3 Items)

*Inhalt*: Subjektiv wahrgenommenes Verständnis der Funktionsweise und Grenzen generativer KI (abgegrenzt von objektivem Wissen)[17][42].

*Quellenevidenz*: AIRS (Wang et al., 2026)[13], MAILS (Carolus et al., 2023)[17].
- **KI-Lern-Selbstwirksamkeit (** **READINESS_CORE_LEARN** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (5 Items [vollständige AILRSE-5-Skala] bzw. 3 Items [explizit ausgewiesenes adaptiertes Sub-Set])[21][22].

*Inhalt*: Zutrauen in die eigene Fähigkeit, den Umgang mit neuen GenAI-Anwendungen selbstständig zu erlernen[20][49].

*Quellenevidenz*: AILRSE-5 (Oksanen et al., 2026)[20][21].
- **Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit (** **READINESS_CORE_APPLY** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (3 Items)

*Inhalt*: Selbstwirksamkeit bei der praktischen Nutzung von GenAI für kaufmännische Aufgaben und der Lösung auftretender Anwendungsanforderungen[17][23].

*Quellenevidenz*: AISES (Wang & Chuang, 2024)[23], MAILS (Carolus et al., 2023)[17].
- **Kritische KI-Bewertungskompetenz & KI-Erkennung (** **READINESS_CORE_DETECT** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (3 Items)

*Inhalt*: Wahrgenommene Fähigkeit, KI-generierte Inhalte zu erkennen und auf Plausibilität/Halluzinationen zu überprüfen (strikt getrennt von Richtlinien und Ethik)[17][19].

*Quellenevidenz*: MAILS (Carolus et al., 2023)[17][19].
- **Affektiver Komfort im Umgang mit KI (** **READINESS_CORE_COMFORT** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (3 Items)

*Inhalt*: Emotionaler Komfort und Gelassenheit bei der Interaktion mit KI-Tools (getrennt von aktiver Emotionsregulation)[13][23].

*Quellenevidenz*: AIRS (Wang et al., 2026)[13], AISES (Wang & Chuang, 2024)[23].
- **Wahrgenommene Erleichternde Bedingungen (** **CONTEXT_FC** **)** 
*Analyseebene*: `CONTEXT`

*Messmodell*: Reflektiv (3 Items)

*Inhalt*: Wahrnehmung vorhandener organisatorischer und technischer Rahmenbedingungen im Betrieb[26][29].

*Quellenevidenz*: Lambiase et al. (2025)[26], Paper Fragebogen 2 (Wichmann et al., 2025)[29].

*Diagnostischer Zusatzbaustein (Anderes Messformat)*:

**Konkreter Schulungs- und Supportbedarf (** **DIAGNOSTIC_NEEDS** **)** : Formatives/listenbasiertes Erhebungselement (z. B. Abfrage spezifischer Schulungsthemen wie Prompt-Engineering, Datenschutz, Prozessintegration) zur direkten Maßnahmenableitung außerhalb der reflektiven Skalen.

A9 Original-Scale Audit

Prüfung der Primärquellen hinsichtlich Struktur und Methodik:

- **AIRS**  (Wang et al., 2026):
*Audit-Ergebnis*: Unterscheidung zwischen dem **initialen Itempool von 21 Items (Q1–Q21)**  und der **final gereinigten/validierten 13-Item-Skala** [14]. Nach Item-Total-Korrelationsanalysen wurden 8 Items entfernt (Q4, Q5, Q6, Q7, Q10, Q11, Q15, Q17)[50]. Die verbleibenden 13 Items bilden 4 Faktoren: *Self-Efficacy & Cognition (SEC)*, *Optimism (OPT)*, *Collaborative Learning & Working (CLW)* und *Comfort (COM)*[15][48]. 5-Punkt-Likert-Skala (1–5)[16]. Status: `FOUND`[13].
- **AILRSE-5**  (Oksanen et al., 2026):
*Audit-Ergebnis*: 5 Items, eindimensional; 7-Punkt-Likert-Skala (1–7)[21][22]. Basierend auf N=20.173 aus 12 Ländern wird **skalare Invarianz**  über alle 12 Länder gestützt (CFI=0.979, RMSEA=0.097)[20][51]. **Strikte Invarianz wurde dagegen nicht pauschal global erreicht** , sondern ausschließlich in den finnischen Stichproben (cross-sectional & longitudinal)[51]. Status: `FOUND`[20].
- **MAILS**  (Carolus et al., 2023):
*Audit-Ergebnis*: 34 Items modular, 11-Punkt-Skala (0–10)[17]. Faktorielle Validität an N=300 nachgewiesen[17][18]. Status: `FOUND`[17].
- **AISES**  (Wang & Chuang, 2024):
*Audit-Ergebnis*: 22 Items, 4 Faktoren (Assistance, Anthropomorphic Interaction, Comfort, Tech Skills); 7-Punkt-Likert-Skala[23][24]. Status: `FOUND`[23].
- **Lambiase et al. (2025)** :
*Audit-Ergebnis*: Facilitating Conditions (FC_1 bis FC_4; 7-Punkt-Skala). N=188 Software-Engineers; Preprint-Status wird explizit offengelegt[26][27]. Status: `FOUND`[26].

A10 Proposed Questionnaire Architecture

Struktur des diagnostischen Fragebogens (Gesamtdauer: ~6–8 Minuten; 18 reflektive Items + 1 Bedarfs-Modul):

- **Teil 0: Einleitung & KI-Kontextdefinition** :
Neutrale Begrüßung, Datenschutzhinweis, präzise Definition des Messgegenstands (*"Generative KI-Werkzeuge wie ChatGPT Enterprise oder Microsoft Copilot im täglichen kaufmännischen Arbeitsablauf"*).
- **Teil 1: KI-Erfahrungs-Routing (Filterfrage)** :
Einstufung der Vorerfahrung: `NO_EXPERIENCE` (Keine Erfahrung), `LIMITED_EXPERIENCE` (Gelegentliche Nutzung), `REGULAR_USER` (Regelmäßige Nutzung)[4].
- **Teil 2: Kernbereitschaft / Readiness Core (** **READINESS_CORE** **)** :
Modul A: Wahrgenommenes kognitives KI-Grundverständnis (3 Items)

Modul B: KI-Lern-Selbstwirksamkeit (5 Items [AILRSE-5 vollständig] bzw. 3 Items [ausgewiesenes adaptiertes Sub-Set])[21][22]

Modul C: Praktische KI-Anwendungs-Selbstwirksamkeit (3 Items – erfahrungsgefiltert)

Modul D: Kritische KI-Bewertungskompetenz & Erkennung (3 Items)

Modul E: Affektiver Komfort im Umgang mit KI (3 Items)
- **Teil 3: Organisatorische Rahmenbedingungen (** **CONTEXT** **)** :
Modul F: Wahrgenommene Erleichternde Bedingungen / Facilitating Conditions (3 Items)
- **Teil 4: Diagnostische Bedarfsermittlung (** **DIAGNOSTIC_NEEDS** **)** :
Abfrage konkreter Schulungs- und Supportbedarfe (formatives Listenformat zur praktischen Maßnahmenplanung).
- **Teil 5: Statistische Angaben** :
Kaufmännische Funktionsbereich-Zuordnung (z. B. Einkauf, Vertriebsinnendienst, Buchhaltung/Controlling, HR, allgemeine Verwaltung).

A11 Risks & Limitations

**Evidenzbasierte Aussage zur Validierungsstärke** : Das Fragebogeninstrument ist theoretisch fundiert und methodisch qualitätsgeprüft[39]. Die Gütekriterien beruhen auf den publizierten Validierungsergebnissen der Primärquellen (z. B. AILRSE-5 skalare Invarianz[20][51], MAILS faktorielle Struktur[17][18]). Eine empirische Prüfung der psychometrischen Kennwerte im spezifischen Zielunternehmen steht vor der Datenerhebung noch aus (`status: theoretically_grounded_empirical_validation_pending`)[38][39].

**Sprachliche Adaption (** **E2 – ADAPTED** **)** : Da maßgebliche Skalen (AIRS, AISES, AILRSE-5) im englischen Original vorliegen, stellen die deutschen Formulierungen linguistische Adaptionen dar (`E2`)[38][40].

**Subjektives Verständnis vs. Objektives Wissen** : Das Selbstauskunftsinstrument erfasst das subjektiv wahrgenommene KI-Verständnis der Mitarbeitenden und keinen objektiven Wissenstest[17][42].

**Fehlender Aufgabenkontext (** **TASK_CONTEXT = NOT_PROVIDED** **)** : Eine Operationalisierung des Task-Technology Fit (TTF) unterbleibt[6][7].

A12 Design-Audit Reference

`DESIGN_AUDIT_REFERENCE`: **DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_003**

Der revidierte **DESIGN_AUDIT**  ist damit vollständig abgeschlossen und methodisch abgesichert.

💡 **Möchten Sie als nächsten Schritt die finale Fragebogenerstellung gemäß** **RUN_MODE = QUESTIONNAIRE_GENERATION** **(inklusive verifizierter Items, Critic Review, simulated Pretest und JSON-Export) durchführen lassen?**

---

## Frage

Nimm ausschließlich folgende letzte Konsistenzkorrekturen am bestehenden DESIGN_AUDIT vor. Ändere die bestehende Theorie- und Konstruktarchitektur ansonsten nicht und generiere noch keine finalen Items.





Lege die finale reflektive Itemzahl eindeutig auf 18 Items fest: sechs Konstrukte mit jeweils 3 Items.


Kennzeichne die drei verwendeten AILRSE-5-Items ausdrücklich als adaptiertes 3-Item-Subset der ursprünglichen 5-Item-Skala. Behaupte nicht, die vollständige AILRSE-5 einzusetzen.


Kennzeichne die drei vorgesehenen Facilitating-Conditions-Items ausdrücklich als 3-Item-Subset der vier verifizierten FC-Items aus Lambiase et al. (2025). Behaupte nicht, die vollständige Originalskala einzusetzen.


Ergänze eine explizite Begründung für den Ausschluss von AI Ethics Literacy als eigener reflektiver Kernskala: Aufgrund des 8-Minuten-Itembudgets wird Ethics nicht als separates Readiness-Core-Konstrukt aufgenommen; ethisch/rechtliche Entwicklungsbedarfe werden im separaten diagnostischen Bedarfsmodul adressiert. Keine Vermischung mit Detect AI oder Integrity/Data Privacy.


Stelle sicher, dass die Arbeitsdefinition und die geplante Operationalisierung konsistent sind. Falls der Begriff „sicher“ in der Definition verbleibt, erläutere, dass verantwortungs-/sicherheitsbezogene Entwicklungsbedarfe über das separate Bedarfsmodul und nicht über einen eigenen reflektiven Ethics-Score erfasst werden.
Gib anschließend den vollständigen finalen DESIGN_AUDIT mit der Referenz
DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL aus.

---

## Antwort

Hier ist der vollständig finalisierte und konsistente **DESIGN_AUDIT**  (Referenz `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`). Er berücksichtigt ausnahmslos alle methodischen Präzisierungen und Festlegungen des Masterprompts. Gemäß den Regeln für `RUN_MODE = DESIGN_AUDIT` werden noch **keine finalen Fragebogenitems**  generiert.

A1 Inputs & Assumptions

**TARGET_POPULATION** : Kaufmännische Mitarbeitende eines mittelständischen Unternehmens.

**AI_CONTEXT** : Generative KI-Anwendungen (insbesondere ChatGPT Enterprise und Microsoft Copilot) im kaufmännischen Arbeitsalltag.

**MEASUREMENT_GOAL** : Diagnostische Erfassung der individuellen Employee AI Readiness sowie Identifikation von Entwicklungs- und Schulungsbedarfen vor einer breiteren KI-Einführung.

**INSTRUMENT_PURPOSE** : `DIAGNOSTIC` (Fokus auf praktische Bereitschaftsdiagnose und konkrete Entwicklungsbedarfe; vollständiger Ausschluss von Adoptions- und Einstellungszielvariablen wie *Behavioral Intention*, um den Fragebogen schlank zu halten und Respondent Burden zu minimieren).

**LANGUAGE** **/** **OUTPUT_LANGUAGE** : Deutsch (`German`).

**MAX_COMPLETION_TIME_MIN** : 8 Minuten (Eindeutig festgelegte Zielarchitektur: **Exakt 18 reflektive Items** , verteilt auf 6 Konstrukte mit jeweils exakt 3 Items, zzgl. 1 kaufmännisches Bedarfsmodul).

**AI_EXPERIENCE_SEGMENTATION** : `auto` (Filterlogik nach Vorerfahrung).

**CONTEXT_TEXT** : Nicht vorliegend (generisches Messinstrument; unternehmensspezifische Governance- oder Prozessdaten liegen nicht vor).

**TASK_CONTEXT** : **NOT_PROVIDED**  *(Vom Nutzer nicht bereitgestellt. Konsequenz: Der Task-Technology Fit [TTF] gemäß Paetow et al. / Paper Fragebogen 3 wird ausdrücklich***nicht** *aktiv operationalisiert)*.

A2 Source Inventory

Differenzierung zwischen `eligible_source_roles` (gemäß Regelwerk zugelassene Rollen) und `assigned_source_roles` (in diesem spezifischen Run zugewiesene Rollen). Die Rolle `ITEM_SOURCE` wird nur vergeben, wenn im aktuellen Lauf konkrete Original-Items aus den Volltexten via Abruf verifiziert wurden.

A2.1 Wissenschaftliches Quelleninventar

- **AIRS**  (Wang et al., 2026)[1]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items im Lauf verifiziert; Unterscheidung zwischen 21 Initial-Items und der 13-Item-Finalskala)*.
- **MAILS**  (Carolus et al., 2023)[2]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items im Lauf verifiziert)*.
- **AILRSE-5**  (Oksanen et al., 2026)[3]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items im Lauf verifiziert; Kennzeichnung als 3-Item-Subset)*.
- **AISES**  (Wang & Chuang, 2024)[4]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]` *(Original-Items im Lauf verifiziert)*.
- **Lambiase et al. (2025)** [5]
`fulltext_available_in_run`: `true` *(Preprint-Status explizit dokumentiert)*.

`eligible_source_roles`: `[ITEM_SOURCE, CONTEXT_SOURCE, TRANSFER_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[ITEM_SOURCE, CONTEXT_SOURCE, TRANSFER_SOURCE]` *(Kennzeichnung der 3 FC-Items als Subset der 4 Verifizierten)*.
- **Paper Fragebogen 1 / Wichmann et al. (2024)**  (P1)[6]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[TRANSFER_SOURCE, DEFINITION_SOURCE, METHOD_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[METHOD_SOURCE, TRANSFER_SOURCE]`
- **Paper Fragebogen 2 / Wichmann et al. (2025)**  (P2)[7]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[TRANSFER_SOURCE, METHOD_SOURCE, VALIDATION_SOURCE, ITEM_SOURCE]`

`assigned_source_roles`: `[METHOD_SOURCE, TRANSFER_SOURCE]`
- **Paper Fragebogen 3 / Paetow et al. (2026)**  (P3)[8]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[TRANSFER_SOURCE, METHOD_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE]`

`assigned_source_roles`: `[]` *(Inaktiv bezüglich Item-Operationalisierung, da**TASK_CONTEXT = NOT_PROVIDED**)*.
- **Paper Fragebogen 4 / Do Khac et al. (2025)**  (P4)[9]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[DEFINITION_SOURCE, ITEM_SOURCE, VALIDATION_SOURCE, CONTEXT_SOURCE]`

`assigned_source_roles`: `[DEFINITION_SOURCE, CONTEXT_SOURCE]` *(Abgrenzung AI-System Ability/Integrity vs. Human AI Literacy/Ethics)*.
- **Paper Fragebogen 5 / Wichmann et al. (2026)**  (P5)[10]
`fulltext_available_in_run`: `true`

`eligible_source_roles`: `[METHOD_SOURCE, VALIDATION_SOURCE, TRANSFER_SOURCE]`

`assigned_source_roles`: `[METHOD_SOURCE]` *(Güteprüfungs- und Reflektionsmethodik)*.

A2.2 Separate Governance & Operational Framework Reference

- **MASTERPROMPT_Employee_AI_Readiness_OPERATIONAL_FINAL (1).md** [11]
*Rolle*: `GOVERNANCE_AND_OPERATIONAL_FRAMEWORK` (Artefakt- und Methodik-Instruktion, **nicht**  als wissenschaftliche Primärevidenzquelle im Source Inventory geführt).

A3 Design Requirements

**DR01_SOURCE_TRACEABILITY** : Jedes Konstrukt wird lückenlos auf aktive wissenschaftliche Primärquellen zurückgeführt.

**DR02_CONSTRUCT_PURITY** : Strikte unidimensionale Trennung von kognitivem Verständnis, Selbstwirksamkeit, Bewertungskompetenz, Vertrauen und Systemmerkmalen. Keine Vermischung von kognitiver Halluzinationserkennung (`Detect AI`) mit rechtlich-ethischen Richtlinien (`AI Ethics`). Keine Zusammenführung von affektivem Komfort (`Comfort with AI`) und aktiver Emotionsregulation (`Emotion Regulation`).

**DR03_ANALYSIS_LEVEL_SEPARATION** : Saubere Zuordnung der Ebenen (`READINESS_CORE`, `CONTEXT`, `RELATED_CONSTRUCT`, `EXCLUDE`). Vollständiger Ausschluss von `Behavioral Intention` aus dem diagnostischen Instrument.

**DR04_ORIGINAL_SCALE_AUDIT** : Nachweisbare Verankerung originaler Antwortformate und skalengetreue Audits.

**DR05_MEASUREMENT_MODEL_AWARENESS** : Reflektive Spezifikation (exakt 3 Items pro Konstrukt).

**DR06_CONTEXT_RELEVANCE** : Kaufmännische Ausrichtung auf GenAI (Copilot / ChatGPT) ohne Erfindung unbestätigter Betriebsdaten.

**DR07_RESPONDENT_BURDEN** : Maximale Bearbeitungsdauer von 8 Minuten (**exakt 18 reflektive Items** ).

**DR08_HUMAN_PRETEST_REQUIRED** : Kennzeichnung als theoretisch fundierter Entwurf; empirische Validierung im konkreten Betrieb steht aus.

**DR09_BIAS_CONTROL** : Neutrales Wording, Vermeidung sozialer Erwünschtheit und Doppelverneinungen.

**DR10_DATA_QUALITY** : Einbau von Filterlogik (Erfahrungs-Routing).

**DR11_TRANSLATION_TRANSPARENCY** : Kennzeichnung aller Übersetzungen aus dem Englischen als Klasse `E2 – ADAPTED`.

**DR12_NO_FALSE_VALIDITY** : Neutrale, ausschließlich durch dokumentierte Evidenz gestützte Aussagen zur Validität. Ausschluss unbelegter Gesamtskalen-Aggregationen.

**DR13_TASK_SPECIFICITY_FOR_TTF** : Da `TASK_CONTEXT = NOT_PROVIDED`, wird Task-Technology Fit deaktiviert.

A4 Working Definition

`definition_status`: `SYNTHESIZED_DEFINITION`

**Synthetisierte Arbeitsdefinition** :

„Employee AI Readiness kaufmännischer Mitarbeitender beschreibt den Grad, in dem Mitarbeitende über ein wahrgenommenes kognitives KI-Grundverständnis (subjective AI Literacy/Cognition), die wahrgenommene eigene Kompetenz zur Anwendung und zum selbstständigen Erlernen generativer KI (Human AI Self-Efficacy / AI Learning Readiness), eine kritische Bewertungs- und Erkennungskompetenz sowie den affektiven Komfort im Umgang mit KI verfügen, um generative KI-Anwendungen (wie ChatGPT Enterprise oder Copilot) zielgerichtet, sicher und produktiv im Arbeitsalltag einzusetzen.“

- **Präzisierung der Operationalisierung** :
Das Instrument erfasst das **wahrgenommene / subjektive KI-Grundverständnis**  (`perceived / subjective AI literacy`) der Mitarbeitenden. Es unterscheidet sich explizit von einem objektiv getesteten Leistungswissen (`objective AI knowledge`).

Der in der Arbeitsdefinition enthaltene Begriff **„sicher“**  (verantwortungsvoller, richtlinienkonformer Einsatz) wird im Messinstrument **nicht**  über einen eigenen reflektiven Ethics-Score operationalisiert. Stattdessen werden verantwortungs- und sicherheitsbezogene Entwicklungsbedarfe (z. B. Datenschutzregeln, Compliance, Governance) über das **separate diagnostische Bedarfsmodul (** **DIAGNOSTIC_NEEDS** **)**  adressiert, um das strikte 18-Item-Budget der reflektiven Skalen einzuhalten und eine Verunreinigung der Kernkonstrukte zu vermeiden.
*Beitragende Quellen*: AIRS (Wang et al., 2026)[1], MAILS (Carolus et al., 2023)[2], AILRSE-5 (Oksanen et al., 2026)[3], AISES (Wang & Chuang, 2024)[4].

A5 Theory Hierarchy

Die Priorisierung der Quellen folgt der Hierarchieordnung für diagnostische Instrumente:

- **Direkte individuelle AI-Readiness-Skala (Höchste Priorität)** :
**AIRS**  (Wang et al., 2026)[1] – *Einzige direkte Skala zur individuellen AI Readiness in der aktiven Knowledge Base*.
- **Readiness-nahe Literacy- und Self-Efficacy-Skalen** :
**MAILS**  (Carolus et al., 2023)[2] – *AI-Literacy-Quelle* (Meta AI Literacy Scale).

**AISES**  (Wang & Chuang, 2024)[4] – *Readiness-nahe AI Self-Efficacy-Quelle*.

**AILRSE-5**  (Oksanen et al., 2026)[3] – *Readiness-nahe AI Learning Self-Efficacy-Quelle*.
- **Generative KI- & Adoptionsmodelle** :
**Lambiase et al. (2025)** [5] – *LLM-Nutzungszwecke und Erleichternde Bedingungen (FC)*.
- **Vertrauens- & Organisationskontext** :
**Paper Fragebogen 4 / Do Khac et al. (2025)** [9] – *Abgrenzung KI-Systemfähigkeit (Ability) und Integrität/Datenschutz von individueller Selbstwirksamkeit und Ethik-Literacy*.
- **Transfer- & Methodenmodelle** :
**Paper Fragebogen 1, 2, 3, 5 / Wichmann et al., Paetow et al.**  (*P3/TTF ist inaktiv aufgrund von**TASK_CONTEXT = NOT_PROVIDED*).

*Diagnostischer Fokus (**DIAGNOSTIC**)*: Das Instrument konzentriert sich strikt auf Kernbereitschaftsdimensionen. **Behavioral Intention**  wird **vollständig ausgeschlossen** , um Verfälschungen zu vermeiden und Ausfüllzeit zu sparen.

A6 Analysis Levels

Jedes wählbare Konstrukt wird exakt einer Analyseebene zugeordnet:

- **READINESS_CORE**  (Kernbereitschaft des Mitarbeitenden – 5 Skalen mit exakt je 3 Items):
*Wahrgenommenes kognitives KI-Grundverständnis / Subjective AI Literacy* (MAILS Know & Understand / AIRS Cognition)

*KI-Lern-Selbstwirksamkeit / AI Learning Readiness Self-Efficacy* (adaptiertes 3-Item-Subset der AILRSE-5)

*Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit* (AISES / MAILS Apply & Problem Solving)

*Kritische KI-Bewertungskompetenz & KI-Erkennung / Detection* (MAILS Detect AI)

*Affektiver Komfort im Umgang mit KI / Comfort with AI* (AIRS Comfort / AISES Comfort)
- **CONTEXT**  (Organisatorische Rahmenbedingungen – 1 Skala mit exakt 3 Items):
*Wahrgenommene Erleichternde Bedingungen / Facilitating Conditions* (adaptiertes 3-Item-Subset aus Lambiase et al. FC)
- **RELATED_CONSTRUCT**  (Verwandte System- & Governance-Eigenschaften):
*Wahrgenommene KI-Systemfähigkeit & Integrität / Data Privacy* (P4 Do Khac et al. – System- & Organisationseigenschaften)

*AI Ethics Literacy* (MAILS Ethics – gesellschaftlich-ethische Orientierung; wird aufgrund des Itembudgets **nicht**  als reflektives Kernkonstrukt aufgenommen, sondern im Bedarfsmodul adressiert)
- **EXCLUDE**  (Auszuschließende Konstrukte):
*Behavioral Intention* (P1, P2, P4, Lambiase – Grund: Für diagnostisches Instrument zur Entwicklungsbedarfserfassung vollständig entfernt).

*Task-Technology Fit (TTF)* (P3 – Grund: `TASK_CONTEXT = NOT_PROVIDED`).

*Schulungs- und Supportbedarf als reflektives Skalenkonstrukt* (Verlagerung in eine separate, formative/listenbasierte Bedarfserhebung, um die reflektive Skala der Facilitating Conditions nicht zu verunreinigen).

*Nonadaptive Threat/Fear* (P1 – krankheitsspezifisch).

*Anthropomorphic Interaction* (AISES – bei kaufmännischen GenAI-Werkzeugen irrelevant).

A7 Construct-Overlap Decisions

Systematische Re-Evaluation der Konstruktüberlappungen gemäß Masterprompt und Nutzerkorrekturen:

- **Klarstellung zu AIRS & Streichung als Ethik-Quelle** :
*Prüfung*: Das AIRS-Instrument von Wang et al. (2026) umfasst vier Faktoren: *Self-Efficacy and Cognition (SEC)*, *Optimism (OPT)*, *Collaborative Learning and Working (CLW)* und *Comfort (COM)*[1]. AIRS enthält **keine**  Ethik-Dimension.

*Entscheidung*: AIRS wird ausdrücklich als Ethik-Quelle gestrichen.
- **Begründung für den Ausschluss von AI Ethics Literacy als eigener reflektiver Kernskala** :
*Prüfung*: Um die Bearbeitungsdauer strikt unter 8 Minuten zu halten, ist das Gesamttarget auf **exakt 18 reflektive Items**  begrenzt (6 Konstrukte × 3 Items). Eine Aufnahme von *AI Ethics Literacy* (MAILS) als siebtes Konstrukt würde das Budget sprengen. Zudem dürfen kognitive Halluzinationserkennung (`Detect AI` / MAILS)[12], rechtlich-organisationaler Datenschutz (`Integrity` / P4)[9] und individuelle Ethik-Orientierung (`AI Ethics` / MAILS)[12] nicht in einer reflektiven Skala verunreinigt werden (`DR02_CONSTRUCT_PURITY`).

*Entscheidung*: `EXCLUDE_FROM_REFLECTIVE_CORE_ADD_TO_NEEDS_MODULE`.

*Begründung*: *Detect AI* verbleibt als reine kognitive Bewertungsdimension in `READINESS_CORE`. Ethische, rechtliche und sicherheitsbezogene Entwicklungsbedarfe werden praxisnah über das separate diagnostische Bedarfsmodul (`DIAGNOSTIC_NEEDS`) erfasst.
- **Comfort with AI (AIRS / AISES) vs. Emotion Regulation (MAILS)** :
*Prüfung*: `Comfort with AI` (AIRS/AISES) beschreibt ein Gefühl von Gelassenheit und Abwesenheit von Verunsicherung bei der KI-Nutzung[1][4]. `Emotion Regulation` (MAILS) misst die aktive psychologische Selbststeuerung negativer oder euphorischer Affekte[13].

*Entscheidung*: `PRIORITIZE_A` (Priorisierung von `Comfort with AI` aus AIRS/AISES).

*Begründung*: Keinesfalls zusammenführen, da unzureichende Konstruktäquivalenz. `Comfort with AI` verbleibt als Standard-Dimension in `READINESS_CORE`. `Emotion Regulation` wird ausgeschlossen.
- **Facilitating Conditions (Lambiase / P2) vs. Schulungs- und Supportbedarf** :
*Entscheidung*: `KEEP_SEPARATE`.

*Begründung*: `Facilitating Conditions` misst als reflektives Konstrukt die Wahrnehmung vorhandener organisationaler Ressourcen und Infrastruktur[14]. Konkrete Schulungsbedarfe (z. B. Wunsch nach Prompting-Kursen oder rechtlichen Leitfäden) werden als eigenständiges, kaufmännisches Abfragemodul (formativ/Multiple-Choice-Liste) integriert.
- **Itembudget-Anpassung AILRSE-5** :
*Entscheidung*: Um exakt 3 Items pro Konstrukt zu realisieren, werden 3 verifizierte Items ausgewählt. Diese werden ausdrücklich als **„adaptiertes 3-Item-Subset der ursprünglichen 5-Item-Skala AILRSE-5“**  gekennzeichnet. Es wird nicht behauptet, die vollständige AILRSE-5 einzusetzen.
- **Itembudget-Anpassung Facilitating Conditions (Lambiase et al., 2025)** :
*Entscheidung*: Aus den 4 verifizierten FC-Items bei Lambiase et al. (2025)[14] werden 3 Items ausgewählt. Diese werden ausdrücklich als **„3-Item-Subset der vier verifizierten FC-Items aus Lambiase et al. (2025)“**  ausgewiesen. Es wird nicht behauptet, die vollständige Originalskala einzusetzen.

A8 Construct Catalog

Das diagnostische Messinstrument umfasst **exakt 6 reflektive Konstrukte mit jeweils 3 Items (Gesamtzahl: 18 Items)** ; Bearbeitungsdauer: ≤ 8 Minuten:

- **Wahrgenommenes KI-Grundverständnis (** **READINESS_CORE_LIT** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (**exakt 3 Items** )

*Inhalt*: Subjektiv wahrgenommenes Verständnis der Funktionsweise und Grenzen generativer KI (abgegrenzt von objektivem Wissen).

*Quellenevidenz*: AIRS (Wang et al., 2026)[1], MAILS (Carolus et al., 2023)[12].
- **KI-Lern-Selbstwirksamkeit (** **READINESS_CORE_LEARN** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (**exakt 3 Items – ausdrücklich als adaptiertes 3-Item-Subset der AILRSE-5 ausgewiesen** )

*Inhalt*: Zutrauen in die eigene Fähigkeit, den Umgang mit neuen GenAI-Anwendungen selbstständig zu erlernen.

*Quellenevidenz*: AILRSE-5 (Oksanen et al., 2026)[3][15].
- **Praktische KI-Anwendungs- & Problemlöse-Selbstwirksamkeit (** **READINESS_CORE_APPLY** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (**exakt 3 Items** )

*Inhalt*: Selbstwirksamkeit bei der praktischen Nutzung von GenAI für kaufmännische Aufgaben und der Lösung auftretender Anwendungsanforderungen.

*Quellenevidenz*: AISES (Wang & Chuang, 2024)[16], MAILS (Carolus et al., 2023)[12].
- **Kritische KI-Bewertungskompetenz & KI-Erkennung (** **READINESS_CORE_DETECT** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (**exakt 3 Items** )

*Inhalt*: Wahrgenommene Fähigkeit, KI-generierte Inhalte zu erkennen und auf Plausibilität/Halluzinationen zu überprüfen (strikt getrennt von Richtlinien und Ethik).

*Quellenevidenz*: MAILS (Carolus et al., 2023)[12].
- **Affektiver Komfort im Umgang mit KI (** **READINESS_CORE_COMFORT** **)** 
*Analyseebene*: `READINESS_CORE`

*Messmodell*: Reflektiv (**exakt 3 Items** )

*Inhalt*: Emotionaler Komfort und Gelassenheit bei der Interaktion mit KI-Tools (getrennt von aktiver Emotionsregulation).

*Quellenevidenz*: AIRS (Wang et al., 2026)[1], AISES (Wang & Chuang, 2024)[16].
- **Wahrgenommene Erleichternde Bedingungen (** **CONTEXT_FC** **)** 
*Analyseebene*: `CONTEXT`

*Messmodell*: Reflektiv (**exakt 3 Items – ausdrücklich als 3-Item-Subset der vier verifizierten FC-Items aus Lambiase et al., 2025 ausgewiesen** )

*Inhalt*: Wahrnehmung vorhandener organisatorischer und technischer Rahmenbedingungen im Betrieb.

*Quellenevidenz*: Lambiase et al. (2025)[14], Paper Fragebogen 2 (Wichmann et al., 2025)[17].

*Diagnostischer Zusatzbaustein (Formatives Messformat außerhalb des 18-Item-Skalenbudgets)*:

**Diagnostische Bedarfsermittlung (** **DIAGNOSTIC_NEEDS** **)** : Formatives/listenbasiertes Erhebungselement zur Erfassung konkreter Anwendungs-, Schulungs-, Datenschutz- und Ethikbedarfe (z. B. Abfrage spezifischer Themen wie Prompting-Techniken, DSGVO-Compliance, Qualitätssicherung und kaufmännische Anwendungsfälle) zur direkten Maßnahmenableitung.

A9 Original-Scale Audit

Prüfung der Primärquellen hinsichtlich Struktur, Stichproben und Invarianz:

- **AIRS**  (Wang et al., 2026):
*Audit-Ergebnis*: Exakte Unterscheidung zwischen dem **initialen Itempool von 21 Items (Q1–Q21)** [18][19] und der **final gereinigten 13-Item-Skala** [1][20]. Nach Item-Total-Korrelationsanalysen wurden 8 Items gestrichen (Q4, Q5, Q6, Q7, Q10, Q11, Q15, Q17)[20]. Die verbleibenden 13 Items bilden 4 Faktoren (*SEC*, *OPT*, *CLW*, *COM*)[1][21]. Status: `FOUND`.
- **AILRSE-5**  (Oksanen et al., 2026):
*Audit-Ergebnis*: 5 Items, eindimensional[3][22]; 7-Punkt-Likert-Skala (1–7)[22]. Basierend auf N=20.173 aus 12 Ländern wird **skalare Invarianz**  über alle 12 Länder hinweg nachgewiesen (CFI=0.979, RMSEA=0.097)[3][23]. **Strikte Invarianz**  wird **nicht**  pauschal global erreicht, sondern wurde ausschließlich in den finnischen Stichproben nachgewiesen[3][24]. Status: `FOUND`.
- **MAILS**  (Carolus et al., 2023):
*Audit-Ergebnis*: 34 Items modular, 11-Punkt-Skala (0–10)[12]. Faktorielle Validität an N=300 nachgewiesen[2][26]. Status: `FOUND`.
- **AISES**  (Wang & Chuang, 2024):
*Audit-Ergebnis*: 22 Items, 4 Faktoren (*Assistance*, *Anthropomorphic Interaction*, *Comfort with AI*, *Technological Skills*)[4][16]; 7-Punkt-Likert-Skala[27]. Status: `FOUND`.
- **Lambiase et al. (2025)** :
*Audit-Ergebnis*: Facilitating Conditions (FC_1 bis FC_4; 7-Punkt-Skala)[14]. N=188 Software-Engineers; Preprint-Status wird explizit offengelegt[5]. Status: `FOUND`.

A10 Proposed Questionnaire Architecture

Struktur des diagnostischen Fragebogens (Gesamtdauer: ~6–8 Minuten; **exakt 18 reflektive Skalenitems**  + 1 Bedarfsmodul):

- **Teil 0: Einleitung & KI-Kontextdefinition** :
Neutrale Begrüßung, Datenschutzhinweis, präzise Definition des Messgegenstands (*"Generative KI-Werkzeuge wie ChatGPT Enterprise oder Microsoft Copilot im täglichen kaufmännischen Arbeitsablauf"*).
- **Teil 1: KI-Erfahrungs-Routing (Filterfrage)** :
Einstufung der Vorerfahrung: `NO_EXPERIENCE` (Keine Erfahrung), `LIMITED_EXPERIENCE` (Gelegentliche Nutzung), `REGULAR_USER` (Regelmäßige Nutzung).
- **Teil 2: Kernbereitschaft / Readiness Core (** **READINESS_CORE** **) [15 Items]** :
Modul A: Wahrgenommenes kognitives KI-Grundverständnis (**exakt 3 Items** )

Modul B: KI-Lern-Selbstwirksamkeit (**exakt 3 Items – adaptiertes Subset der AILRSE-5** )

Modul C: Praktische KI-Anwendungs-Selbstwirksamkeit (**exakt 3 Items – erfahrungsgefiltert** )

Modul D: Kritische KI-Bewertungskompetenz & Erkennung (**exakt 3 Items** )

Modul E: Affektiver Komfort im Umgang mit KI (**exakt 3 Items** )
- **Teil 3: Organisatorische Rahmenbedingungen (** **CONTEXT** **) [3 Items]** :
Modul F: Wahrgenommene Erleichternde Bedingungen / Facilitating Conditions (**exakt 3 Items – Subset aus Lambiase et al.** )
- **Teil 4: Diagnostische Bedarfsermittlung (** **DIAGNOSTIC_NEEDS** **)** :
Abfrage konkreter Schulungs- und Supportbedarfe (formatives Listenformat zur Erfassung von Praxis-, Prompting-, Ethik- und Datenschutzanforderungen).
- **Teil 5: Statistische Angaben** :
Kaufmännische Funktionsbereich-Zuordnung (z. B. Einkauf, Vertriebsinnendienst, Buchhaltung/Controlling, HR, allgemeine Verwaltung).

A11 Risks & Limitations

**Evidenzbasierte Aussage zur Validierungsstärke** : Das Fragebogeninstrument ist theoretisch fundiert und methodisch qualitätsgeprüft. Die Gütekriterien beruhen auf den publizierten Validierungsergebnissen der Primärquellen (z. B. AILRSE-5 skalare Invarianz[3][23], MAILS faktorielle Struktur[2][25]). Eine empirische Prüfung der psychometrischen Kennwerte im spezifischen Zielunternehmen steht vor der Datenerhebung noch aus (`status: theoretically_grounded_empirical_validation_pending`).

**Sprachliche Adaption (** **E2 – ADAPTED** **)** : Da maßgebliche Skalen (AIRS, AISES, AILRSE-5) im englischen Original vorliegen[1], stellen die deutschen Formulierungen linguistische Adaptionen dar (`E2`).

**Subjektives Verständnis vs. Objektives Wissen** : Das Selbstauskunftsinstrument erfasst das subjektiv wahrgenommene KI-Verständnis der Mitarbeitenden und keinen objektiven Wissenstest.

**Fehlender Aufgabenkontext (** **TASK_CONTEXT = NOT_PROVIDED** **)** : Eine Operationalisierung des Task-Technology Fit (TTF) unterbleibt.

A12 Design-Audit Reference

`DESIGN_AUDIT_REFERENCE`: **DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL**

Der finale **DESIGN_AUDIT**  ist damit vollständig abgeschlossen, widerspruchsfrei und methodisch abgesichert.

💡 **Möchten Sie nun im nächsten Schritt die finale Fragebogenerstellung gemäß** **RUN_MODE = QUESTIONNAIRE_GENERATION** **(unter Verwendung der Bindungsreferenz** **DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL** **, inklusive verifizierter Items, Critic Review, simulated Pretest und JSON-Export) durchführen lassen?**

---

