# Design-Audit-Nachtrag A1 — Quellen- und Kontextäquivalenz

**Status: ENTSCHEIDUNGSVORLAGE – NOCH NICHT FREIGEGEBEN.**

Referenz des ursprünglichen Audits: `DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL`.
Vorgeschlagener Nachtrag: `DESIGN_AUDIT_ADDENDUM_004_A1_PROPOSED`.

## Warum eine dokumentierte Änderung nötig ist

Der bisherige Originalquellen-Lock für AIRS Comfort enthält COM3/Q18 über **humanoide KI beziehungsweise Roboter**. Eine Umformulierung zu ChatGPT Enterprise oder Microsoft Copilot ändert das Messobjekt. Auch COM1/Q9 enthält den sozialen Bezugsrahmen „vor anderen Personen“, und COM2/Q8 bezieht sich auf Gesundheits- oder Sicherheitsbedenken; diese Inhalte dürfen nicht als allgemeines Wohlbefinden oder absolute Risikofreiheit ausgegeben werden. Keines dieser drei AIRS-Items darf unter veränderter Bedeutung als semantisch äquivalentes E2-Item gelten.

Der wissenschaftlich passendere Alternativpool für **affektiven Komfort bei KI-Interaktion** ist die Comfort-Subskala der AISES von Wang & Chuang (2024), DOI `10.1007/s10639-023-12015-w`:

- `CF1/Q25`: innere Ruhe während KI-Interaktion;
- `CF3/Q24`: Wohlbefinden während KI-Interaktion;
- `CF5/Q22`: Entspanntheit während KI-Interaktion.

Diese drei Items sind vor der endgültigen E2-Freigabe **an der Primärpublikation** anhand von Itemtext, Faktorzugehörigkeit und Skala zu prüfen. Die vorgeschlagene Originalskala ist 1–7. Die Übertragung auf generative KI bleibt eine Kontextadaption und benötigt einen kognitiven Pretest.

## Änderungsumfang und Begründung

1. `READINESS_CORE_COMFORT`: Ersatz des AIRS-COM1/COM2/COM3-Pools durch AISES `CF1/Q25`, `CF3/Q24`, `CF5/Q22`; Skala von **1–5 auf 1–7**. Andere Konstrukte und die Architektur **6 × 3 = 18 reflektive Items** bleiben erhalten.
2. `READINESS_CORE_LIT`: SOURCE-PROOF-orientierter MAILS-Pool 7/8/12; item 12 erfasst Vorstellung zukünftiger AI-Anwendungen. Dies ist eine dokumentierte inhaltliche Auswahländerung gegenüber früheren Varianten und muss auf Konstruktdeckung geprüft werden.
3. `READINESS_CORE_APPLY`: MAILS Positionen 1/3/24 statt erfundener `Use_AI_2`-Promptidee; Prompting bleibt in `DIAG_01` ein Schulungsbereich und ist **kein** künstlich als MAILS-E2 etikettiertes Originalitem.
4. `READINESS_CORE_DETECT`: MAILS 13/15 betreffen KI-Erkennung; `DETECT_03` bleibt E3 und darf nur bei nachweisbar kompatibler aktiver Theoriegrundlage so deklariert werden. MAILS allein darf nicht als Beleg für eine ursprünglich getestete Faktenprüfungsfrage ausgegeben werden.
5. `READINESS_CORE_LEARN`: AILRSE-5 Teilmenge 1/2/5; genaue Formulierung von Item 5 ist bei der Primärquelle zu prüfen.

## Entscheidung und Governance

Ein vollständiger neuer Fragebogenlauf darf die **vorgeschlagene** Architektur prototypisch demonstrieren. Solange der Nachtrag A1 nicht fachlich freigegeben und der Originalquellennachweis nicht abgeschlossen wurde, lautet der Freigabestatus **`DESIGN_AMENDMENT_REVIEW_REQUIRED`** bzw. **`REVISION_REQUIRED`**, nicht `CONFORMANT_GENERATION`.

Vor Freigabe dokumentieren: verantwortliche prüfende Person, Entscheidungsdatum, begründete Freigabe/Ablehnung, Quellenbelege, Risiko des 3-Item-Comfort-Subsets, Auswirkungen der Skalenänderung und Pretestplan. Erst danach darf der aktuelle Nachtrag als verbindliche Design-Basis markiert werden. **Niemals den ursprünglichen Audit `004_FINAL` stillschweigend überschreiben.**

## Originalquellen zur Nachprüfung

- MAILS, offizielle Würzburger Seite mit Originalitems: https://www.mcm.uni-wuerzburg.de/mp/personen/pd-dr-habil-astrid-carolus/mails/
- Carolus et al. (2023): https://doi.org/10.1016/j.chbah.2023.100014
- AISES, Wang & Chuang (2024): https://doi.org/10.1007/s10639-023-12015-w
- AILRSE-5, Oksanen et al. (2026): https://doi.org/10.1016/j.chbah.2026.100251
- AIRS, Wang et al. (2026): https://doi.org/10.1016/j.ijme.2026.101429
