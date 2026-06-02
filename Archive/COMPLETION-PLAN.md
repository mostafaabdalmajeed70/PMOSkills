---
gov_id: COMPLETION-PLAN-V4
gov_name: PMOSkills Repository Completion Plan v4
version: "4.2.0"
status: Active
authority: PMBOK8 Primary
supersedes: NEXT-STEPS-PLAN.md v3.0.0 · COMPLETION-PLAN.md v4.1.0
file_path: "COMPLETION-PLAN.md"
---

# PMOSkills — Completion Plan v4
**Version:** 4.2.0
**Date:** 2026-06-01
**Repository:** https://github.com/fakhruldeen/PMOSkills
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Supersedes:** NEXT-STEPS-PLAN.md v3.0.0 (2026-05-31) · `COMPLETION-PLAN.md` v4.1.0 (2026-06-01)
**Status:** Active · AI agent executable

> **v4.2.0 update note (2026-06-01):** Phase 0 Structural Cleanup Complete: all legacy root directories and duplicate standards files removed. Staging files in repo/ archived to docs/legacy/. Post-cleanup README alignment to show clean reference/ and artifacts/ structures.

---

## 0. Purpose

This plan defines every remaining work item required to bring the PMOSkills
repository from its current state to a **production-quality, PMO-grade,
AI-executable skills repository** fully grounded in PMI PMBOK 8th Edition
and its companion references.

Structured for AI agent execution. Each phase has:
- A clear **entry condition** (what must be true before starting)
- Explicit **deliverables** with file paths
- A **quality gate** that must pass before the phase is closed
- A **commit convention** for traceability

---

## 1. Current State Assessment (as of 2026-06-01 — v4.1.0)

### 1.1 ✅ Complete

| Layer | Item | Status |
|---|---|---|
| Root governance | README, SKILL-REGISTRY, AUTHORITY-ROUTING, LIFECYCLE-MAP, PRINCIPLES-CROSSWALK, source-authority, pmi_reference_list, MASTER-PLAN, COMPLETION-PLAN-V4, QUALITY-STANDARDS, CHANGELOG | ✅ |
| Repo metadata | LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, .github/ templates | ✅ |
| `docs/` | 9 files: getting-started, how-to-use-skills, how-to-use-artifacts, how-to-use-authority-routing, how-to-contribute, glossary, faq, ai-agent-guide, changelog-guide | ✅ |
| `artifacts/` definitions | A01–A39 canonical definition files | ✅ |
| `artifacts/` templates | 38 template files (B2 complete) | ✅ |
| `artifacts/` examples | 10 example files using Meridian CRM scenario (B3 complete) | ✅ |
| `reference/principles/` | P01–P12 + 00-index.md (C1 complete) | ✅ |
| `reference/performance-domains/` | PD01–PD08 + 00-index.md (C2 complete) | ✅ |
| `reference/focus-areas/` | FA01–FA05 (C3 complete) | ✅ |
| `reference/processes/` | PR11–PR40 + index.md (C4 migration complete) | ✅ |
| Skills scaffolding | 47 skill stubs at v1.1.0 (Packs 01–07) | ✅ |
| Quality standards | `QUALITY-STANDARDS.md` v2.0.0 — §1–§10 complete | ✅ |

### 1.2 ⚠️ Exists But Misplaced or Incomplete

| Item | Problem | Fix |
|---|---|---|
| `reference/processes/` | PR01–PR10 missing (Initiating + early Planning) | Rebuild — Phase 4 |

### 1.3 ❌ Does Not Exist Yet

| Item | Phase |
|---|---|
| `reference/inputs-outputs/inputs-outputs-registry.md` | Phase 4 (C7) |
| `reference/tools-techniques/tools-techniques-registry.md` | Phase 4 (C6) |
| `reference/appendices/X2–X5.md` (4 files) | Phase 4 (C8) |
| `reference/GLOSSARY.md` | Phase 4 (C9) |
| `reference/companion-references/` (23 files) | Phase 4 (C10) — NEW |
| `reference/tailoring/` (9 files) | Phase 4 (C11) — NEW |
| `reference/pmo/` (6 files) | Phase 4 (C12) — NEW |
| PR01–PR10 process records (10 files) | Phase 4 (C4) |
| 47 full skill content files (Packs 01–07) | Phase 3 |
| Pack 08 — PMO Setup and Operations (8 skills) | Phase 3-EXT |
| Pack 09 — Portfolio and Program Management (6 skills) | Phase 3-EXT |
| `shared/` validators, components, routing, checklists (25 files) | Phase 5 |
| `tests/` skill tests + integration tests (69 files) | Phase 6 |
| `docs/ai-agents/source-usage-guide.md`, `audience-guide.md`, `sustainability-guide.md` | Phase 4-NEW |

---

## 2. Quality Standards

> **Single authority: [`QUALITY-STANDARDS.md`](./QUALITY-STANDARDS.md) (v2.0.0)**

All quality standards for this repository — including YAML front-matter schemas, file structure standards, naming conventions, directory rules, source traceability rules, quality gate checklists (universal, per-file-type, and per-phase), enforcement protocols (L1/L2/L3), the NC register, and the AI agent pre-commit checklist — are defined exclusively in **`QUALITY-STANDARDS.md`**.

This file (`COMPLETION-PLAN-V4.md`) does **not** define quality rules. Any apparent conflict between a quality rule in this file and `QUALITY-STANDARDS.md` is resolved in favour of `QUALITY-STANDARDS.md`.

### 2.1 Quick Reference — Where to Find Quality Rules

| Topic | Location in QUALITY-STANDARDS.md |
|---|---|
| File type codes | §1 File Type Registry |
| YAML front-matter schemas (all 9 types) | §2.1–§2.9 |
| Section structure standards (all 9 types) | §3.1–§3.9 |
| File naming conventions | §4 |
| Directory structure and governance | §5 |
| Source traceability and citation rules | §6 |
| Quality gates (universal + per-file-type + per-phase) | §7.1–§7.5 |
| Enforcement protocol (L1/L2/L3) + NC register | §8 |
| AI agent pre-commit checklist (run before every commit) | §9 |

### 2.2 Commit Convention

```
type(scope): short description

Body: what changed and why.
Files: list of files added/modified/deleted.
Phase: which plan phase this commit belongs to.
```

Types: `feat` · `fix` · `docs` · `chore` · `refactor` · `test`
Scopes: `skills` · `artifacts` · `docs` · `reference` · `shared` · `tests` · `root`

Full convention authority: `QUALITY-STANDARDS.md §2.3` (in `MASTER-PLAN.md`).

---

## 3. Canonical Target Structure

Directory rule authority: [`QUALITY-STANDARDS.md §5`](./QUALITY-STANDARDS.md). The tree below is the target state after all phases complete.

```
PMOSkills/
├── [Root governance files — UPPER-KEBAB.md]           ← ✅ Active
├── .github/
│
├── docs/                                               ← ✅ COMPLETE (Phase 1)
│   ├── img/
│   ├── legacy/                                         ← archive location
│   ├── getting-started.md
│   ├── how-to-use-skills.md
│   ├── how-to-use-artifacts.md
│   ├── how-to-use-authority-routing.md
│   ├── how-to-contribute.md
│   ├── glossary.md
│   ├── faq.md
│   ├── ai-agent-guide.md
│   ├── changelog-guide.md
│   ├── source-usage-guide.md                          ← ❌ Phase 4-NEW
│   ├── audience-guide.md                              ← ❌ Phase 4-NEW
│   ├── sustainability-guide.md                        ← ❌ Phase 4-NEW
│   └── skill-reference-map.csv                        ← ❌ Phase 4-NEW (promote from repo/)
│
├── artifacts/                                          ← ✅ COMPLETE (Phases B1+B2+B3)
│   └── [canonical subdirs — see QUALITY-STANDARDS.md §5.1 + MASTER-PLAN.md §1.3]
│
├── skills/                                             ← ❌ PHASE 3 + 3-EXT TARGET
│   ├── 01-organizational-setup/     (3 skills)
│   ├── 02-initiating/               (2 skills)
│   ├── 03-planning/                 (17 skills)
│   ├── 04-executing/                (9 skills)
│   ├── 05-monitoring-controlling/   (9 skills)
│   ├── 06-closing/                  (3 skills)
│   ├── 07-adaptive-hybrid/          (4 skills)
│   ├── 08-pmo-setup-and-operations/ (8 skills — NEW)
│   └── 09-portfolio-and-program/    (6 skills — NEW)
│
├── reference/                                          ← ❌ PHASE 4 TARGET (C4–C12 remaining)
│   ├── README.md
│   ├── GLOSSARY.md                                    ← ❌ Phase 4-C9
│   ├── principles/                                    ← ✅ COMPLETE (C1)
│   ├── performance-domains/                           ← ✅ COMPLETE (C2)
│   ├── focus-areas/                                   ← ✅ COMPLETE (C3)
│   ├── processes/                                     ← 🟡 PARTIAL (C4): PR01–PR10 needed
│   ├── knowledge-areas/                               ← ❌ Phase 0 migration + Phase 4-C5
│   ├── tools-techniques/                              ← ❌ Phase 0 migration + Phase 4-C6
│   ├── inputs-outputs/                                ← ❌ Phase 0 migration + Phase 4-C7
│   ├── appendices/                                    ← ❌ Phase 4-C8
│   ├── companion-references/                          ← ❌ Phase 4-C10 (23 files — NEW)
│   ├── tailoring/                                     ← ❌ Phase 4-C11 (9 files — NEW)
│   └── pmo/                                           ← ❌ Phase 4-C12 (6 files — NEW)
│
├── shared/                                             ← ❌ PHASE 5 TARGET (25 files)
│   ├── README.md
│   ├── validators/
│   ├── checklists/
│   ├── components/
│   └── routing/
│
└── tests/                                              ← ❌ PHASE 6 TARGET (69 files)
    ├── README.md
    ├── skill-tests/                 (61 files: 47 + 14 new)
    └── integration-tests/           (8 files: 6 original + IT-07 + index)
```

---

## 4. Phase Plan

---

### PHASE 0 — Structure Cleanup ✅ COMPLETE
All Phase 0 cleanup operations successfully completed and verified. Stale folders deleted, legacy files archived to `docs/legacy/`, duplicate standards removed, and README documentation fully synchronized.

---

### PHASE 1 — Documentation (`docs/`) ✅ COMPLETE
9/9 files committed 2026-05-31.

---

### PHASE 2 — Artifacts ✅ COMPLETE
B1 (39 definitions) + B2 (38 templates) + B3 (10 examples) committed 2026-05-31.

---

### PHASE 3 — Build Full Skill Content (47 files, Packs 01–07)
**Priority:** 🔴 High
**Sessions:** 6–8
**Entry condition:** Phase 0 + Phase 2 complete
**Commit prefix:** `feat(skills):`
**Quality gate:** `QUALITY-STANDARDS.md §7.2` (skill file gate) + `§7.5 Phase 3 gate`

#### Skill file required structure
See `QUALITY-STANDARDS.md §3.1` for the complete 10-section structure and `§2.1` for the required YAML front-matter. The YAML schema from this file's v4.0.0 is superseded by `QUALITY-STANDARDS.md §2.1`.

#### Build order
| Priority | Skills | Count |
|---|---|---|
| 1 | SKL-01-01, SKL-01-02, SKL-01-03 | 3 |
| 2 | SKL-02-01, SKL-02-02 | 2 |
| 3 | SKL-03-01 → SKL-03-05 | 5 |
| 4 | SKL-03-06 → SKL-03-17 | 12 |
| 5 | SKL-04-01 → SKL-04-09 | 9 |
| 6 | SKL-05-01 → SKL-05-09 | 9 |
| 7 | SKL-06-01 → SKL-06-03 | 3 |
| 8 | SKL-07-01 → SKL-07-04 | 4 |

**Exit gate:** 47/47 skill files fully populated. Every artifact cross-reference resolves. `QUALITY-STANDARDS.md §7.5 Phase 3 gate` passes (P3-01 through P3-04).

---

### PHASE 3-EXT — PMO + PPM Skill Packs (14 files) — NEW
**Priority:** 🔴 High (follows Phase 3)
**Entry condition:** Phase 3 complete
**Commit prefix:** `feat(skills):`
**Authority:** PMO Practice Guide · PMBOK 8 Standard §2 · PMBOK 8 Guide §2.5

| Pack | Skills | Count |
|---|---|---|
| Pack 08 — PMO Setup and Operations | SKL-08-01 → SKL-08-08 | 8 |
| Pack 09 — Portfolio and Program Management | SKL-09-01 → SKL-09-06 | 6 |

Full skill definitions in `MASTER-PLAN.md §5 Phase 3-EXT`.

**Exit gate:** 14/14 Pack 08–09 skill files fully populated. Every file passes `QUALITY-STANDARDS.md §7.2` gate.

---

### PHASE 4 — Complete Reference Layer
**Priority:** 🟡 Medium
**Sessions:** 4–6
**Entry condition:** Phase 0 complete (C5–C7 cleanup done)
**Commit prefix:** `feat(reference):`
**Quality gate:** `QUALITY-STANDARDS.md §7.4` (REF file gate) + `§7.5 Phase 4 gate`

| Sub-phase | Files | Status |
|---|---|---|
| C4 — PR01–PR10 + PR41 | 11 process records | ❌ Rebuild needed |
| C5 — KA Cross-reference | `reference/knowledge-areas/` (migrated from C5) | ⚠️ Migrate + enhance |
| C6 — T&T Taxonomy | `reference/tools-techniques/tools-techniques-registry.md` | ⚠️ Migrate + enhance |
| C7 — I/O Registry | `reference/inputs-outputs/inputs-outputs-registry.md` | ⚠️ Migrate + enhance |
| C8 — Appendices | `reference/appendices/X2-pmo.md`, `X3-ai.md`, `X4-procurement.md`, `X5-evolution.md` | ❌ Not started |
| C9 — Reference GLOSSARY | `reference/GLOSSARY.md` | ❌ Not started |
| C10 — Companion References | 23 files in `reference/companion-references/` | ❌ Not started — NEW |
| C11 — Tailoring Guidance | 9 files in `reference/tailoring/` | ❌ Not started — NEW |
| C12 — PMO Reference Layer | 6 files in `reference/pmo/` | ❌ Not started — NEW |

**Exit gate:** All reference files complete. Every file passes `QUALITY-STANDARDS.md §7.4` gate. `reference/README.md` status = Active.

---

### PHASE 4-NEW — `docs/` Additions
**Priority:** 🔴 High (after Phase 0)
**Commit prefix:** `docs(docs):`

| File | Purpose |
|---|---|
| `docs/ai-agents/source-usage-guide.md` | How to use 23 companion references — short-codes, authority hierarchy, which books apply per phase |
| `docs/skill-reference-map.csv` | Promoted from `repo/` — Skills × PMBOK8 anchor × companion ref mapping |
| `docs/human-practitioners/audience-guide.md` | Usage paths: PMO Director, PM, AI Agent, Book Author |
| `docs/general/sustainability-guide.md` | ESG application within PMBOK 8 context |

---

### PHASE 5 — Shared Components and Validators
**Priority:** 🟡 Medium
**Sessions:** 2
**Entry condition:** Phase 3 complete
**Commit prefix:** `feat(shared):`
**Quality gate:** `QUALITY-STANDARDS.md §7.5 Phase 5 gate`

| Priority | File | Purpose |
|---|---|---|
| 1 | `shared/routing/index.md` | Routing logic catalog |
| 1 | `shared/routing/threshold-router.md` | T1–T4 decision routing logic |
| 1 | `shared/routing/escalation-paths.md` | Escalation path definitions |
| 2 | `shared/validators/index.md` | Validator catalog |
| 2 | `shared/validators/waste-test.md` | Waste detection routine |
| 2 | `shared/validators/artifact-quality-check.md` | Artifact completeness validator |
| 2 | `shared/validators/baseline-integrity-check.md` | Cross-baseline consistency checker |
| 3 | `shared/checklists/` (12 files) | Pack readiness (7) + domain (4) + index (1) |
| 4 | `shared/components/` (7 files) | Field blocks (3) + section patterns (3) + index (1) |

**Exit gate:** All validators produce deterministic PASS/FAIL/WARN output. Every file passes `QUALITY-STANDARDS.md §7.5 Phase 5 gate`.

---

### PHASE 6 — Test Suite
**Priority:** 🟢 Low-Medium
**Sessions:** 2–3
**Entry condition:** Phase 3 + Phase 5 complete
**Commit prefix:** `test(tests):`
**Quality gate:** `QUALITY-STANDARDS.md §7.5 Phase 6 gate`

| File group | Count |
|---|---|
| `tests/skill-tests/ST-SKL-NN-NN.md` (Packs 01–07) | 47 files |
| `tests/skill-tests/ST-SKL-NN-NN.md` (Packs 08–09) | 14 files — NEW |
| `tests/integration-tests/IT-01` through `IT-06` | 6 files |
| `tests/integration-tests/IT-07` | 1 file — NEW |
| `tests/skill-tests/index.md` + `tests/integration-tests/index.md` | 2 files |

Every skill test: ≥ 9 test cases (see `QUALITY-STANDARDS.md §7.5 Phase 6 gate`).
Integration tests: trace artifact flow end-to-end across ≥ 2 lifecycle phases.

**Exit gate:** `QUALITY-STANDARDS.md §7.5 Phase 6 gate` (P6-01 through P6-05) passes.

---

### PHASE 7 — Quality Audit (continuous — after every phase)
**Entry condition:** Completion of any phase or file
**Gate:** `QUALITY-STANDARDS.md §7.5 Phase 7 gate` (Q-01 through Q-06)

Run after every individual file committed, not only at phase end. Full checklist: `QUALITY-STANDARDS.md §9` (AI Agent Pre-Commit Checklist).

---

## 5. Dependency Map (Critical Path)

```
Phase 0 (cleanup: 22 ops)
    │
    ├──► Phase 3 (47 skills, Packs 01–07) ──┬──► Phase 5 (shared: 25 files)
    │         │                            └──► Phase 6 (tests: 69 files) ◄─ Phase 5
    │         └──► Phase 3-EXT (14 skills, Packs 08–09)
    │                   └──► Phase 4-C12 (PMO reference layer)
    │
    ├──► Phase 4 (reference: C4–C12)
    │         ├──► Phase 4-C10 (companion references: 23 files)
    │         └──► Phase 4-C11 (tailoring: 9 files)
    │
    └──► Phase 4-NEW (source-usage-guide + skill-reference-map)

Phase 7 (quality audit) ── continuous ── runs after every file
```

**Immediate critical path:** Phase 0 → Phase 3 → Phase 4 → Phase 5 → Phase 6

---

## 6. Completion Metrics

| Phase | Files to Produce | Priority | Status |
|---|---|---|---|
| Phase 0 | ~22 operations (moves + deletes + README updates) | 🔴 Immediate | ✅ COMPLETE |
| Phase 3 — Skills (Packs 01–07) | 47 | 🔴 High | ❌ |
| Phase 3-EXT — PMO + PPM (Packs 08–09) | 14 | 🔴 High | ❌ NEW |
| Phase 4 — Reference remaining (C4–C12) | 11 processes + 2 registries + 4 appendices + 1 glossary + 23 companion refs + 9 tailoring + 6 PMO = ~56 | 🟡 Medium | ❌ |
| Phase 4-NEW — docs additions | 4 | 🔴 High | ❌ |
| Phase 5 — Shared | 25 | 🟡 Medium | ❌ |
| Phase 6 — Tests | 69 | 🟢 Low-Medium | ❌ |
| **Total remaining** | **~215 files** | | |

---

## 7. Session Execution Protocol

### Session Start
1. Read [`MASTER-PLAN.md`](./MASTER-PLAN.md) to determine current position.
2. Read [`CHANGELOG.md`](./CHANGELOG.md) to confirm last committed version.
3. Read [`QUALITY-STANDARDS.md`](./QUALITY-STANDARDS.md) §9 AI Agent Pre-Commit Checklist before creating any file.
4. Identify the current phase and next unfinished work item.
5. State: “Starting [Phase N], [Work Item], entry condition: [satisfied/not satisfied].”

### Session Work
1. Work one file at a time.
2. After each file: run the full AI Agent Pre-Commit Checklist (`QUALITY-STANDARDS.md §9`).
3. Commit each file individually with a conformant message.
4. Never skip a quality check to save time.

### Session End
1. Update `MASTER-PLAN.md` session log and bump version.
2. Update `CHANGELOG.md`.
3. State which work items are complete and what the next session should start with.

---

## 8. AI Agent Operating Rules

Foundational rules. Full quality enforcement rules in `QUALITY-STANDARDS.md §9.1`.

1. **Never modify a canonical artifact definition file without bumping its version.**
2. **Never create a skill file that references an artifact that does not yet exist** — create the artifact first.
3. **Always check [`MASTER-PLAN.md`](./MASTER-PLAN.md) before starting a session** to avoid duplicating completed work.
4. **Always commit after each file** — not in large batches — to maintain traceability.
5. **Treat every `[FIELD: ...]` placeholder as sacred** — never pre-fill with sample data.
6. **Never cite PMBOK 8 without a section number.**
7. **Apply the waste test to every artifact before committing it.**
8. **When in doubt about scope, authority, or terminology, defer to PMBOK8 as primary source.**
9. **Update `MASTER-PLAN.md` and `CHANGELOG.md` at the end of every session — no exceptions.**
10. **Run the AI Agent Pre-Commit Checklist (`QUALITY-STANDARDS.md §9`) on every file before every commit — no exceptions.**
11. **PMO skills (Pack 08) must cite PMO Practice Guide by chapter and service number.**
12. **Every companion reference file must include the short-code from `pmi_reference_list.md`.**

---

## 9. Immediate Next Actions

| Session | Phase | Work Items |
|---|---|---|
| **Next** | Phase 4 (C4) | Rebuild PR01–PR10 (Initiating + early Planning processes) |
| **+1** | Phase 4 (C4) | Rebuild PR41 (Control Procurements) + PR01–PR10 remainder |
| **+2** | Phase 4 (C6–C7) | Build T&T registry + I/O registry from migrated content |
| **+3** | Phase 4 (C8–C9) | Build 4 appendices + Reference GLOSSARY |
| **+4** | Phase 4 (C10) | Build companion-references/ index + PMO Practice Guide + Book of Forms summaries |
| **+5–+11** | Phase 3 | Build 47 full skill content files (priority order §4) |
| **+13** | Phase 3-EXT | Build Pack 08 (8 PMO skills) |
| **+14** | Phase 3-EXT | Build Pack 09 (6 PPM skills) |
| **+15–+16** | Phase 5 | Build shared validators + components |
| **+17–+19** | Phase 6 | Build test suite (61 skill tests + 8 integration tests) |

---

## 10. Version History

| Version | Date | Changes |
|---|---|---|
| 4.0.0 | 2026-06-01 | Initial creation from NEXT-STEPS-PLAN.md v3.0.0. Full phase plan, quality standards §2.1–§2.6, canonical tree §3, dependency map, metrics, session protocol, 10 operating rules, immediate next actions. |
| 4.1.0 | 2026-06-01 | Removed §2.1–§2.5 inline quality rules (NC-005 resolved). §2 now points exclusively to `QUALITY-STANDARDS.md` v2.0.0. GOV YAML front-matter added. §1.1 updated to include QUALITY-STANDARDS.md. §1.3 updated with new Phase 3-EXT and Phase 4-C10–C12 targets. §3 canonical tree updated to reflect v4.2.0 audit (11 new artifact subdirs, Pack 08–09, all new reference subdirs). §4 Phase gates updated to cite `QUALITY-STANDARDS.md §7`. §7 Session Start updated to read QUALITY-STANDARDS.md §9 first. §8 Operating Rules updated to reference MASTER-PLAN.md (not MASTER-PLAN-V2.md). §9 Immediate Next Actions updated to current state. §10 Version History added. |
| **4.2.0** | **2026-06-01** | **Finalized Phase 0 structural cleanup. Removed all legacy root directories and duplicate standards files. Staging files in repo/ and old artifacts monolith archived to docs/legacy/. Post-cleanup alignment for state assessment, phase plan, immediate next actions, and version scorecard.** |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*
*Source type: PMI-derived + Org-defined*
*Owner: PMO / Repository Governance Authority*
*Approval authority: Repository owner*
*Repository: https://github.com/fakhruldeen/PMOSkills*
*Last Updated: 2026-06-01 · Version 4.2.0*
