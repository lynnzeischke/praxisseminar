# Iterations- und Evaluationsmatrix

Stand: 19.10.2026. Redaktionsnotizen auf Grundlage der projektbezogenen Artefakte, des vorliegenden Chats und der beigefügten NotebookLM-Testausgaben. Die Prüfstatus sind **keine empirischen Validierungskennwerte**.

| Version / Phase | Auslöser / Defizit | Umsetzung im Artefakt | Beobachtbarer Teststatus | DSR-Folge |
|---|---|---|---|---|
| R2 (Vorläufer) | Vollständiger JSON-Export, aber unbelegte MAILS-IDs und verfälschte AIRS-Comfort-Semantik | Quellenkritik und Originalitem-Lock | Wissenschaftlich `REVISION_REQUIRED` | R3: positionsgetreue Item-Kandidaten |
| R3 | Quellenauswahl musste gegen finalen Audit geprüft werden | Wechselvorschlag zu AISES, explizite Originalitem-IDs | Ursprünglich zu strenge Annahme, dass Nachtragsgenehmigung nötig sei | R4: Audit-konforme Quellenentscheidung |
| R4 | Audit erlaubt AIRS **oder** AISES | Quellenentscheidung innerhalb freigegebener Grundlage dokumentiert | Weitere FC-Wortlautprüfung nötig | Datennachweis ergänzt |
| R5 | Nutzer wünschte eine Datei: Audit + Prompt + ein Startbefehl | Finaler Audit vollständig integriert; FC-Originalitem-Auszug | NotebookLM-Ausgabe: Sprungfehler, unbegründete Pretestzahl, fehlende JSON-Routen, missverständliche Adaptionslabels | `REVISION_REQUIRED`; R6 |
| R6 | Funktionale und wissenschaftliche Ausgabe-Sperren fehlten | Feste Pfade aller Erfahrungsgruppen, Traceability B2/B5/B7, korrekter B6-Text, Adaptionslabels | JSON-/Konstrukt-/Routing-Prüfungen positiv; E3-Beleg und Aussagen zu Bearbeitungszeit/Simulation noch kritisch | R6.1 |
| R6.1 | E3-Evidenz, ungetestete Zeitangaben, Scheinbeobachtungen | Theorieanker Lambiase §6.2.4; hypothetische Simulation; keine Zeitbehauptung | R6.1-NotebookLM-Lauf technisch weitgehend konsistent; Teilnehmerformular musste nachformatiert werden | Pretest-Paket als separater Entwurf |
| Pretest-Vorbereitung | Druckbare Eingabefelder, Datenschutzinformationen und Testprotokolle fehlten | Fragebogen, Datenschutz-Ausfüllvorlage, Think-Aloud-Leitfaden | Dokumente erstellt; **keine realen Probanden befragt** | Echter kognitiver Pretest steht aus |

## Zusätzlich belegte Vorläuferlinien

| Modell-/Entwicklungsstand | Dokumentierte Änderung | Nachweisart / Grenze |
|---|---|---|
| Frühe Entwürfe 1.0–V7 | Allgemeine wissenschaftliche Leitlinien wurden zu umfangreicheren, DSR-bezogenen Prompt-Artefakten ausgebaut. | Historische Dateien in [`MODELLHISTORIE.md`](MODELLHISTORIE.md); keine originalen Chat-Turns für jede Fassung verfügbar. |
| V8 / V8.1 / V8.2–V8.4.11 | Modul-Paper-Abdeckung, `METHOD_SOURCE`, `RUN_MODE`, Quellenrollen, Design Requirements, Provenienz und weitere Konsistenz-Gates. | Archivierte Modellfassungen und V8-/V8.1-Changelogs; „FINAL“-Dateinamen sind keine empirische Bestätigung. |
| OPERATIONAL V2 / V2.1 | Hard-STOP, TTF-Gate ohne `TASK_CONTEXT`, Unternehmenskontext-Gate, E3-Kompatibilitätskontrolle. | Vorhandenes V2-Stresstest-Änderungsprotokoll. |
| OPERATIONAL V3–V3.5 | Fail-Closed-Logik, 18-Item-Checksum, Subskalentreue, Quellen- und Skalenprüfung. | Vorhandene Changelogs V3.1–V3.5 und die Modelltexte. |
| V3.5-R1 / R2 | Quellengebundene NotebookLM-Produktionsversuche bis zur Ein-Befehl-Generierung; in früheren Outputs blieben originale MAILS-IDs bzw. AIRS-Comfort-Semantik fehlerhaft. | Promptdateien und ausgewählte ältere NotebookLM-Testausgaben. |

**Methodische Vorsicht:** Die historischen Dateiversionen V8.x und OPERATIONAL V3.x sind unterschiedliche Benennungslinien. Die Tabelle behauptet keine lückenlos rekonstruierbare Zeitfolge aller individuellen Chat-Turns.

## Messarchitektur (bewusst stabil über die letzten Iterationen)

| Konstrukt | Items | Theorie-/Quellenbasis |
|---|---:|---|
| `READINESS_CORE_LIT` | 3 | MAILS: subjektives KI-Grundverständnis |
| `READINESS_CORE_LEARN` | 3 | AILRSE-5: Lern-Selbstwirksamkeit |
| `READINESS_CORE_APPLY` | 3 | MAILS: Anwendung / Problemlösen |
| `READINESS_CORE_DETECT` | 3 | MAILS (2× E2) + theoriegeleitetes E3 zur Ergebnisprüfung |
| `READINESS_CORE_COMFORT` | 3 | AISES: affektiver Komfort |
| `CONTEXT_FC` | 3 | Lambiase et al.: Facilitating Conditions |

Exakt 18 reflektive Items; dazu `DIAG_01`, `DIAG_02`, `DEM_01` (nicht gescort) sowie `EXP_01` als Routingfilter. Sechs Subskalen getrennt behandeln; **keinen unvalidierten Gesamtscore** bilden. Die Reflexivitätsentscheidung ist selbst Teil der methodischen Evaluation, nicht durch diese Dateistruktur empirisch bestätigt.

## Wiederholbarkeit und Grenzen

Die beigefügten Tests sind **gespeicherte NotebookLM-Antworttexte** und lassen sich hinsichtlich JSON-Format und Itemzahlen erneut prüfen. Eine deterministisch identische Generierung durch ein fremdes LLM wird nicht behauptet. Versionsstände, konkrete Quellenauswahl, verwendetes Notebook, dessen Sichtbarkeit und Rechteverwaltung sind für eine vollständige Replikation zusätzlich zu protokollieren.
