# PMOSkills — Completion Plan v4.0
**Version:** 4.0.0
**Date:** 2026-06-01
**Repository:** https://github.com/fakhruldeen/PMOSkills
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Supersedes:** NEXT-STEPS-PLAN.md v3.0.0 (2026-05-31)
**Status:** Active · AI agent executable

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

## 1. Current State Assessment (as of 2026-06-01)

### 1.1 ✅ Complete

| Layer | Item | Status |
|---|---|---|
| Root governance | README, SKILL-REGISTRY, AUTHORITY-ROUTING, LIFECYCLE-MAP, PRINCIPLES-CROSSWALK, source-authority, pmi_reference_list, MASTER-PLAN-V2, CHANGELOG | ✅ |
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

### 1.2 ⚠️ Exists But Misplaced or Incomplete

| Item | Problem | Fix |
|---|---|---|
| `/C4-Process-Records/` (root) | Duplicate of migrated `reference/processes/` | Delete root copy — Phase 0 |
| `/C5-KA-Crossref/` (root) | Content belongs in `reference/` | Audit → migrate → delete — Phase 0 |
| `/C6-TT-Taxonomy/` (root) | Content belongs in `reference/tools-techniques/` | Audit → migrate → delete — Phase 0 |
| `/C7-IO-Registry/` (root) | Content belongs in `reference/inputs-outputs/` | Audit → migrate → delete — Phase 0 |
| `/repo/` (root) | Unknown directory — purpose unclear | Audit → migrate or delete — Phase 0 |
| `reference/C4-Process-Records/` | Source files already migrated | Delete — Phase 0 |
| `reference/C5-KA-Crossref/`, `C6-TT-Taxonomy/`, `C7-IO-Registry/` | Legacy subdirs inside reference/ | Delete after content migration — Phase 0 |
| `reference/processes/` | PR01–PR10 missing (Initiating + early Planning) | Rebuild — Phase 4 |

### 1.3 ❌ Does Not Exist Yet

| Item | Phase |
|---|---|
| `reference/inputs-outputs/inputs-outputs-registry.md` | Phase 4 (C7) |
| `reference/tools-techniques/tools-techniques-registry.md` | Phase 4 (C6) |
| `reference/appendices/X2–X5.md` (4 files) | Phase 4 (C8) |
| `reference/GLOSSARY.md` | Phase 4 (C9) |
| PR01–PR10 process records (10 files) | Phase 4 (C4) |
| 47 full skill content files | Phase 3 |
| `shared/` validators, components, routing, checklists (11 files) | Phase 5 |
| `tests/` skill tests + integration tests (53 files) | Phase 6 |

---

## 2. Quality Standards

### 2.1 Source Traceability
Every claim must cite: `*Authority: [Source] — [Section/Chapter/Page]*`
- PMBOK8 Guide: `§X.X.X`
- PMBOK8 Standard: principle name
- Companion references: short code (WBS-3E, PSS-3E, etc.)
- Synthesis or org-defined: explicitly labeled

### 2.2 Artifact Quality Standard
Every artifact definition must include: `artifact_id`, `artifact_name`, `version`, `status`, `authority`, purpose, inputs, outputs, quality criteria, related artifacts, waste test, migration note.
Every template must include: `[FIELD: description]` placeholders, usage note, parent definition reference.

### 2.3 Skill Quality Standard
Every full skill file must include: ID/name/pack/version/status, Purpose, Scope (includes + excludes), Pre-conditions, numbered Instructions, Inputs table, Outputs table, Authority & Governance (T1–T4), Constraints, Failure Cases, Quality Checks, 2+ Test Cases, PMBOK8 anchor.

### 2.4 Reference File Standard
Every `reference/` file must include: type declaration, PMBOK8 source section, PMI definition (cited), key characteristics, cross-reference table, artifact connections, skill connections, practitioner questions.

### 2.5 Documentation Quality Standard
Every `docs/` file must include: `## Purpose`, `## Audience`, `## Prerequisites`, numbered instructions, cross-references, `## Related Files` table.

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

## 3. Canonical Target Structure

```
PMOSkills/
├── README.md
├── SKILL-REGISTRY.md
├── AUTHORITY-ROUTING.md
├── LIFECYCLE-MAP.md
├── PRINCIPLES-CROSSWALK.md
├── MASTER-PLAN-V2.md
├── COMPLETION-PLAN-V4.md          ← This file
├── CHANGELOG.md
├── source-authority.md
├── pmi_reference_list.md
│
├── docs/                           ← ✅ COMPLETE (Phase 1)
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
├── artifacts/                      ← ✅ COMPLETE (Phases B1+B2+B3)
│   ├── initiation/
│   ├── organizational-setup/
│   ├── planning-and-baselines/
│   ├── monitoring-and-decisions/
│   ├── execution/
│   ├── resources/
│   ├── closing/
│   ├── procurement/
│   ├── adaptive-hybrid/
│   └── organizational/
│
├── skills/                         ← PHASE 3 TARGET
│   ├── 01-organizational-setup/     (3 skills)
│   ├── 02-initiating/               (2 skills)
│   ├── 03-planning/                 (17 skills)
│   ├── 04-executing/                (9 skills)
│   ├── 05-monitoring-controlling/   (9 skills)
│   ├── 06-closing/                  (3 skills)
│   └── 07-adaptive-hybrid/          (4 skills)
│
├── reference/                      ← PHASE 4 TARGET (C4–C9 remaining)
│   ├── README.md
│   ├── principles/                  ← ✅ COMPLETE (C1) — P01–P12 + 00-index
│   ├── performance-domains/         ← ✅ COMPLETE (C2) — PD01–PD08 + 00-index
│   ├── focus-areas/                 ← ✅ COMPLETE (C3) — FA01–FA05
│   ├── processes/                   ← 🟡 PARTIAL (C4) — PR11–PR40 done; PR01–PR10 + PR41 needed
│   │   ├── index.md
│   │   ├── PR01–PR10.md              ← ❌ Rebuild needed
│   │   └── PR11–PR40.md              ← ✅ Done
│   ├── inputs-outputs/              ← ❌ NOT STARTED (C7)
│   │   └── inputs-outputs-registry.md
│   ├── tools-techniques/            ← ❌ NOT STARTED (C6)
│   │   └── tools-techniques-registry.md
│   ├── appendices/                  ← ❌ NOT STARTED (C8)
│   │   ├── X2-pmo.md
│   │   ├── X3-ai.md
│   │   ├── X4-procurement.md
│   │   └── X5-evolution.md
│   └── GLOSSARY.md                  ← ❌ NOT STARTED (C9)
│
├── shared/                         ← PHASE 5 TARGET
│   ├── validators/
│   ├── components/
│   ├── routing/
│   └── checklists/
│
└── tests/                          ← PHASE 6 TARGET
    ├── skill-tests/                 (47 files)
    └── integration-tests/           (6 files)
```

---

## 4. Phase Plan

---

### PHASE 0 — Structure Cleanup
**Priority:** 🔴 Immediate blocker
**Sessions:** 1
**Entry condition:** None
**Commit prefix:** `chore(root):`

Goal: Eliminate all out-of-place directories. No new content until root is clean.

| Step | Action | Target |
|---|---|---|
| 0-A | Audit `/C4-Process-Records/` | Confirm duplicate of `reference/processes/` |
| 0-B | Audit `/C5-KA-Crossref/` | Map files to `reference/` sub-dirs |
| 0-C | Audit `/C6-TT-Taxonomy/` | Map to `reference/tools-techniques/` |
| 0-D | Audit `/C7-IO-Registry/` | Map to `reference/inputs-outputs/` |
| 0-E | Audit `/repo/` | Determine content and destination |
| 0-F | Migrate C5 content | Copy to canonical paths under `reference/` |
| 0-G | Migrate C6 content | Copy to `reference/tools-techniques/` |
| 0-H | Migrate C7 content | Copy to `reference/inputs-outputs/` |
| 0-I | Delete root stale dirs | `/C4-Process-Records/`, `/C5-KA-Crossref/`, `/C6-TT-Taxonomy/`, `/C7-IO-Registry/`, `/repo/` |
| 0-J | Delete `reference/C4-Process-Records/` | Migration complete — remove legacy path |
| 0-K | Delete `reference/C5-KA-Crossref/`, `C6-TT-Taxonomy/`, `C7-IO-Registry/` | After content migrated |
| 0-L | Update `reference/README.md` | Reflect clean structure |

**Exit gate:** No C4/C5/C6/C7 dirs at root or inside `reference/`. All content in canonical paths.

---

### PHASE 1 — Documentation (`docs/`) ✅ COMPLETE
9/9 files committed 2026-05-31.

---

### PHASE 2 — Artifacts ✅ COMPLETE
B1 (39 definitions) + B2 (38 templates) + B3 (10 examples) committed 2026-05-31.

---

### PHASE 3 — Build Full Skill Content (47 files)
**Priority:** 🔴 High
**Sessions:** 6–8
**Entry condition:** Phase 0 + Phase 2 complete
**Commit prefix:** `feat(skills):`

#### Skill file required structure (every file must follow)
```markdown
---
skill_id: SKL-NN-NN
skill_name: [Full skill name]
pack: [Pack number and name]
version: "1.0.0"
status: Active
pmbok8_anchor: "[Section reference]"
focus_area: [Initiating / Planning / Executing / M&C / Closing / Adaptive]
performance_domains: [List]
artifacts_produced: [List of A-IDs]
artifacts_consumed: [List of A-IDs]
authority_threshold: [T1/T2/T3/T4]
---

# SKL-NN-NN — [Skill Name]

## Purpose
## Scope
## Pre-conditions
## Instructions
## Inputs
## Outputs
## Authority and Governance
## Constraints
## Failure Cases
## Quality Checks
## Test Cases
## PMBOK8 Anchor
```

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

**Exit gate:** 47/47 skill files fully populated. Every artifact cross-reference resolves to an existing file.

---

### PHASE 4 — Complete Reference Layer
**Priority:** 🟡 Medium
**Sessions:** 3–4
**Entry condition:** Phase 0 complete (C5–C7 cleanup done)
**Commit prefix:** `feat(reference):`

| Sub-phase | Files | Status |
|---|---|---|
| C4 — PR01–PR10 + PR41 | 11 process records | ❌ Rebuild needed |
| C5 — KA Cross-reference | `reference/inputs-outputs/inputs-outputs-registry.md` | ⚠️ Content exists in C7 — migrate + restructure |
| C6 — T&T Taxonomy | `reference/tools-techniques/tools-techniques-registry.md` | ⚠️ Content exists in C6 — migrate + restructure |
| C7 — I/O Registry | `reference/inputs-outputs/inputs-outputs-registry.md` | ⚠️ Content exists in C7 — migrate + restructure |
| C8 — Appendices | `reference/appendices/X2-pmo.md`, `X3-ai.md`, `X4-procurement.md`, `X5-evolution.md` | ❌ Not started |
| C9 — Reference GLOSSARY | `reference/GLOSSARY.md` | ❌ Not started |

**Exit gate:** All 42 reference files complete. Every file cites a specific PMBOK 8 section. `reference/README.md` status = Active.

---

### PHASE 5 — Shared Components & Validators
**Priority:** 🟡 Medium
**Sessions:** 2
**Entry condition:** Phase 3 complete
**Commit prefix:** `feat(shared):`

| File | Purpose |
|---|---|
| `shared/validators/artifact-waste-test.md` | 10-question universal waste test |
| `shared/validators/skill-quality-check.md` | 15-point skill completeness validator |
| `shared/validators/baseline-integrity-check.md` | Cross-artifact consistency checker |
| `shared/components/field-blocks.md` | Reusable field patterns |
| `shared/components/section-patterns.md` | Common section structures |
| `shared/components/status-indicators.md` | Standard status/RAG values |
| `shared/routing/t1-t4-routing-logic.md` | Machine-readable T1–T4 routing rules |
| `shared/routing/escalation-matrix.md` | Full escalation decision matrix |
| `shared/checklists/phase-entry-checklist.md` | Entry criteria per lifecycle phase |
| `shared/checklists/phase-exit-checklist.md` | Exit criteria per lifecycle phase |
| `shared/checklists/artifact-readiness-checklist.md` | Artifact approval readiness |

**Exit gate:** All validators produce deterministic pass/fail output.

---

### PHASE 6 — Test Suite
**Priority:** 🟢 Low-Medium
**Sessions:** 2–3
**Entry condition:** Phase 3 + Phase 5 complete
**Commit prefix:** `test(tests):`

| File group | Count |
|---|---|
| `tests/skill-tests/ST-SKL-NN-NN.md` | 47 files (min 2 test cases each) |
| `tests/integration-tests/IT-01` through `IT-06` | 6 files |

Integration tests: setup→initiate, initiate→plan, plan→execute, execute→monitor, monitor→close, full lifecycle.

**Exit gate:** Every skill has ≥2 test cases. All 6 integration tests trace artifact flow end-to-end.

---

### PHASE 7 — Quality Audit (continuous — after every phase)
**Entry condition:** Completion of any phase

For every file, verify:
- [ ] YAML front matter complete and valid
- [ ] No `[FIELD: ...]` placeholders accidentally pre-filled in templates
- [ ] All cross-references (artifact IDs, skill IDs, process IDs) resolve to existing files
- [ ] Every PMI citation includes a specific section number
- [ ] No content copied verbatim from PMI copyrighted text
- [ ] Commit message follows §2.6 convention
- [ ] File is in the correct canonical path (§3)
- [ ] Waste test passes for every artifact

---

## 5. Dependency Map (Critical Path)

```
Phase 0 (cleanup) ──┬──► Phase 1 (docs)       ✅ ALREADY COMPLETE
                    │
                    └──► Phase 2 (artifacts)  ✅ ALREADY COMPLETE
                                  │
                                  └──► Phase 3 (skills) ──┬──► Phase 4 (reference remaining)
                                                         ├──► Phase 5 (shared)
                                                         └──► Phase 6 (tests) ◄── Phase 5

Phase 7 (quality audit) ── runs after EVERY phase ── continuous
```

**Immediate critical path:** Phase 0 → Phase 3 → Phase 4 → Phase 5 → Phase 6

---

## 6. Completion Metrics

| Phase | Files to Produce | Priority | Status |
|---|---|---|---|
| Phase 0 | ~40 file moves + ~15 deletes | 🔴 Immediate | ❌ |
| Phase 3 — Skills | 47 | 🔴 High | ❌ |
| Phase 4 — Reference remaining | 11 processes + 2 registries + 4 appendices + 1 glossary = ~18 | 🟡 Medium | ❌ |
| Phase 5 — Shared | 11 | 🟡 Medium | ❌ |
| Phase 6 — Tests | 53 | 🟢 Low-Medium | ❌ |
| **Total remaining** | **~139 files** | | |

---

## 7. Session Execution Protocol

### Session Start
1. Read `MASTER-PLAN-V2.md` to determine current position
2. Read `CHANGELOG.md` to confirm last committed version
3. Identify the current phase and the next unfinished work item
4. State: “Starting [Phase N], [Work Item], entry condition: [satisfied/not satisfied]”

### Session Work
1. Work one file at a time
2. After each file: run the applicable quality check (§2)
3. Commit each file individually with a conformant message
4. Never skip a quality check to save time

### Session End
1. Update `MASTER-PLAN-V2.md` with session summary and version bump
2. Update `CHANGELOG.md`
3. State which work items are complete and what the next session should start with

---

## 8. AI Agent Operating Rules

1. **Never modify a canonical artifact definition file without bumping its version.**
2. **Never create a skill file that references an artifact that does not yet exist** — create the artifact first.
3. **Always check `MASTER-PLAN-V2.md` before starting a session** to avoid duplicating completed work.
4. **Always commit after each file** — not in large batches — to maintain traceability.
5. **Treat every `[FIELD: ...]` placeholder as sacred** — never pre-fill with sample data.
6. **Never cite PMBOK 8 without a section number.**
7. **Apply the waste test to every artifact before committing it.**
8. **When in doubt about scope, authority, or terminology, defer to PMBOK8 as primary source.**
9. **Update `MASTER-PLAN-V2.md` and `CHANGELOG.md` at the end of every session — no exceptions.**
10. **The quality audit checklist (Phase 7) applies to every file, every session.**

---

## 9. Immediate Next Actions

| Session | Phase | Work items |
|---|---|---|
| **Next** | Phase 0 | Audit C4–C7 + `/repo/` → migrate content → delete stale dirs |
| **+1** | Phase 4 (C4) | Rebuild PR01–PR10 (Initiating + early Planning processes) |
| **+2** | Phase 4 (C4) | Rebuild PR41 (Control Procurements) |
| **+3** | Phase 4 (C6–C7) | Build T&T Taxonomy registry + I/O Registry from migrated C6/C7 content |
| **+4** | Phase 4 (C8–C9) | Build 4 appendices + Reference GLOSSARY |
| **+5–+11** | Phase 3 | Build 47 full skill content files (priority order §4) |
| **+12–+13** | Phase 5 | Build shared validators + components |
| **+14–+16** | Phase 6 | Build test suite (47 skill tests + 6 integration tests) |

---

*Plan version: 4.0.0 · Date: 2026-06-01 · Authority: PMBOK8 Primary*
*Repository: https://github.com/fakhruldeen/PMOSkills*
