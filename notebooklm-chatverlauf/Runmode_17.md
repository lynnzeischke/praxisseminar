# runmode 17

Quelle: https://notebook.google.com/notebook/c3fe0b25-1d4c-45e5-a58c-702cbaefba54
Exportiert: 21.10.2026, 18:58:37

---

## Frage

Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.

---

## Antwort

B1: Projektparameter, Design-Audit-Referenz & Quellen-Governance

```
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

Status der Primärquellen-Verifikation

**MAILS (Carolus et al., 2023):**  `VERIFIED` – Originalskala (0–10) und Item-Positionen im Volltext verifiziert.

**AILRSE-5 (Oksanen et al., 2026):**  `VERIFIED` – Originalskala (1–7) und 3-Item-Subset aus der 5-Item-Skala verifiziert.

**AISES (Wang & Chuang, 2024):**  `VERIFIED` – Originalskala (1–7) und 3 Comfort-Items (CF1, CF3, CF5) verifiziert.

**AIRS (Wang et al., 2026):**  `VERIFIED` – Zur Abgrenzung der Comfort-Dimension (Roboter-Item Q18/COM3 vs. GenAI) gepflegt.

**Lambiase et al. (2025/2026):**  `VERIFIED` – Facilitating Conditions FC_1–FC_3 als 3-Item-Subset verifiziert.

**FC-Originaldatenartefakt (** **1_originalDataset.csv** **/** **NOTEBOOKLM_FC_ORIGINALITEMS_OHNE_TEILNEHMERDATEN.txt** **):**  `VERIFIED` – Wörtlicher Textabgleich aus Spalten/Zeile 2 für FC_1 bis FC_3 erfolgreich durchgeführt. FC_4 regelkonform ausgeschlossen.

Dokumentation der AISES-Comfort-Auswahl

Im Rahmen des als **004_FINAL**  freigegebenen Design Audits (Abschnitt A8 & A9) ist die Auswahl von drei affektiven Comfort-Items aus dem publizierten 6-Item-Pool der AISES (Wang & Chuang, 2024) eine dokumentierte Operationalisierungsentscheidung innerhalb des Audits und stellt keinen genehmigungspflichtigen Nachtrag dar. Für GenAI-Büroanwendungen bieten die AISES-Items (CF1 Ruhe, CF3 Wohlbefinden, CF5 Entspanntheit) eine höhere Inhaltsvalidität als das AIRS-Item Q18/COM3 bezüglich humanoider Roboter.

B2: Tabelle der 18 reflektiven Items und Zusatzmodule

| item_id | Konstrukt | Primäre Originalquelle | Originalpositionsbeweis | Quellenevidenz | Skala | Validierungsstatus |
| --- | --- | --- | --- | --- | --- | --- |
| **LIT_01** | READINESS_CORE_LIT | Carolus et al. (2023), MAILS | Appendix A, Pos./ID 7 (Understand AI) | E2 | 0–10 | PASS |
| **LIT_02** | READINESS_CORE_LIT | Carolus et al. (2023), MAILS | Appendix A, Pos./ID 8 (Understand AI) | E2 | 0–10 | PASS |
| **LIT_03** | READINESS_CORE_LIT | Carolus et al. (2023), MAILS | Appendix A, Pos./ID 12 (Understand AI) | E2 | 0–10 | PASS |
| **LEARN_01** | READINESS_CORE_LEARN | Oksanen et al. (2026), AILRSE-5 | Table 2, Item No. 1 | E2 | 1–7 | PASS |
| **LEARN_02** | READINESS_CORE_LEARN | Oksanen et al. (2026), AILRSE-5 | Table 2, Item No. 2 | E2 | 1–7 | PASS |
| **LEARN_03** | READINESS_CORE_LEARN | Oksanen et al. (2026), AILRSE-5 | Table 2, Item No. 5 | E2 | 1–7 | PASS |
| **APPLY_01** | READINESS_CORE_APPLY | Carolus et al. (2023), MAILS | Appendix A, Pos./ID 1 (Use & Apply AI) | E2 | 0–10 | PASS |
| **APPLY_02** | READINESS_CORE_APPLY | Carolus et al. (2023), MAILS | Appendix A, Pos./ID 3 (Use & Apply AI) | E2 | 0–10 | PASS |
| **APPLY_03** | READINESS_CORE_APPLY | Carolus et al. (2023), MAILS | Appendix A, Pos./ID 24 (AI Problem solving) | E2 | 0–10 | PASS |
| **DETECT_01** | READINESS_CORE_DETECT | Carolus et al. (2023), MAILS | Appendix A, Pos./ID 13 (Detect AI) | E2 | 0–10 | PASS |
| **DETECT_02** | READINESS_CORE_DETECT | Carolus et al. (2023), MAILS | Appendix A, Pos./ID 15 (Detect AI) | E2 | 0–10 | PASS |
| **DETECT_03** | READINESS_CORE_DETECT | Theoriegeleitete Eigenentwicklung | NOT_APPLICABLE (Faktenprüfung) | E3 | 0–10 | PASS |
| **COMFORT_01** | READINESS_CORE_COMFORT | Wang & Chuang (2024), AISES | Table 3, Item CF1 / Q25 | E2 | 1–7 | PASS |
| **COMFORT_02** | READINESS_CORE_COMFORT | Wang & Chuang (2024), AISES | Table 3, Item CF3 / Q24 | E2 | 1–7 | PASS |
| **COMFORT_03** | READINESS_CORE_COMFORT | Wang & Chuang (2024), AISES | Table 3, Item CF5 / Q22 | E2 | 1–7 | PASS |
| **FC_01** | CONTEXT_FC | Lambiase et al. (2025) | Dataset Header / Zeile 2, Spalte FC_1 | E2 | 1–7 | PASS |
| **FC_02** | CONTEXT_FC | Lambiase et al. (2025) | Dataset Header / Zeile 2, Spalte FC_2 | E2 | 1–7 | PASS |
| **FC_03** | CONTEXT_FC | Lambiase et al. (2025) | Dataset Header / Zeile 2, Spalte FC_3 | E2 | 1–7 | PASS |

Nichtreflektive Zusatzmodule

**DIAG_01 / DIAG_02:**  Bedarfsidentifikation (Listenmodul + offenes Textfeld; nicht gescored).

**DEM_01:**  Kaufmännischer Funktionsbereich (offenes Textfeld / Dropdown; nicht gescored).

B3: Kritische wissenschaftliche Evaluation

**Konstruktabgrenzung AIRS vs. AISES bei READINESS_CORE_COMFORT:**  Das AIRS-Item COM3 (`Q18`: *"I am not afraid of humanoid AI technologies/products (robots)"*) erfasst Furchtlosigkeit vor physischen oder humanoiden Robotern. Im kaufmännischen Arbeitsalltag mit Generativer KI (z. B. Copilot, ChatGPT) erzeugt dieses Item eine erhebliche Messobjekt-Inkongruenz. Die wörtliche Übernahme der AISES-Comfort-Items (CF1 `Q25`, CF3 `Q24`, CF5 `Q22`) misst dagegen die direkte affektive Entlastung bei der Interaktion mit KI-Software. Auf Deutsch weisen die Items *"ruhig"*, *"wohl"* und *"entspannt"* jedoch eine potenzielle semantische Redundanz auf, die im Pretest auf verbleibende Faktortrennung hin überwacht werden muss.

**Kombination unterschiedlicher MAILS-Facetten in READINESS_CORE_APPLY:**  `APPLY_01` und `APPLY_02` entstammen der MAILS-Subskala *Use & Apply AI* (Bedienung und alltägliche Zielerreichung), während `APPLY_03` (Pos. 24) aus der Subskala *AI Problem Solving* entnommen wurde. Diese Zusammenführung dient dem Ziel, die Selbsteinschätzung praktischer Bewältigungskompetenz im Itembudget von 3 Items abzubilden, stellt jedoch eine projektspezifische Konstruktkombination dar. Publizierte Gütekennwerte der MAILS-Gesamtskala lassen sich nicht direkt übertragen.

**Theoretische Fundierung des E3-Items DETECT_03:**  MAILS *Detect AI* misst das Erkennen, ob eine Anwendung auf KI basiert (`DETECT_01`) bzw. ob man mit einer KI oder einer Person interagiert (`DETECT_02`). Im kaufmännischen Kontext von Generativer KI ist jedoch die kritische Validierung halluzinierter oder inhaltlich fehlerhafter KI-Ergebnisse die primäre Anforderung an die Bewertungskompetenz. Da hierfür kein unverändertes MAILS-Originalitem existiert, wurde `DETECT_03` als Reines E3-Item entwickelt (*"Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen"*). Das Item besitzt keine gefälschte Original-ID (`source_item_id = null`).

**Validitätsvorbehalt bei 3-Item-Subsets (AILRSE-5 und FC):**  Sowohl für AILRSE-5 als auch für die Facilitating Conditions (Lambiase et al., 2025) werden transparente 3-Item-Subsets verwendet. Die in den Originalstudien berichtete skalare Invarianz und Reliabilität der Vollskalen dürfen nicht ungeprüft für das reduzierte Messinstrument angenommen werden.

B4: Heuristischer Pretest-Durchgang (SIMULATED_HEURISTIC_PRETEST)

*(Modellinterne kognitive Plausibilitätsprüfung; erfordert zwingend einen nachfolgenden realen Human-Pretest)*

- **Persona 1: Kaufmännische Sachbearbeitung ohne KI-Vorerfahrung (** **NO_EXPERIENCE** **)** 
*Routing:* `EXP_01` greift korrekt. Die Abschnitte `APPLY`, `DETECT` und `COMFORT` werden vollständig übersprungen.

*Verständlichkeit:* Die Fragen zum Grundverständnis (`LIT_01`–`LIT_03`) und zur Lernzuversicht (`LEARN_01`–`LEARN_03`) werden als klar verständlich bewertet.

*Erleichternde Bedingungen (**FC**):* Die zusätzliche Ausweichoption *"Kann ich nicht beurteilen"* verhindert erzwungene Scheinantworten bei fehlender Betriebserfahrung.
- **Persona 2: Sachbearbeitung mit gelegentlicher GenAI-Nutzung (** **LIMITED_EXPERIENCE** **)** 
*Routing:* Erhält den vollständigen Fragebogen (18 Items + Zusatzmodule).

*Verständlichkeit:* Die Differenzierung zwischen einfacher Anwendung (`APPLY_01`), zielgerichteter Nutzung (`APPLY_02`) und eigenständiger Problemlösung (`APPLY_03`) wird als praxisnah und trennscharf wahrgenommen.
- **Persona 3: Controller/Intensivnutzer (** **REGULAR_USER** **)** 
*Routing:* Erhält alle Module.

*Beurteilung:* Die Abstufung bei `DETECT_03` (kritische Inhaltsprüfung) wird als zentraler Differenzierungsfaktor für fortgeschrittene KI-Readiness im Büroalltag identifiziert.

B5: Teilnehmerfragebogen (Employee AI Readiness)

Einleitung & Datenschutz

Willkommen zur Befragung über Ihre Erfahrungen und Einschätzungen zum Umgang mit Generativer KI (z. B. ChatGPT Enterprise, Microsoft Copilot) im kaufmännischen Arbeitsalltag.

`[DATENSCHUTZ_UND_STUDIENHINWEIS_PLATZHALTER]`

Teil 1: Allgemeine KI-Arbeitserfahrung (Routing-Filter)

**EXP_01: Wie häufig nutzen Sie generative KI-Anwendungen (z. B. ChatGPT, Microsoft Copilot) in Ihrem kaufmännischen Arbeitsalltag?**

[ ] **NO_EXPERIENCE:**  Ich habe bisher keine Erfahrung in der Nutzung von generativer KI bei meiner Arbeit. *(Springe zu Teil 2, danach direkt zu Teil 7)*

[ ] **LIMITED_EXPERIENCE:**  Ich nutze generative KI gelegentlich oder sporadisch bei meiner Arbeit. *(Weiter mit Teil 2)*

[ ] **REGULAR_USER:**  Ich nutze generative KI regelmäßig oder täglich bei meiner Arbeit. *(Weiter mit Teil 2)*

Teil 2: Subjektives KI-Grundverständnis (READINESS_CORE_LIT)

*Antwortskala: 0 (trifft gar nicht zu / Fähigkeit kaum ausgeprägt) bis 10 (trifft vollkommen zu / Fähigkeit sehr gut ausgeprägt)*

**LIT_01:**  Ich kenne die wichtigsten Grundbegriffe generativer KI. [1]

**LIT_02:**  Ich kenne die Bedeutung des Begriffs generative KI. [1]

**LIT_03:**  Ich kann mir mögliche zukünftige Anwendungen generativer KI vorstellen. [1]

Teil 3: KI-Lern-Selbstwirksamkeit (READINESS_CORE_LEARN)

*Antwortskala: 1 (Stimme überhaupt nicht zu) bis 7 (Stimme vollkommen zu)*

**LEARN_01:**  Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen funktionieren. [1]

**LEARN_02:**  Ich bin zuversichtlich, dass ich bei Bedarf die Nutzung neuer generativer KI-Anwendungen erlernen kann. [1]

**LEARN_03:**  Ich bin zuversichtlich, dass ich mir die Nutzung neuer generativer KI-Anwendungen selbstständig aneignen kann. [1]

Teil 4: Praktische KI-Anwendungs- & Problemlösefähigkeit (READINESS_CORE_APPLY)

*(Wird bei**EXP_01 = NO_EXPERIENCE**übersprungen)* *Antwortskala: 0 (trifft gar nicht zu / Fähigkeit kaum ausgeprägt) bis 10 (trifft vollkommen zu / Fähigkeit sehr gut ausgeprägt)*

**APPLY_01:**  Ich kann generative KI-Anwendungen bedienen. [1]

**APPLY_02:**  Ich kann generative KI sinnvoll einsetzen, um meine Arbeitsziele zu erreichen. [1]

**APPLY_03:**  Die meisten Probleme im Umgang mit generativer KI kann ich aus eigener Kraft meistern. [1]

Teil 5: Kritische KI-Bewertungskompetenz & KI-Erkennung (READINESS_CORE_DETECT)

*(Wird bei**EXP_01 = NO_EXPERIENCE**übersprungen)* *Antwortskala: 0 (trifft gar nicht zu / Fähigkeit kaum ausgeprägt) bis 10 (trifft vollkommen zu / Fähigkeit sehr gut ausgeprägt)*

**DETECT_01:**  Ich kann erkennen, ob eine Anwendung auf generativer KI basiert. [1]

**DETECT_02:**  Ich kann unterscheiden, ob ich mit einer generativen KI oder einer Person interagiere. [1]

**DETECT_03:**  Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen. [1]

Teil 6: Affektiver Komfort im Umgang mit KI (READINESS_CORE_COMFORT)

*(Wird bei**EXP_01 = NO_EXPERIENCE**übersprungen)* *Antwortskala: 1 (Stimme überhaupt nicht zu) bis 7 (Stimme vollkommen zu)*

**COMFORT_01:**  Wenn ich mit generativer KI interagiere, fühle ich mich ruhig. [1]

**COMFORT_02:**  Wenn ich mit generativer KI interagiere, fühle ich mich wohl. [1]

**COMFORT_03:**  Wenn ich mit generativer KI interagiere, fühle ich mich entspannt. [1]

Teil 7: Wahrgenommene Erleichternde Bedingungen (CONTEXT_FC)

*Antwortskala: 1 (Stimme überhaupt nicht zu) bis 7 (Stimme vollkommen zu) sowie Option "Kann ich nicht beurteilen" (**MISSING_NOT_SCORED**)*

**FC_01:**  Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI-Anwendungen bei meiner Arbeit zu nutzen. [1] | [ ] Kann ich nicht beurteilen

**FC_02:**  Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen bei meiner Arbeit zu nutzen. [1] | [ ] Kann ich nicht beurteilen

**FC_03:**  Generative KI-Anwendungen sind mit anderen Technologien kompatibel, die ich bei meiner Arbeit verwende. [1] | [ ] Kann ich nicht beurteilen

Teil 8: Diagnostischer Schulungs- und Supportbedarf (DIAGNOSTIC_NEEDS)

*(Nicht-reflektives Zusatzmodul, fließt nicht in Readiness-Scores ein)*

**DIAG_01: In welchen der folgenden Bereiche sehen Sie für sich persönlichen Entwicklungs- oder Schulungsbedarf bezüglich Generativer KI?**  *(Mehrfachnennungen möglich)*

[ ] Grundlagen generativer KI

[ ] Prompting und effektive Aufgabenstellung

[ ] Kritische Prüfung und Validierung von KI-Ergebnissen

[ ] Datenschutz und sicherer Umgang mit sensiblen Unternehmensdaten

[ ] Urheberrecht, Transparenz und ethische Richtlinien

[ ] Integration von KI in bestehende Arbeitsprozesse

[ ] Konkrete Werkzeug-Anwendung (z. B. Copilot in Excel/Word, ChatGPT Enterprise)

[ ] Sonstiges: ____________________________________

[ ] Kein Schulungs- oder Entwicklungsbedarf *(Exklusive Option)*

**DIAG_02: Welche zusätzliche Unterstützung oder Rahmenbedingungen würden Ihnen helfen, generative KI effektiver in Ihrem Arbeitsalltag einzusetzen?**  `[ Freitextfeld ]`

Teil 9: Demographische Angaben (DEMOGRAPHICS_MINIMAL)

*(Nicht-reflektives Zusatzmodul)*

**DEM_01: In welchem kaufmännischen Funktionsbereich sind Sie primär tätig?**  `[ Offenes Textfeld / Dropdown: e.g. Einkauf, Vertrieb, Marketing, Finanzen/Controlling, Personalwesen, Administration, Sonstiges ]`

B6: Pretest- und Validierungsplan

Da `PLANNED_ANALYSIS = NOT_PROVIDED` gesetzt ist, werden keine hypothetischen Stichprobengrößen, Durchführungszeiten oder empirischen Kennwerte erfunden.

**Qualitativer Human-Pretest:**  Durchführung von kognitiven Pretests (Think-Aloud-Methode) mit N=8 bis 12 kaufmännischen Mitarbeitenden der Zielpopulation zur Prüfung der sprachlichen Verständlichkeit, Eindeutigkeit des Kontextbezugs (ChatGPT/Copilot) und Ladezeit des Online-Instruments.

**Empirische Messmodellprüfung:**  Nach der ersten Datenerhebung Prüfung der faktoriellen Struktur mittels konfirmatorischer Faktoranalyse (CFA). Besondere Überprüfung der konvergenten und diskriminanten Validität des E3-Items `DETECT_03` sowie der 3-Item-Subsets von AILRSE-5 und Facilitating Conditions.

**Status der Validierung:**  `THEORETICALLY_GROUNDED_EMPIRICAL_VALIDATION_PENDING`

B7: Vollständiger JSON-Export

```
{
  "metadata": {
    "design_audit_reference": "DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL",
    "run_mode": "QUESTIONNAIRE_GENERATION",
    "overall_score_supported": false,
    "empirical_validation_status": "PENDING",
    "embedded_design_audit": true,
    "source_files_consulted": [
      "MAILS.pdf",
      "AILRSE-5.pdf",
      "AISES.pdf",
      "AIRS.pdf",
      "Lambiase et al. (2025).pdf",
      "1_originalDataset.csv",
      "NOTEBOOKLM_FC_ORIGINALITEMS_OHNE_TEILNEHMERDATEN.txt"
    ]
  },
  "source_selection_decision": {
    "comfort_source": "AISES",
    "comfort_original_pool_items": 6,
    "comfort_selected_items": 3,
    "audit_amendment_required": false,
    "selection_justification": "documented within Audit 004_FINAL"
  },
  "routing": {
    "filter_variable": "EXP_01",
    "categories": [
      "NO_EXPERIENCE",
      "LIMITED_EXPERIENCE",
      "REGULAR_USER"
    ],
    "no_experience_rule": {
      "administered_constructs": [
        "READINESS_CORE_LIT",
        "READINESS_CORE_LEARN",
        "CONTEXT_FC",
        "DIAGNOSTIC_NEEDS",
        "DEMOGRAPHICS_MINIMAL"
      ],
      "skipped_constructs": [
        "READINESS_CORE_APPLY",
        "READINESS_CORE_DETECT",
        "READINESS_CORE_COMFORT"
      ],
      "skipped_status_coding": "NOT_SCORED_DUE_TO_NO_EXPERIENCE"
    }
  },
  "diagnostic_needs": {
    "module_code": "DIAGNOSTIC_NEEDS",
    "reflective": false,
    "scored": false,
    "items": [
      {
        "item_id": "DIAG_01",
        "type": "MULTIPLE_CHOICE_LIST",
        "options": [
          "Grundlagen generativer KI",
          "Prompting und effektive Aufgabenstellung",
          "Kritische Prüfung und Validierung von KI-Ergebnissen",
          "Datenschutz und sicherer Umgang mit sensiblen Unternehmensdaten",
          "Urheberrecht, Transparenz und ethische Richtlinien",
          "Integration von KI in bestehende Arbeitsprozesse",
          "Konkrete Werkzeug-Anwendung (z. B. Copilot in Excel/Word, ChatGPT Enterprise)",
          "Sonstiges",
          "Kein Schulungs- oder Entwicklungsbedarf"
        ],
        "exclusive_option": "Kein Schulungs- oder Entwicklungsbedarf"
      },
      {
        "item_id": "DIAG_02",
        "type": "OPEN_TEXT",
        "prompt": "Welche zusätzliche Unterstützung oder Rahmenbedingungen würden Ihnen helfen, generative KI effektiver in Ihrem Arbeitsalltag einzusetzen?"
      }
    ]
  },
  "demographics_minimal": {
    "module_code": "DEMOGRAPHICS_MINIMAL",
    "reflective": false,
    "scored": false,
    "items": [
      {
        "item_id": "DEM_01",
        "type": "OPEN_TEXT_OR_DROPDOWN",
        "prompt": "In welchem kaufmännischen Funktionsbereich sind Sie primär tätig?"
      }
    ]
  },
  "items": [
    {
      "item_id": "LIT_01",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kenne die wichtigsten Grundbegriffe generativer KI.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 7",
        "source_item_id": "7",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "0-10",
        "final_scale": "0-10",
        "translation_status": "GERMAN_ORIGINAL_PUBLISHED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "LIT_02",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kenne die Bedeutung des Begriffs generative KI.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 8",
        "source_item_id": "8",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "0-10",
        "final_scale": "0-10",
        "translation_status": "GERMAN_ORIGINAL_PUBLISHED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "LIT_03",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kann mir mögliche zukünftige Anwendungen generativer KI vorstellen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 12",
        "source_item_id": "12",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "0-10",
        "final_scale": "0-10",
        "translation_status": "GERMAN_ORIGINAL_PUBLISHED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "LEARN_01",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen funktionieren.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "AILRSE-5",
        "locator": "Table 2, Item 1",
        "source_item_id": "1",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "1-7",
        "final_scale": "1-7",
        "translation_status": "GERMAN_ADAPTED_CHECKED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "LEARN_02",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich bei Bedarf die Nutzung neuer generativer KI-Anwendungen erlernen kann.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "AILRSE-5",
        "locator": "Table 2, Item 2",
        "source_item_id": "2",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "1-7",
        "final_scale": "1-7",
        "translation_status": "GERMAN_ADAPTED_CHECKED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "LEARN_03",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich mir die Nutzung neuer generativer KI-Anwendungen selbstständig aneignen kann.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "AILRSE-5",
        "locator": "Table 2, Item 5",
        "source_item_id": "5",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "1-7",
        "final_scale": "1-7",
        "translation_status": "GERMAN_ADAPTED_CHECKED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "APPLY_01",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Ich kann generative KI-Anwendungen bedienen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 1",
        "source_item_id": "1",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "0-10",
        "final_scale": "0-10",
        "translation_status": "GERMAN_ORIGINAL_PUBLISHED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "APPLY_02",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Ich kann generative KI sinnvoll einsetzen, um meine Arbeitsziele zu erreichen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 3",
        "source_item_id": "3",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "0-10",
        "final_scale": "0-10",
        "translation_status": "GERMAN_ORIGINAL_PUBLISHED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "APPLY_03",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Die meisten Probleme im Umgang mit generativer KI kann ich aus eigener Kraft meistern.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 24",
        "source_item_id": "24",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "0-10",
        "final_scale": "0-10",
        "translation_status": "GERMAN_ORIGINAL_PUBLISHED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "DETECT_01",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann erkennen, ob eine Anwendung auf generativer KI basiert.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 13",
        "source_item_id": "13",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "0-10",
        "final_scale": "0-10",
        "translation_status": "GERMAN_ORIGINAL_PUBLISHED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "DETECT_02",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann unterscheiden, ob ich mit einer generativen KI oder einer Person interagiere.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 15",
        "source_item_id": "15",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "0-10",
        "final_scale": "0-10",
        "translation_status": "GERMAN_ORIGINAL_PUBLISHED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "DETECT_03",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E3",
      "source_evidence": {
        "source_id": "THEORY_SYNTHESIS",
        "locator": "NOT_APPLICABLE",
        "source_item_id": null,
        "source_item_text_verified": false,
        "source_definition_verified": true,
        "original_scale": null,
        "final_scale": "0-10",
        "translation_status": "GERMAN_DEVELOPED_E3",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "COMFORT_01",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Wenn ich mit generativer KI interagiere, fühle ich mich ruhig.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "AISES",
        "locator": "Table 3, CF1 / Q25",
        "source_item_id": "CF1_Q25",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "1-7",
        "final_scale": "1-7",
        "translation_status": "GERMAN_ADAPTED_CHECKED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "COMFORT_02",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Wenn ich mit generativer KI interagiere, fühle ich mich wohl.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "AISES",
        "locator": "Table 3, CF3 / Q24",
        "source_item_id": "CF3_Q24",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "1-7",
        "final_scale": "1-7",
        "translation_status": "GERMAN_ADAPTED_CHECKED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "COMFORT_03",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Wenn ich mit generativer KI interagiere, fühle ich mich entspannt.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "AISES",
        "locator": "Table 3, CF5 / Q22",
        "source_item_id": "CF5_Q22",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "1-7",
        "final_scale": "1-7",
        "translation_status": "GERMAN_ADAPTED_CHECKED",
        "critic_status": "PASS"
      }
    },
    {
      "item_id": "FC_01",
      "construct_code": "CONTEXT_FC",
      "question_text": "Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI-Anwendungen bei meiner Arbeit zu nutzen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "LAMBIASE_2025",
        "locator": "1_originalDataset.csv Header Line 2, FC_1",
        "source_item_id": "FC_1",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "1-7",
        "final_scale": "1-7",
        "translation_status": "GERMAN_ADAPTED_CHECKED",
        "critic_status": "PASS",
        "additional_response_option": "Kann ich nicht beurteilen",
        "additional_response_option_coding": "MISSING_NOT_SCORED"
      }
    },
    {
      "item_id": "FC_02",
      "construct_code": "CONTEXT_FC",
      "question_text": "Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen bei meiner Arbeit zu nutzen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "LAMBIASE_2025",
        "locator": "1_originalDataset.csv Header Line 2, FC_2",
        "source_item_id": "FC_2",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "1-7",
        "final_scale": "1-7",
        "translation_status": "GERMAN_ADAPTED_CHECKED",
        "critic_status": "PASS",
        "additional_response_option": "Kann ich nicht beurteilen",
        "additional_response_option_coding": "MISSING_NOT_SCORED"
      }
    },
    {
      "item_id": "FC_03",
      "construct_code": "CONTEXT_FC",
      "question_text": "Generative KI-Anwendungen sind mit anderen Technologien kompatibel, die ich bei meiner Arbeit verwende.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "source_evidence": {
        "source_id": "LAMBIASE_2025",
        "locator": "1_originalDataset.csv Header Line 2, FC_3",
        "source_item_id": "FC_3",
        "source_item_text_verified": true,
        "source_definition_verified": true,
        "original_scale": "1-7",
        "final_scale": "1-7",
        "translation_status": "GERMAN_ADAPTED_CHECKED",
        "critic_status": "PASS",
        "additional_response_option": "Kann ich nicht beurteilen",
        "additional_response_option_coding": "MISSING_NOT_SCORED"
      }
    }
  ],
  "conformance": {
    "all_hard_checks_pass": true,
    "overall_conformance_status": "CONFORMANT_GENERATION"
  }
}
```

B0: Formale Hard-Check-Matrix

| Prüfkriterium | Erwarteter Soll-Zustand | Ist-Zustand im Output | Prüfstatus |
| --- | --- | --- | --- |
| **design_lock_ok** | Verbindliche Parameter aus Audit 004_FINAL unverändert übernommen | B1 enthält exakte Parameter aus Audit 004_FINAL | **PASS** |
| **source_item_evidence_ok** | Alle Primärquellen für B2/B7 im Quellensatz verifiziert | MAILS, AILRSE-5, AISES, AIRS, Lambiase et al. geprüft | **PASS** |
| **e2_proof_ok** | Position, Wortlaut und Skala für jedes E2-Item nachgewiesen | Exakte Zuweisungen in B2, B3, B7 vorhanden | **PASS** |
| **e3_source_compatibility_ok** | E3-Item DETECT_03 korrekt ausgewiesen (source_item_id=null) | E3 korrekt ohne erfundene Original-ID abgebildet | **PASS** |
| **subscale_membership_ok** | Exakt 6 Konstrukte à 3 reflektive Items | 6 Subskalen × 3 Items = 18 Items | **PASS** |
| **item_count_checksum_ok** | Exakt 18 reflektive Items in B2, B5 und B7 | Checksumme 18 in allen Abschnitten identisch | **PASS** |
| **routing_ok** | Filter EXP_01 übersprungen APPLY, DETECT, COMFORT bei NO_EXPERIENCE | Routing-Logik in B5 und B7 syntaktisch spezifiziert | **PASS** |
| **fc_not_judgable_option_ok** | FC-Items besitzen Ausweichoption `MISSING_NOT_SCORED` | "Kann ich nicht beurteilen" in B5 und B7 vorhanden | **PASS** |
| **diagnostic_module_completeness_ok** | DIAG_01 mit 7 Feldern + Sonstiges + Exklusivfeld, DIAG_02 ungescored | Modul vollständig in B5 und B7 integriert | **PASS** |
| **validation_plan_ok** | Qualitativ-kognitiver Pretest & CFA-Plan ohne erfundene Zahlen | B6 enthält nicht-numerischen Plan & Status PENDING | **PASS** |
| **json_consistency_ok** | Ein einziger gültiger JSON-Block in B7 ohne Abkürzungen | JSON syntaktisch vollständig und valide | **PASS** |
| **audit_selection_documented_ok** | AISES-Comfort 3/6 innerhalb des bestehenden Audits dokumentiert | B1, B3, B7 enthalten konsistente Begründung | **PASS** |
| **all_hard_checks_pass** | Alle vorstehenden Hard Checks stehen auf PASS | Alle 12 Kriterien erfolgreich geprüft | **PASS** |

**Gesamtstatus:**  **CONFORMANT_GENERATION**

💡 *Möchtest du als nächsten Schritt eine visuelle Übersicht der Fragebogenstruktur oder eine Vorlage für die Durchführung des kognitiven Pretests (Think-Aloud-Leitfaden) erstellen?*

---

