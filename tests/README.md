# tests/ — Skill and Integration Test Cases
**Status:** Planned · Not yet built
**Version:** 0.1.0-planned
**Authority:** SKILL-REGISTRY.md · Repo Operating Rules
**File Path:** `tests/README.md`

---

## Purpose

This directory will contain structured test cases for every skill (unit tests) and cross-skill integration flows (integration tests). Tests verify that each skill produces correct outputs from defined inputs, respects quality criteria, and integrates correctly with upstream and downstream skills.

---

## Planned Structure

```
tests/
├── README.md                              ← This file
├── skill-tests/
│   ├── index.md                           ← [planned] Test catalog — all 47 skills
│   ├── 01-organizational-setup/
│   │   ├── SKL-01-01-tests.md             ← [planned] 9 test cases
│   │   ├── SKL-01-02-tests.md             ← [planned] 9 test cases
│   │   └── SKL-01-03-tests.md             ← [planned] 9 test cases
│   ├── 02-initiating/                     ← [planned] 2 skill test files
│   ├── 03-planning/                       ← [planned] 17 skill test files
│   ├── 04-executing/                      ← [planned] 9 skill test files
│   ├── 05-monitoring-controlling/         ← [planned] 9 skill test files
│   ├── 06-closing/                        ← [planned] 3 skill test files
│   └── 07-adaptive-hybrid/                ← [planned] 4 skill test files
└── integration-tests/
    ├── index.md                           ← [planned] Integration test catalog
    ├── IT-01-setup-to-initiating.md       ← [planned] Pack 01 → Pack 02 flow
    ├── IT-02-initiating-to-planning.md    ← [planned] Pack 02 → Pack 03 flow
    ├── IT-03-planning-to-executing.md     ← [planned] Pack 03 → Pack 04 flow
    ├── IT-04-executing-to-mc.md           ← [planned] Pack 04 → Pack 05 flow
    ├── IT-05-mc-to-closing.md             ← [planned] Pack 05 → Pack 06 flow
    ├── IT-06-hybrid-overlay.md            ← [planned] Pack 07 overlay on Pack 03–05
    └── IT-07-full-lifecycle.md            ← [planned] End-to-end flow test
```

---

## Test Case Schema

Each skill test file (`SKL-PP-NN-tests.md`) will follow this structure:

```
## Test: [Test Name]
- **Test ID:** T-PP-NN-##
- **Skill:** SKL-PP-NN
- **Preconditions:** [Artifacts and states required before skill runs]
- **Inputs:** [Specific input values]
- **Expected Outputs:** [Artifact sections produced, fields populated, quality criteria met]
- **Pass Criteria:** [Verifiable assertions]
- **Failure Cases:** [Conditions under which skill should fail or escalate]
- **Notes:** [Edge cases, tailoring considerations]
```

---

## Build Priority

| Priority | Tests | Rationale |
|----------|-------|-----------|
| 1 | Pack 01–02 skill tests | Foundation — all downstream depends on these |
| 2 | IT-01 and IT-02 integration tests | Validate setup → planning handoff |
| 3 | Pack 03 skill tests | Largest pack — 17 skills |
| 4 | IT-03 integration test | Planning → execution gate |
| 5 | Pack 04–05 skill tests | Core execution and control |
| 6 | IT-04 through IT-07 | Full lifecycle validation |
| 7 | Pack 06–07 skill tests | Closing and adaptive |

---

## Test Coverage Target

| Layer | Target |
|-------|--------|
| Skill tests | 9 test cases per skill × 47 skills = **423 test cases** |
| Integration tests | 7 integration flow tests |
| Total | **430 test cases** |

---

## Dependencies

- All 47 skill files — tests validate skill outputs
- All artifact definitions in `artifacts/` — expected outputs reference artifact schemas
- `shared/validators/` — validators called by integration tests

---

*Status: Planned · Build begins after shared/ layer · Authority: SKILL-REGISTRY.md*
*Last Updated: 2026-05-30 · Patch I*
