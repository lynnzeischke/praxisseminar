# CHANGELOG V8

V8 erweitert V7 insbesondere um:

1. **METHOD_SOURCE** als eigene Quellenrolle.
2. **Verbindliche Prüfung aller fünf Modul-Papers** mit Coverage-Gate.
3. **Module Paper Coverage Matrix**: jedes Paper erhält `USED` oder `REVIEWED_NOT_USED`.
4. **Design-Requirement-Extraktion** als eigener Prozessschritt vor der Fragebogengenerierung.
5. Explizite DSR-Design-Requirements `DR01` bis `DR12`.
6. Paper 1, 2 und 5 sind nun genauso explizit eingebunden wie Paper 3 und 4.
7. Strengere Trennung zwischen Theorie-/Item-/Validierungs-/Methodenquelle.
8. Keine „Zier-Zitationen“: jede genannte Quelle braucht eine dokumentierte Funktion.
9. Originalitemstatus `FOUND / PARTIALLY_FOUND / NOT_FOUND`.
10. Datenqualitätsmaßnahmen werden als Feldstudiendesign, nicht als psychometrische Validität klassifiziert.
11. JSON-Export enthält jetzt auch Modul-Paper-Abdeckung und Design Requirements.
12. Traceability wurde erweitert um `Design Requirement`.
13. Stop-Regel, wenn die fünf Modul-Papers nicht vollständig geprüft wurden.