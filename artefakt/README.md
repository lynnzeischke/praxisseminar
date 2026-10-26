# Leitlinienartefakt

## Aktuelle Fassung R6.2

[Masterprompt V3.5-R6.2](MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_2_NOTEBOOKLM.txt) · **TEST_CANDIDATE** · Artefaktstand 24.10.2026.

Die Datei enthält das Projektprofil, das Kandidatenregister mit 18 Items, Herkunfts-/Beleg-/Freigaberegeln, die Ausgabestruktur und den unveränderten Original-Design-Audit. Als wissenschaftliche Quelle ist sie Governance und ersetzt keine Originalpublikation.

- [Vollständiger Produktionstest vom 26.10.2026](../evaluation/R6_2_Vollproduktion_2026-10-26/README.md): JSON-Struktur-PASS, aber doppelte B1–B5-Folge und falsche AISES-Wortlaut-Locatoren. Keine pauschale Konformitätsfreigabe.
- [Einzelitemtests vom 24.10.2026](../evaluation/R6_2_PRUEFBERICHT.md): 22/24 Kriterien, angeleiteter Transfer 4/4; verbleibende Quellenfehler.
- [FC-Originalitem-Auszug ohne Teilnehmerdaten](NOTEBOOKLM_FC_ORIGINALITEMS_OHNE_TEILNEHMERDATEN.txt).

## Ausführung

Nur **eine** Promptversion in einem neuen Notebook aktivieren. Benötigte wissenschaftliche Originale und ergänzende Quellen stehen in Abschnitt 4a der Masterdatei. Keine personenbezogenen Befragtenantworten werden benötigt. Start:

```text
Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.
```

Die tatsächliche Antwort sichern und extern prüfen. Das Modell darf nicht durch seine eigene Konformitätsmeldung als zuverlässig gelten. Änderungen am Prompt erfordern eine neue Version und eine gesonderte Nachprüfung.

## Historische Referenzen

[R6.1](MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_1_NOTEBOOKLM.txt) bleibt Referenz der früheren vollständigen Demonstration. [Ältere Versionen](../modelle_historisch/) und die [Modellhistorie](../MODELLHISTORIE.md) dokumentieren Entwicklungsstände. Für die aktuelle Bewertung gelten die [Evaluationsberichte](../evaluation/README.md).
