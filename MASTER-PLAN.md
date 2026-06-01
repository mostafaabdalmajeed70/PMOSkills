# PMOSkills Repository — Master Development Plan
**Version:** 4.2.0
**Date:** 2026-06-01
**Repository:** [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)
**Authority:** PMBOK 8 Primary · PMI Companion References Secondary
**Status:** Active roadmap
**Supersedes:** `NEXT-STEPS-PLAN.md` v1.0.0 · `NEXT-STEPS-PLAN.md` v3.0.0 · `MASTER-PLAN-V2.md` v2.12.0 (2026-05-31)

> **v4.2.0 update note (2026-06-01):** Full repository directory audit completed. Every directory crawled and compared against the canonical intended structure. Critical new findings: (1) `artifacts/` has 17 subdirs vs 6 documented — 11 undocumented dirs need audit and README update; (2) `repo/` contains 7 identifiable legacy files that need audit and archival/deletion; (3) `C4-Process-Records/` root contains 30 old pre-migration PR files (PR11–PR40) confirmed as duplicates of `reference/processes/`; (4) C5/C6/C7 all contain live content that must be migrated before deletion; (5) `reference/` has 4 stale legacy subdirs still present; (6) `reference/` is missing `tools-techniques/`, `inputs-outputs/`, and `appendices/` subdirs. All findings added as critical Phase 0 tasks. Phase 0 now has 22 distinct operations.

---

## 0. Purpose

This is the active session tracking plan for the PMOSkills repository. For the full phase-by-phase completion plan, see [`COMPLETION-PLAN-V4.md`](./COMPLETION-PLAN-V4.md).

This document tracks:
- Current state of every layer (from live directory audit)
- Session-by-session progress log
- Scorecard against all known targets

---

## 1. Live Directory Audit (as of 2026-06-01 — v4.2.0)

### 1.1 Root Level — Files

| File | Status | Notes |
|---|---|---|
| `README.md` | ⚠️ Stale | References C4-Process-Records/ and C5-KA-Crossref/ paths — must be updated post-Phase 0 (P0-M) |
| `MASTER-PLAN.md` | ✅ Current | This file |
| `COMPLETION-PLAN-V4.md` | ✅ Current | Full phase plan |
| `SKILL-REGISTRY.md` | ✅ | Master skill index v1.3.0 |
| `AUTHORITY-ROUTING.md` | ✅ | T1–T4 threshold model |
| `LIFECYCLE-MAP.md` | ✅ | Phase-by-phase lifecycle flow |
| `PRINCIPLES-CROSSWALK.md` | ✅ | 12 principles × 11 domains matrix |
| `source-authority.md` | ✅ | Source authority rules |
| `pmi_reference_list.md` | ✅ | Canonical PMI reference list |
| `CHANGELOG.md` | ✅ | Change log |
| `CONTRIBUTING.md` | ✅ | Contribution rules |
| `CODE_OF_CONDUCT.md` | ✅ | Code of conduct |
| `SECURITY.md` | ✅ | Security policy |
| `LICENSE` | ✅ | License |
| `.gitignore` | ✅ | Git ignore rules |

### 1.2 Root Level — Directories

| Directory | Actual Contents | Status | Action Required |
|---|---|---|---|
| `.github/` | Issue/PR templates | ✅ Correct | None |
| `docs/` | 9 documentation files + img/ | ✅ Complete | None |
| `artifacts/` | **17 subdirs** (see §1.3 below) | ⚠️ Undocumented dirs | Audit + update README |
| `skills/` | 7 pack dirs (01–07) | ✅ Structure correct | Build content (Phase 3) |
| `reference/` | 9 subdirs incl. 4 stale legacy (see §1.4) | ⚠️ Mixed state | Phase 0 cleanup |
| `shared/` | README.md only | ✅ Seeded | Build content (Phase 5) |
| `tests/` | README.md only | ✅ Seeded | Build content (Phase 6) |
| **`C4-Process-Records/`** | **30 files PR11–PR40** | **❌ STALE ROOT DIR** | **Verify duplicates → Delete** |
| **`C5-KA-Crossref/`** | **1 file: KA-Crossref-Index.md (15KB)** | **❌ LIVE CONTENT IN WRONG PLACE** | **Migrate → Delete** |
| **`C6-TT-Taxonomy/`** | **1 file: TT-Taxonomy-Index.md (16KB)** | **❌ LIVE CONTENT IN WRONG PLACE** | **Migrate → Delete** |
| **`C7-IO-Registry/`** | **1 file: IO-Registry-Index.md (13KB)** | **❌ LIVE CONTENT IN WRONG PLACE** | **Migrate → Delete** |
| **`repo/`** | **7 legacy staging files** | **❌ UNPLANNED LEGACY DIR** | **Audit each → Archive or Delete** |

### 1.3 `artifacts/` — Full Subdirectory Audit

Root README documents **6 subdirs**. Actual count: **17 subdirs**.

| Subdir | In README? | Status | Action |
|---|---|---|---|
| `closing/` | ✅ Yes | Present | Audit content; confirm correct |
| `monitoring-and-decisions/` | ✅ Yes | Present | Audit content; confirm correct |
| `planning-and-baselines/` | ✅ Yes | Present | Audit content; confirm correct |
| `procurement/` | ✅ Yes | Present | Audit content; confirm correct |
| `resources/` | ✅ Yes | Present | Audit content; confirm correct |
| `stakeholders/` | ✅ Yes | Present | Audit content; confirm correct |
| **`closure/`** | **❌ No** | **Undocumented** | **Audit → consolidate into `closing/` or document** |
| **`communications/`** | **❌ No** | **Undocumented** | **Audit → determine canonical dir** |
| **`extended-procurement/`** | **❌ No** | **Undocumented** | **Audit → consolidate into `procurement/` or document** |
| **`extended-resources/`** | **❌ No** | **Undocumented** | **Audit → consolidate into `resources/` or document** |
| **`governance/`** | **❌ No** | **Undocumented** | **Audit → determine if correct canonical dir** |
| **`initiating/`** | **❌ No** | **Undocumented** | **Audit → determine canonical dir** |
| **`knowledge/`** | **❌ No** | **Undocumented** | **Audit → determine canonical dir** |
| **`pmo/`** | **❌ No** | **Undocumented** | **Audit → determine canonical dir** |
| **`portfolio/`** | **❌ No** | **Undocumented** | **Audit → determine canonical dir** |
| **`quality/`** | **❌ No** | **Undocumented** | **Audit → determine canonical dir** |
| **`stakeholders-communications/`** | **❌ No** | **Undocumented** | **Audit → consolidate into `stakeholders/` or `communications/`** |
| **`team-resources/`** | **❌ No** | **Undocumented** | **Audit → consolidate into `resources/` or document** |

> **Critical:** README.md documents only 6 artifact subdirs. 11 additional dirs exist. These may contain valid content (from earlier sessions) that is simply undocumented, or may be redundant/misnamed. Full content audit of each required before any consolidation.

### 1.4 `reference/` — Full Subdirectory Audit

| Subdir | Status | Action |
|---|---|---|
| `principles/` | ✅ Complete (C1) | None |
| `performance-domains/` | ✅ Complete (C2) | None |
| `focus-areas/` | ✅ Complete (C3) | None |
| `processes/` | ✅ PR11–PR40 + index.md | Build PR01–PR10 + PR41 (Phase 4) |
| `README.md` | ⚠️ Stale | Update to show current state + canonical subdirs (P0-N) |
| **`C4-Process-Records/`** | **❌ Legacy subdir** | **Delete (confirmed empty / duplicate)** |
| **`C5-KA-Crossref/`** | **❌ Legacy subdir** | **Delete after C5 root migration** |
| **`C6-TT-Taxonomy/`** | **❌ Legacy subdir** | **Delete after C6 root migration** |
| **`C7-IO-Registry/`** | **❌ Legacy subdir** | **Delete after C7 root migration** |
| **`tools-techniques/`** | **❌ MISSING** | **Create after C6 migration (Phase 4-C6)** |
| **`inputs-outputs/`** | **❌ MISSING** | **Create after C7 migration (Phase 4-C7)** |
| **`appendices/`** | **❌ MISSING** | **Create in Phase 4-C8** |
| **`GLOSSARY.md`** | **❌ MISSING** | **Create in Phase 4-C9** |

### 1.5 `repo/` — Legacy File Audit

| File | Size | Content | Disposition |
|---|---|---|---|
| `Artifacts-V-1.0.5-export-4.md` | 82KB | Old monolithic artifacts export (pre-split) | Archive to `docs/legacy/` |
| `Skill-PMBOK8anchor-Corepurpose-Primaryartifacts-Ma.csv` | 3.5KB | Skills × PMBOK8 anchor CSV mapping | Move to `docs/` or `shared/` as reference data |
| `risk-domain-package-index.md` | 2.5KB | Risk domain package index | Audit — may belong in `reference/` |
| `risk-domain-readme.md` | 2.9KB | Risk domain readme | Audit — may belong in `docs/` |
| `risk-skills-manifest.json` | 3.2KB | Risk skills machine manifest | Audit — may belong in `shared/` |
| `risk-skills-manifest.yaml` | 2.4KB | Risk skills YAML manifest | Audit — may belong in `shared/` |
| `risk-skills-taxonomy-map.md` | 4.8KB | Risk skills taxonomy map | Audit — may belong in `reference/` |

---

## 2. Quality Standards

See [`COMPLETION-PLAN-V4.md §2`](./COMPLETION-PLAN-V4.md) for full quality standards.

Short reference:
- **§2.1** Source traceability: every claim cites `*Authority: [Source] — [§X.X.X]*`
- **§2.2** Artifact quality: artifact_id + purpose + inputs + outputs + waste test required
- **§2.3** Skill quality: 14-section structure required for every full skill file
- **§2.4** Reference file quality: type + PMBOK8 source + PMI definition + cross-refs required
- **§2.5** Documentation quality: Purpose + Audience + Prerequisites + Related Files required
- **§2.6** Commit convention: `type(scope): description` with Body + Files + Phase

---

## 3. Canonical Target Structure

The full annotated tree is in [`COMPLETION-PLAN-V4.md §3`](./COMPLETION-PLAN-V4.md).

For `shared/` and `tests/` canonical structures, see `MASTER-PLAN.md §3.1` and `§3.2` (v4.1.0 — those sections still apply).

---

## 4. Phase Roadmap

| Phase | Name | Entry Condition | Status |
|---|---|---|---|
| **Phase 0** | Full Structural Cleanup (22 ops) | None | ❌ **NEXT — START HERE** |
| Phase 1 | Documentation (`docs/`) | Phase 0 | ✅ COMPLETE (2026-05-31) |
| Phase 2 (B1+B2+B3) | Artifacts | Phase 0 | ✅ COMPLETE (2026-05-31) |
| Phase 3 | Full Skill Content (47 files) | Phase 0 + Phase 2 | ❌ Not started |
| Phase 4 (C4–C9) | Reference Layer remainder | Phase 0 | ❌ In progress |
| Phase 5 | Shared Components + Validators (25 files) | Phase 3 | ❌ Not started |
| Phase 6 | Test Suite (55 files, 430 test cases) | Phase 3 + Phase 5 | ❌ Not started |
| Phase 7 | Quality Audit | After each phase | ❌ Continuous |

---

## 5. Detailed Task Lists

### PHASE 0 — Full Structural Cleanup (22 operations)

#### 0A — `C4-Process-Records/` Root Dir (30 files)

| Task ID | Task | Detail | Priority |
|---|---|---|---|
| P0-A | Verify `C4-Process-Records/` root is full duplicate | Cross-check PR11–PR40 SHAs against `reference/processes/` | 🔴 |
| P0-B | Delete `C4-Process-Records/` root dir (all 30 files) | Only after SHA verification confirms duplicates | 🔴 |

#### 0B — `C5-KA-Crossref/` Migration

| Task ID | Task | Detail | Priority |
|---|---|---|---|
| P0-C | Create `reference/knowledge-areas/` subdir | New canonical location for KA cross-reference | 🔴 |
| P0-D | Move `C5-KA-Crossref/KA-Crossref-Index.md` → `reference/knowledge-areas/KA-Crossref-Index.md` | 15KB live content | 🔴 |
| P0-E | Delete `C5-KA-Crossref/` root dir | After migration confirmed | 🔴 |
| P0-F | Delete `reference/C5-KA-Crossref/` legacy subdir | Empty legacy subdir | 🔴 |

#### 0C — `C6-TT-Taxonomy/` Migration

| Task ID | Task | Detail | Priority |
|---|---|---|---|
| P0-G | Create `reference/tools-techniques/` subdir | New canonical location | 🔴 |
| P0-H | Move `C6-TT-Taxonomy/TT-Taxonomy-Index.md` → `reference/tools-techniques/TT-Taxonomy-Index.md` | 16KB live content | 🔴 |
| P0-I | Delete `C6-TT-Taxonomy/` root dir | After migration confirmed | 🔴 |
| P0-J | Delete `reference/C6-TT-Taxonomy/` legacy subdir | Empty legacy subdir | 🔴 |

#### 0D — `C7-IO-Registry/` Migration

| Task ID | Task | Detail | Priority |
|---|---|---|---|
| P0-K | Create `reference/inputs-outputs/` subdir | New canonical location | 🔴 |
| P0-L | Move `C7-IO-Registry/IO-Registry-Index.md` → `reference/inputs-outputs/IO-Registry-Index.md` | 13KB live content | 🔴 |
| P0-M-del | Delete `C7-IO-Registry/` root dir | After migration confirmed | 🔴 |
| P0-N-del | Delete `reference/C7-IO-Registry/` legacy subdir | Empty legacy subdir | 🔴 |

#### 0E — `reference/` Remaining Legacy Cleanup

| Task ID | Task | Detail | Priority |
|---|---|---|---|
| P0-O | Delete `reference/C4-Process-Records/` | Legacy path — migration to `reference/processes/` confirmed | 🔴 |
| P0-P | Update `reference/README.md` | Mark C1–C4 complete; add knowledge-areas/, tools-techniques/, inputs-outputs/ to planned structure | 🔴 |

#### 0F — `repo/` Legacy Dir Audit + Disposition

| Task ID | Task | Detail | Priority |
|---|---|---|---|
| P0-Q1 | Archive `Artifacts-V-1.0.5-export-4.md` | Move to `docs/legacy/Artifacts-V-1.0.5-export-4.md` | 🟡 |
| P0-Q2 | Move `Skill-PMBOK8anchor-Corepurpose-Primaryartifacts-Ma.csv` | Move to `docs/Skill-anchor-map.csv` | 🟡 |
| P0-Q3 | Move `risk-domain-package-index.md` | Move to `reference/knowledge-areas/` or `docs/` | 🟡 |
| P0-Q4 | Move `risk-domain-readme.md` | Move to `docs/` | 🟡 |
| P0-Q5 | Move `risk-skills-manifest.json` + `.yaml` | Move to `shared/` manifests area or `docs/` | 🟡 |
| P0-Q6 | Move `risk-skills-taxonomy-map.md` | Move to `reference/` | 🟡 |
| P0-Q7 | Delete empty `repo/` dir | After all files migrated | 🟡 |

#### 0G — `artifacts/` Undocumented Dirs Audit (11 dirs)

| Task ID | Subdir | Action Required | Priority |
|---|---|---|---|
| P0-R1 | `artifacts/closure/` | Audit content → consolidate into `closing/` or keep + document | 🔴 |
| P0-R2 | `artifacts/communications/` | Audit → keep as canonical dir or merge into `stakeholders/` | 🔴 |
| P0-R3 | `artifacts/extended-procurement/` | Audit → consolidate into `procurement/` or keep + document | 🔴 |
| P0-R4 | `artifacts/extended-resources/` | Audit → consolidate into `resources/` or keep + document | 🔴 |
| P0-R5 | `artifacts/governance/` | Audit → keep as canonical dir or merge | 🔴 |
| P0-R6 | `artifacts/initiating/` | Audit → keep as canonical dir or merge | 🔴 |
| P0-R7 | `artifacts/knowledge/` | Audit → keep as canonical dir or merge | 🔴 |
| P0-R8 | `artifacts/pmo/` | Audit → keep as canonical dir or merge | 🔴 |
| P0-R9 | `artifacts/portfolio/` | Audit → keep as canonical dir or merge | 🔴 |
| P0-R10 | `artifacts/quality/` | Audit → keep as canonical dir or merge | 🔴 |
| P0-R11 | `artifacts/stakeholders-communications/` | Audit → consolidate into `stakeholders/` or `communications/` | 🔴 |
| P0-R12 | `artifacts/team-resources/` | Audit → consolidate into `resources/` or keep + document | 🔴 |

#### 0H — Documentation Updates

| Task ID | Task | Detail | Priority |
|---|---|---|---|
| P0-M | **Update root `README.md`** | Replace C4-Process-Records/ and C5-KA-Crossref/ refs with canonical paths; update artifacts/ structure tree to show all canonical subdirs; update Related Files table | 🔴 CRITICAL |
| P0-S | Update `SKILL-REGISTRY.md` | Verify no stale path references to C4–C7 root dirs | 🟡 |

---

### PHASE 3 — Full Skill Content (47 files)

| Task ID | Pack | Files | Priority |
|---|---|---|---|
| P3-01–03 | Pack 01 | SKL-01-01, SKL-01-02, SKL-01-03 | 🔴 |
| P3-04–05 | Pack 02 | SKL-02-01, SKL-02-02 | 🔴 |
| P3-06–22 | Pack 03 | SKL-03-01 → SKL-03-17 (17 files) | 🔴 |
| P3-23–31 | Pack 04 | SKL-04-01 → SKL-04-09 (9 files) | 🟡 |
| P3-32–40 | Pack 05 | SKL-05-01 → SKL-05-09 (9 files) | 🟡 |
| P3-41–43 | Pack 06 | SKL-06-01 → SKL-06-03 (3 files) | 🟡 |
| P3-44–47 | Pack 07 | SKL-07-01 → SKL-07-04 (4 files) | 🟡 |

---

### PHASE 4 — Reference Layer Remainder

| Task ID | Task | Files | Priority |
|---|---|---|---|
| P4-C4-01–11 | Rebuild PR01–PR10 + PR41 | 11 files in `reference/processes/` | 🔴 |
| P4-C5 | Upgrade KA-Crossref-Index (migrated from C5) | Enhance migrated file in `reference/knowledge-areas/` | 🟡 |
| P4-C6 | Upgrade TT-Taxonomy (migrated from C6) | Enhance migrated file in `reference/tools-techniques/` | 🟡 |
| P4-C7 | Upgrade IO-Registry (migrated from C7) | Enhance migrated file in `reference/inputs-outputs/` | 🟡 |
| P4-C8-01 | Build Appendix X2 — PMO | `reference/appendices/X2-pmo.md` | 🟡 |
| P4-C8-02 | Build Appendix X3 — AI | `reference/appendices/X3-ai.md` | 🟡 |
| P4-C8-03 | Build Appendix X4 — Procurement | `reference/appendices/X4-procurement.md` | 🟡 |
| P4-C8-04 | Build Appendix X5 — PMBOK Evolution | `reference/appendices/X5-evolution.md` | 🟡 |
| P4-C9 | Build Reference GLOSSARY | `reference/GLOSSARY.md` | 🟡 |

---

### PHASE 5 — Shared Components + Validators (25 files)

**Priority 1 — Routing**
| S5-R-00 | `shared/routing/index.md` | Routing logic catalog |
| S5-R-01 | `shared/routing/threshold-router.md` | T1–T4 decision routing logic |
| S5-R-02 | `shared/routing/escalation-paths.md` | Escalation path definitions |

**Priority 2 — Validators**
| S5-V-00 | `shared/validators/index.md` | Validator catalog |
| S5-V-01 | `shared/validators/waste-test.md` | Waste detection routine |
| S5-V-02 | `shared/validators/artifact-quality-check.md` | Artifact completeness validator |
| S5-V-03 | `shared/validators/baseline-integrity-check.md` | Cross-baseline consistency checker |

**Priority 3 — Checklists**
| S5-CL-00 to S5-CL-11 | 12 checklist files in `shared/checklists/` | Pack readiness (7) + domain (4) + index (1) |

**Priority 4 — Components**
| S5-C-00 to S5-C-06 | 7 files in `shared/components/` | Field blocks (3) + section patterns (3) + index (1) |

---

### PHASE 6 — Test Suite (55 files, 430 test cases)

| Priority | Files | Detail |
|---|---|---|
| 1 | Pack 01–02 skill tests (5 files, 45 cases) | Foundation |
| 2 | `tests/skill-tests/index.md` + IT-01, IT-02 | Catalog + first 2 integration tests |
| 3 | Pack 03 skill tests (17 files, 153 cases) | Largest pack |
| 4 | IT-03 integration test | Planning → execution gate |
| 5 | Pack 04–05 skill tests (18 files, 162 cases) | Core execution |
| 6 | IT-04, IT-05, IT-06 | Flow integration |
| 7 | Pack 06–07 skill tests (7 files, 63 cases) + IT-07 + integration index | Closing + full lifecycle |

---

## 6. Dependency Map

```
Phase 0 (22 ops: cleanup + artifacts audit + repo/ cleanup + README updates)
    │
    ├──► Phase 3 (skills: 47 files) ──┬──► Phase 5 (shared: 25 files)
    │                                └──► Phase 6 (tests: 55 files) ◄── Phase 5
    └──► Phase 4 (reference: C4–C9 + knowledge-areas upgrade)

Phase 7 (quality audit) ── continuous ── runs after EVERY phase
```

---

## 7. Execution Scorecard

| Phase | Deliverable | Target | Done | Status |
|---|---|---|---|---|
| A | Skill scaffolding v1.1.0 | 47 | 47 | ✅ |
| B1 | Artifact definitions | 39 | 39 | ✅ |
| B2 | Artifact templates | 38 | 38 | ✅ |
| B3 | Artifact examples | 10 | 10 | ✅ |
| Phase 1 | `docs/` files | 9 | 9 | ✅ |
| C1 | Principles | 13 | 13 | ✅ |
| C2 | Performance Domains | 9 | 9 | ✅ |
| C3 | Focus Areas | 5 | 5 | ✅ |
| C4 | Process records PR11–PR40 + index | 32 | 32 | ✅ |
| **Phase 0** | **Cleanup: C4–C7 migrate/delete + repo/ + artifacts/ audit + README updates** | **~22 ops** | **0** | **❌ NEXT** |
| C4 | PR01–PR10 + PR41 rebuild | 11 | 0 | ❌ |
| C5/C6/C7 | Upgrade migrated KA/TT/IO files | 3 | 0 | ❌ |
| C8 | Appendices X2–X5 | 4 | 0 | ❌ |
| C9 | Reference GLOSSARY | 1 | 0 | ❌ |
| Phase 3 | Full skill content files | 47 | 0 | ❌ |
| Phase 5 | Shared files | 25 | 1 (README) | ❌ |
| Phase 6 | Test files | 55 | 1 (README) | ❌ |
| **TOTAL** | **All files** | **~350** | **~163** | **~47% complete** |

---

## 8. Session Log

| Session | Date | Phase | Work Completed | Version |
|---|---|---|---|---|
| S-001 | 2026-05-29 | A | Skill scaffolding 47 stubs | v1.0.0 |
| S-002 | 2026-05-30 | A | QA all 47 skills to v1.1.0 | v2.2.0 |
| S-003 | 2026-05-30 | B1 | 39 artifact definitions | v2.3.0 |
| S-004 | 2026-05-31 | B2+B3 | 38 templates + 10 examples | v2.7.0 |
| S-005 | 2026-05-31 | Phase 1 | 9 docs files | v2.6.0 |
| S-006 | 2026-05-31 | C1–C3 | 13 principles + 9 domains + 5 focus areas | v2.10.0 |
| S-007 | 2026-05-31 | C4 | PR11–PR40 migration to reference/processes/ | v2.12.0 |
| S-008 | 2026-06-01 | C4 | PR35–PR40 + index.md complete; structural audit done | v4.0.0 |
| S-009 | 2026-06-01 | Governance | COMPLETION-PLAN-V4.md created; MASTER-PLAN renamed | v4.0.1 |
| S-010 | 2026-06-01 | Governance | README audit — tests/ + shared/ tasks added | v4.1.0 |
| S-011 | 2026-06-01 | Governance | Full directory audit — all dirs crawled; 22 Phase 0 ops; artifacts/ 11 undocumented dirs; repo/ 7 legacy files identified | v4.2.0 |
| **S-012** | **TBD** | **Phase 0** | **Start cleanup: verify C4 duplication → delete C4 root → migrate C5/C6/C7 → audit repo/ → audit artifacts/** | |

---

## 9. AI Agent Operating Rules

See [`COMPLETION-PLAN-V4.md §8`](./COMPLETION-PLAN-V4.md) for full rules.

Core rules:
1. Never modify an artifact definition without bumping version.
2. Never create a skill that references an artifact that does not exist.
3. Always check this file (`MASTER-PLAN.md`) before starting a session.
4. Always commit file-by-file with conformant messages.
5. Never cite PMBOK 8 without a section number.
6. Update this file and CHANGELOG.md at the end of every session.
7. When building `shared/` files, follow the exact structure in `shared/README.md`.
8. When building `tests/` files, follow the exact structure and 9-test-case schema in `tests/README.md`.
9. **Never delete a directory with live content without first verifying migration is complete.**
10. **Never consolidate two `artifacts/` subdirs without first auditing both for content conflicts.**

---

## 10. Version History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-05-29 | Initial plan |
| 2.0.0 | 2026-05-30 | Full rebuild |
| 2.2.0–2.12.0 | 2026-05-30–31 | Phase A–C4 progress |
| 4.0.0 | 2026-06-01 | Full rebuild · Structural audit · Phase 0 added |
| 4.0.1 | 2026-06-01 | Renamed MASTER-PLAN-V2.md → MASTER-PLAN.md |
| 4.1.0 | 2026-06-01 | README audit · tests/ + shared/ tasks (56 + 26 files) added |
| **4.2.0** | **2026-06-01** | **Full directory crawl audit · artifacts/ 17 subdirs found (11 undocumented) · repo/ 7 legacy files identified · C5/C6/C7 confirmed as live content to migrate · Phase 0 expanded to 22 ops · 2 new AI agent rules** |

---

*Authority: PMBOK8 Guide Primary · PMI Companion References Secondary*
*Repository: [https://github.com/fakhruldeen/PMOSkills](https://github.com/fakhruldeen/PMOSkills)*
*Maintainer: @fakhruldeen*
*Last Updated: 2026-06-01 · Version 4.2.0*
