sed -i 's|companion_ref_shortcode: PG-APG-5.18|companion_ref_shortcode: PG-APG-5.18\nrelated_skills:\n  - SKL-03-11\nrelated_artifacts:\n  - A19|' \
  reference/processes/PR21-plan-risk-management.md

# PR22 — Identify Risks (PG-APG-5.19)
sed -i 's|companion_ref_shortcode: PG-APG-5.19|companion_ref_shortcode: PG-APG-5.19\nrelated_skills:\n  - SKL-03-11\nrelated_artifacts:\n  - A19|' \
  reference/processes/PR22-identify-risks.md

# PR23 — Perform Qualitative Risk Analysis (PG-APG-5.20)
sed -i 's|companion_ref_shortcode: PG-APG-5.20|companion_ref_shortcode: PG-APG-5.20\nrelated_skills:\n  - SKL-03-11\nrelated_artifacts:\n  - A19|' \
  reference/processes/PR23-perform-qualitative-risk-analysis.md

# PR24 — Perform Quantitative Risk Analysis (PG-APG-5.21)
sed -i 's|companion_ref_shortcode: PG-APG-5.21|companion_ref_shortcode: PG-APG-5.21\nrelated_skills:\n  - SKL-03-12\nrelated_artifacts:\n  - A19\n  - A20|' \
  reference/processes/PR24-perform-quantitative-risk-analysis.md

# PR25 — Plan Risk Responses (PG-APG-5.22)
sed -i 's|companion_ref_shortcode: PG-APG-5.22|companion_ref_shortcode: PG-APG-5.22\nrelated_skills:\n  - SKL-03-12\nrelated_artifacts:\n  - A19|' \
  reference/processes/PR25-plan-risk-responses.md

# PR26 — Plan Procurement Management (PG-APG-5.24 not confirmed; use file_path anchor)
sed -i '/^file_path: "reference\/processes\/PR26-plan-procurement/i related_skills:\n  - SKL-03-15\nrelated_artifacts:\n  - A31' \
  reference/processes/PR26-plan-procurement-management.md

# PR27 — Plan Stakeholder Engagement (PG-APG-5.24)
sed -i 's|companion_ref_shortcode: PG-APG-5.24|companion_ref_shortcode: PG-APG-5.24\nrelated_skills:\n  - SKL-03-08\nrelated_artifacts:\n  - A07|' \
  reference/processes/PR27-plan-stakeholder-engagement.md

# PR28 — Direct and Manage Project Work (PG-APG-6.1)
sed -i 's|companion_ref_shortcode: PG-APG-6.1|companion_ref_shortcode: PG-APG-6.1\nrelated_skills:\n  - SKL-04-01\nrelated_artifacts:\n  - A18\n  - A14|' \
  reference/processes/PR28-direct-and-manage-project-work.md

# PR29 — Manage Project Knowledge (PG-APG-6.2)
sed -i 's|companion_ref_shortcode: PG-APG-6.2|companion_ref_shortcode: PG-APG-6.2\nrelated_skills:\n  - SKL-04-03\nrelated_artifacts:\n  - A30|' \
  reference/processes/PR29-manage-project-knowledge.md

# PR30 — Monitor and Control Project Work (PG-APG-7.1 — shared; use file_path anchor)
sed -i '/^file_path: "reference\/processes\/PR30-monitor-and-control/i related_skills:\n  - SKL-05-01\nrelated_artifacts:\n  - A17\n  - A18' \
  reference/processes/PR30-monitor-and-control-project-work.md



grep -l 'related_skills' reference/processes/PR2{1..9}-*.md reference/processes/PR30-*.md
