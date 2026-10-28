# Nachprüfung vom 28 Oktober 2026

Vorab festgelegte Zusatzprüfung zu zwei offenen Grenzen der Hausarbeit (Kapitel 5.2 und 6.2). Plan, Aufgaben, Kriterien und Sollantworten wurden **vor dem ersten Lauf** in [Vorabplan.json](Vorabplan.json) gespeichert. Der Git-Commit dieses Ordners belegt den Zeitpunkt.

| Teil | Frage | Läufe | Endpunkte |
|---|---|---|---|
| 1 Wiederholung | Tritt die doppelte B1–B5-Folge des Volllaufs vom 26.10.2026 erneut auf? | W1–W3, je R6.2 vollständig | W-K1 bis W-K4 |
| 2 Neue Fälle | Unterscheiden sich Basis und R6.2 an vorher unbekannten Fällen unter gleichen Bedingungen? | B1–B3 Basis, A1–A3 R6.2 | N1 bis N8 |

## Durchführung

Reihenfolge laut [Protokoll.csv](Protokoll.csv) einhalten. Für **jeden** Lauf:

1. In NotebookLM ein **neues** Notebook anlegen.
2. Quellen hochladen und alle auswählen:
   - **W1–W3:** dieselben zwölf Dateien wie am 26.10.2026 (Liste und SHA256 in [../R6_2_Vollproduktion_2026-10-26/Vorabplan.json](../R6_2_Vollproduktion_2026-10-26/Vorabplan.json)), darunter der unveränderte [R6.2-Masterprompt](../../artefakt/MASTERPROMPT_Employee_AI_Readiness_V3_5_R6_2_NOTEBOOKLM.txt) und der [FC-Auszug](../../artefakt/NOTEBOOKLM_FC_ORIGINALITEMS_OHNE_TEILNEHMERDATEN.txt).
   - **B1–B3:** nur MAILS, AILRSE-5, AISES und AIRS (dieselben Dateien wie am 24.10.2026).
   - **A1–A3:** dieselben vier PDFs plus der unveränderte R6.2-Masterprompt.
3. Die automatische Notebook-Zusammenfassung ignorieren. Als ersten Chatturn genau einfügen:
   - **W1–W3:** `Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.`
   - **B1–B3:** den vollständigen Text aus [aufgabe_basis.txt](aufgabe_basis.txt)
   - **A1–A3:** den vollständigen Text aus [aufgabe_r62.txt](aufgabe_r62.txt)
4. Antwort vollständig abwarten. Keine Rückfragen, keine Folgeturns, kein Neu-Generieren.
5. Die **gesamte sichtbare Antwort** markieren, kopieren und unverändert als `antworten/<Lauf>_Antwort.txt` speichern. Bei langen Antworten bis zum Ende scrollen.
6. In [Protokoll.csv](Protokoll.csv) Notebook-URL, Datum/Uhrzeit, Zahl der ausgewählten Quellen und Besonderheiten (z. B. Abbruch) eintragen.

**Regeln:** Kein Lauf wird wiederholt, verworfen oder korrigiert. Ein Abbruch zählt als Lauf und wird so berichtet. Aufgaben, Quellen und Masterprompt bleiben unverändert.

## Auswertung

- **Teil 1:** `python3 evaluation/Nachpruefung_2026-10-28/auswertung_volllauf.py` im Projektstamm. Das Skript nutzt den unveränderten Strukturprüfer und schreibt `Auswertung_Wiederholung.json`. Es wurde vorab an der Antwort vom 26.10.2026 getestet und reproduziert deren Befunde (doppelte Folge, Strukturcheck PASS, Wortlaut gleich, AISES Table 2).
- **Teil 2:** Kodierung nach N1–N8 in [Kodierbogen_neue_Faelle.csv](Kodierbogen_neue_Faelle.csv), getrennt durch die Autorin und KI-gestützt. Für die Kodierung der Autorin werden die sechs Antworten vorher anonymisiert und gemischt, damit die Bedingung nicht erkennbar ist. Berichtet werden Summen je Bedingung und die Übereinstimmung beider Kodierungen.

## Grenzen

Drei Läufe je Bedingung und vier Volläufe erlauben nur deskriptive Aussagen. Der Backend-Modellstand von NotebookLM ist nicht offengelegt. Die Autorin ist keine unabhängige Zweitbewerterin; die Verblindung mindert, aber beseitigt diese Grenze nicht.
