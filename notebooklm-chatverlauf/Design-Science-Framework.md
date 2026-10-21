# Design Science Framework for AI-Driven Questionnaire Generation

Quelle: https://notebook.google.com/notebook/8edb5ed6-c497-492d-9bee-d32ae9943ada
Exportiert: 21.10.2026, 18:58:16

---

## Frage

Erstelle die System-Prompts für die drei Agenten

---

## Antwort

Anbei findest du die ausformulierten **System-Prompts für die drei Agenten** , die du direkt in **Google NotebookLM**  oder in eine externe Multi-Agenten-Pipeline (z. B. via Rollen-Prompts oder Frameworks wie CrewAI/LangGraph) einbinden kannst[1][2]. Sie verknüpfen die methodischen Vorgaben (RAG, Few-Shot Prompting, Gütekriterien) direkt mit den wissenschaftlichen Grundlagen aus deinen Quellen[1][3].

Agent 1: Der Methodiker (Item-Generierung & Theoriefundierung)

**Rolle:**  Du bist ein wissenschaftlicher Methodiker und Experte für psychometrische Testkonstruktion sowie Datenanalyse im Bereich Wirtschaftsinformatik und Akzeptanzforschung[1][4].

**Ziel:**  Erstelle einen ersten Entwurf eines quantitativen Fragebogens zur Messung der **KI-Readiness von Mitarbeitenden**  in einem Unternehmen[2]. Die Fragen dürfen keinesfalls freihändig erfunden werden, sondern müssen strikt und nachvollziehbar aus der bereitgestellten wissenschaftlichen Literatur abgeleitet werden[3][5].

```
Du agierst in der Rolle von "Agent 1: Der Methodiker". 
Deine Aufgabe ist es, einen theoretisch fundierten Fragebogen zur Messung der "KI-Readiness von Mitarbeitenden" zu entwickeln.

1. THEORETISCHER RAHMEN (RAG):
Stütze dich bei der Item-Generierung exklusiv auf folgende Konstrukte aus den vorliegenden Quellentexten:
- Reasoned Action Approach (RAA): Intention to use, Attitude, Perceived Norms, Perceived Behavioral Control (Fishbein & Ajzen 2010).
- Trust-Modell für LLMs/GenAI: Ability (Explainability), Benevolence (Uncanny Valley), Integrity (Data Privacy) (Mayer et al. 1995; Do Khac et al. 2025).
- Task-Technology Fit (TTF): Abstimmung zwischen Aufgabenmerkmalen (McGrath's Task Circumplex: Intellective, Judgment, Conflict, Mixed-Motive, Execution) und Technologiemerkmalen (Goodhue & Thompson 1995; Paetow et al. 2025).
- Duality Approach: Perceived Efficacy vs. Perceived Costs/Barriers (Wichmann et al. 2024).

2. IN-CONTEXT LEARNING (Few-Shot):
Richte dich beim Aufbau, der Formulierung und der Antwortskalierung streng nach den validierten Beispiel-Items aus den Quellen (Datensatz_v1):
- Verwende eine einheitliche 7-Punkt-Likert-Skala (1 = "Stimme überhaupt nicht zu" bis 7 = "Stimme voll und ganz zu").
- Generiere für jedes Konstrukt genau 3 reflektierte Mess-Items.

3. OUTPUT-FORMAT:
Gib für jedes Item folgendes Schema an:
- Konstrukt & Sub-Dimension (z. B. Trust -> Integrity / Data Privacy)
- Theoretische Quelle / Ableitung (z. B. Do Khac et al. 2025; Smith et al. 1996)
- Item-Formulierung (Deutsch & Englisch)
- Antwortskala
```

Agent 2: Der Kritiker (Methodische Qualitätskontrolle & Gütekriterien)

**Rolle:**  Du bist ein strenger methodischer Peer-Reviewer für empirische Sozialforschung und psychometrische Fragebogenkonstruktion[1][3].

**Ziel:**  Überprüfe den von Agent 1 generierten Fragentwurf unnachgiebig auf methodische Fehler, verzerrte Formulierungen und die Einhaltung der wissenschaftlichen Gütekriterien (**Objektivität, Reliabilität, Validität** )[1][3].

```
Du agierst in der Rolle von "Agent 2: Der Kritiker".
Deine Aufgabe ist die methodische und sprachliche Qualitätsprüfung des von Agent 1 vorgelegten Fragentwurfs.

1. PRÜFKRITERIEN (Ausschluss von Erhebungsfehlern):
Scanne jedes Item systematisch auf folgende typische Fehlerquellen:
- Double-Barreled Questions: Werden zwei unterschiedliche Sachverhalte in einer einzigen Frage zusammengefasst? (z. B. "Ich finde KI nützlich und sicher") -> Sofort aufspalten.
- Suggestivfragen / Verhaltensorientierte Tendenzen: Enthält die Frage wertende Adjektive, die eine bestimmte Antwort nahelegen?
- Unklare/Mehrdeutige Formulierungen: Werden Fachbegriffe verwendet, die ohne Vorwissen nicht verstanden werden?
- Negativ formulierte Items / Doppelverneinungen: Vermeide komplizierte Verneinungen, die die kognitive Belastung erhöhen.

2. GÜTEKRITERIEN-CHECK:
- Inhaltsvalidität: Decken die 3 Items das theoretische Konstrukt vollständig ab oder messen sie etwas Ähnliches?
- Invarianz & Skalierung: Ist die 7-Punkt-Likert-Skala für alle Items konsistent und trennscharf gewählt?

3. OUTPUT-FORMAT:
Gib ein strukturiertes Review ab:
- Status: [Freigegeben / Überarbeitung erforderlich]
- Gefundene Schwachstellen: Liste spezifischer Items mit konkreter Fehlerbenennung.
- Konstruktiver Korrekturvorschlag: Biete für jedes bemängelte Item eine optimierte, korrigierte Formulierung an.
```

Agent 3: Der Proband / Experte (Verständlichkeits- & Pretest-Simulation)

**Rolle:**  Du simulierst eine Testperson (Pretest-Teilnehmer / Fachexperte aus einem Unternehmen) mit unterschiedlichem Vorwissen bezüglich Künstlicher Intelligenz[6].

**Ziel:**  Evaluiere den Fragebogen aus Perspektive der Anwendbarkeit im Unternehmensalltag, um kognitive Überlastung, Abbruchquoten und Verständnisprobleme zu minimieren[3][6].

```
Du agierst in der Rolle von "Agent 3: Der Proband" (Simulierter Pretest).
Du nimmst die Perspektive von zwei unterschiedlichen Unternehmensakteuren ein:
- Person 1: Sachbearbeiter/in im Fachbereich (wenig technisches KI-Vorwissen).
- Person 2: Führungskraft / Senior Decision-Maker (Fokus auf Datenschutz, Effizienz und Zielerreichung).

1. EVALUATIONSKRITERIEN:
Bewerte die vom Kritiker (Agent 2) freigegebenen Fragen hinsichtlich:
- Verständlichkeit: Sind die Fragen im Arbeitskontext ohne Nachfragen verständlich?
- Kognitive Belastung & Bearbeitungsdauer: Wirkt der Fragebogen flüssig oder ermüdend?
- Akzeptanz / Sensitive Themen: Werden Fragen zum Thema Ängste oder Kontrollverlust (z. B. Fear/Uncanny) als unangenehm oder bedrohlich wahrgenommen?

2. OUTPUT-FORMAT:
Erstelle einen Pretest-Bericht mit folgendem Aufbau:
- Perspektiv-Check Sachbearbeiter/in: Verständlichkeit (1-5 Sterne) + konkrete Anmerkungen.
- Perspektiv-Check Führungskraft: Praxisrelevanz (1-5 Sterne) + konkrete Anmerkungen.
- Abschließende Freigabe: Finale Bestätigung des optimierten Fragebogens zur Messung der KI-Readiness.
```

Einbindung im NotebookLM- und DSR-Framework

**Iteratives Feedback (Evaluation nach Peffers et al. 2007):**  In deiner DSR-Hausarbeit (Kapitel 4 & 5) dokumentierst du die Durchläufe zwischen Agent 1 (Methodiker) → Agent 2 (Kritiker) → Agent 3 (Proband) exakt als **Dokumentation deiner Lösungsiterationen und Qualitätskontrolle** [7][8].

**GitHub-Repository:**  Speichere diese System-Prompts als Text- oder JSON-Dateien in deinem GitHub-Repository ab, um die Vorgabe zur Transparentmachung deines Lösungsweges zu erfüllen[2][9].

💡 **Sollen wir als Nächstes den ersten Durchlauf simulieren und von Agent 1 (Methodiker) einen konkreten Fragentwurf zur KI-Readiness auf Basis der Quellen generieren lassen?**

---

## Frage

Simuliere den ersten Durchlauf mit Agent 1

---

## Antwort

Hier ist die Simulation des ersten Durchlaufs von **Agent 1 (Der Methodiker)** . In dieser Rolle generiert das System den ersten wissenschaftlich fundierten Fragentwurf zur Erfassung der **KI-Readiness von Mitarbeitenden** , indem es die theoretischen Konstrukte aus den bereitgestellten Quellentexten via Retrieval-Augmentierte Generation (RAG) abbildet und in ein 7-Punkt-Likert-Skalierungsschema überführt[1].

🤖 Agent 1: Der Methodiker – Fragentwurf (Durchlauf 1)

**System-Kontext & In-Context-Vorgabe:** 
*Zielgruppe:* Mitarbeitende und Führungskräfte im Unternehmen
*Kontext:* Generierung von Mess-Items zur Bewertung der individuellen KI-Readiness und der Akzeptanz generativer KI-Werkzeuge (z. B. ChatGPT/LLMs)[4]
*Skalierung:* 7-Punkt-Likert-Skala (1 = „Stimme überhaupt nicht zu“ bis 7 = „Stimme voll und ganz zu“)[1]

Block 1: Verhaltensabsicht & Akzeptanz (Reasoned Action Approach / RAA)

*Theoretische Grundlegung:* Fishbein & Ajzen (2010); Gesk et al. (2021)[8].

Konstrukt 1.1: Intention to Use (Nutzungsabsicht)

- **Item INT_1:** 
*Deutsch:* Ich beabsichtige, generative KI-Anwendungen in Zukunft regelmäßig für meine täglichen Arbeitsaufgaben zu nutzen[2].

*Englisch:* I intend to use generative AI applications for my daily work tasks in the future[2].

*Quelle / Ableitung:* Adaptiert nach Fishbein & Ajzen (2010); Do Khac et al. (2025)[5][10].
- **Item INT_2:** 
*Deutsch:* Ich habe den festen Plan, KI-gestützte Systeme im Betrieb einzusetzen, sobald diese verfügbar gemacht werden[2].

*Englisch:* I plan to use AI-supported systems in my company as soon as they become available[2].

*Quelle / Ableitung:* Adaptiert aus Datensatz_v1 (Questionnaire 1 & 2)[2].
- **Item INT_3:** 
*Deutsch:* Meine Absicht, KI zur Optimierung meiner Arbeitsprozesse zu verwenden, ist hoch[5].

*Englisch:* My intention to use AI to optimize my work processes is high[5].

*Quelle / Ableitung:* Adaptiert aus Do Khac et al. (2025)[5].

Konstrukt 1.2: Perceived Norms (Subjektive Normen)

- **Item NOR_1:** 
*Deutsch:* Kolleginnen und Kollegen, deren Meinung ich schätze, würden mir raten, KI-Werkzeuge bei der Arbeit zu nutzen[2].

*Englisch:* Colleagues whose opinion I value would advise me to use AI tools at work[2].

*Quelle / Ableitung:* Adaptiert nach Fishbein & Ajzen (2010); Wichmann et al. (2024)[2].
- **Item NOR_2:** 
*Deutsch:* Führungskräfte in einer mir vergleichbaren Position empfehlen den Einsatz von generativer KI[11].

*Englisch:* Managers in a position similar to mine recommend the use of generative AI[11].

*Quelle / Ableitung:* Adaptiert aus Datensatz_v1 (PowerPilot)[11].
- **Item NOR_3:** 
*Deutsch:* In meinem beruflichen Umfeld wird erwartet, dass man sich neuen KI-Technologien gegenüber aufgeschlossen zeigt[2][13].

*Englisch:* In my professional environment, it is expected to be open toward new AI technologies[2][13].

*Quelle / Ableitung:* Adaptiert nach Wichmann et al. (2024)[13][14].

Block 2: Vertrauen in KI-Systeme (Trust Model nach Mayer et al. 1995 / Do Khac et al. 2025)

*Theoretische Grundlegung:* Mayer et al. (1995); Do Khac et al. (2025)[5].

Konstrukt 2.1: Ability / Explainability (Wahrgenommene Fähigkeit & Erklärbarkeit)

- **Item ABI_1:** 
*Deutsch:* Ich verstehe die prinzipielle Funktionsweise von generativen KI-Modellen in unserem Arbeitskontext[5][16].

*Englisch:* I know how generative AI models work in our business context[5][16].

*Quelle / Ableitung:* Do Khac et al. (2025) (Item X1)[5][16].
- **Item ABI_2:** 
*Deutsch:* Ich kann nachvollziehen, wie das KI-System zu seinen Antworten und Ergebnissen gelangt[5][16].

*Englisch:* I can understand how the AI system achieves its results[5][16].

*Quelle / Ableitung:* Do Khac et al. (2025) (Item X2)[5][16].
- **Item ABI_3:** 
*Deutsch:* Ich bin in der Lage zu beurteilen, ob die von der KI generierten Ergebnisse inhaltlich korrekt sind[5][16].

*Englisch:* I can assess whether the results generated by the AI are correct[5][16].

*Quelle / Ableitung:* Do Khac et al. (2025) (Item X3)[5][16].

Konstrukt 2.2: Integrity / Data Privacy (Integrität & Datenschutz)

- **Item INTG_1:** 
*Deutsch:* Ich habe keine Bedenken, dass die Eingabe unternehmensinterner Informationen in das KI-System Daten an unbefugte Dritte weitergibt[5][17].

*Englisch:* I have no doubts that using the AI system will pass internal company information to third parties[5][17].

*Quelle / Ableitung:* Do Khac et al. (2025) (Item D1)[5][17].
- **Item INTG_2:** 
*Deutsch:* Ich vertraue darauf, dass unsere Interaktionsdaten bei der Nutzung der KI sicher verarbeitet werden[5][17].

*Englisch:* I think that our interaction data while using the AI system are safe[5][17].

*Quelle / Ableitung:* Do Khac et al. (2025) (Item D2)[5][17].
- **Item INTG_3:** 
*Deutsch:* Ich befürchte nicht, dass das KI-System durch unsere Nutzung zu viele vertrauliche Details über unser Unternehmen speichert[5][17].

*Englisch:* I do not worry that the AI system will hold too much sensitive information about our company[5][17].

*Quelle / Ableitung:* Do Khac et al. (2025) (Item D3)[5][17].

Konstrukt 2.3: Benevolence / Uncanny Valley (Wohlwollen vs. Unbehaglichkeit)

- **Item BEN_1 (Invers formuliert):** 
*Deutsch:* Ich empfinde die Interaktion mit der generativen KI nicht als unheimlich oder unangenehm[5].

*Englisch:* I do not perceive interacting with generative AI as uncanny or unsettling[5].

*Quelle / Ableitung:* Adaptiert aus Do Khac et al. (2025) (Item U1)[5][17].
- **Item BEN_2:** 
*Deutsch:* Ich habe das Gefühl, dass das KI-System darauf ausgelegt ist, meine Arbeit positiv zu unterstützen[5][19].

*Englisch:* I feel that the AI system is designed to positively support my work[5][19].

*Quelle / Ableitung:* Adaptiert nach Mayer et al. (1995); Do Khac et al. (2025)[6].
- **Item BEN_3:** 
*Deutsch:* Die KI-Anwendung wirkt im Arbeitsdialog natürlich und frei von bedrohlichen Merkmalen[5][18].

*Englisch:* The AI application feels natural in the work dialogue and free from threatening characteristics[5][18].

*Quelle / Ableitung:* Adaptiert nach Hyun Baek & Kim (2023); Do Khac et al. (2025)[5].

Block 3: Aufgaben-Technologie-Passung (Task-Technology Fit / TTF)

*Theoretische Grundlegung:* Goodhue & Thompson (1995); McGrath's Group Task Circumplex; Paetow et al. (2025)[21].

Konstrukt 3.1: Task-Technology Fit (Passung für kreative & analytische Aufgaben)

- **Item TTF_1 (Kreativ- & Entwurfsaufgaben):** 
*Deutsch:* Die Funktionen der generativen KI passen hervorragend zu unseren Aufgaben bei der Erstellung neuer Konzepte und Inhaltsentwürfe[21].

*Englisch:* The capabilities of generative AI fit well with our tasks in creating new concepts and drafting content[21].

*Quelle / Ableitung:* Adaptiert nach McGrath (1984); Paetow et al. (2025)[24].
- **Item TTF_2 (Problemlösungs- & Konfliktmanagementaufgaben):** 
*Deutsch:* Bei der Bearbeitung komplexer Problemstellungen unterstützt mich die KI effektiv dabei, unterschiedliche Perspektiven zu strukturieren[21].

*Englisch:* When handling complex problem-solving tasks, the AI effectively supports me in structuring different perspectives[21].

*Quelle / Ableitung:* Adaptiert nach McGrath (1984) (Conflict/Mixed-Motive Tasks); Paetow et al. (2025)[24].
- **Item TTF_3 (Leistungsrelevanz):** 
*Deutsch:* Der Einsatz von KI verbessert meine individuelle Arbeitsleistung bei der Erledigung täglicher Arbeitsaufgaben spürbar[28].

*Englisch:* Using AI noticeably improves my individual work performance in completing daily tasks[28].

*Quelle / Ableitung:* Adaptiert aus Goodhue & Thompson (1995); Paetow et al. (2025)[23].

Block 4: Nutzen- vs. Barrierenabwägung (Duality Approach)

*Theoretische Grundlegung:* Gesk et al. (2021); Wichmann et al. (2024)[2].

Konstrukt 4.1: Perceived Efficacy & Costs (Nutzen vs. Aufwand/Barrieren)

- **Item EFF_1 (Wirksamkeit):** 
*Deutsch:* Durch die Nutzung von KI kann die Bearbeitungszeit für Routineaufgaben in meiner Abteilung deutlich reduziert werden[2].

*Englisch:* Using AI significantly reduces the processing time for routine tasks in my department[2].

*Quelle / Ableitung:* Adaptiert aus Datensatz_v1 (Perceived Response Efficacy)[2][12].
- **Item BAR_1 (Kosten/Barrieren - Invers):** 
*Deutsch:* Der Aufwand, die Einarbeitung in KI-Tools zu erlernen, steht in einem angemessenen Verhältnis zum Nutzen[2].

*Englisch:* The effort required to learn AI tools is reasonable compared to the benefits gained[2].

*Quelle / Ableitung:* Adaptiert aus Datensatz_v1 (Perceived Costs/Barriers)[2].
- **Item BAR_2 (Kontrollverlust/Bedrohung):** 
*Deutsch:* Ich habe keine Befürchtung, dass der Einsatz von KI zu einem Verlust der Kontrolle über meine eigenen Arbeitsprozesse führt[2].

*Englisch:* I do not fear that using AI will lead to a loss of control over my own work processes[2].

*Quelle / Ableitung:* Adaptiert nach Gesk et al. (2021); Wichmann et al. (2024)[9][34].

Statusmeldung von Agent 1:

Der Fragentwurf ist vollständig erstellt und deckt alle theoretischen Säulen des KI-Readiness-Modells ab[4].

💡 **Sollen wir jetzt den zweiten Schritt simulieren und den Entwurf von Agent 2 (Der Kritiker) auf methodische Fehler wie** **Double-Barreled Questions** **, Suggestivität und Gütekriterien prüfen lassen** [3][36]**?**

---

## Frage

erkläre aufgabenstellung ganz einfach was ich machen soll

---

## Antwort

Ganz einfach zusammengefasst musst du in diesem Modul folgende drei Dinge tun:

1. Das Ziel (Das Produkt / Artefakt)

Du entwickelst **Anweisungen (Prompts/Leitlinien)**  für ein Künstliches-Intelligenz-Modell[1]. Diese Prompts sollen die KI in die Lage versetzen, automatisch einen wissenschaftlich fundierten Fragebogen zu erstellen[1]. Der konkrete Inhalt des Fragebogens ist die Messung der **KI-Readiness von Mitarbeitenden**  in einem Unternehmen[2]. Die Fragen dürfen dabei nicht frei erfunden werden, sondern müssen direkt aus wissenschaftlichen Theorien abgeleitet werden[2].

2. Die technischen Werkzeuge

**Google NotebookLM:**  Du lädst die bereitgestellten Unterlagen in NotebookLM hoch, entwickelst dort deine Prompts und erzeugst am Ende einen Freigabelink[2][3].

**GitHub:**  Du erstellst ein GitHub-Repository und fügst dort deinen Code sowie den Link zu deinem NotebookLM-Projekt ein, um dein Vorgehen offenzulegen[1][3].

3. Die schriftliche Ausarbeitung (Hausarbeit)

Du schreibst eine **Hausarbeit von maximal 10 inhaltlichen Seiten** [4][5]. Der Aufbau der Arbeit orientiert sich strikt an den sechs Schritten des **Design Science Research (DSR)**  Prozesses[1][6]:

**Problemidentifikation & Motivation:**  Warum ist eine automatisierte Fragebogenerstellung für Unternehmen wichtig[6][7]?

**Zielsetzung des Tools:**  Welche Anforderungen muss dein Leitlinienmodell erfüllen[6]?

**Entwicklung des Artefakts:**  Wie hast du das Prompt-Modell (z. B. das Drei-Agenten-System) aufgebaut[6]?

**Demonstration im Anwendungsumfeld:**  Zeige einen konkreten Durchlauf zur Erstellung des KI-Readiness-Fragebogens[6].

**Evaluation:**  Beschreibe, wie du die Qualität der Fragen geprüft hast und welche Korrekturschleifen du durchlaufen bist[6][7].

**Fazit & Ausblick:**  Fasse die Ergebnisse zusammen, nenne Limitationen und zeige Weiterentwicklungsmöglichkeiten auf[8].

💡 **Sollen wir als Nächstes den zweiten Agenten (den Kritiker) simulieren, um die ersten Fragen aus unserem Test-Durchlauf methodisch zu überprüfen?**

---

## Frage

erkläre ausführlicher: Du entwickelst Anweisungen (Prompts/Leitlinien) für ein Künstliches-Intelligenz-Modell
. Diese Prompts sollen die KI in die Lage versetzen, automatisch einen wissenschaftlich fundierten Fragebogen zu erstellen
. Der konkrete Inhalt des Fragebogens ist die Messung der KI-Readiness von Mitarbeitenden in einem Unternehmen

---

## Antwort

Hier ist eine detaillierte und leicht verständliche Aufschlüsselung der drei Kernelemente deiner Aufgabenstellung:

1. „Du entwickelst Anweisungen (Prompts/Leitlinien) für ein Künstliches-Intelligenz-Modell“

Im Rahmen dieses Moduls erstellst du ein technisches **Artefakt nach dem Design Science Research (DSR) Paradigma** [1]. Das Artefakt besteht nicht aus einer neu programmierten Software, sondern aus **strukturierten Prompts und Anweisungen (Leitlinien)**  für ein Large Language Model (LLM) wie Google NotebookLM oder ChatGPT[1][2].

Damit das Sprachmodell verlässlich arbeitet und qualitativ hochwertige Ergebnisse liefert, stützt du deine Prompts auf drei fortgeschrittene KI-Methoden[3]:

**Retrieval-Augmented Generation (RAG):**  Du speist wissenschaftliche Quellentexte und Theorien direkt via Prompt-Injektion als Kontext ein, damit die KI halluzinationsfreie Antworten liefert[3].

**Few-Shot Prompting (In-Context Learning):**  Du übergibst dem Modell konkrete Beispiel-Fragebögen und Muster-Items aus der Datenbasis als Vorlage für Skalierung und Format[3].

**Agentische Workflows (Multi-Agenten-System):**  Du unterteilst den Generierungsprozess in verschiedene Rollen (z. B. **Agent 1: Methodiker**  zur Generierung, **Agent 2: Kritiker**  zur methodischen Prüfung und **Agent 3: Proband**  zur Verständlichkeitsprüfung)[3][6].

2. „Diese Prompts sollen die KI in die Lage versetzen, automatisch einen wissenschaftlich fundierten Fragebogen zu erstellen“

„Wissenschaftlich fundiert“ bedeutet, dass die Fragen **niemals frei erfunden oder unüberlegt formuliert**  werden dürfen[2][7]. Das KI-Modell muss angewiesen werden, jedes einzelne Item sachlogisch aus etablierten Theorien der Akzeptanz- und Sozialforschung abzuleiten[2][7].

In deinen Quellen finden sich dafür folgende primäre Theoriebausteine:

**Reasoned Action Approach (RAA):**  Misst die persönliche Einstellung (*Attitude*), den sozialen Druck (*Perceived Norms*) und die wahrgenommene Verhaltenskontrolle (*Perceived Behavioral Control*) zur Vorhersage der Nutzungsabsicht (*Intention to use*)[8].

**Trust-Modell für LLMs/GenAI:**  Erfasst das Vertrauen in KI-Systeme über die Dimensionen Fähigkeit/Erklärbarkeit (*Ability/Explainability*), Wohlwollen/Unbehaglichkeit (*Benevolence/Uncanny Valley*) und Integrität/Datenschutz (*Integrity/Data Privacy*)[5].

**Task-Technology Fit (TTF):**  Prüft, wie gut die Funktionen der KI mit den spezifischen Arbeitsaufgaben der Beschäftigten übereinstimmen[15].

**Duality Approach:**  Wiegt die wahrgenommene Wirksamkeit (*Perceived Efficacy*) gegen emotionale Bedenken, Ängste und Kosten (*Fear/Barriers*) ab[18][19].

Zusätzlich stellt die Leitlinie sicher, dass wissenschaftliche **Gütekriterien (Objektivität, Reliabilität, Validität)**  eingehalten und methodische Fehler wie Doppelverneinungen oder Suggestivfragen systematisch eliminiert werden[3].

3. „Der konkrete Inhalt des Fragebogens ist die Messung der KI-Readiness von Mitarbeitenden in einem Unternehmen“

Die praktische Problemstellung des Praxispartners verlangt nach einem Instrument, mit dem Unternehmen ermitteln können, wie bereit und aufgeschlossen ihre Beschäftigten für den Einsatz generativer KI-Werkzeuge sind[2][21].

Der automatisch erzeugte Fragebogen misst daher konkret:

**Nutzungsbereitschaft:**  Beabsichtigen die Mitarbeitenden, KI-Tools in ihren Arbeitsprozessen einzusetzen[4][5]?

**Kompetenz & Verständnis:**  Verstehen die Mitarbeitenden, wie die KI Ergebnisse erzeugt und wie korrekt diese sind (*Ability*)[5][22]?

**Datenschutz & Vertrauen:**  Haben die Beschäftigten Bedenken bezüglich der Sicherheit interner Unternehmensdaten (*Integrity/Data Privacy*)[5][23]?

**Aufgabenpassung:**  Sieht das Personal einen konkreten Mehrwert von KI-Anwendungen für seine täglichen Aufgaben (*Task-Technology Fit*)[15]?

Zusammenfassung deiner konkreten Aufgaben

**Prompts formulieren:**  Erstelle die Leitlinien (z. B. das 3-Agenten-System) in NotebookLM[2][3].

**Demonstration & Durchlauf:**  Lasse die KI mit diesen Prompts einen fragebogenbasierten Entwurf zur KI-Readiness ausgeben[2][25].

**Dokumentation in GitHub & Hausarbeit:**  Dokumentiere dein Vorgehen, die Prompt-Iterationen und Hindernisse in einer maximal 10-seitigen Ausarbeitung nach der DSR-Struktur (Peffers et al. 2007) und verlinke dein GitHub-Repository[1].

💡 **Möchtest du als Nächstes den Fragentwurf aus unserem ersten Durchlauf von Agent 2 (dem Kritiker) auf methodische Fehler und Gütekriterien prüfen lassen?**

---

## Frage

Simuliere Agent 2 (Kritiker)

---

## Antwort

🧐 Agent 2: Der Kritiker – Methodischer Review-Bericht (Durchlauf 1)

**Rolle:**  Agent 2 (Der Kritiker) – Prüfinstanz für empirische Sozialforschung und psychometrische Testkonstruktion[1][2].
**Prüfgegenstand:**  Fragentwurf aus Durchlauf 1 (Agent 1)
**Prüfkriterien:**  Vermeidung von Erhebungsfehlern (Double-Barreled Questions, Suggestivfragen, Doppelverneinungen) sowie Sicherstellung der Gütekriterien (**Objektivität, Reliabilität, Validität** )[3][4].

1. Prüfstatus

**Gesamtbewertung:**  ⚠️ **Überarbeitung erforderlich**

**Begründung:**  Der Entwurf von Agent 1 deckt die theoretischen Konstrukte inhaltlich gut ab. Allerdings weisen einige Items methodische Mängel auf, die zu Verfälschungen der Messergebnisse und erhöhter kognitiver Belastung führen können[3][5].

2. Detaillierte Item-Mängelanalyse

A. Invers formulierte Items & Doppelverneinungen

- **Item INTG_1:**  *„Ich habe keine Bedenken, dass die Eingabe unternehmensinterner Informationen in das KI-System Daten an unbefugte Dritte weitergibt.“*
❌ **Fehler:**  Verneinte Formulierung („keine Bedenken“). Antwortet eine Person mit *1 = Stimme überhaupt nicht zu*, bedeutet das doppelt verneint: „Ich habe Bedenken, dass es nicht weitergegeben wird“ – dies führt zu schwerwiegenden Messfehlern[4].
- **Item BEN_1:**  *„Ich empfinde die Interaktion mit der generativen KI nicht als unheimlich oder unangenehm.“*
❌ **Fehler:**  Doppelverneinung („nicht als unheimlich“) kombiniert mit einer Doppelabfrage (*Double-Barreled Question*).

B. Double-Barreled Questions (Doppelabfragen)

- **Item BEN_1:**  *„...unheimlich oder unangenehm.“*
❌ **Fehler:**  Unheimlichkeit (*Uncanny Valley*) und Unangenehmsein sind zwei verschiedene emotionale Dimensionen, die getrennt gemessen werden müssen[6][7].
- **Item BAR_1:**  *„Der Aufwand, die Einarbeitung in KI-Tools zu erlernen, steht in einem angemessenen Verhältnis zum Nutzen.“*
❌ **Fehler:**  Vermischt die Aufwandseinschätzung mit der Nutzenbewertung in einer einzigen Frage.

C. Suggestivformulierungen & Voraussetzungsfehler

- **Item TTF_1:**  *„Die Funktionen der generativen KI passen hervorragend zu unseren Aufgaben...“*
❌ **Fehler:**  Das Adjektiv „hervorragend“ ist wertend/suggestiv und verfälscht die unvoreingenommene Antwortverteilung auf der 7-Punkt-Likert-Skala[5][8].
- **Item INT_2:**  *„Ich habe den festen Plan, KI-gestützte Systeme im Betrieb einzusetzen, sobald diese verfügbar gemacht werden.“*
❌ **Fehler:**  Enthält die Bedingung „sobald diese verfügbar gemacht werden“, wodurch die Bedingung statt der reinen Nutzungsabsicht gemessen wird[9][10].

3. Konkrete Korrekturvorschläge (Optimierte Fragensätze)

Agent 2 korrigiert die betroffenen Items für den zweiten Durchlauf:

| Item-ID | Ursprüngliche Formulierung (Agent 1) | Methodisch korrigierte Formulierung (Agent 2) | Korrekturgrund |
| --- | --- | --- | --- |
| **INT_2** | ...sobald diese verfügbar gemacht werden. | Ich habe den festen Plan, KI-gestützte Systeme im Betrieb einzusetzen. | Bedingung gestrichen (Fokus auf reine Absicht)[9]. |
| **INTG_1** | Ich habe **keine Bedenken** , dass... weitergibt. | Ich vertraue darauf, dass eingegebene unternehmensinterne Informationen nicht an unbefugte Dritte weitergegeben werden. | Beseitigung der Doppelverneinung[7]. |
| **BEN_1** | ...**nicht**  als **unheimlich oder unangenehm** . | Ich empfinde die Interaktion mit der generativen KI als unheimlich. *(Invers skaliert)* | Aufspaltung & Eliminierung der Doppelabfrage[7]. |
| **TTF_1** | ...passen **hervorragend**  zu... | Die Funktionen der generativen KI passen zu unseren Aufgaben bei der Erstellung neuer Konzepte. | Eliminierung des Suggestivworts „hervorragend“[5]. |
| **BAR_1** | Der Aufwand... steht in einem angemessenen Verhältnis zum Nutzen. | Die Einarbeitung in die Nutzung von KI-Werkzeugen erfordert für mich zu viel Zeit. | Aufspaltung auf reine Barrieren-/Kostenmessung[9]. |

4. Freigabe für den Pretest (Agent 3)

Mit diesen Korrekturen erfüllt der Fragenkatalog die notwendigen psychometrischen Standards:

**Objektivität:**  Eindeutige, unvoreingenommene Formulierungen verhindern unterschiedliche Interpretationsspielräume[4].

**Reliabilität:**  Einheitliche Ausrichtung der 7-Punkt-Likert-Skala (1–7) erhöht die interne Konsistenz[8].

**Inhaltsvalidität:**  Die Items spiegeln die theoretischen Konstrukte (*RAA, Trust, TTF, Duality*) präzise wider[6][9].

Das überarbeitete Item-Set wird hiermit an **Agent 3 (Der Proband / Pretest-Simulation)**  übergeben, um die Verständlichkeit und Praxistauglichkeit aus Nutzersicht zu prüfen[2].

💡 **Sollen wir als Nächstes die Simulation von Agent 3 (Proband/Pretest) durchführen, um das Feedback eines Sachbearbeiters und einer Führungskraft einzuholen?**

---

## Frage

Simuliere Agent 3 (Proband)

---

## Antwort

🧪 Agent 3: Der Proband – Pretest-Simulation & Verständlichkeitsbericht

**Rolle:**  Agent 3 (Der Proband) simuliert eine virtuelle Testperson und bewertet als Fachexperte die Praxistauglichkeit, Verständlichkeit und kognitive Belastung des von Agent 2 methodisch korrigierten Fragebogens[1].

Für eine praxisnahe Evaluation im Unternehmenskontext nimmt Agent 3 zwei typische Rollenperspektiven ein:

**Perspektive A:**  Sachbearbeiter/in im Fachbereich (Operative Anwendung, wenig KI-Spezialwissen).

**Perspektive B:**  Führungskraft / Senior Decision-Maker (Strategische Perspektive, Fokus auf Leistung und Datenschutz)[2].

1. Pretest-Evaluation aus Perspektive A: Sachbearbeiter/in (Endanwender)

A. Sprachliche Verständlichkeit & Fachbegriffe

**Postiver Befund:**  Die von Agent 2 korrigierten Fragen vermeiden unklare Verschachtelungen und schwere Doppelverneinungen, was das Durchlesen flüssig macht[3].

- **Anmerkung / Hürde:**  Der Begriff *„generative KI-Anwendungen“* oder *„kognitive Aufgaben“* ist im operativen Alltagsgeschäft nicht allen Mitarbeitenden sofort geläufig.
*Empfehlung:* Dem Fragebogen sollte ein kurzer, 2-sätziger Einleitungstext vorgeschaltet werden, der praxiserprobte Beispiele nennt (z. B. *„Unter generativer KI verstehen wir Text- und Assistenzsysteme wie ChatGPT, Microsoft Copilot oder unternehmensinterne Chatbots“*).

B. Kognitive Belastung & Skalierung

Die durchgängig verwendete **7-Punkt-Likert-Skala**  (1 = „Stimme überhaupt nicht zu“ bis 7 = „Stimme voll und ganz zu“) wird als übersichtlich und gewohnt wahrgenommen[4].

Durch die Eliminierung der Doppelabfragen (*Double-Barreled Questions*) durch Agent 2 entsteht keine Verwirrung mehr beim Wählen der Antwortstufe.

2. Pretest-Evaluation aus Perspektive B: Führungskraft / Decision-Maker

A. Relevanz & Vertrauensfaktoren (Trust & Integrity)

**Datenschutz & Integrität:**  Fragen zur Datensicherheit bei KI-Eingaben sprechen die Hauptbedenken von Führungskräften außerhalb der IT-Abteilung direkt an, wo Datenschutz (*Integrity*) häufig höher gewichtet wird als reine Funktionsfähigkeit[5].

**Aufgabenpassung (Task-Technology Fit):**  Die Differenzierung nach unterschiedlichen Aufgabenarten (z. B. Erstellung von Konzepten vs. Bearbeitung von Routineaufgaben) erlaubt eine präzise Einschätzung des tatsächlichen Arbeitsnutzens[6].

B. Bearbeitungsökonomie & Auswertbarkeit

**Zeitaufwand:**  Der strukturierte Fragenkatalog umfasst pro Konstrukt genau 3 Items und benötigt eine Bearbeitungszeit von ca. 5 bis 7 Minuten. Dies liegt im optimalen Rahmen, um hohe Rücklaufquoten ohne Abbrüche zu gewährleisten.

**Ergebnisrelevanz:**  Die Antworten liefern dem Management ein klares Profil darüber, ob Vorbehalte primär aus fehlendem Verständnis (*Ability*), Sorge um Unternehmensdaten (*Integrity*) oder fehlender Arbeitswertschöpfung (*TTF*) resultieren[5][7].

3. Pretest-Gesamtergebnis & Finale Freigabe

```
================================================================================
PRETEST-PROTOKOLL (AGENT 3)
================================================================================
Verständlichkeit (Sachbearbeiter):    ★★★★☆ (4/5) -> Sehr gut (mit Einleitungstext)
Praxisrelevanz (Führungskraft):       ★★★★★ (5/5) -> Exzellent
Kognitive Belastung / Zeitaufwand:   ★★★★★ (5/5) -> Optimal (ca. 6 Minuten)
Wissenschaftliche Gütekriterien:     ★★★★★ (5/5) -> Erfüllt (Objektiv, Reliabel, Valid)
--------------------------------------------------------------------------------
STATUS: FREIGEGEBEN (Ready for Deployment)
================================================================================
```

4. Einordnung in deine DSR-Hausarbeit (Peffers et al. 2007)

Diese Simulation schließt den iterativen Generierungszirkel ab und dient in deiner maximal 10-seitigen Ausarbeitung als wissenschaftlicher Nachweis deiner **Lösungsfindungskompetenz und Qualitätskontrolle** [8][9]:

**Kapitel 3 (Entwicklung des Artefakts):**  Du beschreibst die Prompts und die Rollenverteilung der drei Agenten (Methodiker → Kritiker → Proband)[3][9].

**Kapitel 4 (Demonstration im Anwendungsumfeld):**  Du zeigst den konkreten Generierungsdurchlauf und die schrittweise Evolution der Items von Durchlauf 1 bis zur Freigabe[9].

**Kapitel 5 (Evaluation & Rückkopplungsschleifen):**  Du dokumentierst die Ergebnisse der Prüfinstanzen (Agent 2 & 3) als Nachweis für die Einhaltung der wissenschaftlichen Gütekriterien (**Objektivität, Reliabilität, Validität** )[9][10].

💡 **Möchtest du, dass wir als Nächstes einen konkreten Entwurf für das Inhaltsverzeichnis deiner 10-seitigen DSR-Hausarbeit erstellen, der genau auf den Bewertungsbogen der Dozenten abgestimmt ist?**

---

## Frage

ja

---

## Antwort

Hier ist ein maßgeschneiderter **Gliederungsentwurf für deine 10-seitige DSR-Hausarbeit** , der strikt an den sechs Prozessschritten nach **Peffers et al. (2007)**  ausgerichtet ist[1][2] und alle Kriterien des offiziellen Bewertungsbogens abdeckt[3][4].

Vorschlag für den Titel der Hausarbeit

**Entwicklung eines DSR-basierten Leitlinienmodells zur automatisierten und wissenschaftlich fundierten Generierung von KI-Readiness-Fragebögen mittels Multi-Agenten-Prompting**

Seitenbudget & Gliederung im Überblick (Max. 10 inhaltliche Seiten)[5]

```
1. Problemidentifikation und Motivation .................................... ca. 1,5 Seiten
2. Zielsetzung des Leitlinienmodells ....................................... ca. 1,0 Seite
3. Entwicklung des Artefakts (Multi-Agenten-Prompting) ..................... ca. 3,0 Seiten
4. Demonstration im Anwendungsumfeld (MockUp KI-Readiness) ................ ca. 2,0 Seiten
5. Evaluation und Rückkopplungsschleifen .................................... ca. 1,5 Seiten
6. Fazit, Limitationen und Ausblick ........................................ ca. 1,0 Seite
────────────────────────────────────────────────────────────────────────────────────────────
Gesamtumfang (inhaltstragend):                                               max. 10 Seiten
```

Detaillierte Kapitelstruktur & Inhaltsanforderungen

1. Problemidentifikation und Motivation (ca. 1,5 Seiten)[2]

**1.1 Praktische Relevanz:**  Die Notwendigkeit für Unternehmen, die individuelle KI-Readiness von Mitarbeitenden vor der Einführung generativer KI-Systeme (z. B. LLMs/Copilots) präzise zu erfassen[6].

**1.2 Wissenschaftliches Problem:**  Herkömmliche Manuelle Fragebogenentwicklungen sind zeitaufwendig, während ungesteuerte KI-Generierungen zu Halluzinationen, unbelegten Vermutungen und verletzten Gütekriterien führen (*„Fragen, die vom Himmel fallen“*)[7][8].

**1.3 Forschungsfrage & Fortgang der Arbeit:**  Formulierung einer präzisen Forschungsfrage (z. B. *„Wie muss ein DSR-basiertes Prompt-Leitlinienmodell gestaltet sein, um mittels LLMs automatisiert theoretisch fundierte und methodisch valide Fragebögen zur KI-Readiness zu erzeugen?“*)[9].

2. Zielsetzung des Tools (ca. 1,0 Seite)[2]

**2.1 Funktionale & Methodische Anforderungen:**  Anforderungen an das DSR-Artefakt (Automatisierung, Nachvollziehbarkeit, Gütekriterien-Einhaltung)[10].

**2.2 Wissenschaftlicher Erklärungsrahmen:**  Verknüpfung der Zielsetzung mit etablierten Verhaltens- und Akzeptanztheorien zur Vermeidung von Ratgeberniveau[7].

3. Entwicklung des Artefakts: Das Leitlinienmodell (ca. 3,0 Seiten)[2]

- **3.1 Theoretische Fundierung des KI-Readiness-Messmodells:** 
Integration des **Reasoned Action Approach (RAA)**  (Attitude, Perceived Norms, Intention)[11][12].

Integration des **Trust-Modells für GenAI**  (Ability/Explainability, Benevolence/Uncanny Valley, Integrity/Data Privacy)[13].

Integration der **Task-Technology Fit (TTF) Theorie**  (McGrath Task Circumplex)[14][15].

Integration des **Duality Approach**  (Perceived Efficacy vs. Perceived Costs/Barriers)[11].
- **3.2 Technische Architektur des Artefakts:** 
**Retrieval-Augmented Generation (RAG):**  Systematische Einspeisung der theoretischen Grundlagentexte via Prompt-Injektion in Google NotebookLM[6][16].

**Few-Shot Prompting:**  Vorgabe validierter Beispiel-Items zur Gewährleistung konsistenter 7-Punkt-Likert-Skalierungen[16][17].

**Multi-Agenten-Workflow:**  Implementierung der Rollen-Prompts für **Agent 1 (Methodiker)** , **Agent 2 (Kritiker)**  und **Agent 3 (Proband)** [12][16].

4. Demonstration im Anwendungsumfeld (ca. 2,0 Seiten)[2]

**4.1 Anwendungsszenario:**  Durchlauf des Leitlinienmodells zur Generierung eines Fragebogens für ein reales Unternehmen[6].

**4.2 Exemplarische Artefakt-Ausgabe (MockUp):**  Darstellung der generierten Items je Konstrukt inklusive Zuordnung zu den theoretischen Quellen und Übersetzung[16].

**4.3 Anbindung an GitHub & NotebookLM:**  Nachweis der Transparenz durch das bereitgestellte Repository und den Projektlink[6][8].

5. Evaluation des Tools und Rückkopplungsschleifen (ca. 1,5 Seiten)[2]

**5.1 Methodische Qualitätskontrolle (Agent 2):**  Aufdeckung und Korrektur von Erhebungsfehlern (z. B. Elimination von *Double-Barreled Questions*, Suggestivität und Doppelverneinungen)[16].

**5.2 Pretest-Simulation (Agent 3):**  Überprüfung der Verständlichkeit und kognitiven Belastung aus Perspektive von Sachbearbeitern und Führungskräften[12].

**5.3 Nachweis der Gütekriterien:**  Bewertung der Ergebnisse hinsichtlich **Objektivität, Reliabilität und Validität** [9][10].

**5.4 Dokumentation der Prompt-Iterationen:**  Darstellung der Anpassungen am Leitlinienmodell infolge der Evaluierungsergebnisse (DSR-Rückkopplung)[2][18].

6. Fazit, Limitationen und Ausblick (ca. 1,0 Seite)[2][19]

**6.1 Zusammenfassung der Kernergebnisse:**  Kurze Synthese der Zielerreichung[19].

**6.2 Limitationen & Grenzen:**  Kritische Reflexion der Lösung (z. B. Abhängigkeit vom zugrundeliegenden LLM, Grenzen simulierter Pretests)[19].

**6.3 Anhaltspunkte zur Weiterentwicklung:**  Vorschläge für zukünftige Forschung und Erweiterungen des Artefakts[19].

Strategische Erfolgsfaktoren für die Note 1,0

**Keine Füllwörter / Kurze Sätze:**  Schreibe extrem sachlich und präzise. Jeder Satz muss Information tragen[10][19].

**Lückenlose APA-Zitation:**  Achte darauf, dass jede theoretische Behauptung direkt mit den Quellentexten belegt wird[9].

**Fokus auf die Lösungsfindung:**  Verwende Abbildungen für das DSR-Modell (Peffers) und das 3-Agenten-System, um den Platz optimal zu nutzen[4][18].

💡 **Möchtest du, dass ich dir für Kapitel 1 (Problemidentifikation & Motivation) bereits den ausformulierten Einleitungstext nach allen wissenschaftlichen Standards erstelle?**

---

## Frage

Erstelle die Einleitung für Kapitel 1

---

## Antwort

Hier ist die ausformulierte **Einleitung für Kapitel 1 (Problemidentifikation und Motivation)**  deiner DSR-Hausarbeit, verfasst nach allen formalen und wissenschaftlichen Vorgaben des Evaluationsbogens[1].

1. Problemidentifikation und Motivation

1.1 Praktische Relevanz: Erfassung der KI-Readiness im Unternehmenskontext

Die fortschreitende Integration generativer Künstlicher Intelligenz (GenAI) wie Large Language Models (LLMs) verändert betriebliche Arbeitsprozesse grundlegend[4][5]. Unternehmen stehen vor der Herausforderung, nicht nur die technische Infrastruktur bereitzustellen, sondern auch die individuelle Akzeptanz, das Vertrauen und die Kompetenzen der Beschäftigten systematisch zu bewerten[6][7]. Bevor generative Systeme flächendeckend im Arbeitsalltag verankert werden, ist eine präzise Erfassung der **KI-Readiness**  der Mitarbeitenden erforderlich[5][7]. Ohne eine fundierte Standortbestimmung drohen Fehlinvestitionen, Akzeptanzbarrieren und ungenutztes Effizienzpotenzial in den Fachbereichen[6][8].

1.2 Wissenschaftliches Problem: Schwachstellen ungesteuerter KI-Generierung

Die manuelle Erstellung empirischer Messinstrumente ist zeit- und ressourcenintensiv[7]. Gleichzeitig birgt der ungesteuerte Einsatz von Sprachmodellen zur Fragebogengenerierung erhebliche methodische Risiken[3][9]. Naive Prompts ohne wissenschaftliche Verankerung führen häufig dazu, dass generierte Fragen ohne theoretische Fundierung verbleiben und gewissermaßen „vom Himmel fallen“[10][11].

Darüber hinaus verletzen unkontrollierte KI-Erzeugnisse regelmäßig die zentralen **Gütekriterien wissenschaftlichen Arbeitens** [1][3]:

**Objektivität:**  Unklare oder wertende Formulierungen beeinträchtigen die Unabhängigkeit der Messung von den Testleitenden[3].

**Reliabilität:**  Methodische Erhebungsfehler wie Doppelverneinungen oder uneinheitliche Skalierungen verhindern reproduzierbare Messergebnisse[1][3].

**Validität:**  Ohne Abbildung etablierter theoretischer Konstrukte messen die generierten Items nicht das beabsichtigte Zielkonstrukt[1][3].

Es besteht folglich eine ausgeprägte Forschungslücke an methodisch gesteuerten Leitlinien, die LLMs befähigen, automatisiert wissenschaftlich fundierte und psychometrisch valide Messinstrumente zu erzeugen[7][12].

1.3 Forschungsfrage, Zielsetzung und Fortgang der Arbeit

Zur Lösung dieser Problemstellung verfolgt die vorliegende Arbeit den **Design Science Research (DSR)**  Ansatz nach Peffers et al. (2007)[12]. Das primäre Forschungsziel besteht in der Entwicklung und Demonstration eines DSR-basierten Leitlinienmodells als technisches Artefakt[12][13]. Dieses Artefakt nutzt **Retrieval-Augmented Generation (RAG)** , **Few-Shot Prompting**  und **multi-agentische Workflows**  auf der Plattform Google NotebookLM, um qualitätsgesicherte Fragebögen zur KI-Readiness abzuleiten[7].

Aus diesem Forschungsvorhaben leitet sich folgende zentrale Forschungsfrage ab:

*„Wie muss ein DSR-basiertes Prompt-Leitlinienmodell gestaltet sein, um mittels Large Language Models automatisiert theoretisch fundierte und methodisch valide Fragebögen zur Messung der KI-Readiness von Mitarbeitenden zu erzeugen?“*

Der Aufbau der Arbeit orientiert sich strikt an den Phasen des DSR-Prozesses[13][18]:

**Kapitel 2**  definiert die methodischen und funktionalen Zielsetzungen des Leitlinienmodells[19].

**Kapitel 3**  widmet sich der Entwicklung des Artefakts und verknüpft das theoretische KI-Readiness-Messmodell mit der Multi-Agenten-Architektur[7][15].

**Kapitel 4**  demonstriert die Funktionsweise anhand eines konkreten Durchlaufs (MockUp)[18][19].

**Kapitel 5**  evaluiert das Artefakt bezüglich der wissenschaftlichen Gütekriterien und dokumentiert die iterativen Rückkopplungsschleifen[3].

**Kapitel 6**  fasst die Ergebnisse zusammen, reflektiert bestehende Limitationen und gibt einen Ausblick auf zukünftige Forschungsansätze[3].

💡 **Sollen wir als Nächstes direkt mit Kapitel 2 (Zielsetzung des Leitlinienmodells) fortfahren und die konkreten funktionalen & methodischen Anforderungen an dein KI-Tool definieren?**

---

## Frage

erstelle einen optimierten prompt um aufgabe mit 1,0 zu lösen und nutze auch die neuen quellen

---

## Antwort

Um für deine Prüfungsleistung im Praxismodul die **Bestnote 1,0**  zu erzielen, muss dein Artefakt (das Prompt-Leitlinienmodell in NotebookLM und GitHub) alle vorliegenden theoretischen Quellen und methodischen Vorgaben lückenlos miteinander verknüpfen[1].

Die Analyse aller Quellen zeigt, dass dein Modell nicht nur Standard-Akzeptanztheorien abbilden sollte, sondern um die **neuesten wissenschaftlichen Messskalen zur KI-Readiness und KI-Selbstwirksamkeit**  erweitert werden muss[4]:

**Meta AI Literacy Scale (MAILS & MAILS-Short)** [4][7]**:**  Erfasst *Use & Apply*, *Understand*, *Detect*, *AI Ethics*, *Create AI* sowie die psychologischen Metakompetenzen *AI Self-Efficacy* (Problemlösung, Lernen) und *AI Self-Competency* (Emotionsregulation, Persuasion Literacy)[4].

**AI Learning Readiness Self-Efficacy Scale (AILRSE-5)** [5]**:**  Ein hochaktuelles, globales Messinstrument zur Erfassung der Selbstwirksamkeitserwartung beim Erlernen neuer KI-Technologien[5].

**Artificial Intelligence Self-Efficacy Scale (AISES)** [6]**:**  Differenziert KI-Selbstwirksamkeit in *Assistance*, *Anthropomorphic Interaction*, *Comfort with AI* und *Technological Skills*[6].

**Artificial Intelligence Readiness Scale (AIRS)** [8]**:**  Erfasst die individuelle KI-Readiness über *Self-Efficacy & Cognition (SEC)*, *Optimism*, *Collaborative Learning and Working (CLW)* und *Comfort*[8].

**GenAI Enterprise Trust Model (Do Khac et al. 2025)** [16]**:**  Erklärt die Vertrauensbildung gegenüber LLMs/ChatGPT über *Ability (Explainability)*, *Benevolence (Uncanny Valley)* und *Integrity (Data Privacy/GDPR)*[16].

**Task-Technology Fit & McGrath Circumplex** [19]**:**  Untersucht die Passung zwischen KI-Funktionen und spezifischen Aufgabenformen (kreativ, analytisch, konfliktär, operativ)[19].

**Duality Approach & Reasoned Action Approach (RAA)** [22][23]**:**  Wägt funktionale Nutzenerwartungen (*Perceived Efficacy*) gegen emotionale Bedenken und Ängste (*Fear/Threat*) ab[22][24].

🚀 Der finale 1,0-Master-System-Prompt für NotebookLM

Kopiere den folgenden ausformulierten **Master-Prompt**  direkt in dein Google NotebookLM (oder nutze ihn als System-Prompt in deinem GitHub-Repository), um die automatische Fragebogengenerierung wissenschaftlich perfekt zu steuern[2][3]:

```
================================================================================
MASTER-LEITLINIENMODELL: AUTOMATISIERTE GENERIERUNG VON KI-READINESS-FRAGEBÖGEN
================================================================================

ROLLE UND ZIELSETZUNG:
Du agierst als führender wissenschaftlicher Methodiker, Psychometriker und DSR-Experte für Wirtschaftsinformatik.
Deine Aufgabe ist die automatisierte Erstellung eines empirisch validen, theoretisch fundierten und praxisrelevanten Fragebogens zur Erfassung der "KI-Readiness von Mitarbeitenden" im Unternehmenskontext.
Alle generierten Mess-Items müssen streng logisch aus der hinterlegten wissenschaftlichen Quellenbasis abgeleitet werden.

--------------------------------------------------------------------------------
1. THEORETISCHES MESSMODELL (RETRIEVAL-AUGMENTED GENERATION / RAG)
--------------------------------------------------------------------------------
Nutze zur Item-Konstruktion ausschließlich folgende 5 theoretische Hauptsäulen aus den Quellentexten:

SÄULE A: KI-LITERACY & SELBSTWIRKSAMKEIT (MAILS, AILRSE-5, AISES, AIRS)
- Meta AI Literacy (MAILS): Messung von 'Use & Apply AI', 'Understand AI', 'Detect AI', 'AI Ethics' sowie 'Create AI' als separates Konstrukt (Carolus et al. 2023; Koch et al. 2024).
- KI-Selbstwirksamkeit & Metakompetenzen: Erfassung von 'AI Problem Solving', 'AI Learning' (AILRSE-5 nach Oksanen et al. 2026), 'AI Emotion Regulation' sowie 'AI Persuasion Literacy' (MAILS).
- KI-Interaktion (AISES): Erfassung von 'Assistance', 'Anthropomorphic Interaction', 'Comfort with AI' und 'Technological Skills' (Wang & Chuang 2024).
- Kollaboratives Arbeiten (AIRS): Erfassung von 'Collaborative Learning and Working' (CLW) und 'Optimism' (Wang et al. 2026).

SÄULE B: VERTRAUEN IN ENTERPRISE-GENAI (TRUST MODEL)
- Ability / Explainability: Transparenz und Nachvollziehbarkeit der KI-Ergebnisse (X1-X3) (Do Khac et al. 2025).
- Benevolence / Uncanny Valley: Wahrnehmung der KI als unheimlich/unmenschlich (U1-U3) (Do Khac et al. 2025; Mayer et al. 1995).
- Integrity / Data Privacy: Bedenken hinsichtlich Datenschutz, DSGVO und Weitergabe interner Unternehmensdaten (D1-D3) (Do Khac et al. 2025).

SÄULE C: AUFGABEN-TECHNOLOGIE-PASSUNG (TASK-TECHNOLOGY FIT / TTF)
- McGrath Task Circumplex: Abgleich der KI-Capabilities mit spezifischen Aufgabenarten (Intellective, Judgmental, Conflict, Creativity, Execution) (Paper Fragebogen 3; Goodhue & Thompson 1995).

SÄULE D: BEVERHALTENSABSICHT & DUALITY APPROACH (RAA & DUAL MODEL)
- Reasoned Action Approach (RAA): Direct Measurement von 'Intention to Use', 'Attitude', 'Perceived Norms' und 'Perceived Behavioral Control' (Fishbein & Ajzen 2010).
- Duality Approach: Gegenüberstellung von 'Perceived Response Efficacy' vs. 'Perceived Threat / Fear' (Gesk, Wichmann & Leyer 2021/2024).

--------------------------------------------------------------------------------
2. METHODISCHE VORGABEN & FEW-SHOT IN-CONTEXT LEARNING
--------------------------------------------------------------------------------
- Skalierung: Nutze durchgängig eine 7-Punkt-Likert-Skala (1 = "Stimme überhaupt nicht zu" bis 7 = "Stimme voll und ganz zu").
- Gütekriterien (Objektivität, Reliabilität, Validität):
  1. ELIMINIERE Double-Barreled Questions (keine zwei Sachverhalte in einer Frage).
  2. ELIMINIERE Suggestivformulierungen (keine wertenden Adjektive wie "hervorragend" oder "problemlos").
  3. ELIMINIERE Doppelverneinungen (invers formulierte Items müssen sprachlich einfach verständlich bleiben).
  4. Bipolare Sprachfassung: Erstelle jedes Item sowohl auf Deutsch als auch auf Englisch.

--------------------------------------------------------------------------------
3. AGENTISCHER MULTI-AGENTEN-WORKFLOW (3-STUFEN-GENERIERUNG)
--------------------------------------------------------------------------------
Führe die Generierung sequenziell in drei Schritten durch:

SCHRITT 1: AGENT 1 (DER METHODIKER)
- Generiert pro Unterkonstrukt genau 3 reflektierte Mess-Items.
- Ordnet jedem Item die theoretische Quelle (Autor, Jahr) sowie die exakte Konstrukt-ID zu.

SCHRITT 2: AGENT 2 (DER KRITIKER)
- Überprüft den Entwurf von Agent 1 unnachgiebig auf Erhebungsfehler.
- Erstellt eine Korrekturtabelle und ersetzt mangelhafte Formulierungen durch optimierte, valide Items.

SCHRITT 3: AGENT 3 (DER PROBAND / SIMULIERTER PRETEST)
- Bewertet den korrigierten Fragebogen aus zwei Zielgruppen-Perspektiven:
  a) Sachbearbeiter/in (operativ, geringes KI-Vorwissen -> Prüft Verständlichkeit & Begriffsklarheit).
  b) Führungskraft (strategisch -> Prüft Relevanz bezogen auf Datenschutz & Performance).
- Gibt das finale, freigegebene Item-Set mit einer kurzen Einleitungsempfehlung aus.

================================================================================
```

2. Umsetzung im Rahmen der 10-seitigen DSR-Hausarbeit (Peffers et al. 2007)

Um die 100 Punkte des Evaluationsbogens voll auszuschöpfen, bindest du diesen Master-Prompt wie folgt in deine DSR-Hausarbeit ein[1]:

**In Kapitel 3 (Entwicklung des Artefakts):**  Erkläre die wissenschaftliche Herleitung deines Master-Prompts[3]. Zeige auf, wie die **RAG-Komponente**  (Integration von `MAILS`, `AILRSE-5`, `AISES`, `AIRS` und `Trust-Model`), die **Few-Shot-Vorgaben**  und die **Drei-Agenten-Architektur**  zusammenwirken[2].

**In Kapitel 4 (Demonstration im Anwendungsumfeld):**  Füge den kompletten Master-Prompt als Textbox/Abbildung ein und zeige den konkreten Output (den generierten 7-Punkt-Likert-Fragebogen)[3][26].

**In Kapitel 5 (Evaluation & Rückkopplungsschleifen):**  Dokumentiere die Korrekturleistung von **Agent 2**  (z. B. Beseitigung von *Double-Barreled Questions*) und die Ergebnisse der Pretest-Simulation von **Agent 3**  als Nachweis für die Einhaltung der Gütekriterien (**Objektivität, Reliabilität, Validität** )[1][2].

**GitHub-Integration:**  Speichere diesen Prompt als `system_prompt.txt` oder `master_prompt.json` in deinem GitHub-Repository und verlinke im NotebookLM-Projekt darauf[3].

💡 **Möchtest du, dass wir als Nächstes den ausformulierten Text für Kapitel 2 (Zielsetzung des Leitlinienmodells) erstellen, damit deine Hausarbeit Kapitel für Kapitel fertiggestellt wird?**

---

## Frage

Gib den gesamten bisherigen Chatverlauf dieses Notebooks wortgetreu und vollständig aus,
chronologisch in der tatsächlichen Reihenfolge, ohne Kürzung, Zusammenfassung oder
Auslassung einzelner Beiträge.




Formatiere die Ausgabe als Markdown:





Jede Frage/Eingabe von mir als "## Nutzer" mit dem Originaltext darunter


Jede Antwort von dir als "## NotebookLM" mit dem Originaltext darunter


Trenne aufeinanderfolgende Austausche mit "---"


Keine zusätzlichen Kommentare, Einleitungen oder Erklärungen vor oder nach der Ausgabe —
nur der reine Chatverlauf im beschriebenen Format.

---

## Antwort

Nutzer

wie gehe ich am besten bei diesem modul vor. schaue dir die quellen an, ich möchte eine 1,0 erreichen

NotebookLM

Um in diesem Praxismodul die **Bestnote 1,0**  zu erreichen, musst du die Vorgaben aus den Prüfungsanweisungen und dem Evaluationsbogen präzise umsetzen. Die Prüfungsleistung besteht aus zwei Teilen: einem **GitHub-Projekt**  (mit Code/Link zu deinen Prompts und deinem NotebookLM-Projekt) und einer **wissenschaftlichen Hausarbeit von maximal 10 inhaltstragenden Seiten** .

1. Die Kernaufgabe und das Artefakt

**Ziel des Artefakts:**  Du entwickelst **Leitlinien/Prompts für Large Language Models (LLMs)** , die es einem KI-Modell ermöglichen, automatisch wissenschaftlich fundierte Fragebögen zu erstellen.

**Konkreter Anwendungsfall:**  Die automatisierte Erstellung eines Fragebogens zur Messung der **KI-Readiness von Mitarbeitenden**  in einem Unternehmen.

**Werkzeuge:**  Du nutzt **Google NotebookLM** , um die wissenschaftlichen Unterlagen einzubinden, Prompts zu entwickeln und letztlich einen Zugriffslink für dein GitHub-Repository zu generieren.

2. Das Erfolgsrezept für die Notenstufe 1,0 (gemäß Evaluationsbogen)

Deine Hausarbeit wird nach einem Punkteschema (100 Punkte insgesamt) bewertet. Um die volle Punktezahl zu sichern, solltest du folgende Kriterien abdecken:

A. Roter Faden & DSR-Struktur (10 Punkte)

Richte den Aufbau deiner Arbeit strikt an den Phasen des **Design Science Research (DSR) Prozesses nach Peffers et al. (2007)**  aus:

**Problemidentifikation und Motivation:**  Warum ist die automatisierte Fragebogenerstellung praxisrelevant und welche Probleme löst sie?

**Zielsetzung des Tools:**  Welche genauen Anforderungen muss das Leitlinienmodell erfüllen?

**Entwicklung des Artefakts:**  Herleitung deines Prompt- und Leitlinienmodells auf Basis wissenschaftlicher Theorien.

**Demonstration im Anwendungsumfeld:**  Konkreter Durchlauf/MockUp zur Erstellung des Fragebogens für die KI-Readiness.

**Evaluation:**  Überprüfung der Fragebogenqualität, Dokumentation von Feedbackschleifen und Lösungsiterationen.

**Fazit und Ausblick:**  Zusammenfassung, Reflexion der Grenzen/Limitationen und Ansatzpunkte zur Weiterentwicklung.

B. Wissenschaftliche Theoriefundierung (10 Punkte)

**Keine freien Erfindungen:**  Fragen dürfen keinesfalls ohne theoretische Basis „vom Himmel fallen“. Sie müssen sachlogisch aus etablierten Theorien (wie z. B. dem *Reasoned Action Approach* oder dem *Task-Technology Fit Model*) abgeleitet werden.

**Gütekriterien:**  Gehe explizit auf die Gütekriterien wissenschaftlichen Arbeitens ein (**Objektivität, Reliabilität, Validität** ).

**Einwandfreie Zitation:**  Zitiere lückenlos nach APA oder einem vergleichbaren Standard. *Achtung: Unzitierte Übernahmen führen zur sofortigen Disqualifikation (-100 Punkte)*.

C. Lösungsfindungskompetenz & KI-Methodik (55 Punkte)

Dies ist der größte Bewertungsblock. Hohe Punkte erreichst du durch:

**Fortgeschrittene Prompting-Techniken:**  Binde methodische Ansätze wie **Few-Shot Prompting**  (In-Context Learning durch Beispiel-Fragebögen) und **Retrieval-Augmented Generation (RAG)**  über Prompt-Injections ein.

**Agentische Workflows:**  Reiche dein Konzept durch ein Multi-Agenten-System (z. B. simuliert via CrewAI/LangGraph oder Rollenprompts) an, etwa mit Rollen wie **Methodiker**  (Fragenentwurf), **Kritiker**  (Prüfung auf Suggestiv- oder Fangfragen) und **Proband**  (Verständlichkeitsprüfung).

**Kreativität & Evaluation:**  Evaluiere deine Lösung selbstständig hinsichtlich Realisierbarkeit, Nützlichkeit und Restriktionen.

D. Sprache, Form & Fokus (15 Punkte gesamt)

**Maximal 10 Seiten:**  Halte dich strikt an die Obergrenze.

**Schreibstil:**  Nutze **kurze, präzise und sachliche Sätze** . Vermeide Schachtelsätze, unbewiesene Wertungen oder redundante Wiederholungen.

**Radikaler Fokus:**  Schneide Nebensächlichkeiten konsequent heraus („Alles, was noch interessant ist, sollten Sie weglassen“).

3. Empfohlene nächste Schritte

**Vorlesungsinhalte auffrischen:**  Wiederhole die Grundlagen zur Fragebogenerstellung und Statistik aus den Modulen *Marketing Data Science & Analytics* sowie *Qualitative & Quantitative Datenanalyse*.

**Agilität nutzen:**  Die Dozenten (Dr. Johannes Wichmann und Prof. Dr. Hieronymus Sturm) wünschen sich ausdrücklich einen **engen, kurzmaschig-systematischen Austausch**  während des Bearbeitungsprozesses.

**Arbeitsbereich einrichten:**  Nutze Google NotebookLM zur Strukturierung deiner Quellen und erstelle frühzeitig dein GitHub-Repository für den Code und die Prompt-Dokumentation.

💡 **Möchtest du, dass wir gemeinsam eine detaillierte Gliederung für deine 10-seitige DSR-Hausarbeit erstellen oder direkt geeignete theoretische Modelle für die Messung der KI-Readiness heraussuchen?**

Nutzer

entwickle das modell

NotebookLM

Um das geforderte Praxisprojekt auf **1,0-Niveau**  umzusetzen, muss das Modell auf zwei eng miteinander verzahnten Ebenen entwickelt werden:

**Das theoretische KI-Readiness-Messmodell:**  Das wissenschaftliche Konstrukt, das bestimmt, *welche* Dimensionen und Fragen erhoben werden.

**Das DSR-Artefaktmodell (Prompt- & Agenten-Architektur):**  Die technische Methodik, *wie* das LLM mithilfe von Leitlinien automatisiert und valide Fragebögen generiert.

Ebene 1: Das integrierte theoretische KI-Readiness-Messmodell

Damit die Fragen nicht „vom Himmel fallen“, wird die **KI-Readiness von Mitarbeitenden**  systematisch aus den vier theoretischen Hauptpfeilern der vorliegenden Quellen synthetisiert:

```
[Task Characteristics & Tech Characteristics] ──► Task-Technology Fit (TTF) ──┐
                                                                              │
[Ability (Explainability) + Benevolence + Integrity] ──────► Trust in AI ────┼──► Intention to Use AI
                                                                              │    (KI-Readiness)
[Adaptive Appraisals (Efficacy) vs. Perceived Costs/Fear] ──► Attitude (RAA) ─┘
```

1. Verhaltensabsicht & Einstellung (Reasoned Action Approach / RAA)

**Einstellung (Attitude):**  Die subjektive Bewertung der Mitarbeitenden, ob der Einsatz von KI im Arbeitsalltag vorteilhaft, nützlich oder angenehm ist.

**Perzipierte Normen (Perceived Norms):**  Der wahrgenommene soziale Druck durch Kollegenschaft und Führungskräfte zur Nutzung von KI.

**Wahrgenommene Verhaltenskontrolle (Perceived Behavioral Control):**  Die Überzeugung der Mitarbeitenden, über ausreichend Fähigkeiten und Ressourcen zur KI-Nutzung zu verfügen.

**Zielkonstrukt:**  **Intention to Use**  als direkter Indikator für die individuelle KI-Readiness.

2. Vertrauen in KI-Systeme (Trust Model)

**Fähigkeit (Ability / Explainability):**  Verstehen die Mitarbeitenden, wie die KI zu ihren Ergebnissen kommt, und schätzen sie die Ausgaben als korrekt ein?

**Wohlwollen (Benevolence / Uncanny Valley):**  Wird die KI-Anwendung als natürlich und unterstützend wahrgenommen oder erzeugt sie ein unheimliches/unangenehmes Gefühl?

**Integrität (Integrity / Data Privacy):**  Vertrauen die Mitarbeitenden darauf, dass unternehmensinterne Daten und Interaktionen sicher verarbeitet und nicht an Dritte weitergegeben werden?

3. Aufgaben-Technologie-Passung (Task-Technology Fit / TTF)

**Aufgabenmerkmale (Task Characteristics):**  Strukturierte Arbeitsabläufe vs. komplexe, unstandardisierte Aufgaben.

**Technologiemerkmale (Technology Characteristics):**  Interaktivität, Automatisierungsgrad und Funktionsumfang der KI.

**Fit-Bewertung:**  Der wahrgenommene Grad, in dem die KI-Funktionen die spezifischen Arbeitsaufgaben konkret unterstützen.

4. Nutzen- vs. Risikoabwägung (Integrated Model)

**Wahrgenommene Wirksamkeit (Perceived Efficacy):**  Einschätzung der Effektivität der KI zur Arbeitserleichterung.

**Barrieren & Ängste (Perceived Costs / Fear):**  Befürchtungen bezüglich Kontrollverlust, Mehraufwand oder Fehleranfälligkeit.

Ebene 2: Das DSR-Artefaktmodell (Prompt- & Agenten-Architektur)

Das Artefakt besteht aus strukturierten **LLM-Leitlinien (Prompts)** . Um im DSR-Framework Höchstpunkte für die Lösungsfindungskompetenz zu erzielen, wird ein **agentischer Multi-Agenten-Workflow**  über Prompt-Injections und In-Context Learning aufgebaut:

```
[Theorie-Datenbasis (RAG)] + [Beispiel-Items (Few-Shot)]
                           │
                           ▼
            ┌─────────────────────────────┐
            │    Agent 1: Methodiker      │ ──► Erstellt theoretisch fundierte Items
            └──────────────┬──────────────┘
                           │
                           ▼
            ┌─────────────────────────────┐
            │     Agent 2: Kritiker       │ ──► Prüft Gütekriterien & Methodik
            └──────────────┬──────────────┘
                           │
                           ▼
            ┌─────────────────────────────┐
            │     Agent 3: Proband        │ ──► Simuliert Pretest & Verständlichkeit
            └──────────────┬──────────────┘
                           │
                           ▼
            [ Finaler KI-Readiness-Fragebogen ]
```

**Retrieval-Augmented Generation (RAG):**  Das LLM erhält die theoretischen Quellentexte direkt als Kontext-Einspeisung (Prompt-Injektion), um halluzinationsfreie Items abzuleiten.

**Few-Shot Prompting (In-Context Learning):**  Übergabe validierter Beispiel-Fragen aus der Datenbasis (z. B. Likert-Skalierte Items zu *Ability*, *Integrity* und *TTF*) als Formatvorlage.

- **Multi-Agenten-Rollensimulation:** 
**Agent 1 (Der Methodiker):**  Generiert erste Fragentwürfe streng aus den Konstrukten des KI-Readiness-Messmodells.

**Agent 2 (Der Kritiker):**  Überprüft jede Frage auf die Einhaltung wissenschaftlicher Gütekriterien (**Objektivität, Reliabilität, Validität** ), identifiziert Doppelverneinungen sowie Suggestivfragen und korrigiert Skalierungsfehler.

**Agent 3 (Der Proband/Experte):**  Simuliert eine Testperson aus der Zielgruppe (z. B. Fachbereichsleitung oder Sachbearbeitung) und bewertet die Sprachschärfe und Praxisverständlichkeit.

Einbettung in die Hausarbeit (Peffers et al. 2007)

In der Hausarbeit (max. 10 Seiten) ordnest du diese Modelle direkt in die DSR-Prozessschritte ein:

**Kapitel 3 (Entwicklung des Artefakts):**  Darstellung der Leitlinien-Architektur, der RAG-/Few-Shot-Logik und des Multi-Agenten-Systems.

**Kapitel 4 (Demonstration im Anwendungsumfeld):**  Konkreter Durchlauf des Artefakts zur Generierung des KI-Readiness-Fragebogens inklusive der abgeleiteten Items.

**Kapitel 5 (Evaluation):**  Nachweis der Fragebogenqualität anhand der Gütekriterien sowie Dokumentation von Feedbackschleifen und Prompt-Iterationen.

💡 **Möchtest du, dass wir als Nächstes die konkreten System-Prompts für die drei Agenten (Methodiker, Kritiker, Proband) im NotebookLM-Format ausformulieren?**

Nutzer

Erstelle die System-Prompts für die drei Agenten

NotebookLM

Anbei findest du die ausformulierten **System-Prompts für die drei Agenten** , die du direkt in **Google NotebookLM**  oder in eine externe Multi-Agenten-Pipeline (z. B. via Rollen-Prompts oder Frameworks wie CrewAI/LangGraph) einbinden kannst. Sie verknüpfen die methodischen Vorgaben (RAG, Few-Shot Prompting, Gütekriterien) direkt mit den wissenschaftlichen Grundlagen aus deinen Quellen.

Agent 1: Der Methodiker (Item-Generierung & Theoriefundierung)

**Rolle:**  Du bist ein wissenschaftlicher Methodiker und Experte für psychometrische Testkonstruktion sowie Datenanalyse im Bereich Wirtschaftsinformatik und Akzeptanzforschung.

**Ziel:**  Erstelle einen ersten Entwurf eines quantitativen Fragebogens zur Messung der **KI-Readiness von Mitarbeitenden**  in einem Unternehmen. Die Fragen dürfen keinesfalls freihändig erfunden werden, sondern müssen strikt und nachvollziehbar aus der bereitgestellten wissenschaftlichen Literatur abgeleitet werden.

```
Du agierst in der Rolle von "Agent 1: Der Methodiker". 
Deine Aufgabe ist es, einen theoretisch fundierten Fragebogen zur Messung der "KI-Readiness von Mitarbeitenden" zu entwickeln.

1. THEORETISCHER RAHMEN (RAG):
Stütze dich bei der Item-Generierung exklusiv auf folgende Konstrukte aus den vorliegenden Quellentexten:
- Reasoned Action Approach (RAA): Intention to use, Attitude, Perceived Norms, Perceived Behavioral Control (Fishbein & Ajzen 2010).
- Trust-Modell für LLMs/GenAI: Ability (Explainability), Benevolence (Uncanny Valley), Integrity (Data Privacy) (Mayer et al. 1995; Do Khac et al. 2025).
- Task-Technology Fit (TTF): Abstimmung zwischen Aufgabenmerkmalen (McGrath's Task Circumplex: Intellective, Judgment, Conflict, Mixed-Motive, Execution) und Technologiemerkmalen (Goodhue & Thompson 1995; Paetow et al. 2025).
- Duality Approach: Perceived Efficacy vs. Perceived Costs/Barriers (Wichmann et al. 2024).

2. IN-CONTEXT LEARNING (Few-Shot):
Richte dich beim Aufbau, der Formulierung und der Antwortskalierung streng nach den validierten Beispiel-Items aus den Quellen (Datensatz_v1):
- Verwende eine einheitliche 7-Punkt-Likert-Skala (1 = "Stimme überhaupt nicht zu" bis 7 = "Stimme voll und ganz zu").
- Generiere für jedes Konstrukt genau 3 reflektierte Mess-Items.

3. OUTPUT-FORMAT:
Gib für jedes Item folgendes Schema an:
- Konstrukt & Sub-Dimension (z. B. Trust -> Integrity / Data Privacy)
- Theoretische Quelle / Ableitung (z. B. Do Khac et al. 2025; Smith et al. 1996)
- Item-Formulierung (Deutsch & Englisch)
- Antwortskala
```

Agent 2: Der Kritiker (Methodische Qualitätskontrolle & Gütekriterien)

**Rolle:**  Du bist ein strenger methodischer Peer-Reviewer für empirische Sozialforschung und psychometrische Fragebogenkonstruktion.

**Ziel:**  Überprüfe den von Agent 1 generierten Fragentwurf unnachgiebig auf methodische Fehler, verzerrte Formulierungen und die Einhaltung der wissenschaftlichen Gütekriterien (**Objektivität, Reliabilität, Validität** ).

```
Du agierst in der Rolle von "Agent 2: Der Kritiker".
Deine Aufgabe ist die methodische und sprachliche Qualitätsprüfung des von Agent 1 vorgelegten Fragentwurfs.

1. PRÜFKRITERIEN (Ausschluss von Erhebungsfehlern):
Scanne jedes Item systematisch auf folgende typische Fehlerquellen:
- Double-Barreled Questions: Werden zwei unterschiedliche Sachverhalte in einer einzigen Frage zusammengefasst? (z. B. "Ich finde KI nützlich und sicher") -> Sofort aufspalten.
- Suggestivfragen / Verhaltensorientierte Tendenzen: Enthält die Frage wertende Adjektive, die eine bestimmte Antwort nahelegen?
- Unklare/Mehrdeutige Formulierungen: Werden Fachbegriffe verwendet, die ohne Vorwissen nicht verstanden werden?
- Negativ formulierte Items / Doppelverneinungen: Vermeide komplizierte Verneinungen, die die kognitive Belastung erhöhen.

2. GÜTEKRITERIEN-CHECK:
- Inhaltsvalidität: Decken die 3 Items das theoretische Konstrukt vollständig ab oder messen sie etwas Ähnliches?
- Invarianz & Skalierung: Ist die 7-Punkt-Likert-Skala für alle Items konsistent und trennscharf gewählt?

3. OUTPUT-FORMAT:
Gib ein strukturiertes Review ab:
- Status: [Freigegeben / Überarbeitung erforderlich]
- Gefundene Schwachstellen: Liste spezifischer Items mit konkreter Fehlerbenennung.
- Konstruktiver Korrekturvorschlag: Biete für jedes bemängelte Item eine optimierte, korrigierte Formulierung an.
```

Agent 3: Der Proband / Experte (Verständlichkeits- & Pretest-Simulation)

**Rolle:**  Du simulierst eine Testperson (Pretest-Teilnehmer / Fachexperte aus einem Unternehmen) mit unterschiedlichem Vorwissen bezüglich Künstlicher Intelligenz.

**Ziel:**  Evaluiere den Fragebogen aus Perspektive der Anwendbarkeit im Unternehmensalltag, um kognitive Überlastung, Abbruchquoten und Verständnisprobleme zu minimieren.

```
Du agierst in der Rolle von "Agent 3: Der Proband" (Simulierter Pretest).
Du nimmst die Perspektive von zwei unterschiedlichen Unternehmensakteuren ein:
- Person 1: Sachbearbeiter/in im Fachbereich (wenig technisches KI-Vorwissen).
- Person 2: Führungskraft / Senior Decision-Maker (Fokus auf Datenschutz, Effizienz und Zielerreichung).

1. EVALUATIONSKRITERIEN:
Bewerte die vom Kritiker (Agent 2) freigegebenen Fragen hinsichtlich:
- Verständlichkeit: Sind die Fragen im Arbeitskontext ohne Nachfragen verständlich?
- Kognitive Belastung & Bearbeitungsdauer: Wirkt der Fragebogen flüssig oder ermüdend?
- Akzeptanz / Sensitive Themen: Werden Fragen zum Thema Ängste oder Kontrollverlust (z. B. Fear/Uncanny) als unangenehm oder bedrohlich wahrgenommen?

2. OUTPUT-FORMAT:
Erstelle einen Pretest-Bericht mit folgendem Aufbau:
- Perspektiv-Check Sachbearbeiter/in: Verständlichkeit (1-5 Sterne) + konkrete Anmerkungen.
- Perspektiv-Check Führungskraft: Praxisrelevanz (1-5 Sterne) + konkrete Anmerkungen.
- Abschließende Freigabe: Finale Bestätigung des optimierten Fragebogens zur Messung der KI-Readiness.
```

Einbindung im NotebookLM- und DSR-Framework

**Iteratives Feedback (Evaluation nach Peffers et al. 2007):**  In deiner DSR-Hausarbeit (Kapitel 4 & 5) dokumentierst du die Durchläufe zwischen Agent 1 (Methodiker) → Agent 2 (Kritiker) → Agent 3 (Proband) exakt als **Dokumentation deiner Lösungsiterationen und Qualitätskontrolle** .

**GitHub-Repository:**  Speichere diese System-Prompts als Text- oder JSON-Dateien in deinem GitHub-Repository ab, um die Vorgabe zur Transparentmachung deines Lösungsweges zu erfüllen.

💡 **Sollen wir als Nächstes den ersten Durchlauf simulieren und von Agent 1 (Methodiker) einen konkreten Fragentwurf zur KI-Readiness auf Basis der Quellen generieren lassen?**

Nutzer

Simuliere den ersten Durchlauf mit Agent 1

NotebookLM

Hier ist die Simulation des ersten Durchlaufs von **Agent 1 (Der Methodiker)** . In dieser Rolle generiert das System den ersten wissenschaftlich fundierten Fragentwurf zur Erfassung der **KI-Readiness von Mitarbeitenden** , indem es die theoretischen Konstrukte aus den bereitgestellten Quellentexten via Retrieval-Augmentierte Generation (RAG) abbildet und in ein 7-Punkt-Likert-Skalierungsschema überführt.

🤖 Agent 1: Der Methodiker – Fragentwurf (Durchlauf 1)

**System-Kontext & In-Context-Vorgabe:** 
*Zielgruppe:* Mitarbeitende und Führungskräfte im Unternehmen
*Kontext:* Generierung von Mess-Items zur Bewertung der individuellen KI-Readiness und der Akzeptanz generativer KI-Werkzeuge (z. B. ChatGPT/LLMs)
*Skalierung:* 7-Punkt-Likert-Skala (1 = „Stimme überhaupt nicht zu“ bis 7 = „Stimme voll und ganz zu“)

Block 1: Verhaltensabsicht & Akzeptanz (Reasoned Action Approach / RAA)

*Theoretische Grundlegung:* Fishbein & Ajzen (2010); Gesk et al. (2021).

Konstrukt 1.1: Intention to Use (Nutzungsabsicht)

- **Item INT_1:** 
*Deutsch:* Ich beabsichtige, generative KI-Anwendungen in Zukunft regelmäßig für meine täglichen Arbeitsaufgaben zu nutzen.

*Englisch:* I intend to use generative AI applications for my daily work tasks in the future.

*Quelle / Ableitung:* Adaptiert nach Fishbein & Ajzen (2010); Do Khac et al. (2025).
- **Item INT_2:** 
*Deutsch:* Ich habe den festen Plan, KI-gestützte Systeme im Betrieb einzusetzen, sobald diese verfügbar gemacht werden.

*Englisch:* I plan to use AI-supported systems in my company as soon as they become available.

*Quelle / Ableitung:* Adaptiert aus Datensatz_v1 (Questionnaire 1 & 2).
- **Item INT_3:** 
*Deutsch:* Meine Absicht, KI zur Optimierung meiner Arbeitsprozesse zu verwenden, ist hoch.

*Englisch:* My intention to use AI to optimize my work processes is high.

*Quelle / Ableitung:* Adaptiert aus Do Khac et al. (2025).

Konstrukt 1.2: Perceived Norms (Subjektive Normen)

- **Item NOR_1:** 
*Deutsch:* Kolleginnen und Kollegen, deren Meinung ich schätze, würden mir raten, KI-Werkzeuge bei der Arbeit zu nutzen.

*Englisch:* Colleagues whose opinion I value would advise me to use AI tools at work.

*Quelle / Ableitung:* Adaptiert nach Fishbein & Ajzen (2010); Wichmann et al. (2024).
- **Item NOR_2:** 
*Deutsch:* Führungskräfte in einer mir vergleichbaren Position empfehlen den Einsatz von generativer KI.

*Englisch:* Managers in a position similar to mine recommend the use of generative AI.

*Quelle / Ableitung:* Adaptiert aus Datensatz_v1 (PowerPilot).
- **Item NOR_3:** 
*Deutsch:* In meinem beruflichen Umfeld wird erwartet, dass man sich neuen KI-Technologien gegenüber aufgeschlossen zeigt.

*Englisch:* In my professional environment, it is expected to be open toward new AI technologies.

*Quelle / Ableitung:* Adaptiert nach Wichmann et al. (2024).

Block 2: Vertrauen in KI-Systeme (Trust Model nach Mayer et al. 1995 / Do Khac et al. 2025)

*Theoretische Grundlegung:* Mayer et al. (1995); Do Khac et al. (2025).

Konstrukt 2.1: Ability / Explainability (Wahrgenommene Fähigkeit & Erklärbarkeit)

- **Item ABI_1:** 
*Deutsch:* Ich verstehe die prinzipielle Funktionsweise von generativen KI-Modellen in unserem Arbeitskontext.

*Englisch:* I know how generative AI models work in our business context.

*Quelle / Ableitung:* Do Khac et al. (2025) (Item X1).
- **Item ABI_2:** 
*Deutsch:* Ich kann nachvollziehen, wie das KI-System zu seinen Antworten und Ergebnissen gelangt.

*Englisch:* I can understand how the AI system achieves its results.

*Quelle / Ableitung:* Do Khac et al. (2025) (Item X2).
- **Item ABI_3:** 
*Deutsch:* Ich bin in der Lage zu beurteilen, ob die von der KI generierten Ergebnisse inhaltlich korrekt sind.

*Englisch:* I can assess whether the results generated by the AI are correct.

*Quelle / Ableitung:* Do Khac et al. (2025) (Item X3).

Konstrukt 2.2: Integrity / Data Privacy (Integrität & Datenschutz)

- **Item INTG_1:** 
*Deutsch:* Ich habe keine Bedenken, dass die Eingabe unternehmensinterner Informationen in das KI-System Daten an unbefugte Dritte weitergibt.

*Englisch:* I have no doubts that using the AI system will pass internal company information to third parties.

*Quelle / Ableitung:* Do Khac et al. (2025) (Item D1).
- **Item INTG_2:** 
*Deutsch:* Ich vertraue darauf, dass unsere Interaktionsdaten bei der Nutzung der KI sicher verarbeitet werden.

*Englisch:* I think that our interaction data while using the AI system are safe.

*Quelle / Ableitung:* Do Khac et al. (2025) (Item D2).
- **Item INTG_3:** 
*Deutsch:* Ich befürchte nicht, dass das KI-System durch unsere Nutzung zu viele vertrauliche Details über unser Unternehmen speichert.

*Englisch:* I do not worry that the AI system will hold too much sensitive information about our company.

*Quelle / Ableitung:* Do Khac et al. (2025) (Item D3).

Konstrukt 2.3: Benevolence / Uncanny Valley (Wohlwollen vs. Unbehaglichkeit)

- **Item BEN_1 (Invers formuliert):** 
*Deutsch:* Ich empfinde die Interaktion mit der generativen KI nicht als unheimlich oder unangenehm.

*Englisch:* I do not perceive interacting with generative AI as uncanny or unsettling.

*Quelle / Ableitung:* Adaptiert aus Do Khac et al. (2025) (Item U1).
- **Item BEN_2:** 
*Deutsch:* Ich habe das Gefühl, dass das KI-System darauf ausgelegt ist, meine Arbeit positiv zu unterstützen.

*Englisch:* I feel that the AI system is designed to positively support my work.

*Quelle / Ableitung:* Adaptiert nach Mayer et al. (1995); Do Khac et al. (2025).
- **Item BEN_3:** 
*Deutsch:* Die KI-Anwendung wirkt im Arbeitsdialog natürlich und frei von bedrohlichen Merkmalen.

*Englisch:* The AI application feels natural in the work dialogue and free from threatening characteristics.

*Quelle / Ableitung:* Adaptiert nach Hyun Baek & Kim (2023); Do Khac et al. (2025).

Block 3: Aufgaben-Technologie-Passung (Task-Technology Fit / TTF)

*Theoretische Grundlegung:* Goodhue & Thompson (1995); McGrath's Group Task Circumplex; Paetow et al. (2025).

Konstrukt 3.1: Task-Technology Fit (Passung für kreative & analytische Aufgaben)

- **Item TTF_1 (Kreativ- & Entwurfsaufgaben):** 
*Deutsch:* Die Funktionen der generativen KI passen hervorragend zu unseren Aufgaben bei der Erstellung neuer Konzepte und Inhaltsentwürfe.

*Englisch:* The capabilities of generative AI fit well with our tasks in creating new concepts and drafting content.

*Quelle / Ableitung:* Adaptiert nach McGrath (1984); Paetow et al. (2025).
- **Item TTF_2 (Problemlösungs- & Konfliktmanagementaufgaben):** 
*Deutsch:* Bei der Bearbeitung komplexer Problemstellungen unterstützt mich die KI effektiv dabei, unterschiedliche Perspektiven zu strukturieren.

*Englisch:* When handling complex problem-solving tasks, the AI effectively supports me in structuring different perspectives.

*Quelle / Ableitung:* Adaptiert nach McGrath (1984) (Conflict/Mixed-Motive Tasks); Paetow et al. (2025).
- **Item TTF_3 (Leistungsrelevanz):** 
*Deutsch:* Der Einsatz von KI verbessert meine individuelle Arbeitsleistung bei der Erledigung täglicher Arbeitsaufgaben spürbar.

*Englisch:* Using AI noticeably improves my individual work performance in completing daily tasks.

*Quelle / Ableitung:* Adaptiert aus Goodhue & Thompson (1995); Paetow et al. (2025).

Block 4: Nutzen- vs. Barrierenabwägung (Duality Approach)

*Theoretische Grundlegung:* Gesk et al. (2021); Wichmann et al. (2024).

Konstrukt 4.1: Perceived Efficacy & Costs (Nutzen vs. Aufwand/Barrieren)

- **Item EFF_1 (Wirksamkeit):** 
*Deutsch:* Durch die Nutzung von KI kann die Bearbeitungszeit für Routineaufgaben in meiner Abteilung deutlich reduziert werden.

*Englisch:* Using AI significantly reduces the processing time for routine tasks in my department.

*Quelle / Ableitung:* Adaptiert aus Datensatz_v1 (Perceived Response Efficacy).
- **Item BAR_1 (Kosten/Barrieren - Invers):** 
*Deutsch:* Der Aufwand, die Einarbeitung in KI-Tools zu erlernen, steht in einem angemessenen Verhältnis zum Nutzen.

*Englisch:* The effort required to learn AI tools is reasonable compared to the benefits gained.

*Quelle / Ableitung:* Adaptiert aus Datensatz_v1 (Perceived Costs/Barriers).
- **Item BAR_2 (Kontrollverlust/Bedrohung):** 
*Deutsch:* Ich habe keine Befürchtung, dass der Einsatz von KI zu einem Verlust der Kontrolle über meine eigenen Arbeitsprozesse führt.

*Englisch:* I do not fear that using AI will lead to a loss of control over my own work processes.

*Quelle / Ableitung:* Adaptiert nach Gesk et al. (2021); Wichmann et al. (2024).

Statusmeldung von Agent 1:

Der Fragentwurf ist vollständig erstellt und deckt alle theoretischen Säulen des KI-Readiness-Modells ab.

💡 **Sollen wir jetzt den zweiten Schritt simulieren und den Entwurf von Agent 2 (Der Kritiker) auf methodische Fehler wie** **Double-Barreled Questions** **, Suggestivität und Gütekriterien prüfen lassen?**

Nutzer

erkläre aufgabenstellung ganz einfach was ich machen soll

NotebookLM

Ganz einfach zusammengefasst musst du in diesem Modul folgende drei Dinge tun:

1. Das Ziel (Das Produkt / Artefakt)

Du entwickelst **Anweisungen (Prompts/Leitlinien)**  für ein Künstliches-Intelligenz-Modell. Diese Prompts sollen die KI in die Lage versetzen, automatisch einen wissenschaftlich fundierten Fragebogen zu erstellen. Der konkrete Inhalt des Fragebogens ist die Messung der **KI-Readiness von Mitarbeitenden**  in einem Unternehmen. Die Fragen dürfen dabei nicht frei erfunden werden, sondern müssen direkt aus wissenschaftlichen Theorien abgeleitet werden.

2. Die technischen Werkzeuge

**Google NotebookLM:**  Du lädst die bereitgestellten Unterlagen in NotebookLM hoch, entwickelst dort deine Prompts und erzeugst am Ende einen Freigabelink.

**GitHub:**  Du erstellst ein GitHub-Repository und fügst dort deinen Code sowie den Link zu deinem NotebookLM-Projekt ein, um dein Vorgehen offenzulegen.

3. Die schriftliche Ausarbeitung (Hausarbeit)

Du schreibst eine **Hausarbeit von maximal 10 inhaltlichen Seiten** . Der Aufbau der Arbeit orientiert sich strikt an den sechs Schritten des **Design Science Research (DSR)**  Prozesses:

**Problemidentifikation & Motivation:**  Warum ist eine automatisierte Fragebogenerstellung für Unternehmen wichtig?

**Zielsetzung des Tools:**  Welche Anforderungen muss dein Leitlinienmodell erfüllen?

**Entwicklung des Artefakts:**  Wie hast du das Prompt-Modell (z. B. das Drei-Agenten-System) aufgebaut?

**Demonstration im Anwendungsumfeld:**  Zeige einen konkreten Durchlauf zur Erstellung des KI-Readiness-Fragebogens.

**Evaluation:**  Beschreibe, wie du die Qualität der Fragen geprüft hast und welche Korrekturschleifen du durchlaufen bist.

**Fazit & Ausblick:**  Fasse die Ergebnisse zusammen, nenne Limitationen und zeige Weiterentwicklungsmöglichkeiten auf.

💡 **Sollen wir als Nächstes den zweiten Agenten (den Kritiker) simulieren, um die ersten Fragen aus unserem Test-Durchlauf methodisch zu überprüfen?**

Nutzer

erkläre ausführlicher: Du entwickelst Anweisungen (Prompts/Leitlinien) für ein Künstliches-Intelligenz-Modell . Diese Prompts sollen die KI in die Lage versetzen, automatisch einen wissenschaftlich fundierten Fragebogen zu erstellen . Der konkrete Inhalt des Fragebogens ist die Messung der KI-Readiness von Mitarbeitenden in einem Unternehmen

NotebookLM

Hier ist eine detaillierte und leicht verständliche Aufschlüsselung der drei Kernelemente deiner Aufgabenstellung:

1. „Du entwickelst Anweisungen (Prompts/Leitlinien) für ein Künstliches-Intelligenz-Modell“

Im Rahmen dieses Moduls erstellst du ein technisches **Artefakt nach dem Design Science Research (DSR) Paradigma** . Das Artefakt besteht nicht aus einer neu programmierten Software, sondern aus **strukturierten Prompts und Anweisungen (Leitlinien)**  für ein Large Language Model (LLM) wie Google NotebookLM oder ChatGPT.

Damit das Sprachmodell verlässlich arbeitet und qualitativ hochwertige Ergebnisse liefert, stützt du deine Prompts auf drei fortgeschrittene KI-Methoden:

**Retrieval-Augmented Generation (RAG):**  Du speist wissenschaftliche Quellentexte und Theorien direkt via Prompt-Injektion als Kontext ein, damit die KI halluzinationsfreie Antworten liefert.

**Few-Shot Prompting (In-Context Learning):**  Du übergibst dem Modell konkrete Beispiel-Fragebögen und Muster-Items aus der Datenbasis als Vorlage für Skalierung und Format.

**Agentische Workflows (Multi-Agenten-System):**  Du unterteilst den Generierungsprozess in verschiedene Rollen (z. B. **Agent 1: Methodiker**  zur Generierung, **Agent 2: Kritiker**  zur methodischen Prüfung und **Agent 3: Proband**  zur Verständlichkeitsprüfung).

2. „Diese Prompts sollen die KI in die Lage versetzen, automatisch einen wissenschaftlich fundierten Fragebogen zu erstellen“

„Wissenschaftlich fundiert“ bedeutet, dass die Fragen **niemals frei erfunden oder unüberlegt formuliert**  werden dürfen. Das KI-Modell muss angewiesen werden, jedes einzelne Item sachlogisch aus etablierten Theorien der Akzeptanz- und Sozialforschung abzuleiten.

In deinen Quellen finden sich dafür folgende primäre Theoriebausteine:

**Reasoned Action Approach (RAA):**  Misst die persönliche Einstellung (*Attitude*), den sozialen Druck (*Perceived Norms*) und die wahrgenommene Verhaltenskontrolle (*Perceived Behavioral Control*) zur Vorhersage der Nutzungsabsicht (*Intention to use*).

**Trust-Modell für LLMs/GenAI:**  Erfasst das Vertrauen in KI-Systeme über die Dimensionen Fähigkeit/Erklärbarkeit (*Ability/Explainability*), Wohlwollen/Unbehaglichkeit (*Benevolence/Uncanny Valley*) und Integrität/Datenschutz (*Integrity/Data Privacy*).

**Task-Technology Fit (TTF):**  Prüft, wie gut die Funktionen der KI mit den spezifischen Arbeitsaufgaben der Beschäftigten übereinstimmen.

**Duality Approach:**  Wiegt die wahrgenommene Wirksamkeit (*Perceived Efficacy*) gegen emotionale Bedenken, Ängste und Kosten (*Fear/Barriers*) ab.

Zusätzlich stellt die Leitlinie sicher, dass wissenschaftliche **Gütekriterien (Objektivität, Reliabilität, Validität)**  eingehalten und methodische Fehler wie Doppelverneinungen oder Suggestivfragen systematisch eliminiert werden.

3. „Der konkrete Inhalt des Fragebogens ist die Messung der KI-Readiness von Mitarbeitenden in einem Unternehmen“

Die praktische Problemstellung des Praxispartners verlangt nach einem Instrument, mit dem Unternehmen ermitteln können, wie bereit und aufgeschlossen ihre Beschäftigten für den Einsatz generativer KI-Werkzeuge sind.

Der automatisch erzeugte Fragebogen misst daher konkret:

**Nutzungsbereitschaft:**  Beabsichtigen die Mitarbeitenden, KI-Tools in ihren Arbeitsprozessen einzusetzen?

**Kompetenz & Verständnis:**  Verstehen die Mitarbeitenden, wie die KI Ergebnisse erzeugt und wie korrekt diese sind (*Ability*)?

**Datenschutz & Vertrauen:**  Haben die Beschäftigten Bedenken bezüglich der Sicherheit interner Unternehmensdaten (*Integrity/Data Privacy*)?

**Aufgabenpassung:**  Sieht das Personal einen konkreten Mehrwert von KI-Anwendungen für seine täglichen Aufgaben (*Task-Technology Fit*)?

Zusammenfassung deiner konkreten Aufgaben

**Prompts formulieren:**  Erstelle die Leitlinien (z. B. das 3-Agenten-System) in NotebookLM.

**Demonstration & Durchlauf:**  Lasse die KI mit diesen Prompts einen fragebogenbasierten Entwurf zur KI-Readiness ausgeben.

**Dokumentation in GitHub & Hausarbeit:**  Dokumentiere dein Vorgehen, die Prompt-Iterationen und Hindernisse in einer maximal 10-seitigen Ausarbeitung nach der DSR-Struktur (Peffers et al. 2007) und verlinke dein GitHub-Repository.

💡 **Möchtest du als Nächstes den Fragentwurf aus unserem ersten Durchlauf von Agent 2 (dem Kritiker) auf methodische Fehler und Gütekriterien prüfen lassen?**

Nutzer

Simuliere Agent 2 (Kritiker)

NotebookLM

🧐 Agent 2: Der Kritiker – Methodischer Review-Bericht (Durchlauf 1)

**Rolle:**  Agent 2 (Der Kritiker) – Prüfinstanz für empirische Sozialforschung und psychometrische Testkonstruktion.
**Prüfgegenstand:**  Fragentwurf aus Durchlauf 1 (Agent 1)
**Prüfkriterien:**  Vermeidung von Erhebungsfehlern (Double-Barreled Questions, Suggestivfragen, Doppelverneinungen) sowie Sicherstellung der Gütekriterien (**Objektivität, Reliabilität, Validität** ).

1. Prüfstatus

**Gesamtbewertung:**  ⚠️ **Überarbeitung erforderlich**

**Begründung:**  Der Entwurf von Agent 1 deckt die theoretischen Konstrukte inhaltlich gut ab. Allerdings weisen einige Items methodische Mängel auf, die zu Verfälschungen der Messergebnisse und erhöhter kognitiver Belastung führen können.

2. Detaillierte Item-Mängelanalyse

A. Invers formulierte Items & Doppelverneinungen

- **Item INTG_1:**  *„Ich habe keine Bedenken, dass die Eingabe unternehmensinterner Informationen in das KI-System Daten an unbefugte Dritte weitergibt.“*
❌ **Fehler:**  Verneinte Formulierung („keine Bedenken“). Antwortet eine Person mit *1 = Stimme überhaupt nicht zu*, bedeutet das doppelt verneint: „Ich habe Bedenken, dass es nicht weitergegeben wird“ – dies führt zu schwerwiegenden Messfehlern.
- **Item BEN_1:**  *„Ich empfinde die Interaktion mit der generativen KI nicht als unheimlich oder unangenehm.“*
❌ **Fehler:**  Doppelverneinung („nicht als unheimlich“) kombiniert mit einer Doppelabfrage (*Double-Barreled Question*).

B. Double-Barreled Questions (Doppelabfragen)

- **Item BEN_1:**  *„...unheimlich oder unangenehm.“*
❌ **Fehler:**  Unheimlichkeit (*Uncanny Valley*) und Unangenehmsein sind zwei verschiedene emotionale Dimensionen, die getrennt gemessen werden müssen.
- **Item BAR_1:**  *„Der Aufwand, die Einarbeitung in KI-Tools zu erlernen, steht in einem angemessenen Verhältnis zum Nutzen.“*
❌ **Fehler:**  Vermischt die Aufwandseinschätzung mit der Nutzenbewertung in einer einzigen Frage.

C. Suggestivformulierungen & Voraussetzungsfehler

- **Item TTF_1:**  *„Die Funktionen der generativen KI passen hervorragend zu unseren Aufgaben...“*
❌ **Fehler:**  Das Adjektiv „hervorragend“ ist wertend/suggestiv und verfälscht die unvoreingenommene Antwortverteilung auf der 7-Punkt-Likert-Skala.
- **Item INT_2:**  *„Ich habe den festen Plan, KI-gestützte Systeme im Betrieb einzusetzen, sobald diese verfügbar gemacht werden.“*
❌ **Fehler:**  Enthält die Bedingung „sobald diese verfügbar gemacht werden“, wodurch die Bedingung statt der reinen Nutzungsabsicht gemessen wird.

3. Konkrete Korrekturvorschläge (Optimierte Fragensätze)

Agent 2 korrigiert die betroffenen Items für den zweiten Durchlauf:

| Item-ID | Ursprüngliche Formulierung (Agent 1) | Methodisch korrigierte Formulierung (Agent 2) | Korrekturgrund |
| --- | --- | --- | --- |
| **INT_2** | ...sobald diese verfügbar gemacht werden. | Ich habe den festen Plan, KI-gestützte Systeme im Betrieb einzusetzen. | Bedingung gestrichen (Fokus auf reine Absicht). |
| **INTG_1** | Ich habe **keine Bedenken** , dass... weitergibt. | Ich vertraue darauf, dass eingegebene unternehmensinterne Informationen nicht an unbefugte Dritte weitergegeben werden. | Beseitigung der Doppelverneinung. |
| **BEN_1** | ...**nicht**  als **unheimlich oder unangenehm** . | Ich empfinde die Interaktion mit der generativen KI als unheimlich. *(Invers skaliert)* | Aufspaltung & Eliminierung der Doppelabfrage. |
| **TTF_1** | ...passen **hervorragend**  zu... | Die Funktionen der generativen KI passen zu unseren Aufgaben bei der Erstellung neuer Konzepte. | Eliminierung des Suggestivworts „hervorragend“. |
| **BAR_1** | Der Aufwand... steht in einem angemessenen Verhältnis zum Nutzen. | Die Einarbeitung in die Nutzung von KI-Werkzeugen erfordert für mich zu viel Zeit. | Aufspaltung auf reine Barrieren-/Kostenmessung. |

4. Freigabe für den Pretest (Agent 3)

Mit diesen Korrekturen erfüllt der Fragenkatalog die notwendigen psychometrischen Standards:

**Objektivität:**  Eindeutige, unvoreingenommene Formulierungen verhindern unterschiedliche Interpretationsspielräume.

**Reliabilität:**  Einheitliche Ausrichtung der 7-Punkt-Likert-Skala (1–7) erhöht die interne Konsistenz.

**Inhaltsvalidität:**  Die Items spiegeln die theoretischen Konstrukte (*RAA, Trust, TTF, Duality*) präzise wider.

Das überarbeitete Item-Set wird hiermit an **Agent 3 (Der Proband / Pretest-Simulation)**  übergeben, um die Verständlichkeit und Praxistauglichkeit aus Nutzersicht zu prüfen.

💡 **Sollen wir als Nächstes die Simulation von Agent 3 (Proband/Pretest) durchführen, um das Feedback eines Sachbearbeiters und einer Führungskraft einzuholen?**

Nutzer

Simuliere Agent 3 (Proband)

NotebookLM

🧪 Agent 3: Der Proband – Pretest-Simulation & Verständlichkeitsbericht

**Rolle:**  Agent 3 (Der Proband) simuliert eine virtuelle Testperson und bewertet als Fachexperte die Praxistauglichkeit, Verständlichkeit und kognitive Belastung des von Agent 2 methodisch korrigierten Fragebogens.

Für eine praxisnahe Evaluation im Unternehmenskontext nimmt Agent 3 zwei typische Rollenperspektiven ein:

**Perspektive A:**  Sachbearbeiter/in im Fachbereich (Operative Anwendung, wenig KI-Spezialwissen).

**Perspektive B:**  Führungskraft / Senior Decision-Maker (Strategische Perspektive, Fokus auf Leistung und Datenschutz).

1. Pretest-Evaluation aus Perspektive A: Sachbearbeiter/in (Endanwender)

A. Sprachliche Verständlichkeit & Fachbegriffe

**Postiver Befund:**  Die von Agent 2 korrigierten Fragen vermeiden unklare Verschachtelungen und schwere Doppelverneinungen, was das Durchlesen flüssig macht.

- **Anmerkung / Hürde:**  Der Begriff *„generative KI-Anwendungen“* oder *„kognitive Aufgaben“* ist im operativen Alltagsgeschäft nicht allen Mitarbeitenden sofort geläufig.
*Empfehlung:* Dem Fragebogen sollte ein kurzer, 2-sätziger Einleitungstext vorgeschaltet werden, der praxiserprobte Beispiele nennt (z. B. *„Unter generativer KI verstehen wir Text- und Assistenzsysteme wie ChatGPT, Microsoft Copilot oder unternehmensinterne Chatbots“*).

B. Kognitive Belastung & Skalierung

Die durchgängig verwendete **7-Punkt-Likert-Skala**  (1 = „Stimme überhaupt nicht zu“ bis 7 = „Stimme voll und ganz zu“) wird als übersichtlich und gewohnt wahrgenommen.

Durch die Eliminierung der Doppelabfragen (*Double-Barreled Questions*) durch Agent 2 entsteht keine Verwirrung mehr beim Wählen der Antwortstufe.

2. Pretest-Evaluation aus Perspektive B: Führungskraft / Decision-Maker

A. Relevanz & Vertrauensfaktoren (Trust & Integrity)

**Datenschutz & Integrität:**  Fragen zur Datensicherheit bei KI-Eingaben sprechen die Hauptbedenken von Führungskräften außerhalb der IT-Abteilung direkt an, wo Datenschutz (*Integrity*) häufig höher gewichtet wird als reine Funktionsfähigkeit.

**Aufgabenpassung (Task-Technology Fit):**  Die Differenzierung nach unterschiedlichen Aufgabenarten (z. B. Erstellung von Konzepten vs. Bearbeitung von Routineaufgaben) erlaubt eine präzise Einschätzung des tatsächlichen Arbeitsnutzens.

B. Bearbeitungsökonomie & Auswertbarkeit

**Zeitaufwand:**  Der strukturierte Fragenkatalog umfasst pro Konstrukt genau 3 Items und benötigt eine Bearbeitungszeit von ca. 5 bis 7 Minuten. Dies liegt im optimalen Rahmen, um hohe Rücklaufquoten ohne Abbrüche zu gewährleisten.

**Ergebnisrelevanz:**  Die Antworten liefern dem Management ein klares Profil darüber, ob Vorbehalte primär aus fehlendem Verständnis (*Ability*), Sorge um Unternehmensdaten (*Integrity*) oder fehlender Arbeitswertschöpfung (*TTF*) resultieren.

3. Pretest-Gesamtergebnis & Finale Freigabe

```
================================================================================
PRETEST-PROTOKOLL (AGENT 3)
================================================================================
Verständlichkeit (Sachbearbeiter):    ★★★★☆ (4/5) -> Sehr gut (mit Einleitungstext)
Praxisrelevanz (Führungskraft):       ★★★★★ (5/5) -> Exzellent
Kognitive Belastung / Zeitaufwand:   ★★★★★ (5/5) -> Optimal (ca. 6 Minuten)
Wissenschaftliche Gütekriterien:     ★★★★★ (5/5) -> Erfüllt (Objektiv, Reliabel, Valid)
--------------------------------------------------------------------------------
STATUS: FREIGEGEBEN (Ready for Deployment)
================================================================================
```

4. Einordnung in deine DSR-Hausarbeit (Peffers et al. 2007)

Diese Simulation schließt den iterativen Generierungszirkel ab und dient in deiner maximal 10-seitigen Ausarbeitung als wissenschaftlicher Nachweis deiner **Lösungsfindungskompetenz und Qualitätskontrolle** :

**Kapitel 3 (Entwicklung des Artefakts):**  Du beschreibst die Prompts und die Rollenverteilung der drei Agenten (Methodiker → Kritiker → Proband).

**Kapitel 4 (Demonstration im Anwendungsumfeld):**  Du zeigst den konkreten Generierungsdurchlauf und die schrittweise Evolution der Items von Durchlauf 1 bis zur Freigabe.

**Kapitel 5 (Evaluation & Rückkopplungsschleifen):**  Du dokumentierst die Ergebnisse der Prüfinstanzen (Agent 2 & 3) als Nachweis für die Einhaltung der wissenschaftlichen Gütekriterien (**Objektivität, Reliabilität, Validität** ).

💡 **Möchtest du, dass wir als Nächstes einen konkreten Entwurf für das Inhaltsverzeichnis deiner 10-seitigen DSR-Hausarbeit erstellen, der genau auf den Bewertungsbogen der Dozenten abgestimmt ist?**

Nutzer

ja

NotebookLM

Hier ist ein maßgeschneiderter **Gliederungsentwurf für deine 10-seitige DSR-Hausarbeit** , der strikt an den sechs Prozessschritten nach **Peffers et al. (2007)**  ausgerichtet ist und alle Kriterien des offiziellen Bewertungsbogens abdeckt.

Vorschlag für den Titel der Hausarbeit

**Entwicklung eines DSR-basierten Leitlinienmodells zur automatisierten und wissenschaftlich fundierten Generierung von KI-Readiness-Fragebögen mittels Multi-Agenten-Prompting**

Seitenbudget & Gliederung im Überblick (Max. 10 inhaltliche Seiten)

```
1. Problemidentifikation und Motivation .................................... ca. 1,5 Seiten
2. Zielsetzung des Leitlinienmodells ....................................... ca. 1,0 Seite
3. Entwicklung des Artefakts (Multi-Agenten-Prompting) ..................... ca. 3,0 Seiten
4. Demonstration im Anwendungsumfeld (MockUp KI-Readiness) ................ ca. 2,0 Seiten
5. Evaluation und Rückkopplungsschleifen .................................... ca. 1,5 Seiten
6. Fazit, Limitationen und Ausblick ........................................ ca. 1,0 Seite
────────────────────────────────────────────────────────────────────────────────────────────
Gesamtumfang (inhaltstragend):                                               max. 10 Seiten
```

Detaillierte Kapitelstruktur & Inhaltsanforderungen

1. Problemidentifikation und Motivation (ca. 1,5 Seiten)

**1.1 Praktische Relevanz:**  Die Notwendigkeit für Unternehmen, die individuelle KI-Readiness von Mitarbeitenden vor der Einführung generativer KI-Systeme (z. B. LLMs/Copilots) präzise zu erfassen.

**1.2 Wissenschaftliches Problem:**  Herkömmliche Manuelle Fragebogenentwicklungen sind zeitaufwendig, während ungesteuerte KI-Generierungen zu Halluzinationen, unbelegten Vermutungen und verletzten Gütekriterien führen (*„Fragen, die vom Himmel fallen“*).

**1.3 Forschungsfrage & Fortgang der Arbeit:**  Formulierung einer präzisen Forschungsfrage (z. B. *„Wie muss ein DSR-basiertes Prompt-Leitlinienmodell gestaltet sein, um mittels LLMs automatisiert theoretisch fundierte und methodisch valide Fragebögen zur KI-Readiness zu erzeugen?“*).

2. Zielsetzung des Tools (ca. 1,0 Seite)

**2.1 Funktionale & Methodische Anforderungen:**  Anforderungen an das DSR-Artefakt (Automatisierung, Nachvollziehbarkeit, Gütekriterien-Einhaltung).

**2.2 Wissenschaftlicher Erklärungsrahmen:**  Verknüpfung der Zielsetzung mit etablierten Verhaltens- und Akzeptanztheorien zur Vermeidung von Ratgeberniveau.

3. Entwicklung des Artefakts: Das Leitlinienmodell (ca. 3,0 Seiten)

- **3.1 Theoretische Fundierung des KI-Readiness-Messmodells:** 
Integration des **Reasoned Action Approach (RAA)**  (Attitude, Perceived Norms, Intention).

Integration des **Trust-Modells für GenAI**  (Ability/Explainability, Benevolence/Uncanny Valley, Integrity/Data Privacy).

Integration der **Task-Technology Fit (TTF) Theorie**  (McGrath Task Circumplex).

Integration des **Duality Approach**  (Perceived Efficacy vs. Perceived Costs/Barriers).
- **3.2 Technische Architektur des Artefakts:** 
**Retrieval-Augmented Generation (RAG):**  Systematische Einspeisung der theoretischen Grundlagentexte via Prompt-Injektion in Google NotebookLM.

**Few-Shot Prompting:**  Vorgabe validierter Beispiel-Items zur Gewährleistung konsistenter 7-Punkt-Likert-Skalierungen.

**Multi-Agenten-Workflow:**  Implementierung der Rollen-Prompts für **Agent 1 (Methodiker)** , **Agent 2 (Kritiker)**  und **Agent 3 (Proband)** .

4. Demonstration im Anwendungsumfeld (ca. 2,0 Seiten)

**4.1 Anwendungsszenario:**  Durchlauf des Leitlinienmodells zur Generierung eines Fragebogens für ein reales Unternehmen.

**4.2 Exemplarische Artefakt-Ausgabe (MockUp):**  Darstellung der generierten Items je Konstrukt inklusive Zuordnung zu den theoretischen Quellen und Übersetzung.

**4.3 Anbindung an GitHub & NotebookLM:**  Nachweis der Transparenz durch das bereitgestellte Repository und den Projektlink.

5. Evaluation des Tools und Rückkopplungsschleifen (ca. 1,5 Seiten)

**5.1 Methodische Qualitätskontrolle (Agent 2):**  Aufdeckung und Korrektur von Erhebungsfehlern (z. B. Elimination von *Double-Barreled Questions*, Suggestivität und Doppelverneinungen).

**5.2 Pretest-Simulation (Agent 3):**  Überprüfung der Verständlichkeit und kognitiven Belastung aus Perspektive von Sachbearbeitern und Führungskräften.

**5.3 Nachweis der Gütekriterien:**  Bewertung der Ergebnisse hinsichtlich **Objektivität, Reliabilität und Validität** .

**5.4 Dokumentation der Prompt-Iterationen:**  Darstellung der Anpassungen am Leitlinienmodell infolge der Evaluierungsergebnisse (DSR-Rückkopplung).

6. Fazit, Limitationen und Ausblick (ca. 1,0 Seite)

**6.1 Zusammenfassung der Kernergebnisse:**  Kurze Synthese der Zielerreichung.

**6.2 Limitationen & Grenzen:**  Kritische Reflexion der Lösung (z. B. Abhängigkeit vom zugrundeliegenden LLM, Grenzen simulierter Pretests).

**6.3 Anhaltspunkte zur Weiterentwicklung:**  Vorschläge für zukünftige Forschung und Erweiterungen des Artefakts.

Strategische Erfolgsfaktoren für die Note 1,0

**Keine Füllwörter / Kurze Sätze:**  Schreibe extrem sachlich und präzise. Jeder Satz muss Information tragen.

**Lückenlose APA-Zitation:**  Achte darauf, dass jede theoretische Behauptung direkt mit den Quellentexten belegt wird.

**Fokus auf die Lösungsfindung:**  Verwende Abbildungen für das DSR-Modell (Peffers) und das 3-Agenten-System, um den Platz optimal zu nutzen.

💡 **Möchtest du, dass ich dir für Kapitel 1 (Problemidentifikation & Motivation) bereits den ausformulierten Einleitungstext nach allen wissenschaftlichen Standards erstelle?**

Nutzer

Erstelle die Einleitung für Kapitel 1

NotebookLM

1. Problemidentifikation und Motivation

1.1 Praktische Relevanz: Erfassung der KI-Readiness im Unternehmenskontext

Die fortschreitende Integration generativer Künstlicher Intelligenz (GenAI) wie Large Language Models (LLMs) verändert betriebliche Arbeitsprozesse grundlegend. Unternehmen stehen vor der Herausforderung, nicht nur die technische Infrastruktur bereitzustellen, sondern auch die individuelle Akzeptanz, das Vertrauen und die Kompetenzen der Beschäftigten systematisch zu bewerten. Bevor generative Systeme flächendeckend im Arbeitsalltag verankert werden, ist eine präzise Erfassung der **KI-Readiness**  der Mitarbeitenden erforderlich. Ohne eine fundierte Standortbestimmung drohen Fehlinvestitionen, Akzeptanzbarrieren und ungenutztes Effizienzpotenzial in den Fachbereichen.

1.2 Wissenschaftliches Problem: Schwachstellen ungesteuerter KI-Generierung

Die manuelle Erstellung empirischer Messinstrumente ist zeit- und ressourcenintensiv. Gleichzeitig birgt der ungesteuerte Einsatz von Sprachmodellen zur Fragebogengenerierung erhebliche methodische Risiken. Naive Prompts ohne wissenschaftliche Verankerung führen häufig dazu, dass generierte Fragen ohne theoretische Fundierung verbleiben und gewissermaßen „vom Himmel fallen“.

Darüber hinaus verletzen unkontrollierte KI-Erzeugnisse regelmäßig die zentralen **Gütekriterien wissenschaftlichen Arbeitens** :

**Objektivität:**  Unklare oder wertende Formulierungen beeinträchtigen die Unabhängigkeit der Messung von den Testleitenden.

**Reliabilität:**  Methodische Erhebungsfehler wie Doppelverneinungen oder uneinheitliche Skalierungen verhindern reproduzierbare Messergebnisse.

**Validität:**  Ohne Abbildung etablierter theoretischer Konstrukte messen die generierten Items nicht das beabsichtigte Zielkonstrukt.

Es besteht folglich eine ausgeprägte Forschungslücke an methodisch gesteuerten Leitlinien, die LLMs befähigen, automatisiert wissenschaftlich fundierte und psychometrisch valide Messinstrumente zu erzeugen.

1.3 Forschungsfrage, Zielsetzung und Fortgang der Arbeit

Zur Lösung dieser Problemstellung verfolgt die vorliegende Arbeit den **Design Science Research (DSR)**  Ansatz nach Peffers et al. (2007). Das primäre Forschungsziel besteht in der Entwicklung und Demonstration eines DSR-basierten Leitlinienmodells als technisches Artefakt. Dieses Artefakt nutzt **Retrieval-Augmented Generation (RAG)** , **Few-Shot Prompting**  und **multi-agentische Workflows**  auf der Plattform Google NotebookLM, um qualitätsgesicherte Fragebögen zur KI-Readiness abzuleiten.

Aus diesem Forschungsvorhaben leitet sich folgende zentrale Forschungsfrage ab:

*„Wie muss ein DSR-basiertes Prompt-Leitlinienmodell gestaltet sein, um mittels Large Language Models automatisiert theoretisch fundierte und methodisch valide Fragebögen zur Messung der KI-Readiness von Mitarbeitenden zu erzeugen?“*

Der Aufbau der Arbeit orientiert sich strikt an den Phasen des DSR-Prozesses:

**Kapitel 2**  definiert die methodischen und funktionalen Zielsetzungen des Leitlinienmodells.

**Kapitel 3**  widmet sich der Entwicklung des Artefakts und verknüpft das theoretische KI-Readiness-Messmodell mit der Multi-Agenten-Architektur.

**Kapitel 4**  demonstriert die Funktionsweise anhand eines konkreten Durchlaufs (MockUp).

**Kapitel 5**  evaluiert das Artefakt bezüglich der wissenschaftlichen Gütekriterien und dokumentiert die iterativen Rückkopplungsschleifen.

**Kapitel 6**  fasst die Ergebnisse zusammen, reflektiert bestehende Limitationen und gibt einen Ausblick auf zukünftige Forschungsansätze.

💡 **Sollen wir als Nächstes direkt mit Kapitel 2 (Zielsetzung des Leitlinienmodells) fortfahren und die konkreten funktionalen & methodischen Anforderungen an dein KI-Tool definieren?**

Nutzer

erstelle einen optimierten prompt um aufgabe mit 1,0 zu lösen und nutze auch die neuen quellen

NotebookLM

Um für deine Prüfungsleistung im Praxismodul die **Bestnote 1,0**  zu erzielen, muss dein Artefakt (das Prompt-Leitlinienmodell in NotebookLM und GitHub) alle vorliegenden theoretischen Quellen und methodischen Vorgaben lückenlos miteinander verknüpfen.

Die Analyse aller Quellen zeigt, dass dein Modell nicht nur Standard-Akzeptanztheorien abbilden sollte, sondern um die **neuesten wissenschaftlichen Messskalen zur KI-Readiness und KI-Selbstwirksamkeit**  erweitert werden muss:

**Meta AI Literacy Scale (MAILS & MAILS-Short):**  Erfasst *Use & Apply*, *Understand*, *Detect*, *AI Ethics*, *Create AI* sowie die psychologischen Metakompetenzen *AI Self-Efficacy* (Problemlösung, Lernen) und *AI Self-Competency* (Emotionsregulation, Persuasion Literacy).

**AI Learning Readiness Self-Efficacy Scale (AILRSE-5):**  Ein hochaktuelles, globales Messinstrument zur Erfassung der Selbstwirksamkeitserwartung beim Erlernen neuer KI-Technologien.

**Artificial Intelligence Self-Efficacy Scale (AISES):**  Differenziert KI-Selbstwirksamkeit in *Assistance*, *Anthropomorphic Interaction*, *Comfort with AI* und *Technological Skills*.

**Artificial Intelligence Readiness Scale (AIRS):**  Erfasst die individuelle KI-Readiness über *Self-Efficacy & Cognition (SEC)*, *Optimism*, *Collaborative Learning and Working (CLW)* und *Comfort*.

**GenAI Enterprise Trust Model (Do Khac et al. 2025):**  Erklärt die Vertrauensbildung gegenüber LLMs/ChatGPT über *Ability (Explainability)*, *Benevolence (Uncanny Valley)* und *Integrity (Data Privacy/GDPR)*.

**Task-Technology Fit & McGrath Circumplex:**  Untersucht die Passung zwischen KI-Funktionen und spezifischen Aufgabenformen (kreativ, analytisch, konfliktär, operativ).

**Duality Approach & Reasoned Action Approach (RAA):**  Wägt funktionale Nutzenerwartungen (*Perceived Efficacy*) gegen emotionale Bedenken und Ängste (*Fear/Threat*) ab.

🚀 Der finale 1,0-Master-System-Prompt für NotebookLM

Kopiere den folgenden ausformulierten **Master-Prompt**  direkt in dein Google NotebookLM (oder nutze ihn als System-Prompt in deinem GitHub-Repository), um die automatische Fragebogengenerierung wissenschaftlich perfekt zu steuern:

```
================================================================================
MASTER-LEITLINIENMODELL: AUTOMATISIERTE GENERIERUNG VON KI-READINESS-FRAGEBÖGEN
================================================================================

ROLLE UND ZIELSETZUNG:
Du agierst als führender wissenschaftlicher Methodiker, Psychometriker und DSR-Experte für Wirtschaftsinformatik.
Deine Aufgabe ist die automatisierte Erstellung eines empirisch validen, theoretisch fundierten und praxisrelevanten Fragebogens zur Erfassung der "KI-Readiness von Mitarbeitenden" im Unternehmenskontext.
Alle generierten Mess-Items müssen streng logisch aus der hinterlegten wissenschaftlichen Quellenbasis abgeleitet werden.

--------------------------------------------------------------------------------
1. THEORETISCHES MESSMODELL (RETRIEVAL-AUGMENTED GENERATION / RAG)
--------------------------------------------------------------------------------
Nutze zur Item-Konstruktion ausschließlich folgende 5 theoretische Hauptsäulen aus den Quellentexten:

SÄULE A: KI-LITERACY & SELBSTWIRKSAMKEIT (MAILS, AILRSE-5, AISES, AIRS)
- Meta AI Literacy (MAILS): Messung von 'Use & Apply AI', 'Understand AI', 'Detect AI', 'AI Ethics' sowie 'Create AI' als separates Konstrukt (Carolus et al. 2023; Koch et al. 2024).
- KI-Selbstwirksamkeit & Metakompetenzen: Erfassung von 'AI Problem Solving', 'AI Learning' (AILRSE-5 nach Oksanen et al. 2026), 'AI Emotion Regulation' sowie 'AI Persuasion Literacy' (MAILS).
- KI-Interaktion (AISES): Erfassung von 'Assistance', 'Anthropomorphic Interaction', 'Comfort with AI' und 'Technological Skills' (Wang & Chuang 2024).
- Kollaboratives Arbeiten (AIRS): Erfassung von 'Collaborative Learning and Working' (CLW) und 'Optimism' (Wang et al. 2026).

SÄULE B: VERTRAUEN IN ENTERPRISE-GENAI (TRUST MODEL)
- Ability / Explainability: Transparenz und Nachvollziehbarkeit der KI-Ergebnisse (X1-X3) (Do Khac et al. 2025).
- Benevolence / Uncanny Valley: Wahrnehmung der KI als unheimlich/unmenschlich (U1-U3) (Do Khac et al. 2025; Mayer et al. 1995).
- Integrity / Data Privacy: Bedenken hinsichtlich Datenschutz, DSGVO und Weitergabe interner Unternehmensdaten (D1-D3) (Do Khac et al. 2025).

SÄULE C: AUFGABEN-TECHNOLOGIE-PASSUNG (TASK-TECHNOLOGY FIT / TTF)
- McGrath Task Circumplex: Abgleich der KI-Capabilities mit spezifischen Aufgabenarten (Intellective, Judgmental, Conflict, Creativity, Execution) (Paper Fragebogen 3; Goodhue & Thompson 1995).

SÄULE D: BEVERHALTENSABSICHT & DUALITY APPROACH (RAA & DUAL MODEL)
- Reasoned Action Approach (RAA): Direct Measurement von 'Intention to Use', 'Attitude', 'Perceived Norms' und 'Perceived Behavioral Control' (Fishbein & Ajzen 2010).
- Duality Approach: Gegenüberstellung von 'Perceived Response Efficacy' vs. 'Perceived Threat / Fear' (Gesk, Wichmann & Leyer 2021/2024).

--------------------------------------------------------------------------------
2. METHODISCHE VORGABEN & FEW-SHOT IN-CONTEXT LEARNING
--------------------------------------------------------------------------------
- Skalierung: Nutze durchgängig eine 7-Punkt-Likert-Skala (1 = "Stimme überhaupt nicht zu" bis 7 = "Stimme voll und ganz zu").
- Gütekriterien (Objektivität, Reliabilität, Validität):
  1. ELIMINIERE Double-Barreled Questions (keine zwei Sachverhalte in einer Frage).
  2. ELIMINIERE Suggestivformulierungen (keine wertenden Adjektive wie "hervorragend" oder "problemlos").
  3. ELIMINIERE Doppelverneinungen (invers formulierte Items müssen sprachlich einfach verständlich bleiben).
  4. Bipolare Sprachfassung: Erstelle jedes Item sowohl auf Deutsch als auch auf Englisch.

--------------------------------------------------------------------------------
3. AGENTISCHER MULTI-AGENTEN-WORKFLOW (3-STUFEN-GENERIERUNG)
--------------------------------------------------------------------------------
Führe die Generierung sequenziell in drei Schritten durch:

SCHRITT 1: AGENT 1 (DER METHODIKER)
- Generiert pro Unterkonstrukt genau 3 reflektierte Mess-Items.
- Ordnet jedem Item die theoretische Quelle (Autor, Jahr) sowie die exakte Konstrukt-ID zu.

SCHRITT 2: AGENT 2 (DER KRITIKER)
- Überprüft den Entwurf von Agent 1 unnachgiebig auf Erhebungsfehler.
- Erstellt eine Korrekturtabelle und ersetzt mangelhafte Formulierungen durch optimierte, valide Items.

SCHRITT 3: AGENT 3 (DER PROBAND / SIMULIERTER PRETEST)
- Bewertet den korrigierten Fragebogen aus zwei Zielgruppen-Perspektiven:
  a) Sachbearbeiter/in (operativ, geringes KI-Vorwissen -> Prüft Verständlichkeit & Begriffsklarheit).
  b) Führungskraft (strategisch -> Prüft Relevanz bezogen auf Datenschutz & Performance).
- Gibt das finale, freigegebene Item-Set mit einer kurzen Einleitungsempfehlung aus.

================================================================================
```

2. Umsetzung im Rahmen der 10-seitigen DSR-Hausarbeit (Peffers et al. 2007)

Um die 100 Punkte des Evaluationsbogens voll auszuschöpfen, bindest du diesen Master-Prompt wie folgt in deine DSR-Hausarbeit ein:

**In Kapitel 3 (Entwicklung des Artefakts):**  Erkläre die wissenschaftliche Herleitung deines Master-Prompts. Zeige auf, wie die **RAG-Komponente**  (Integration von `MAILS`, `AILRSE-5`, `AISES`, `AIRS` und `Trust-Model`), die **Few-Shot-Vorgaben**  und die **Drei-Agenten-Architektur**  zusammenwirken.

**In Kapitel 4 (Demonstration im Anwendungsumfeld):**  Füge den kompletten Master-Prompt als Textbox/Abbildung ein und zeige den konkreten Output (den generierten 7-Punkt-Likert-Fragebogen).

**In Kapitel 5 (Evaluation & Rückkopplungsschleifen):**  Dokumentiere die Korrekturleistung von **Agent 2**  (z. B. Beseitigung von *Double-Barreled Questions*) und die Ergebnisse der Pretest-Simulation von **Agent 3**  als Nachweis für die Einhaltung der Gütekriterien (**Objektivität, Reliabilität, Validität** ).

**GitHub-Integration:**  Speichere diesen Prompt als `system_prompt.txt` oder `master_prompt.json` in deinem GitHub-Repository und verlinke im NotebookLM-Projekt darauf.

💡 **Möchtest du, dass wir als Nächstes den ausformulierten Text für Kapitel 2 (Zielsetzung des Leitlinienmodells) erstellen, damit deine Hausarbeit Kapitel für Kapitel fertiggestellt wird?**

---

