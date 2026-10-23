# Reproduzierbare technische Prüfergebnisse

Stand: 19.10.2026. Aufruf jeweils mit `python tools/check_output.py notebooklm_tests/NotebookLM_Ausgabe_<VERSION>.txt`. Der enthaltene Python-Code prüft nur **JSON-Struktur**, nicht Quellenvalidität, linguistische Item-Äquivalenz oder psychometrische Güte.

| NotebookLM-Lauf | Prüfergebnis | Grund / Interpretation |
|---|---|---|
| R5 | **FAIL** | Mindestens eine vollständige Routinggruppe fehlt im JSON unter der erwarteten Struktur. Dies deckt sich mit dem dokumentierten R5-Fehler. |
| R6 | **PASS (nur technisch)** | JSON parsebar; 18 Items; sechs Konstrukte; erwartetes Routing, FC-Missing-Regeln und E3-Codierung vorhanden. Wissenschaftliche Einschränkungen blieben bestehen. |
| R6.1 | **PASS (nur technisch)** | Dieselben technischen Grundbedingungen erfüllt. Die E3-Quellenbegründung wurde zusätzlich *inhaltlich* geprüft, jedoch **nicht** durch dieses Skript empirisch validiert. |

## Tatsächliche Konsolenausgaben

### R5 (Exit-Code 1)

```text
Traceback (most recent call last):
AssertionError: Routinggruppe fehlt: NO_EXPERIENCE
```

### R6 (Exit-Code 0)

```text
PASS: JSON parsebar; 18 Items; sechs 3er-Konstrukte; Routing/E3/FC und kein Gesamtscore. Datei: /mnt/data/Employee_AI_Readiness_GitHub_Projekt/notebooklm_tests/NotebookLM_Ausgabe_R6.txt
HINWEIS: Kein Beweis für korrekte Quellen, Itemvalidität, kognitiven Pretest oder wissenschaftliche Freigabe.
```

### R6_1 (Exit-Code 0)

```text
PASS: JSON parsebar; 18 Items; sechs 3er-Konstrukte; Routing/E3/FC und kein Gesamtscore. Datei: /mnt/data/Employee_AI_Readiness_GitHub_Projekt/notebooklm_tests/NotebookLM_Ausgabe_R6_1.txt
HINWEIS: Kein Beweis für korrekte Quellen, Itemvalidität, kognitiven Pretest oder wissenschaftliche Freigabe.
```

## Grenzen

Ein technisch bestandener Lauf darf keine pauschale Aussage `CONFORMANT_GENERATION` im wissenschaftlichen Sinn begründen. Die im Repository enthaltenen Zeitpunkte der NotebookLM-Dateien dienen der Dateizuordnung, nicht der Rekonstruktion sekundengenauer Original-Chatzeitstempel. Für Feldfreigabe sind reale kognitive Pretests und eine projektspezifische Validierungsplanung notwendig.
