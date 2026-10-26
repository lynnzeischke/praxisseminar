```json
{
  "metadata": {
    "design_audit_reference": "DESIGN_AUDIT_REF_2026_KMU_GENAI_DIAG_004_FINAL",
    "embedded_design_audit": true,
    "target_population": "Kaufmännische Mitarbeitende eines mittelständischen Unternehmens",
    "ai_context": "Generative KI, insbesondere ChatGPT Enterprise und Microsoft Copilot, im kaufmännischen Arbeitsalltag",
    "measurement_goal": "Individuelle Employee AI Readiness diagnostisch erfassen und Schulungs-/Entwicklungsbedarfe identifizieren",
    "instrument_purpose": "DIAGNOSTIC",
    "language": "DE",
    "source_files_consulted": [
      "MAILS.pdf",
      "AILRSE-5.pdf",
      "AISES.pdf",
      "AIRS.pdf",
      "Lambiase et al. (2025).pdf",
      "NOTEBOOKLM_FC_ORIGINALITEMS_OHNE_TEILNEHMERDATEN.txt"
    ],
    "overall_score_supported": false,
    "empirical_validation_status": "PENDING"
  },
  "source_selection_decision": {
    "comfort_source_selected": "AISES",
    "comfort_source_rationale": "Die AISES-Comfort-Items erfassen das affektive Erleben bei der KI-Interaktion und passen besser zum GenAI-Bürokontext als AIRS COM3/Q18 (Angst vor humanoiden Robotern).",
    "audit_compliance": "Operationalisierungsentscheidung innerhalb der im freigegebenen Audit A8/A9 dokumentierten Quellenoptionen."
  },
  "routing": {
    "filter_variable": "EXP_01",
    "categories": [
      "NO_EXPERIENCE",
      "LIMITED_EXPERIENCE",
      "REGULAR_USER"
    ],
    "NO_EXPERIENCE": {
      "included_modules": [
        "READINESS_CORE_LIT",
        "READINESS_CORE_LEARN",
        "CONTEXT_FC",
        "DIAGNOSTIC_NEEDS",
        "DEMOGRAPHICS_MINIMAL"
      ],
      "skipped_modules": [
        "READINESS_CORE_APPLY",
        "READINESS_CORE_DETECT",
        "READINESS_CORE_COMFORT"
      ],
      "skipped_status_coding": "NOT_SCORED_DUE_TO_NO_EXPERIENCE",
      "participant_path": [
        "Teil 2",
        "Teil 3",
        "Teil 7",
        "Teil 8",
        "Teil 9"
      ]
    },
    "LIMITED_EXPERIENCE": {
      "included_modules": [
        "READINESS_CORE_LIT",
        "READINESS_CORE_LEARN",
        "READINESS_CORE_APPLY",
        "READINESS_CORE_DETECT",
        "READINESS_CORE_COMFORT",
        "CONTEXT_FC",
        "DIAGNOSTIC_NEEDS",
        "DEMOGRAPHICS_MINIMAL"
      ],
      "skipped_modules": [],
      "participant_path": [
        "Teil 2",
        "Teil 3",
        "Teil 4",
        "Teil 5",
        "Teil 6",
        "Teil 7",
        "Teil 8",
        "Teil 9"
      ]
    },
    "REGULAR_USER": {
      "included_modules": [
        "READINESS_CORE_LIT",
        "READINESS_CORE_LEARN",
        "READINESS_CORE_APPLY",
        "READINESS_CORE_DETECT",
        "READINESS_CORE_COMFORT",
        "CONTEXT_FC",
        "DIAGNOSTIC_NEEDS",
        "DEMOGRAPHICS_MINIMAL"
      ],
      "skipped_modules": [],
      "participant_path": [
        "Teil 2",
        "Teil 3",
        "Teil 4",
        "Teil 5",
        "Teil 6",
        "Teil 7",
        "Teil 8",
        "Teil 9"
      ]
    }
  },
  "diagnostic_needs": {
    "module_code": "DIAGNOSTIC_NEEDS",
    "reflective_measurement": false,
    "scored": false,
    "items": [
      {
        "item_id": "DIAG_01",
        "question_text": "In welchen der folgenden Bereiche sehen Sie für sich persönlichen Schulungs- oder Entwicklungsbedarf bezüglich generativer KI?",
        "type": "MULTIPLE_CHOICE",
        "options": [
          "Grundlagen generativer KI",
          "Effective Prompting & Formulierung von Anfragen",
          "Kritische Prüfung & Validierung von KI-Ergebnissen",
          "Datenschutz & sicherer Umgang mit sensiblen Unternehmensdaten",
          "Urheberrechtliche & ethische Aspekte",
          "Integration von KI in bestehende Arbeitsabläufe",
          "Konkrete Anwendung spezifischer KI-Tools (z. B. ChatGPT Enterprise, MS Copilot)"
        ],
        "other_option": "Sonstiges: ______",
        "exclusive_option": "Kein Schulungs-/Entwicklungsbedarf"
      },
      {
        "item_id": "DIAG_02",
        "question_text": "Welche konkrete Unterstützung oder welche Rahmenbedingungen würden Ihnen helfen, generative KI in Ihrem Arbeitsalltag effektiver zu nutzen?",
        "type": "OPEN_TEXT"
      }
    ]
  },
  "demographics_minimal": {
    "module_code": "DEMOGRAPHICS_MINIMAL",
    "reflective_measurement": false,
    "scored": false,
    "items": [
      {
        "item_id": "DEM_01",
        "question_text": "In welchem kaufmännischen Funktionsbereich sind Sie primär tätig?",
        "type": "OPEN_TEXT_OR_SINGLE_CHOICE",
        "placeholder": "[FUNKTIONSBEREICHE_DER_ORGANISATION_EINFÜGEN]"
      }
    ]
  },
  "items": [
    {
      "item_id": "LIT_01",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kenne die wichtigsten Grundbegriffe generativer KI.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "0-10",
      "final_scale": "0-10",
      "translation_status": "GERMAN_CONTEXT_ADAPTED_FROM_SOURCE",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 7 (Know & Understand)",
        "source_item_id": "Item 7",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "LIT_02",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kenne die Bedeutung des Begriffs generative KI.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "0-10",
      "final_scale": "0-10",
      "translation_status": "GERMAN_CONTEXT_ADAPTED_FROM_SOURCE",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 8 (Know & Understand)",
        "source_item_id": "Item 8",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "LIT_03",
      "construct_code": "READINESS_CORE_LIT",
      "question_text": "Ich kann mir mögliche zukünftige Anwendungen generativer KI vorstellen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "0-10",
      "final_scale": "0-10",
      "translation_status": "GERMAN_CONTEXT_ADAPTED_FROM_SOURCE",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 12 (Know & Understand)",
        "source_item_id": "Item 12",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "LEARN_01",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich verstehen kann, wie neue generative KI-Anwendungen funktionieren.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "1-7",
      "final_scale": "1-7",
      "translation_status": "GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "AILRSE_5",
        "locator": "Table 2, Item 1",
        "source_item_id": "Item 1",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "LEARN_02",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich bei Bedarf die Nutzung neuer generativer KI-Anwendungen erlernen kann.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "1-7",
      "final_scale": "1-7",
      "translation_status": "GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "AILRSE_5",
        "locator": "Table 2, Item 2",
        "source_item_id": "Item 2",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "LEARN_03",
      "construct_code": "READINESS_CORE_LEARN",
      "question_text": "Ich bin zuversichtlich, dass ich mir die Nutzung neuer generativer KI-Anwendungen selbstständig aneignen kann.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "1-7",
      "final_scale": "1-7",
      "translation_status": "GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "AILRSE_5",
        "locator": "Table 2, Item 5",
        "source_item_id": "Item 5",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "APPLY_01",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Ich kann generative KI-Anwendungen bedienen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "0-10",
      "final_scale": "0-10",
      "translation_status": "GERMAN_CONTEXT_ADAPTED_FROM_SOURCE",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 1 (Use & Apply)",
        "source_item_id": "Item 1",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "APPLY_02",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Ich kann generative KI sinnvoll einsetzen, um meine Arbeitsziele zu erreichen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "0-10",
      "final_scale": "0-10",
      "translation_status": "GERMAN_CONTEXT_ADAPTED_FROM_SOURCE",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 3 (Use & Apply)",
        "source_item_id": "Item 3",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "APPLY_03",
      "construct_code": "READINESS_CORE_APPLY",
      "question_text": "Die meisten Probleme im Umgang mit generativer KI kann ich aus eigener Kraft meistern.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "0-10",
      "final_scale": "0-10",
      "translation_status": "GERMAN_CONTEXT_ADAPTED_FROM_SOURCE",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 24 (AI Problem solving)",
        "source_item_id": "Item 24",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "DETECT_01",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann erkennen, ob eine Anwendung auf generativer KI basiert.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "0-10",
      "final_scale": "0-10",
      "translation_status": "GERMAN_CONTEXT_ADAPTED_FROM_SOURCE",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 13 (Detect AI)",
        "source_item_id": "Item 13",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "DETECT_02",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann unterscheiden, ob ich mit einer generativen KI oder einer Person interagiere.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "0-10",
      "final_scale": "0-10",
      "translation_status": "GERMAN_CONTEXT_ADAPTED_FROM_SOURCE",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "MAILS",
        "locator": "Appendix A, Pos. 15 (Detect AI)",
        "source_item_id": "Item 15",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "DETECT_03",
      "construct_code": "READINESS_CORE_DETECT",
      "question_text": "Ich kann die inhaltliche Richtigkeit von Ergebnissen, die durch generative KI erzeugt wurden, kritisch überprüfen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E3",
      "original_scale": null,
      "final_scale": "0-10",
      "translation_status": "GERMAN_DEVELOPED_E3",
      "translation_equivalence_status": "NOT_APPLICABLE",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "LAMBIASE_2025",
        "locator": "Section 6.2.4, paragraph on LLM hallucinations and misleading outputs",
        "source_item_id": null,
        "source_item_text_verified": false,
        "source_definition_verified": false,
        "theoretical_rationale_verified": true,
        "theoretical_rationale": {
          "source_id": "LAMBIASE_2025",
          "source_locator": "Section 6.2.4, paragraph on LLM hallucinations and misleading outputs",
          "support_type": "THEORY_RATIONALE_ONLY",
          "evidence_summary": "Fehlerhafte/halluzinierte LLM-Inhalte können Vertrauen und fachliche Überprüfung erschweren",
          "project_inference": "Die Fähigkeit zur inhaltlichen Prüfung von GenAI-Ergebnissen ist ein relevantes projektseitiges Diagnostikkriterium",
          "not_an_original_or_validated_item": true
        }
      }
    },
    {
      "item_id": "COMFORT_01",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Wenn ich mit generativer KI interagiere, fühle ich mich ruhig.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "1-7",
      "final_scale": "1-7",
      "translation_status": "GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "AISES",
        "locator": "Section 5.3 / Table 2, CF1/Q25",
        "source_item_id": "Q25",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "COMFORT_02",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Wenn ich mit generativer KI interagiere, fühle ich mich wohl.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "1-7",
      "final_scale": "1-7",
      "translation_status": "GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "AISES",
        "locator": "Section 5.3 / Table 2, CF3/Q24",
        "source_item_id": "Q24",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "COMFORT_03",
      "construct_code": "READINESS_CORE_COMFORT",
      "question_text": "Wenn ich mit generativer KI interagiere, fühle ich mich entspannt.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "1-7",
      "final_scale": "1-7",
      "translation_status": "GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "AISES",
        "locator": "Section 5.3 / Table 2, CF5/Q22",
        "source_item_id": "Q22",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "FC_01",
      "construct_code": "CONTEXT_FC",
      "question_text": "Mir stehen die notwendigen Ressourcen zur Verfügung, um generative KI-Anwendungen bei meiner Arbeit zu nutzen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "1-7",
      "final_scale": "1-7",
      "additional_response_option": "Kann ich nicht beurteilen",
      "additional_response_option_coding": "MISSING_NOT_SCORED",
      "translation_status": "GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "LAMBIASE_2025",
        "locator": "Online-Anhang / Dataset, Item FC_1",
        "source_item_id": "FC_1",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "FC_02",
      "construct_code": "CONTEXT_FC",
      "question_text": "Ich verfüge über das notwendige Wissen, um generative KI-Anwendungen bei meiner Arbeit zu nutzen.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "1-7",
      "final_scale": "1-7",
      "additional_response_option": "Kann ich nicht beurteilen",
      "additional_response_option_coding": "MISSING_NOT_SCORED",
      "translation_status": "GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "LAMBIASE_2025",
        "locator": "Online-Anhang / Dataset, Item FC_2",
        "source_item_id": "FC_2",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    },
    {
      "item_id": "FC_03",
      "construct_code": "CONTEXT_FC",
      "question_text": "Generative KI-Anwendungen sind mit anderen Technologien kompatibel, die ich bei meiner Arbeit verwende.",
      "measurement_model": "REFLECTIVE",
      "evidence_class": "E2",
      "original_scale": "1-7",
      "final_scale": "1-7",
      "additional_response_option": "Kann ich nicht beurteilen",
      "additional_response_option_coding": "MISSING_NOT_SCORED",
      "translation_status": "GERMAN_TRANSLATED_AND_CONTEXT_ADAPTED",
      "translation_equivalence_status": "NOT_EMPIRICALLY_ESTABLISHED",
      "reviewer_status": "PASS",
      "source_verification_status": "VERIFIED",
      "verification_issue": null,
      "target_language_original_verified": false,
      "exact_original_match": false,
      "source_evidence": {
        "source_id": "LAMBIASE_2025",
        "locator": "Online-Anhang / Dataset, Item FC_3",
        "source_item_id": "FC_3",
        "source_item_text_verified": true,
        "source_definition_verified": true
      }
    }
  ],
  "conformance": {
    "run_mode": "QUESTIONNAIRE_GENERATION",
    "design_lock_ok": true,
    "source_item_evidence_ok": true,
    "e2_proof_ok": true,
    "e3_source_compatibility_ok": true,
    "subscale_membership_ok": true,
    "item_count_checksum_ok": true,
    "traceability_consistency_ok": true,
    "adaptation_labeling_ok": true,
    "participant_rendering_ok": true,
    "routing_ok": true,
    "fc_not_judgable_option_ok": true,
    "diagnostic_module_completeness_ok": true,
    "validation_plan_ok": true,
    "json_consistency_ok": true,
    "audit_selection_documented_ok": true,
    "overall_conformance_status": "CONFORMANT_GENERATION"
  }
}
```