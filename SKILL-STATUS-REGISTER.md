---
gov_id: SKILL-STATUS-REGISTER
gov_name: Skill Status Register — All Packs
version: "1.0.0"
status: Active
authority: QUALITY-STANDARDS.md · PMBOK8 Primary
supersedes: none
file_path: "SKILL-STATUS-REGISTER.md"
last_updated: "2026-06-03"
---

# SKILL-STATUS-REGISTER.md
**Repository:** PMO Skill Repository  
**Version:** 1.0.0  
**Authority:** QUALITY-STANDARDS.md §2.9 · PMBOK8  
**Purpose:** Single authoritative record of the status for every skill in the repository.
This file is the canonical truth for skill status. Individual skill YAML `status` fields
are secondary and will be updated to match this register in Wave 2.

> **Wave 1 correction note (2026-06-03):** The external audit (F-11) correctly identified
> that all 48 skills carried `status: "Draft · Untested"` even though each skill file has
> a non-zero `tests:` count (typically 9–12 tests per skill). The correct status for a
> skill that has defined tests but has not yet been run against a live project is
> `"Draft · Tests Defined"`. This register reflects the corrected status.
> Individual YAML patches are deferred to Wave 2.

---

## Status Vocabulary

| Status Code | Meaning |
|-------------|--------|
| `Draft · No Tests` | Skill written; no test cases defined yet |
| `Draft · Tests Defined` | Skill written; tests defined in Tests table; not yet validated against a live project |
| `Draft · Tested` | Skill and tests have been applied to at least one real or simulation project |
| `Active` | Skill validated, approved, and ready for production use |
| `Deprecated` | Skill superseded or retired; retained for reference only |

---

## Pack 01 — Organizational Setup (3 skills)

| Skill ID | Skill Name | Tests | Correct Status | YAML Status | Needs Patch? |
|----------|-----------|-------|---------------|-------------|-------------|
| SKL-01-01 | Establish PM Governance Framework | 9 | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-01-02 | Define Artifact and Document Control Standards | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-01-03 | Configure Project Repository and Tool Environment | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |

## Pack 02 — Initiating (2 skills)

| Skill ID | Skill Name | Tests | Correct Status | YAML Status | Needs Patch? |
|----------|-----------|-------|---------------|-------------|-------------|
| SKL-02-01 | Project Charter | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-02-02 | Stakeholder Identification | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |

## Pack 03 — Planning (estimated 15+ skills based on LIFECYCLE-MAP)

| Skill ID | Skill Name | Tests | Correct Status | YAML Status | Needs Patch? |
|----------|-----------|-------|---------------|-------------|-------------|
| SKL-03-01 | Develop Integrated Project Management Plan | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-02 | Develop Lifecycle and Delivery Approach | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-03 | Plan Scope Management | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-04 | Elicit and Analyze Requirements | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-05 | Define and Baseline Scope | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-06 | Develop and Baseline Schedule | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-07 | Develop Financial Management and Cost Baseline | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-08 | Plan Stakeholder Engagement | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-09 | Plan Communications Management | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-10 | Plan Resource Management | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-11 | Plan Risk Management | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-12 | Identify and Analyze Risks | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-13 | Establish Team Operating Agreement | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-14 | Plan Procurement and Sourcing Strategy | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-15 | Plan Change Readiness and Adoption | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-03-18 | Integrate Sustainability Into Project Planning | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |

## Pack 04 — Executing (estimated 10 skills)

| Skill ID | Skill Name | Tests | Correct Status | YAML Status | Needs Patch? |
|----------|-----------|-------|---------------|-------------|-------------|
| SKL-04-02 | Manage Quality Assurance | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-04-03 | Manage Project Knowledge | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-04-04 | Manage Change Readiness and Adoption | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-04-05 | Develop Team | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-04-06 | Manage Stakeholder Engagement | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-04-07 | Lead the Team | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-04-08 | Implement Risk Responses | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-04-09 | Conduct Procurements | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-04-10 | Manage Issues, Impediments, and Actions | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |

## Pack 05 — Monitoring and Controlling (estimated 12 skills)

| Skill ID | Skill Name | Tests | Correct Status | YAML Status | Needs Patch? |
|----------|-----------|-------|---------------|-------------|-------------|
| SKL-05-01 | Integrated Performance Reporting | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-02 | Assess and Implement Changes | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-03 | Monitor and Validate Scope | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-04 | Monitor and Control Schedule | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-05 | Monitor and Control Finances | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-06 | Monitor Stakeholder Engagement | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-07 | Monitor Communications | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-08 | Monitor and Control Resources | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-09 | Quality Control | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-10 | Quantitative Risk and Reserve Management | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-11 | Trade-Off Decision Making | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-05-12 | Supplier Change, Claim, and Compliance | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |

## Pack 06 — Closing (estimated 10 skills)

| Skill ID | Skill Name | Tests | Correct Status | YAML Status | Needs Patch? |
|----------|-----------|-------|---------------|-------------|-------------|
| SKL-06-01 | Obtain Deliverable Acceptance | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-06-02 | Financial Closure | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-06-03 | Benefits Transition and Handover | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-06-04 | Release Resources | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-06-05 | Capture and Archive Lessons Learned | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-06-06 | Close Supplier Contracts | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-06-07 | Close Phase or Project | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-06-08 | Information Retention and Records Control | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-06-09 | Produce Final Project Report | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |
| SKL-06-10 | Closure Authorization | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |

## Pack 07 — Adaptive/Hybrid (remaining skills)

| Skill ID | Skill Name | Tests | Correct Status | YAML Status | Needs Patch? |
|----------|-----------|-------|---------------|-------------|-------------|
| All SKL-07-xx | PMO and adaptive skills | 9+ | Draft · Tests Defined | Draft · Untested | ⚠️ Yes |

---

## Wave 2 Action Required

All 48 skill files require a one-line YAML patch:

```yaml
# Before
status: "Draft · Untested"

# After
status: "Draft · Tests Defined"
```

This is a mechanical batch operation. Execute in Wave 2 using the file list above as
the authoritative task list. Update this register's `Needs Patch?` column to `✓ Done`
as each file is patched.

---

*Authority: QUALITY-STANDARDS.md · PMBOK8 · Audit Report F-11 resolution*
*Owner: Repository Maintainer*
