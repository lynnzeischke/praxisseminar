# V3.5-R6 Änderungsprotokoll und Regression

**Ausgangsbasis:** V3.5-R5 INTEGRATED-AUDIT AUTORUN. **Status:** TEST_CANDIDATE. Der original freigegebene Design Audit ist **byte- und SHA-256-identisch** eingebettet. Keine Änderung der Quellenentscheidung AISES, der 18 Kandidaten/Item-IDs, Konstrukte, Skalen oder des 8-Minuten-Zielbudgets.

## Gezielte Korrekturen

1. **Routing:** Die Teilnehmeroptionen für `EXP_01` und der Weg für `NO_EXPERIENCE` sind verbindlich: Teil 2 und Teil 3, anschließend Teil 7–9; Teile 4–6 entfallen. Vollständige JSON-Pfade für alle drei Erfahrungsgruppen mit Include-/Skip-Arrays.
2. **Validierung:** B6 als wörtlich fixiertes, nichtnumerisches Fallback; keine erfundenen Pretest-Zahlen, gewählten quantitativen Verfahren oder Validitätsansprüche. B4 bleibt eine Simulation.
3. **Traceability:** B2 enthält verpflichtend den vollen finalen deutschen Itemwortlaut und eine konkrete Originalquellenposition. Exakte Übereinstimmung B2/B5/B7 ist Hard-Gate.
4. **E2/E3 und Wording:** GenAI-spezifische MAILS-Versionen sind Adaptationen, nicht `GERMAN_ORIGINAL_PUBLISHED`; Übersetzungs-/Adaptationsstatus von tatsächlich nachgewiesenem Originalwortlaut und empirischer Äquivalenz getrennt. E3-ID bleibt `null`.
5. **Antwortdarstellung:** Keine leeren Backticks nach B5-Items; Fähigkeits- und Zustimmungsskalen unterscheidbar; FC-Ausweichoptionen und Diagnostik-Sonstiges/Kein Bedarf getrennt.
6. **Fail-closed:** Zusätzliche Checks `traceability_consistency_ok`, `adaptation_labeling_ok`, `participant_rendering_ok`; ein nicht belegter PASS ist kein Nachweis.

## Regressions-Testfälle am NotebookLM-Ergebnis

- Wenn B5 `NO_EXPERIENCE → Teil 2 → Teil 7` schreibt, **FAIL**.
- Wenn JSON `LIMITED_EXPERIENCE` oder `REGULAR_USER` nur im Kategorienarray nennt, **FAIL**.
- Wenn B4/B6 eine Pretest-Fallzahl wie `8–12` oder `5–10` empfiehlt oder CFA als beschlossen bezeichnet, **FAIL**.
- Wenn B2 einen der 18 endgültigen Fragewortlaute nicht vollständig enthält, **FAIL**.
- Wenn ein auf generative KI angepasstes MAILS-Item `GERMAN_ORIGINAL_PUBLISHED` trägt, **FAIL**.
- Wenn B5 am Ende eines Items leere Backticks enthält, **FAIL**.
- Wenn B7 nicht genau 18 reflektive Items, zwei DIAG-Items und DEM_01 enthält, **FAIL**.
- Wenn ein Gate nicht belegt ist und trotzdem `CONFORMANT_GENERATION` gemeldet wird, **FAIL**.

**Ausführungsbefehl:** `Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.`

**Hinweis:** Es sind lokale **statische** Prüfungen des Prompts erfolgt (Auditidentität, Abschnittsstruktur, 18 IDs und Routing-JSON-Syntax). Keine tatsächliche NotebookLM-Ausführung und keine empirische Fragebogenvalidierung.
