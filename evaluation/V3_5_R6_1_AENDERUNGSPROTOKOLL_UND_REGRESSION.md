# Änderungsprotokoll & statische Prüfung – V3.5-R6.1

**Status:** TEST_CANDIDATE, nicht als empirisch validierter Fragebogen oder als getesteter NotebookLM-Lauf freigegeben.

## Korrekturen gegenüber R6

1. `DETECT_03` besitzt jetzt einen **konkreten, zu verifizierenden Theorieanker** in Lambiase et al., § 6.2.4 zum Problem halluzinierter bzw. irreführender LLM-Ausgaben. Die Publikation ist nicht die Originalquelle des E3-Items. Das Item bleibt selbst entwickelt; `source_item_id=null`, `source_item_text_verified=false`, `original_scale=null`. `source_definition_verified=false` ohne direkte definitorische Quelle. Neues Pflichtobjekt `theoretical_rationale` samt `theoretical_rationale_verified` in B7; B2/B3 müssen auf denselben tatsächlichen Quellenanker verweisen.
2. Die Teilnehmer-Einleitung B5 enthält **keine ungeprüfte Bearbeitungsdauer**. `MAX_COMPLETION_TIME_MIN=8` bleibt ausschließlich das ursprüngliche (noch zu überprüfende) Designziel.
3. B4 ist strikt **hypothetisch-heuristisch**: mögliche Risiken statt behaupteter Beobachtungen oder Abbruchergebnisse bei simulierten Personen.
4. Bestehende B0-Gates wurden um konkrete Sichtprüfungen erweitert, **ohne neue Messkonstrukte oder zusätzliche Messitems**.

## Statische Prüfergebnisse (Datei, nicht NotebookLM-Ausführung)

- Original-Design-Audit-Anhang A byte-/textgleich zu R6: **PASS**.
- Audit-SHA256 im UTF-8-Textblock (inkl. führender und abschließender Zeilenwechsel): `87bffb6df1c2347759f68a692cfb558056bf7a7f514ab33f0e5df2c91a183449`.
- 18 unveränderte Item-IDs und komplette Formulierungen in §5: **PASS**.
- Zwei Ausgabeformate `.md`/`.txt` bytegleich: **PASS**.
- Einziger Startbefehl unverändert: `Führe RUN_MODE = QUESTIONNAIRE_GENERATION aus.`

**Noch zu prüfen:** Verifiziert NotebookLM die Passage in der hochgeladenen Originalquelle? Ist die E3-Ableitung explizit begrenzt? Fehlen Zeitbehauptungen und vermeintliche Simulationsbeobachtungen? Wird das B7-JSON mit genau 18 Itemobjekten ausgegeben und ist es parsebar? Bestehen die alten Routing-/Skalen-/Itemgates weiterhin?
