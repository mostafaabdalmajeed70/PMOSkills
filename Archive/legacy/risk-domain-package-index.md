# Risk Domain Package Index

**Purpose:** Provide a single package-style index for the generated risk-domain files so they can be located, downloaded, and placed into a repository structure quickly.

## Package contents

| File | Type | Purpose | Suggested repo path |
|---|---|---|---|
| `SKL-04-01-implement-risk-responses.md` | Skill definition | Execution skill for carrying out agreed risk responses and handing them to monitoring | `skills/04-executing/SKL-04-01-implement-risk-responses.md` |
| `SKL-05-01-monitor-risks.md` | Skill definition | Monitoring and controlling skill for tracking risks, response effectiveness, residual exposure, and emergent risks | `skills/05-monitoring-controlling/SKL-05-01-monitor-risks.md` |
| `risk-skills-taxonomy-map.md` | Crosswalk / taxonomy | One-page mapping across the four risk skills, PMBOK8 anchors, artifacts, roles, and outputs | `repo/risk-skills-taxonomy-map.md` |
| `risk-domain-readme.md` | Domain README | Landing page for the risk domain with sequence, artifact model, naming standard, and repo structure | `repo/risk-domain-readme.md` |
| `risk-skills-manifest.json` | Machine-readable manifest | JSON manifest for skills, anchors, artifacts, outputs, and handoffs | `repo/risk-skills-manifest.json` |
| `risk-skills-manifest.yaml` | Machine-readable manifest | YAML manifest for skills, anchors, artifacts, outputs, and handoffs | `repo/risk-skills-manifest.yaml` |

## Suggested repository layout

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
  risk-domain-readme.md
  risk-skills-manifest.json
  risk-skills-manifest.yaml
  risk-domain-package-index.md
```

## Download checklist

- Download the two generated skill files first.
- Download the taxonomy map for human-readable navigation.
- Download the README for the domain landing page.
- Download the JSON and YAML manifests for machine-readable integration.
- Use this index file as the top-level package checklist.

## Notes

- The package is centered on the PMI-aligned risk skill chain and the repository artifact model.
- A19 remains the central risk artifact across the chain, with A18, A12, A16, and optional A20 supporting execution, control, and reserve-related decisions.
- Canonical naming remains `Monitor Risks`, while `Monitor Risk` is retained only as a shorthand alias.
