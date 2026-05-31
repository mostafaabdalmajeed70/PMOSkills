# PMOSkills Repository — Master Development Plan
**Version:** 2.12.0
**Date:** 2026-05-31
**Repository:** [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Status:** Active roadmap — supersedes NEXT-STEPS-PLAN.md v1.0.0 (2026-05-29) and v3.0.0 (2026-05-31)
**Supersedes:** `NEXT-STEPS-PLAN.md` v1.0.0 · `NEXT-STEPS-PLAN.md` v3.0.0

> **v2.12.0 update note (2026-05-31):** Path correction applied — canonical path for C4 processes is `reference/processes/` (not `reference/C4-Process-Records/`). PR11–PR40 exist at root `C4-Process-Records/` and at `reference/C4-Process-Records/` (wrong paths — migration in progress). PR01–PR10 confirmed missing — queued for rebuild. C5/C6/C7 legacy files exist at root and are queued for migration to `reference/`. Session order updated.

---

## 0. Purpose of This Plan

This plan defines every remaining work item required to transform the PMOSkills repository from its current state into a **production-quality, PMO-grade, AI-executable skills repository** that covers the full project lifecycle according to PMI PMBOK 8th Edition and its companion references.

The plan is structured for AI agent execution. Each phase has:
- A clear **entry condition** (what must be true before starting)
- Explicit **deliverables** with file paths
- A **quality gate** that must pass before the phase is closed
- A **commit convention** for traceability

---

## 1. Current State Assessment (as of 2026-05-31 — v2.12.0)

### 1.1 Repository Structure

| Directory / File | Status | Notes |
|---|---|---|
| `README.md` | ✅ v1.3.0 | Updated Patch C |
| `SKILL-REGISTRY.md` | ✅ 54,932 bytes | Full registry — Packs 01–07 |
| `AUTHORITY-ROUTING.md` | ✅ 14,543 bytes | T1–T4 routing complete |
| `LIFECYCLE-MAP.md` | ✅ 12,559 bytes | All 7 packs mapped |
| `PRINCIPLES-CROSSWALK.md` | ✅ 8,110 bytes | 12 principles × domains |
| `pmi_reference_list.md` | ✅ 6,819 bytes | 23 references catalogued |
| `source-authority.md` | ✅ 8,344 bytes | Authority hierarchy documented |
| `CODE_OF_CONDUCT.md` | ✅ Present | Contributor Covenant 2.1 + PMI ethics |
| `CONTRIBUTING.md` | ✅ Present | Full workflow, authority rules, commit conventions |
| `SECURITY.md` | ✅ Present | Secrets, PII, AI agent security |
| `.github/ISSUE_TEMPLATE/` | ✅ Present | 3 templates: bug, content, improvement |
| `.github/pull_request_template.md` | ✅ Present | Full PMBOK-quality PR checklist |
| `MASTER-PLAN-V2.md` | ✅ v2.12.0 | This document — updated 2026-05-31 |
| `CHANGELOG.md` | ✅ Present | Updated 2026-05-31 |
| `LICENSE` | ✅ Present | |
| `.gitignore` | ✅ Present | |

### 1.2 Skills Layer

| Status | Detail |
|---|---|
| Skills scaffolded | ✅ 47 skills at v1.1.0 (Packs 01–07), YAML front matter + Tests table + Change Log present |
| Skills full content | ❌ 0/47 full content files built — **Phase 3 target** |

### 1.3 Artifact Definitions Layer — Phase B1 Complete ✅

All 39 definitions present (A01–A39, A38/A40/A41 consolidated per v1.0.5 rules).

### 1.4 Documentation Layer — Phase 1 COMPLETE ✅

| File | Status | SHA | Committed |
|---|---|---|---|
| `docs/getting-started.md` | ✅ Done | 19cab09a | 2026-05-31 |
| `docs/how-to-use-skills.md` | ✅ Done | 1b710aa9 | 2026-05-31 |
| `docs/ai-agent-guide.md` | ✅ Done | 6097fb1c | 2026-05-31 |
| `docs/how-to-use-artifacts.md` | ✅ Done | 9987331c | 2026-05-31 |
| `docs/changelog-guide.md` | ✅ Done | 36b5aa8f | 2026-05-31 |
| `docs/faq.md` | ✅ Done | 08b30c5c | 2026-05-31 |
| `docs/how-to-use-authority-routing.md` | ✅ Done | d7ad07a5 | 2026-05-31 |
| `docs/how-to-contribute.md` | ✅ Done | 3d5b20bd | 2026-05-31 |
| `docs/glossary.md` | ✅ Done | 9199a797 | 2026-05-31 |

**Phase 1 COMPLETE — 9/9 docs files committed.**

### 1.5 Artifact Templates Layer — Phase B2 COMPLETE ✅

All 38 templates committed. Full inventory in CHANGELOG v2.7.0.

**Phase B2 COMPLETE — 38/38 templates committed.**

### 1.6 Artifact Examples Layer — Phase B3 COMPLETE ✅

All 10 examples use the "Meridian CRM Modernization" scenario (Nexus Solutions Ltd., fictional).

**Phase B3 COMPLETE — 10/10 examples committed.**

### 1.7 Reference Layer — Phase C In Progress 🟡

| Sub-phase | Target | Status |
|---|---|---|
| C1 — 12 Principle files | `reference/principles/P01–P12.md` + `00-index.md` | ✅ COMPLETE — 2026-05-31 |
| C2 — 8 Performance Domain files | `reference/performance-domains/PD01–PD08.md` + `00-index.md` | ✅ COMPLETE — 2026-05-31 |
| C3 — 5 Focus Area files | `reference/focus-areas/FA01–FA05.md` | ✅ COMPLETE — 2026-05-31 |
| C4 — 40 Process records | `reference/processes/PR01–PR40.md` + `00-index.md` | 🟡 Migration in progress — see §1.7.1 |
| C5 — KA Cross-reference Index | `reference/KA-Crossref-Index.md` | 🟡 File exists at root `C5-KA-Crossref/` — migration queued |
| C6 — T&T Taxonomy | `reference/TT-Taxonomy-Index.md` | 🟡 File exists at root `C6-TT-Taxonomy/` — migration queued |
| C7 — I/O Registry | `reference/IO-Registry-Index.md` | 🟡 File exists at root `C7-IO-Registry/` — migration queued |
| C8 — Appendices X2–X5 | `reference/appendices/` | ❌ Not started |
| C9 — Reference GLOSSARY | `reference/GLOSSARY.md` | ❌ Not started |

#### 1.7.1 C4 Process Records — Path Migration Status

**Canonical path:** `reference/processes/` (per §3 target structure)

| File Range | Current Location | Status |
|---|---|---|
| PR01–PR10 | ❌ Missing from repo | Rebuild required |
| PR11–PR40 | `C4-Process-Records/` (root) | 🟡 Migration to `reference/processes/` queued |
| PR11–PR40 | `reference/C4-Process-Records/` | ⚠️ Wrong path — delete after migration |

### 1.8 Shared Layer — Phase D Seeded 🟡

| File | Status |
|---|---|
| `shared/README.md` | ✅ Seeded |
| `shared/validators/artifact-waste-test.md` | ❌ Not built |
| `shared/validators/skill-quality-check.md` | ❌ Not built |
| `shared/validators/baseline-integrity-check.md` | ❌ Not built |
| `shared/components/field-blocks.md` | ❌ Not built |
| `shared/components/section-patterns.md` | ❌ Not built |
| `shared/components/status-indicators.md` | ❌ Not built |
| `shared/routing/t1-t4-routing-logic.md` | ❌ Not built |
| `shared/routing/escalation-matrix.md` | ❌ Not built |
| `shared/checklists/phase-entry-checklist.md` | ❌ Not built |
| `shared/checklists/phase-exit-checklist.md` | ❌ Not built |
| `shared/checklists/artifact-readiness-checklist.md` | ❌ Not built |

### 1.9 Tests Layer — Phase E Seeded 🟡

| File | Status |
|---|---|
| `tests/README.md` | ✅ Seeded |
| `tests/skill-tests/` (47 files) | ❌ Not built |
| `tests/integration-tests/IT-01 through IT-06` | ❌ Not built |

---

## 2. Quality Standards (from Plan v3.0.0 §2)

### 2.1 Source Traceability Standard
- Every claim, process, artifact, or principle reference must cite a specific PMI source using the format: `*Authority: [Source] — [Section/Chapter/Page]*`
- Allowed sources in order of authority:
  1. PMBOK8 Guide (sections cited as `§X.X.X`)
  2. PMBOK8 Standard (principles cited by principle name)
  3. PMI companion references (cited by short code: WBS-3E, PSS-3E, etc.)
  4. Synthesis (explicitly labeled)
  5. Organization-defined (explicitly labeled)
- No unsourced claims about PMI standards or processes.

### 2.2 Artifact Quality Standard
- Every artifact definition must include: `artifact_id`, `artifact_name`, `version`, `status`, `authority`, purpose, inputs, outputs, quality criteria, related artifacts, waste test, migration note.
- Every artifact template must include: `[FIELD: description]` placeholders — no blank fields, usage note at top, parent definition reference in YAML front matter.

### 2.3 Skill Quality Standard (Phase 3)
Every full skill file must include:
- Skill ID, name, pack, version, status
- Purpose (one paragraph)
- Scope — includes AND excludes (explicit)
- Pre-conditions (numbered)
- Step-by-step instructions (numbered, precise, executable)
- Inputs table (source artifact, required?)
- Outputs table (target artifact, quality criterion)
- Authority and Governance (T1–T4 threshold, approver, escalation trigger)
- Constraints (regulatory, process, authority)
- Failure Cases (numbered)
- Quality Checks (numbered pass criteria)
- Test Cases (minimum 2: happy path + failure path)
- PMBOK8 anchor (specific section)

### 2.4 Reference File Standard (Phase C)
Every `reference/` file must include:
- Type declaration (Principle / Performance Domain / Focus Area / Process Record)
- PMBOK8 source section (specific — no vague references)
- PMI definition (cited, not paraphrased without attribution)
- Key characteristics (bulleted, PMI-sourced)
- Relationship to other principles/domains (cross-reference table)
- Artifact connections (which artifacts this governs)
- Skill connections (which skills implement this)
- Practitioner questions (3–5 grounded in the principle/domain/process)

### 2.5 Documentation Quality Standard
Every `docs/` file must include: `## Purpose`, `## Audience`, `## Prerequisites`, numbered instructions (for procedural files), cross-references to related skills and artifacts, `## Related Files` table at bottom.

### 2.6 Commit Convention
```
type(scope): short description

Body: what changed and why.
Files: list of files added/modified/deleted.
Phase: which plan phase this commit belongs to.
```
Types: `feat` · `fix` · `docs` · `chore` · `refactor` · `test`
Scopes: `skills` · `artifacts` · `docs` · `reference` · `shared` · `tests` · `root`

---

## 3. Repository Target Structure

```
PMOSkills/
├── README.md
├── SKILL-REGISTRY.md
├── AUTHORITY-ROUTING.md
├── LIFECYCLE-MAP.md
├── PRINCIPLES-CROSSWALK.md
├── MASTER-PLAN-V2.md
├── CHANGELOG.md
├── source-authority.md
├── pmi_reference_list.md
│
├── docs/                              ← PHASE 1 ✅ COMPLETE
│   ├── img/pmoskills.jpg
│   ├── getting-started.md
│   ├── how-to-use-skills.md
│   ├── how-to-use-artifacts.md
│   ├── how-to-use-authority-routing.md
│   ├── how-to-contribute.md
│   ├── glossary.md
│   ├── faq.md
│   ├── ai-agent-guide.md
│   └── changelog-guide.md
│
├── artifacts/                         ← PHASES B1/B2/B3 ✅ COMPLETE
│   └── [39 definitions + 38 templates + 10 examples]
│
├── skills/                            ← PHASE 3 TARGET
│   ├── 01-organizational-setup/       (3 skills)
│   ├── 02-initiating/                 (2 skills)
│   ├── 03-planning/                   (17 skills)
│   ├── 04-executing/                  (9 skills)
│   ├── 05-monitoring-controlling/     (9 skills)
│   ├── 06-closing/                    (3 skills)
│   └── 07-adaptive-hybrid/            (4 skills)
│
├── reference/                         ← PHASE C TARGET (in progress)
│   ├── principles/                    ← ✅ COMPLETE (C1)
│   ├── performance-domains/           ← ✅ COMPLETE (C2)
│   ├── focus-areas/                   ← ✅ COMPLETE (C3)
│   ├── processes/                     ← 🟡 IN PROGRESS (C4) — migration + PR01–PR10 rebuild
│   │   ├── 00-index.md
│   │   ├── PR01-develop-project-charter.md
│   │   ├── PR02-identify-stakeholders.md
│   │   ├── ... PR03–PR40
│   ├── KA-Crossref-Index.md           ← 🟡 Migration queued (C5)
│   ├── TT-Taxonomy-Index.md           ← 🟡 Migration queued (C6)
│   ├── IO-Registry-Index.md           ← 🟡 Migration queued (C7)
│   ├── appendices/                    ← ❌ NOT STARTED (C8)
│   └── GLOSSARY.md                    ← ❌ NOT STARTED (C9)
│
├── shared/                            ← PHASE D TARGET
└── tests/                             ← PHASE E TARGET
```

---

## 4. Master Build Roadmap

### Phase A — Stabilize and QA ✅ COMPLETE (2026-05-30)

### Phase 1 — Documentation Layer (`docs/`) ✅ COMPLETE (2026-05-31)

### Phase B — Artifact Templates and Examples ✅ COMPLETE (2026-05-31)
- B1: Definitions (39 total) ✅
- B2: Templates (38 total) ✅
- B3: Examples (10 total) ✅

### Phase C — Reference Layer 🟡 IN PROGRESS

**Entry condition:** Phase B complete ✅  
**Exit quality gate:** All 12 principle files, 8 performance domain files, 5 focus area files, 40 process records, KA cross-reference index, T&T taxonomy, I/O registry, and 4 appendix files complete. Each sourced to a specific PMBOK 8 section.

| Sub-phase | Deliverables | Count | Status |
|---|---|---|---|
| C1 | `reference/principles/P01–P12.md` + `00-index.md` | 13 files | ✅ COMPLETE — 2026-05-31 |
| C2 | `reference/performance-domains/PD01–PD08.md` + `00-index.md` | 9 files | ✅ COMPLETE — 2026-05-31 |
| C3 | `reference/focus-areas/FA01–FA05.md` | 5 files | ✅ COMPLETE — 2026-05-31 |
| C4 | `reference/processes/PR01–PR40.md` + `00-index.md` | 41 files | 🟡 PR11–PR40 migration + PR01–PR10 rebuild |
| C5 | `reference/KA-Crossref-Index.md` | 1 file | 🟡 Migration queued |
| C6 | `reference/TT-Taxonomy-Index.md` | 1 file | 🟡 Migration queued |
| C7 | `reference/IO-Registry-Index.md` | 1 file | 🟡 Migration queued |
| C8 | `reference/appendices/X2–X5.md` | 4 files | ❌ Not started |
| C9 | `reference/GLOSSARY.md` | 1 file | ❌ Not started |

### Phase 3 — Build Full Skill Content (47 files) ❌ NOT STARTED

**Entry condition:** Phase C complete (reference files cited by skills)  
**Exit quality gate:** All 47 skill files pass §2.3 Skill Quality Standard. Each cross-checked against its PMBOK 8 anchor section.

**Skill build priority order:**

| Priority | Skills | Reason |
|---|---|---|
| 1 | SKL-01-01, SKL-01-02, SKL-01-03 | Foundation — organizational setup gates all else |
| 2 | SKL-02-01, SKL-02-02 | Initiating — Charter and Stakeholder identification gate all planning |
| 3 | SKL-03-01 through SKL-03-05 | Core planning (Tailoring, Scope, WBS, Requirements) |
| 4 | SKL-03-06 through SKL-03-17 | Remaining planning skills |
| 5 | SKL-04-01 through SKL-04-09 | Executing skills |
| 6 | SKL-05-01 through SKL-05-09 | Monitoring & Controlling |
| 7 | SKL-06-01 through SKL-06-03 | Closing |
| 8 | SKL-07-01 through SKL-07-04 | Adaptive & Hybrid |

### Phase D — Shared Components and Validators ❌ NOT STARTED

**Entry condition:** Phase 3 complete  

### Phase E — Test Suite ❌ NOT STARTED

**Entry condition:** Phase 3 and Phase D complete  

### Phase F — Extended Packs (PMO + AI) ❌ NOT STARTED
### Phase G — MCP Server Design ❌ NOT STARTED
### Phase H — AI Agent Design ❌ NOT STARTED
### Phase I — Book Authoring Track ❌ NOT STARTED

### Phase 7 (Quality Audit) — Ongoing After Each Phase

For each file produced, the AI agent must verify:
- [ ] YAML front matter complete and valid
- [ ] All `[FIELD: ...]` placeholders present in templates (none pre-filled)
- [ ] All cross-references resolve to files that exist
- [ ] Every PMI citation includes a specific section reference (no vague "PMBOK 8" citations)
- [ ] Waste test passes (artifact is not redundant)
- [ ] Commit message follows convention (§2.6)
- [ ] File is in the correct directory per target structure (§3)
- [ ] No content copied verbatim from PMI copyrighted text

---

## 5. Dependency Map

```
Phase 1 (docs/)           ✅ COMPLETE
Phase B (artifacts)       ✅ COMPLETE
Phase C (reference)       🟡 IN PROGRESS — no dependency on Phase 3
Phase 3 (skill content)   ← Requires Phase B complete ✅ + Phase C complete
Phase D (shared)          ← Requires Phase 3 complete
Phase E (tests)           ← Requires Phase 3 + Phase D complete
Phase 7 (quality audit)   ← Runs after EACH phase — continuous
```

---

## 6. Execution Scorecard

| Phase | Deliverable | Target | Status |
|---|---|---|---|
| A | QA all 47 skills → v1.1.0 | 47 skills | ✅ Complete — 2026-05-30 |
| B1 | Artifact definitions | 39 | ✅ Complete — 2026-05-30 |
| B2 | Artifact templates | 38 | ✅ Complete — 2026-05-31 |
| B3 | Artifact examples | 10 | ✅ Complete — 2026-05-31 |
| Phase 1 | docs/ documentation | 9 | ✅ Complete — 2026-05-31 |
| C1 | Reference: 12 principles | 13 files | ✅ Complete — 2026-05-31 |
| C2 | Reference: 8 performance domains | 9 files | ✅ Complete — 2026-05-31 |
| C3 | Reference: 5 focus areas | 5 files | ✅ Complete — 2026-05-31 |
| C4 | Reference: 40 processes | 41 files | 🟡 PR11–PR40 migration + PR01–PR10 rebuild |
| C5 | KA Cross-reference Index | 1 file | 🟡 Migration queued |
| C6 | T&T Taxonomy Index | 1 file | 🟡 Migration queued |
| C7 | I/O Registry Index | 1 file | 🟡 Migration queued |
| C8–C9 | Appendices + GLOSSARY | 5 | ❌ |
| Phase 3 | 47 full skill content files | 47 | ❌ |
| Phase D | Shared components + validators | 11 | ❌ |
| Phase E | Test suite | 53 | ❌ |
| Phase F | Extended packs PMO + AI | 10 skills | ❌ |
| Phase G | MCP Server design | TBD | ❌ |
| Phase H | AI Agent definitions | TBD | ❌ |
| Phase I | Book authoring | TBD | ❌ |

---

## 7. Recommended Session Order

1. ~~Phase C1 — 12 principle files + index~~ ✅ COMPLETE
2. ~~Phase C2 — 8 performance domain files + index~~ ✅ COMPLETE
3. ~~Phase C3 — 5 focus area files~~ ✅ COMPLETE
4. ~~Phase C4 Batch 1 — PR01–PR10 (Initiating + Scope chain + Schedule chain)~~ ✅ FILES LOST — rebuild queued
5. **Current session:** C4 path fix — migrate PR11–PR40 to `reference/processes/`; migrate C5/C6/C7 to `reference/`; rebuild PR01–PR10; push `00-index.md`; delete old root directories
6. **Session +1:** C8 — 4 appendix files (`reference/appendices/X2–X5.md`)
7. **Session +2:** C9 — Reference GLOSSARY (`reference/GLOSSARY.md`)
8. **Session +3:** Phase 3 — Skill content Pack 01 + Pack 02 (5 skills)
9. **Sessions +4–7:** Phase 3 — Remaining 42 skill files
10. **Sessions +8–9:** Phase D (shared) + Phase E (tests)
11. **Sessions beyond:** Phase F, G, H, I

---

## 8. AI Agent Operating Rules (Plan v3.0.0 §10 — preserved verbatim)

1. **Never modify a canonical artifact definition file without bumping its version.**
2. **Never create a skill file that references an artifact that does not yet exist** — create the artifact first.
3. **Always check `MASTER-PLAN-V2.md` before starting a session** to avoid duplicating completed work.
4. **Always commit after each file** — not in large batches — to maintain traceability.
5. **Treat every `[FIELD: ...]` placeholder as sacred** — they must appear in templates exactly as specified, never pre-filled with sample data.
6. **Never cite PMBOK 8 without a section number.**
7. **Apply the waste test to every artifact before committing it** — if it fails, revise or consolidate.
8. **When in doubt about scope, authority, or terminology, defer to PMBOK8 as primary source.**
9. **Update MASTER-PLAN-V2.md and CHANGELOG.md at the end of every session — no exceptions.**
10. **The quality audit checklist (§4 Phase 7) applies to every file, every session.**

---

## 9. Version History of This Plan

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-05-29 | Initial plan |
| 2.0.0 | 2026-05-30 | Full rebuild |
| 2.1.0 | 2026-05-30 | Skills inventory corrected |
| 2.2.0 | 2026-05-30 | Phase A complete |
| 2.3.0 | 2026-05-30 | Phase B1 complete |
| 2.4.0 | 2026-05-30 | Duplicates deleted · B2 progress table added |
| 2.5.0 | 2026-05-31 | Phase 1 opened · B2 Batch 3 started |
| 2.6.0 | 2026-05-31 | Phase 1 COMPLETE · B2 expanded to 24 templates |
| 2.7.0 | 2026-05-31 | Phase B2 COMPLETE (38/38) · Phase B3 COMPLETE (10/10) |
| 2.8.0 | 2026-05-31 | Merged Plan v3.0.0 — added Phase 3 (skills), Phase D (shared), Phase E (tests), quality standards §2, dependency map, completion metrics, session order; Phase C1 in progress |
| 2.9.0 | 2026-05-31 | Phase C1 COMPLETE (13 files: P01–P12 + index) · Phase C2 + C3 in progress |
| 2.10.0 | 2026-05-31 | Phase C2 COMPLETE (9 files: PD01–PD08 + index) · Phase C3 COMPLETE (5 files: FA01–FA05) · Phase C4 in progress |
| 2.11.0 | 2026-05-31 | Phase C4 Batch 1 COMPLETE (PR01–PR10 committed — now confirmed missing; rebuild queued) · PR11–PR40 committed to wrong paths |
| 2.12.0 | 2026-05-31 | Path correction — canonical C4 path = `reference/processes/` · C5/C6/C7 legacy files identified at root · PR01–PR10 confirmed missing · Full migration plan documented · Session order updated |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*
*Repository: [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)*
*Maintainer: @fakhruldeen*
*Last Updated: 2026-05-31 · Version 2.12.0*
