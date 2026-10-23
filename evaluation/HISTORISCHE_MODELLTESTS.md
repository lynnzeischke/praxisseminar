# Historische Modelltests: zusätzliche Evidenz und Grenzen

**Art:** Dokumentation aus tatsächlich erhaltenen älteren NotebookLM-Ausgabe-Textdateien. Keine nachträglich generierte Pseudokonversation.

| Belegdatei | Feststellbarer Befund | Konsequenz |
|---|---|---|
| [`NotebookLM_Output_20261014_110858.txt`](../notebooklm_tests/historisch/NotebookLM_Output_20261014_110858.txt) | Frühe Ausgabe behauptet `CONFORMANT_GENERATION`; enthält AIRS-Comfort-Referenzen. | Selbsturteile eines Modells werden unabhängig überprüft. |
| [`NotebookLM_Output_20261019_133226.txt`](../notebooklm_tests/historisch/NotebookLM_Output_20261019_133226.txt) | Im Text kommt `Know_AI_1` als MAILS-Referenz vor; eine positive Konformitätsmeldung ist vorhanden. | Originalpositionen im MAILS-Appendix statt erfundener synthetischer Kennungen prüfen. |
| [`NotebookLM_Output_20261019_143359.txt`](../notebooklm_tests/historisch/NotebookLM_Output_20261019_143359.txt) | Erhaltener Modelloutput beschreibt eine provisorische Konformitätsmatrix und AIRS-Comfort-Herkunft. | Eine vorläufige Prüftabelle ist kein Beleg für tatsächliche Quellentreue. |
| [`NotebookLM_Output_20261019_144332.txt`](../notebooklm_tests/historisch/NotebookLM_Output_20261019_144332.txt) | Enthält das als MAILS-Original ausgegebene `Know_AI_1` und selbst attestierte Konformität. | R3/R4 erfordern echte Originalitem-Positionen und Quellenprüfung. |

**Zuordnungsgrenze:** Da in diesen Ausgaben der aktive Masterprompt nicht in allen Fällen unverwechselbar ausgewiesen ist, werden sie nicht ausschließlich anhand des Upload-Zeitstempels bestimmten Dateiversionen zugeordnet.

**Quellenabgleich:** MAILS Appendix A verwendet nummerierte Items (z. B. 7 für Grundbegriffe, 8 für Definitionen, 12 für künftige Anwendungen); die künstliche Kennung `Know_AI_1` ist kein solches publiziertes Originalitem. AIRS Q18 bezieht sich auf humanoide Roboter, was für rein textbasierte Büro-GenAI kontextfremd ist. Das war Anlass für die spätere auditkonforme AISES-Auswahl.

**Publikationsgrenze:** In diesen historischen Outputs stehen potentiell falsche Itemzitate und Quellenbehauptungen. Sie sind **als Fehlertest-Material** aufbewahrt; sie dürfen nicht isoliert als wissenschaftliche Belege verwendet werden.
