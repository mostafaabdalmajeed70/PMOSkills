# Risk Domain README

**Purpose:** Provide a repository landing page for the PMI-aligned risk skill chain, its artifact model, and navigation links.

## Domain scope

This domain covers the project-level risk management cycle aligned to PMBOK8 and the repository artifact model:
- SKL-03-11 — Perform Risk Analysis
- SKL-03-12 — Plan Risk Responses
- SKL-04-01 — Implement Risk Responses
- SKL-05-01 — Monitor Risks

## Canonical sequence

1. **SKL-03-11 — Perform Risk Analysis**  
   Analyze identified risks iteratively to understand exposure, priority, and where justified quantified effects.

2. **SKL-03-12 — Plan Risk Responses**  
   Select response strategies, assign owners, define triggers, and integrate response actions into plans.

3. **SKL-04-01 — Implement Risk Responses**  
   Execute agreed responses, activate contingent actions when triggers occur, and convert realized risks into issue control.

4. **SKL-05-01 — Monitor Risks**  
   Track identified risks, monitor response effectiveness, detect emergent, secondary, and residual risks, and loop findings back into analysis and planning.

## Primary artifacts

- **A19 — Risk Management Record**: central risk artifact across planning, execution, and monitoring.
- **A18 — Issue, Impediment, and Action Log**: active control record for realized risks and operational follow-up.
- **A12 — Change and Exception Decision Log**: governance vehicle for material changes, exceptions, escalations, and risk-related decisions.
- **A16 — Financial Management and Cost Baseline Record**: reserve logic, reserve usage traceability, and financial thresholds.
- **A20 — Quantitative Risk and Reserve Decision Record**: optional decision-focused artifact for materially important quantitative analysis.

## Operating logic

- Risks are analyzed first, then responses are planned, then approved responses are implemented, and finally effectiveness is monitored.
- Monitoring can loop work back to analysis, response planning, or further implementation when exposure changes.
- Realized risks remain traceable in A19 but are actively controlled through A18.
- Material threshold breaches, new exceptions, or major response changes move through A12.

## Naming standard

Use these canonical repository names:
- SKL-03-11 — Perform Risk Analysis
- SKL-03-12 — Plan Risk Responses
- SKL-04-01 — Implement Risk Responses
- SKL-05-01 — Monitor Risks

Retained shorthand alias:
- SKL-05 — Monitor Risk

## Recommended repo structure

```text
skills/
  03-planning/
    SKL-03-11-perform-risk-analysis.md
    SKL-03-12-plan-risk-responses.md
  04-executing/
    SKL-04-01-implement-risk-responses.md
  05-monitoring-controlling/
    SKL-05-01-monitor-risks.md
repo/
  risk-skills-taxonomy-map.md
  risk-skills-manifest.yaml
  risk-domain-readme.md
```

## Crosswalk

See also:
- `repo/risk-skills-taxonomy-map.md`
- `repo/risk-skills-manifest.yaml`
