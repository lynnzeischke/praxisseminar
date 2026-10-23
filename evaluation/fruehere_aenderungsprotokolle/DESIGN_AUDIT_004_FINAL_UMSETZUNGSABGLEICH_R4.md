# Quellenwahl-Protokoll zu DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL

**Grundlage:** Nutzerseitig bereitgestellter Original-Design-Audit `02_DESIGN_AUDIT_FINAL_2026_KMU_GENAI_DIAG(1).md` (Status FINAL).

## Entschiedene Auslegung

- A8 führt für READINESS_CORE_COMFORT ausdrücklich **AIRS und AISES** als Primärquellen. A9 beschreibt AISES mit **siebenstufiger** Originalskala und dem Faktor Comfort. Damit ist die dokumentierte Auswahl der AISES-Comfort-Facette im freigegebenen Quellenraum **möglich, ohne automatisch eine Änderung der ursprünglichen Architektur** zu behaupten.
- Zuvor definierte Masterprompt-spezifische AIRS-Q9/Q8/Q18-Hardlocks sind zusätzliche Operationalisierungsregeln aus späteren Testständen, nicht wörtlich im hochgeladenen Design Audit als einzige zulässige Comfort-Quelle festgelegt. Sie haben gegenüber Audit 004_FINAL keine Priorität.
- Die Auswahl AISES CF1/Q25, CF3/Q24, CF5/Q22 ist ein **spezifisches Drei-Item-Subset aus sechs Comfort-Originalitems**. Semantischer GenAI-Kontexttransfer, Redundanz und verkürzter Faktor müssen offen dokumentiert und empirisch nachgeprüft werden. Die bisherige im alten Masterprompt geforderte formale Freigabe eines separaten Nachtrags A1 ist **nicht allein wegen dieser Quellenwahl notwendig**.
- Die MAILS-Quelle weist für die Originalpositionen 1/3/7/8/12/13/15/24 die in R4 genannten Kompetenzthemen nach. Dies sind **Positionsnummern**, keine neu erfundenen Variablennamen. Neue E2-Items müssen gleichwohl die tatsächliche Originalsemantik einhalten.
- Bei neuen Masterprompt-Iterationen bleibt der historisch im Audit genannte operative Masterprompt V2.1 als dokumentierte historische Basis erhalten; die R4-Version ist ein weiterentwickeltes Operationalisierungsartefakt und **keine rückwirkende Änderung** des freigegebenen Audits.

## Unverändert

- 6 × 3 = 18 reflektive Items; fünf individuelle Kernskalen + CONTEXT_FC.
- DIAGNOSTIC_NEEDS separat; minimale Funktionsbereichsangabe.
- Kein TTF ohne TASK_CONTEXT, keine Behavioral Intention, keine erfundene Unternehmenserklärung, kein unvalidierter Gesamt-Readiness-Score.
- E2-Originalquellenbeweis, E3-Theoriebeleg, kognitiver Human-Pretest und empirische Validierung bleiben Pflicht.

## Noch zu verifizieren vor endgültiger Freigabe

- Tatsächlich in NotebookLM verfügbare Volltexte für AISES, AILRSE-5, Lambiase et al. und die E3-konkrete Bewertungsgrundlage.
- E2-Itembedeutungen, Skalenanker und GenAI-Transfer für die 18 vorgeschlagenen Itemkandidaten.
- B2/B5/B7-Inhaltsgleichheit sowie tatsächliche JSON-Syntax, nicht nur Modell-PASS.

**Status:** R4 ist ein Audit-ausgerichteter Masterprompt-**Testkandidat**. Ein erfolgreich generierter Fragebogen bleibt ohne echten Human-Pretest und empirische Prüfung ein wissenschaftlich begründeter, noch nicht validierter Entwurf.
