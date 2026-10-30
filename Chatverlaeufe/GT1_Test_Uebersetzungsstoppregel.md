# GT1-Test: Übersetzungs-Stoppregel

Quelle: https://notebook.google.com/notebook/1b5b496e-bbb9-4f50-a3ec-65328261ec3d
(dasselbe Notebook wie `Runmode_18_NOTEBOOKLM.md`, Fortsetzung desselben
Chats)
Exportiert/übernommen: 23.10.2026

**Nachtrag (23.10.2026):** Die Nutzerin hat den vollständigen Chatverlauf
zur Verfügung gestellt, darin bestätigt sich, dass dieser Testlauf im
selben NotebookLM-Chat erfolgte, in dem am Montag, 19.10.2026, zuvor der
vollständige `RUN_MODE = QUESTIONNAIRE_GENERATION`-Lauf (B0–B7, 18
reflektive Items, `CONFORMANT_GENERATION`) ausgeführt und bereits als
`Runmode_18_NOTEBOOKLM.md` archiviert wurde. Der exakte Prompt-Wortlaut
ist unten ergänzt.

---

## Frage

```
Ich teste gezielt deine Übersetzungs- und Stopp-Logik, nicht die vollständige Fragebogengenerierung. Wähle aus deinen geladenen Quellen (MAILS, AILRSE-5, AISES, AIRS, Lambiase FC) zwei Beispielitems aus:

(A) ein fremdsprachiges Originalitem, das sich eindeutig und ohne Bedeutungsverlust ins Deutsche übertragen lässt, aber noch keine validierte deutsche Fassung hat,
(B) ein fremdsprachiges Originalitem, dessen Bedeutungsgehalt sich im Zielkontext (kaufmännische Mitarbeitende, generative KI am Arbeitsplatz) nicht hinreichend eindeutig ins Deutsche übertragen lässt.

Gib für beide Fälle an: Originaltext, Quelle, deine Übersetzung oder STOPP-Entscheidung, evidence_class, translation_status, und eine kurze Begründung.
```

---

## Antwort

Hier ist die Gegenüberstellung der Übersetzungs- und Stopp-Logik anhand von zwei repräsentativen Originalitems aus den geladenen wissenschaftlichen Primärquellen.

Fall (A): Validierbare Übersetzung eines fremdsprachigen Originalitems (E2)

* Originaltext: „I'm confident in my ability to learn how to use new AI technologies if necessary."
* Quelle: Oksanen et al. (2026), AILRSE-5 (AI Learning Readiness Self-Efficacy Scale), Table 2 (Item 2)
* Übersetzung: „Ich bin zuversichtlich, dass ich bei Bedarf die Nutzung neuer generativer KI-Anwendungen erlernen kann."
* evidence_class: `E2` (Verifiziertes Originalitem mit sprachlicher und kontextbezogener Adaption)
* translation_status: `GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED` (unter dem Äquivalenzstatus `NOT_EMPIRICALLY_ESTABLISHED` / `NEEDS_EQUIVALENCE_CHECK`)
* Begründung: Der psychometrische Gehalt der Lern-Selbstwirksamkeitserwartung lässt sich präzise und ohne Bedeutungsverlust ins Deutsche übertragen. Die leichte Spezialisierung von „new AI technologies" auf „neue generative KI-Anwendungen" stellt den Bezug zum kaufmännischen Bürokontext her, ohne das gemessene Kompetenzkonstrukt zu verfälschen. Da für diese konkrete deutsche Zielformulierung jedoch noch keine publizierte empirische Invarianz- oder Äquivalenzprüfung vorliegt, wird das Item transparent als `E2` deklariert und erfordert vor dem Feldeinsatz einen kognitiven Pretest.

Fall (B): STOPP-Entscheidung bei Konstrukt- und Messobjektverschiebung

* Originaltext: „I am not afraid of humanoid AI technologies/products (robots)."
* Quelle: Wang et al. (2026), AIRS (Artificial Intelligence Readiness Scale), Item Q18 / COM3
* Übersetzung / Entscheidung: STOPP-ENTSCHEIDUNG (Ablehnung der E2-Übertragung/Adaption für das Messziel „GenAI am kaufmännischen Arbeitsplatz").
* evidence_class: `E2_NOT_VERIFIED` / `REJECTED`
* translation_status: `STOPPED_DUE_TO_CONSTRUCT_MISMATCH`
* Begründung: Das Originalitem erhebt die affektive Haltung gegenüber humanoiden physischen Robotern (`robots`). Eine Übertragung auf den Zielkontext (kaufmännische Mitarbeitende, die mit sprachbasierten GenAI-Tools wie ChatGPT Enterprise oder Microsoft Copilot interagieren) würde das Messobjekt grundlegend verändern. Das schlichte Ersetzen von „robots" durch „generative KI" unter Beibehaltung des behaupteten E2-Quellenbelegs würde eine falsche Quellenequivalenz vortäuschen, da die publizierten Gütekennwerte einer Roboter-Angst-Skala psychometrisch nicht auf Bildschirm-Text-Anwendungen übertragbar sind. Hier greift die wissenschaftliche Stopp-Logik: Das Item wird verworfen und nicht fälschlich als E2-Comfort-Item zugelassen.

---

## Prüfbefund (Claude, 23.10.2026)

- **Fall A** entspricht exakt der GT1-A-Erwartung (MASTER_ARTEFAKT V8.4.11): übersetzbares Originalitem → kein Stopp, `E2`, `NEEDS_EQUIVALENCE_CHECK`. **Erfüllt.**
- **Fall B** löst korrekt einen Stopp aus, prüft aber inhaltlich einen anderen Fall als die V8.4.11-Definition von GT1-B (dort: sprachliche Unübersetzbarkeit/Mehrdeutigkeit). Das hier verwendete Beispiel ist eine **Konstrukt- bzw. Messobjektverschiebung** (physischer Roboter vs. Text-GenAI), kein Übersetzungsproblem im engeren Sinn. Die Stopp-Logik funktioniert korrekt, testet aber nicht wortgetreu die „Übersetzungs-Stoppregel" nach GT1-B.
- Quellenprüfung: Beide zitierten Originalitems (AILRSE-5 Table 2 Item 2; AIRS Q18/COM3) sind in den im Projekt vorliegenden Primärquellen mit exaktem Wortlaut verifiziert.
- Ergänzender Testlauf für einen wortgetreuen GT1-B-Fall (sprachliche Übersetzungsmehrdeutigkeit statt Konstruktverschiebung) folgt in `GT1B_Test_Uebersetzungsmehrdeutigkeit.md`.
