# Vollständiger R6.2 Test vom 26 Oktober 2026

Ein neuer vollständiger NotebookLM-Lauf mit dem unveränderten R6.2 und zwölf ausgewählten Quellen. [Vorabplan](Vorabplan.json), [Prüfbericht](Pruefbericht.md), [Originalseiteninhalt](Seiteninhalt_original.txt), [DOM-Sicherung](DOM_original.txt), [extrahiertes JSON](B7_extrahiert.json) und [automatische Befunde](Automatische_Pruefung.json) sind getrennt abgelegt. Der erzeugte Fragebogen liegt als [Lesefassung](Fragebogen_B5.md) mit unverändertem Wortlaut und geprüften Fundstellen vor.

**Ergebnis:** JSON-Struktur-PASS mit 18 Items; zugleich nicht konforme Gesamtfolge (B1–B5 doppelt) und drei falsche AISES-Wortlaut-Locatoren. R6.2 bleibt TEST_CANDIDATE. Der Lauf ist kein Robustheits- oder psychometrischer Nachweis.

## Nachrechnen

Im Projektstamm:

```bash
python3 evaluation/R6_2_Vollproduktion_2026-10-26/pruefe_gesamtantwort.py
```

Das Skript verwendet ausschließlich die Python-Standardbibliothek und ruft den unveränderten bisherigen Strukturprüfer auf. Es erzeugt den extrahierten JSON-Block und die maschinenlesbaren Befunde erneut. Die semantische Quellenprüfung ist im Prüfbericht erläutert.

Die zwölf Quellen sind mit Dateinamen und SHA256 im Vorabplan dokumentiert. Vollständige wissenschaftliche PDFs werden nicht im Repository vervielfältigt; der Masterprompt und der teilnehmerdatenfreie FC-Auszug liegen unter [artefakt](../../artefakt/). Absolute lokale Quellpfade im Vorabplan dokumentieren die damalige Versuchsanordnung und müssen zum Nachrechnen der gespeicherten Antwort nicht existieren.

[Notebook des Laufs](https://notebook.google.com/notebook/1b551523-3c0c-4508-b13c-d8dbf7238032) – Zugänglichkeit hängt vom Google-Konto ab. [Zur Evaluationsübersicht](../README.md).
