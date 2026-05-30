# reference/ — PMBOK 8 Reference Layer
**Status:** Planned · Not yet built
**Version:** 0.1.0-planned
**Authority:** PMBOK8 Primary · PMI Companion References Secondary
**File Path:** `reference/README.md`

---

## Purpose

This directory will contain the authoritative PMBOK 8 reference layer — structured, source-grounded content for every principle, performance domain, focus area, process, input/output, tool/technique, and appendix. It is designed to support book authoring, AI agent knowledge bases, and MCP server resource endpoints.

---

## Planned Structure

```
reference/
├── README.md                          ← This file
├── principles/
│   ├── index.md                       ← [planned] All 12 PMBOK 8 principles overview
│   ├── P01-stewardship.md             ← [planned]
│   ├── P02-team.md                    ← [planned]
│   ├── P03-stakeholders.md            ← [planned]
│   ├── P04-value.md                   ← [planned]
│   ├── P05-systems-thinking.md        ← [planned]
│   ├── P06-leadership.md              ← [planned]
│   ├── P07-tailoring.md               ← [planned]
│   ├── P08-quality.md                 ← [planned]
│   ├── P09-complexity.md              ← [planned]
│   ├── P10-risk.md                    ← [planned]
│   ├── P11-adaptability.md            ← [planned]
│   └── P12-change.md                  ← [planned]
├── performance-domains/
│   ├── index.md                       ← [planned] All 8 performance domains overview
│   ├── PD01-stakeholders.md           ← [planned]
│   ├── PD02-team.md                   ← [planned]
│   ├── PD03-development-approach.md   ← [planned]
│   ├── PD04-planning.md               ← [planned]
│   ├── PD05-project-work.md           ← [planned]
│   ├── PD06-delivery.md               ← [planned]
│   ├── PD07-measurement.md            ← [planned]
│   └── PD08-uncertainty.md            ← [planned]
├── focus-areas/
│   ├── index.md                       ← [planned] All 5 focus areas with artifact triggers
│   ├── FA01-initiating.md             ← [planned]
│   ├── FA02-planning.md               ← [planned]
│   ├── FA03-executing.md              ← [planned]
│   ├── FA04-monitoring-controlling.md ← [planned]
│   └── FA05-closing.md                ← [planned]
├── processes/
│   ├── index.md                       ← [planned] All 40 processes with I/O/T&T
│   └── [40 process files]             ← [planned] One file per PMBOK 8 process
├── inputs-outputs/
│   └── inputs-outputs-registry.md     ← [planned] All 40 process I/O per PMBOK 8 §4
├── tools-techniques/
│   └── tools-techniques-registry.md   ← [planned] All tools and techniques per PMBOK 8 §5
└── appendices/
    ├── X2-pmo.md                      ← [planned] PMO appendix
    ├── X3-ai.md                       ← [planned] AI governance appendix
    ├── X4-procurement.md              ← [planned] Procurement appendix
    └── X5-evolution.md                ← [planned] PMBOK evolution appendix
```

---

## Build Priority

| Priority | Directory | Rationale |
|----------|-----------|----------|
| 1 | `principles/` | Foundational — referenced by every skill |
| 2 | `performance-domains/` | Core PMBOK 8 structure |
| 3 | `focus-areas/` | Lifecycle navigation |
| 4 | `processes/` | Largest body of work — 40 files |
| 5 | `inputs-outputs/` | Registry format — builds on processes |
| 6 | `tools-techniques/` | Registry format |
| 7 | `appendices/` | Supplementary |

---

## Dependencies

- `SKILL-REGISTRY.md` — skills reference process anchors defined here
- `PRINCIPLES-CROSSWALK.md` — will draw from `principles/` content
- MCP server resource endpoints will serve content from this directory
- Book authoring chapters will draw source content from `processes/` and `principles/`

---

*Status: Planned · Build begins after artifact layer complete · Authority: PMBOK8 Primary*
*Last Updated: 2026-05-30 · Patch I*
