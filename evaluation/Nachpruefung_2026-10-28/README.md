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
5. Die **gesamte Antwort** unverändert als `antworten/<Lauf>_Antwort.txt` speichern. Durchgeführt am 28.10.2026 durch Claude (Anthropic) in Chrome im Konto der Autorin: Upload, Aufgabentext per Formulareingabe (Zeichenzahl gegen die Aufgabendatei geprüft), Senden; nach Abschluss wurde der `innerText` der Antwortkarte (`.to-user-message-inner-content`) ohne Abtippen als Datei heruntergeladen. Eingeklappte Denkschritte („Thoughts“) und Zitatnummern erscheinen so, wie NotebookLM sie im Text ausgibt. Metadaten je Lauf in `antworten/<Lauf>_Metadaten.json`.
6. In [Protokoll.csv](Protokoll.csv) Notebook-URL, Datum/Uhrzeit, Zahl der ausgewählten Quellen und Besonderheiten (z. B. Abbruch) eintragen.

**Regeln:** Kein Lauf wird wiederholt, verworfen oder korrigiert. Ein Abbruch zählt als Lauf und wird so berichtet. Aufgaben, Quellen und Masterprompt bleiben unverändert.

## Auswertung

- **Teil 1:** `python3 evaluation/Nachpruefung_2026-10-28/auswertung_volllauf.py` im Projektstamm. Das Skript nutzt den unveränderten Strukturprüfer und schreibt `Auswertung_Wiederholung.json`. Es wurde vorab an der Antwort vom 26.10.2026 getestet und reproduziert deren Befunde (doppelte Folge, Strukturcheck PASS, Wortlaut gleich, AISES Table 2). Korrektur nach W1 (28.10.2026, vor Auswertung von W2/W3): Das Skript erkannte AISES-Items nur bei der Quell-ID „AISES“; W1 schreibt „AISES_2024“. Die Erkennung prüft jetzt den Präfix „AISES“. Das Kriterium W-K4 selbst ist unverändert.
- **Teil 2:** Kodierung nach N1–N8 in [Kodierbogen_neue_Faelle.csv](Kodierbogen_neue_Faelle.csv), getrennt durch die Autorin und KI-gestützt. Für die Kodierung der Autorin werden die sechs Antworten vorher anonymisiert und gemischt, damit die Bedingung nicht erkennbar ist. Berichtet werden Summen je Bedingung und die Übereinstimmung beider Kodierungen.

## Ergebnisse (28.10.2026)

Alle neun Läufe wurden in der vorab festgelegten Reihenfolge durchgeführt; kein Lauf wurde wiederholt oder verworfen, kein Lauf brach ab (Details in [Protokoll.csv](Protokoll.csv)).

**Teil 1 – Wiederholung** ([Auswertung_Wiederholung.json](Auswertung_Wiederholung.json))

| Lauf | W-K1 eine Folge | W-K2 Strukturcheck | W-K3 Wortlaut | W-K4 AISES Table 3 | Summe |
|---|---|---|---|---|---|
| W1 | nein (B2–B5 doppelt) | ja | ja | nein („Section 5.4“) | 2/4 |
| W2 | ja | ja | ja | nein („Table 2 / Table 6“) | 3/4 |
| W3 | nein (B2–B5 doppelt) | ja | ja | nein („Table 6“) | 2/4 |

Die doppelte Teilfolge trat in 3 von 4 Volläufen auf (26.10. sowie W1 und W3). Strukturcheck und Wortlaut waren in allen Läufen stabil. Kein Lauf nennt für AISES die Wortlauttabelle Table 3; Table 2 und Table 6 enthalten nur Ladungen (EFA bzw. CFA), Section 5.4 ist der Abschnitt, in dem Table 3 steht.

**Teil 2 – Neue Fälle J–N** (KI-Kodierung, [Auswertung_neue_Faelle_KI.json](Auswertung_neue_Faelle_KI.json))

| Bedingung | Läufe | Summe | Abweichungen |
|---|---|---|---|
| Basis | B1, B2, B3 | 19/24 | N1 in 0/3 (J jedes Mal als deutsches E1-Original freigegeben); N6 in 1/3 |
| R6.2 | A1, A2, A3 | 24/24 | keine |

**Abweichung vom Vorabplan:** Die vorgesehene Kodierung durch die Autorin wurde nicht durchgeführt. Stattdessen kodierte am 29.10.2026 ein unabhängiger Claude-Subagent die anonymisierten, gemischten Antworten aus [verblindet/](verblindet/) (Seed 20261029), ohne Erstkodierung, Zuordnung oder Repository zu sehen. Vorgegeben waren nur Aufgabe, Kriterien, Sollantworten und Auslegungshinweise zu N3, N6 und N8, die aus der Erstkodierung stammen. Beide KI-Kodierungen stimmen in 48 von 48 Entscheidungen überein (Cohens κ = 1,0; [Zweitkodierung_KI_verblindet.json](Zweitkodierung_KI_verblindet.json)). Belegt ist damit die Übereinstimmung unter diesen Bedingungen, weder eine allgemeine Eindeutigkeit der Kriterien noch eine menschliche Reliabilität: Beide Kodierungen stammen aus derselben Modellfamilie und teilen die Auslegungshinweise. Die Verblindung ist zudem unvollständig, weil R6.2-Antworten an Begriffen wie `evidence_class` erkennbar sind.

**Nachprüfung des zentralen Befunds durch die Autorin** ([Pruefung_Fall_J_Autorin.json](Pruefung_Fall_J_Autorin.json)): Am 29.10.2026 beantwortete die Autorin für die sechs gemischten Antworten nur die Frage, ob J als deutsches E1-Original freigegeben wird (Kriterium N1). Für die Antworten 2 bis 6 stimmt ihr Urteil ohne Korrektur mit beiden KI-Kodierungen überein (5/5). Antwort 1 war vorher im Gespräch als Beispiel erläutert worden und ist daher nicht verblindet; ihren Wert korrigierte die Autorin nach einem Hinweis auf den Widerspruch zu dieser Erläuterung (danach 6/6). Die übrigen Kriterien wurden nicht menschlich kodiert.

## Grenzen

Drei Läufe je Bedingung und vier Volläufe tragen als kleine, teilweise abhängige Datenbasis keine belastbare inferenzstatistische Aussage. Der Backend-Modellstand von NotebookLM ist nicht offengelegt. Die Autorin ist keine unabhängige Zweitbewerterin; die Verblindung mindert, aber beseitigt diese Grenze nicht. Die Erstkodierung stammt von demselben System (Claude), das die Läufe bedient hat, und ist nicht verblindet; die Zweitkodierung ist verblindet, aber ebenfalls KI-gestützt. Menschlich nachgeprüft ist nur Kriterium N1.
