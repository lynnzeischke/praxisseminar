# R6.2 Prüfbericht vom 24 Oktober 2026

## Ergebnis und Freigabe

R6.2 wurde in drei neuen NotebookLM-/Gemini-Notebook-Notebooks mit jeweils
einem ersten Chatturn getestet. Die bekannte Fünf-Fall-Aufgabe war gegenüber
der R6.1-Serie unverändert; nur Promptdatei und deren Aktivierung wurden
auf R6.2 umgestellt. Alle vier wissenschaftlichen PDFs waren byteidentisch.

**Ergebnis: 22 von 24 Kriterienerfüllungen, keine allgemeine Freigabe.**

| Lauf | K1 | K2 | K3 | K4 | K5 | K6 | K7 | K8 | Summe |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R62_1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 8/8 |
| R62_2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 7/8 |
| R62_3 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 7/8 |

Die beiden gezielt bearbeiteten Regeln funktionieren in allen drei neuen
Läufen: A wird wegen des fehlenden deutschen Originalnachweises nicht als
belegtes E1 freigegeben (K1); die neue Zusammensetzung D wird E3 (K4).
Die Quellenprüfung bleibt fehleranfällig: R62_2 nennt AISES Table 2 statt
der Wortlaut-Tabelle 3 (K8). R62_3 behauptet verifizierte Ausgangsquellen
und übersieht die falsche AISES-Teilquelle (K5), obwohl das Item als E3
klassifiziert und wegen Mehrfachinhalt gestoppt wird.

**Zusätzlicher Transferlauf: vier von vier festgelegten Kriterien erfüllt.**
F weist einen neuen deutschen MAILS-Originalanspruch zurück; G erkennt eine
neue Kombination aus MAILS Position 1 und 13 als E3 und beanstandet die
Mehrfachaussage; H behandelt eine neue AILRSE-Übersetzung als E2 ohne behauptete
empirische Äquivalenz; I erkennt den unveränderten englischen Originalwortlaut
für einen ausdrücklich englischen Forschungsanhang als E1 an. Die Quellanker
wurden gegen MAILS Appendix A (PDF-Seite 9) und AILRSE Table 2 (PDF-Seite 4)
geprüft. Die Transferaufgabe ist angeleitet, nach der Revision definiert und
nur einmal ausgeführt, kein verblindeter unabhängiger Validierungstest.

## Kriterien und Kodierung

- K1: A ohne deutschen Wortlautnachweis nicht als belegtes E1 freigeben;
  die Nachweislücke muss als Grund sichtbar sein.
- K2/K3/K4: B/C/D als E2/E2/E3 kennzeichnen.
- K5: Die nicht belegte AISES-Teilquelle in D ausdrücklich beanstanden.
- K6: Übersetzungsunsicherheit/konkurrierende Bedeutungen oder sachlich
  begründeten Übersetzungs-Stopp bei E ausweisen. Architektur-Stopp allein
  genügt nicht; alle drei R6.2-Läufe liefern hier Bedeutungsanalysen.
- K7: Keine bereits empirisch belegte Äquivalenz oder neue Validität behaupten.
- K8: AILRSE Table 2 Item 1, MAILS Appendix A Pos. 3 und AISES Table 3 TS3/Q6
  als korrekte Wortlautanker angeben. Eine Ladungsmatrix ist kein Wortlautbeleg.

Je Kriterium 1 erfüllt, sonst 0. Die Kriterien, Laufzahl und Transferfälle
wurden vor dem ersten R6.2-Lauf lokal gespeichert; der ursprüngliche Plan
bleibt unverändert. Sein Status PLANNED_NOT_RUN beschreibt den Planungszeitpunkt.
Ergebnisse.json dokumentiert die tatsächliche Durchführung. Keine Wiederholungen
bis zum Wunschresultat und keine nachträgliche Änderung des getesteten Prompts.

## Zusätzliche qualitative Fehler

R62_2 und R62_3 behaupten trotz gegenteiliger Promptregel, statistische
Messinvarianz könne im kognitiven Pretest geprüft werden. Das ist fachlich
falsch: Verständnisprüfung und statistische Invarianzprüfung benötigen
unterschiedliche Daten/Verfahren. K7 bleibt erfüllt, weil dort keine bereits
nachgewiesene Äquivalenz behauptet wird; diese Nebenfehler werden nicht durch
die Punktzahl verdeckt. Bei D unterstellen Antworten teilweise eine E2-Behauptung,
die in der Nutzeraufgabe nicht steht. Bei A sind kategorische Aussagen wie
„ist falsch“ stärker als der sichere Befund „aus dem Quellenbestand nicht
nachgewiesen“. R62_2 verkürzt zudem Statusnamen. Eine insgesamt fehlerfreie
Antwort oder vollständige JSON-Schema-Konformität ist nicht nachgewiesen.

## Änderungen gegenüber R6.1

1. E1 verlangt exakten Zielsprachenwortlaut mit Fundstelle; Stichprobenland,
   Autorensprache und eigene Rückübersetzung reichen nicht.
2. Herkunftsklasse, Belegstatus und Freigabe werden getrennt. E2_NOT_VERIFIED
   ist ein Prüfproblem, keine Ersatz-Herkunftsklasse. Neue Synthesen sind E3;
   jeder Teilbeleg bleibt separat nachzuprüfen.
3. ITEM_EVIDENCE_REVIEW begrenzt Einzelitemaufträge auf die angefragten Fälle
   und trennt sie von Architekturaufnahme und vollständiger Generierung.
4. Übersetzungsplausibilität, Verständnis und empirische Äquivalenz sind getrennt;
   unbelegte Aussagen über zerstörte psychometrische Eigenschaften sind untersagt.
5. Der vollständige eingebettete Original-Design-Audit ist unverändert erhalten.
   Routing, Itemregister und bestehende Ausgabevorgaben wurden beibehalten;
   ihr Verhalten wurde in dieser Serie nicht vollständig ausgeführt.

Der genaue Textunterschied steht in
[R6_1_zu_R6_2.diff](R6_1_zu_R6_2.diff).

## Vergleich und Aussagegrenze

Die frühere R6.1-Serie erzielte 21/24, R6.2 jetzt 22/24. Die Verbesserung
um einen Punkt ist deskriptiv, kein gesicherter allgemeiner Wirksamkeitsvorteil:
bekannte Fälle, kleine Laufzahl, zeitlich getrennte Serien, nicht offengelegter
Backend-Modellstand und KI-gestützte Kodierung ohne verblindete menschliche
Doppelkodierung. Überlappende Kriterien sind keine unabhängigen Erfolgsereignisse.
Der Transferlauf wird separat als 4/4 berichtet und nicht zur 24er-Summe addiert.
Die automatische Notebook-Zusammenfassung ist keine Testantwort.

**Version: TEST_CANDIDATE. Freigabeentscheidung: REVISION_REQUIRED_FOR_GENERAL_RELEASE.**
Die Datei ist geprüft und weiterentwickelt, aber weder allgemein fehlerfrei
noch als vollständige 18-Item-Produktion, psychometrisch oder im Feld validiert.

## Nachweise und Replikation

[R6_2_TESTNACHWEISE.zip](R6_2_TESTNACHWEISE.zip) enthält den vorab gespeicherten
Plan, genaue Aufgaben, geprüften R6.2-Prompt, ursprüngliche R6.1-Vergleichsdaten,
vollständige sichtbare DOM-/Textaufnahmen aller vier neuen Läufe,
Notebook-URLs, Quellhashes und Ergebnisse.json. Wissenschaftliche PDFs und
Befragtenantworten werden nicht mit hochgeladen. Der ZIP-Inhalt ist mit
PAKET_SHA256SUMS.txt nachrechenbar. Die ursprünglichen Quellen sind für eine
neue Durchführung selbst bereitzustellen; alle vier PDFs plus ausschließlich
R6.2 auswählen und pro Lauf ein neues Notebook mit der gespeicherten Aufgabe
verwenden. Dokumentierte Antworten sind Beobachtungen, keine garantierten
Ausgaben späterer Läufe.

Die textuellen Antworten und DOM-Aufnahmen enthalten die sichtbaren
Quellenmarker; maßgeblich für die Bewertung ist die vollständige Antwort
nach dem ersten Nutzerturn, nicht die automatische Zusammenfassung oder
die modellinterne Thoughts-Ansicht. Der Nachweis der tatsächlichen Quellenlage
erfolgte anhand der lokal verfügbaren Original-PDFs.
