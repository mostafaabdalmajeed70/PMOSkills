# reference/ — PMBOK 8 Reference Layer

**Status:** Partially Built · In Active Development
**Version:** 1.0.0
**Authority:** PMBOK8 Primary · PMI Companion References Secondary
**File Path:** `reference/README.md`
**Last Updated:** 2026-06-01 · Phase 0 — Structural Cleanup

---

## Purpose

This directory contains the authoritative PMBOK 8 reference layer — structured, source-grounded content for every principle, performance domain, focus area, process, input/output, tool/technique, and appendix. It is designed to support book authoring, AI agent knowledge bases, and MCP server resource endpoints.

---

## Current State

```
reference/
├── README.md                                    ← This file
├── processes/                                   ← ✅ COMPLETE (42 files)
│   ├── 00-index.md                              ← Master index of all 40 processes
│   ├── index.md                                 ← Navigation index
│   └── PR01–PR40 *.md                           ← One file per PMBOK 8 process (40 files)
├── knowledge-areas/                             ← ✅ COMPLETE (1 file)
│   └── KA-Crossref-Index.md                     ← Knowledge Area cross-reference index
├── tools-techniques/                            ← ✅ COMPLETE (1 file)
│   └── TT-Taxonomy-Index.md                     ← Tools & Techniques taxonomy
├── inputs-outputs/                              ← ✅ COMPLETE (1 file)
│   └── IO-Registry-Index.md                     ← Master I/O registry (73 artifacts, 40 processes)
├── principles/                                  ← [planned]
│   ├── index.md
│   ├── P01-stewardship.md
│   ├── P02-team.md
│   ├── P03-stakeholders.md
│   ├── P04-value.md
│   ├── P05-systems-thinking.md
│   ├── P06-leadership.md
│   ├── P07-tailoring.md
│   ├── P08-quality.md
│   ├── P09-complexity.md
│   ├── P10-risk.md
│   ├── P11-adaptability.md
│   └── P12-change.md
├── performance-domains/                         ← [planned]
│   ├── index.md
│   ├── PD01-stakeholders.md
│   ├── PD02-team.md
│   ├── PD03-development-approach.md
│   ├── PD04-planning.md
│   ├── PD05-project-work.md
│   ├── PD06-delivery.md
│   ├── PD07-measurement.md
│   └── PD08-uncertainty.md
├── focus-areas/                                 ← [planned]
│   ├── index.md
│   ├── FA01-initiating.md
│   ├── FA02-planning.md
│   ├── FA03-executing.md
│   ├── FA04-monitoring-controlling.md
│   └── FA05-closing.md
└── appendices/                                  ← [planned]
    ├── X2-pmo.md
    ├── X3-ai.md
    ├── X4-procurement.md
    └── X5-evolution.md
```

---

## Build Status

| Directory | Status | Files | Notes |
|---|---|---|---|
| `processes/` | ✅ Complete | 42 | PR01–PR40 + 2 index files |
| `knowledge-areas/` | ✅ Complete | 1 | KA cross-reference index |
| `tools-techniques/` | ✅ Complete | 1 | TT taxonomy index |
| `inputs-outputs/` | ✅ Complete | 1 | IO master registry (73 artifacts) |
| `principles/` | ⏳ Planned | 0 | 12 files + index |
| `performance-domains/` | ⏳ Planned | 0 | 8 files + index |
| `focus-areas/` | ⏳ Planned | 0 | 5 files + index |
| `appendices/` | ⏳ Planned | 0 | 4 files |

---

## Build Priority

| Priority | Directory | Rationale |
|---|---|---|
| 1 | `principles/` | Foundational — referenced by every skill |
| 2 | `performance-domains/` | Core PMBOK 8 structure |
| 3 | `focus-areas/` | Lifecycle navigation |
| 4 | `appendices/` | Supplementary |

---

## Key Reference Files

| File | Description |
|---|---|
| `processes/00-index.md` | Master index of all 40 PMBOK processes |
| `processes/PR01–PR40` | Individual process records with I/T&T/O |
| `knowledge-areas/KA-Crossref-Index.md` | KA → Process cross-reference |
| `tools-techniques/TT-Taxonomy-Index.md` | Full TT taxonomy (PMBOK 8) |
| `inputs-outputs/IO-Registry-Index.md` | 73 artifacts × 40 processes registry |

---

## Dependencies

- `SKILL-REGISTRY.md` — skills reference process anchors defined in `processes/`
- `PRINCIPLES-CROSSWALK.md` — will draw from `principles/` content when built
- MCP server resource endpoints will serve content from this directory
- Book authoring chapters draw source content from `processes/` and `principles/`

---

*Authority: PMBOK 8th Edition Primary | Process Groups Practice Guide Secondary*
*Phase 0 — Structural Cleanup complete 2026-06-01*
