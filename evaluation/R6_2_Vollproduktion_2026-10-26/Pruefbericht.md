# Vollständige R6.2 Generierung am 26 Oktober 2026

## Versuchsaufbau

Ein neues Notebook ohne vorherige Nutzerturns, unverändertes R6.2 und zwölf Quellen gemäß Vorabplan.json. Alle Quellen waren verarbeitet und ausgewählt. Start: „Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.“ Kein Korrekturturn und keine Erfolgsselektion durch Wiederholung.

Notebook: https://notebook.google.com/notebook/1b551523-3c0c-4508-b13c-d8dbf7238032

## Dokumentation und Verfahren

Der Kopierknopf lieferte keinen Text. Der sichtbare DOM-Seiteninhalt wurde deshalb als Seiteninhalt_original.txt gesichert; DOM_original.txt enthält zusätzlich den strukturierten Snapshot. Die automatische Notebook-Zusammenfassung ist kein Testlauf. Der JSON-Block wurde ohne Inhaltsänderung aus der sichtbaren Antwort extrahiert. Das Einfassen in einen JSON-Codeblock dient nur dem unveränderten alten Parser; dessen PASS darf nicht als PASS für die ursprüngliche Gesamtantwort gelesen werden.

Reproduktion: `python3 pruefe_gesamtantwort.py`. Das Skript erzeugt Automatische_Pruefung.json und ruft check_output.py unverändert auf. Der Vorabplan enthält die SHA256-Werte aller zwölf Eingabedateien. Der Backend-Modellstand und der Zufallsstartwert waren nicht angezeigt.

## Befunde

- JSON-Struktur PASS: 18 eindeutige IDs, sechs Dreiergruppen, 17 E2 und ein E3 (DETECT_03), kein Gesamtscore, erwartete Routingstruktur und FC-Nichtbeurteilbarkeit als MISSING_NOT_SCORED.
- Endskalen: neun Items 0–10, neun Items 1–7. Die projektspezifische E3-Skala wird nicht als Originalskala ausgegeben.
- Textpräsenz: je 18/18 normalisierte Endtexte in beiden B2- und beiden B5-Blöcken. Das beweist keine globale Konsistenz.
- Gesamtfolge FAIL: B1, B2, B3, B4 und B5 stehen jeweils zweimal in der Antwort. Der erste B5-Durchgang endet nach FC; danach beginnt „Teil ### B1“ erneut. Erst die zweite B5-Fassung enthält alle neun Teile. B6, B7 und B0 stehen einmal. Die Regel einer eindeutigen B1–B7-Folge ist verletzt.
- Wortlaut-Locatoren FAIL für drei AISES-Comfort-Items: „Section 5.3 / Table 2“ führt nicht zur Wortlauttabelle. Die geladenen Originale weisen CF1/Q25, CF3/Q24 und CF5/Q22 in Table 3 (PDF-Dateiseite 11) nach; Table 2 zeigt Ladungen. Das ist eine falsche Fundstelle, kein Beleg dafür, dass diese Originalitems nicht existieren.
- Quellenanker geprüft: MAILS Appendix A (PDF-Dateiseite 9), Positionen 1/3/7/8/12/13/15/24; AILRSE-5 Table 2 (PDF-Dateiseite 4), Items 1/2/5; AISES Table 3 (PDF-Dateiseite 11), CF1/Q25, CF3/Q24, CF5/Q22; FC_1–FC_3 im teilnehmerdatenfreien Originalextrakt; Lambiase § 6.2.4 mit Halluzinationsabsatz. Die deutschen Formulierungen bleiben Adaptionen; der Quellenabgleich ist keine empirische Äquivalenzprüfung. Bei DETECT_03 trägt die Quelle den Risikobezug, keine validierte Kompetenzfrage.
- Teilnehmerpfad: Der zweite B5-Durchgang und JSON führen Personen ohne Erfahrung über LIT, LEARN und FC plus Zusatzmodule und überspringen APPLY/DETECT/COMFORT. Die erste B5-Fassung ist als Gesamtfassung unvollständig.
- B5 behauptet keine gemessene Bearbeitungszeit; der Datenschutztext bleibt sichtbar ein Platzhalter. Die Ausgabe bleibt ein Entwurf, keine einsetzbare Feldfreigabe.

## Urteil und Grenzen

Das modellseitige CONFORMANT_GENERATION und die Bezeichnung der eigenen B0-Matrix als „unabhängig“ sind nicht bestätigt. Der vollständige Test ergänzt die bisherige Einzelitemevaluation mit einem negativen Produktionsbefund. R6.2 bleibt TEST_CANDIDATE. Einzelner Lauf, KI-gestützte Kodierung ohne verblindete menschliche Doppelbewertung; keine Robustheits-, Überlegenheits-, Nutzen- oder Messgüteaussage. Originalantwort, Vorabplan und Prüfer sind in diesem Verzeichnis dokumentiert. Die wissenschaftlichen Original-PDFs bleiben außerhalb des Repositorys.
