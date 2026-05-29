---
skill_id: SKL-04-09
skill_name: Conduct Procurements
pack: "04 — Executing"
version: "1.1.0"
status: "Draft · Untested"
source_type: PMI-derived
primary_artifact: "A31 — Procurement and Supplier Management Record"
artifacts_updated:
  - "A16 — Financial Management and Cost Baseline Record (contracted costs in §4)"
  - "A26 — Resource Capacity and Acquisition Record (external resource acquisition)"
  - "A18 — Issue, Impediment and Action Log (supplier performance issues)"
pmbok8_anchor: "Guide §2.8 Procurement Management"
performance_domains:
  - Resources
  - Finance
  - Governance
focus_area: Executing
upstream_prerequisites:
  - "SKL-03-16 — A26 resource management plan (acquisition strategy)"
  - "SKL-02-03 — A06 tailoring (procurement formality level)"
downstream_skills:
  - "SKL-05-05 — Control Costs (contracted cost tracking)"
  - "SKL-06-01 — Close Project or Phase (contract closure via A31 §6)"
file_path: "skills/04-executing/SKL-04-09-conduct-procurements.md"
tests: 9
---

# SKL-04-09 — Conduct Procurements

**Pack:** 04 — Executing
**Status:** Draft · Untested
**Primary Artifact:** A31 — Procurement and Supplier Management Record
**PMBOK8 Anchor:** Guide §2.8 Procurement Management

---

## Purpose

Conduct Procurements selects suppliers, awards contracts, and manages ongoing supplier performance. All procurement activity is consolidated in A31. Contracted costs feed A16. External resources feed A26. Contract closure feeds A31 §6 and is consumed by SKL-06-01.

---

## A31 Section Map

| Section | Content |
|---|---|
| §1 | Procurement policy and approvals |
| §2 | Procurement plan summary |
| §3 | Procurement approach per item (method, criteria, type) |
| §4 | Procurement register (all items, status) |
| §5 | Supplier evaluation log |
| §6 | Contract management log (per contract) |
| §7 | Contract financial summary |
| §8 | Procurement risk cross-reference |

---

## Inputs

| Input | Artifact | Section | Status required |
|---|---|---|---|
| Procurement plan | A31 | §2–§3 | Complete |
| Resource management plan | A26 | §1 | Complete |
| Procurement approval thresholds | A06 | §4 authority levels | Current |
| Risk register | A19 | Risk register | Current |
| Cost baseline | A16 | §4 | Current |

---

## Steps

### Step 1 — Issue Procurement Documents
For each planned procurement in A31 §4 with status = Ready:
- Prepare and issue the appropriate document per A31 §3:
  - **RFP** (Request for Proposal) — for complex or service-based procurements
  - **RFQ** (Request for Quotation) — for commodity or price-driven procurements
  - **IFB** (Invitation for Bid) — for construction or fixed-specification procurements
- Record issuance date in A31 §4.
- Confirm distribution to the prospective supplier list.

### Step 2 — Receive and Evaluate Proposals
Receive supplier responses by the deadline specified in the procurement document.
Complete A31 §5 evaluation log for each responding supplier:
- Supplier name
- Evaluation criteria scores (from A31 §3)
- Technical evaluation summary
- Financial evaluation summary
- Risk assessment
- Evaluator(s) and date

### Step 3 — Select Supplier
Apply the selection method defined in A31 §3:

| Method | Description | Use when |
|---|---|---|
| Competitive evaluation | Multi-criteria scoring of all proposals | Multiple qualified suppliers; complex requirements |
| Negotiation | Direct negotiation without competitive process | Sole-source justification exists |
| Sole source | Single supplier without competition | Only one supplier can meet requirements; documented in A06 |

Document selection rationale in A31 §5. Obtain required approvals per A06 thresholds before proceeding to contract award.

### Step 4 — Award Contract
Execute contract with the selected supplier. Create A31 §6 contract management log entry:
- Contract ID
- Procurement ID (from A31 §4)
- Supplier name
- Contract type (Fixed Price / Time and Material / Cost Reimbursable)
- Contract value
- Payment milestones and amounts
- Deliverables schedule
- Performance review dates
- Contract manager name

### Step 5 — Update A16 and A26
- Add contracted cost to A16 §4 cost estimates (update BAC if this contract adds to planned cost)
- Update A26 with any externally acquired resources, noting contract reference

### Step 6 — Manage Supplier Performance
At each performance review date defined in A31 §6:
- Assess supplier against contracted deliverables, quality standards, and SLAs
- Record status in A31 §6: **On track** / **At risk** / **In default**
- For At risk or In default status: log issue in A18 and notify contract manager
- Discuss findings with supplier and document agreed corrective actions

### Step 7 — Manage Contract Changes
All contract changes (scope, price, terms, timeline) must:
1. Be assessed for impact on A16 and A15
2. Route through A12 Integrated Change Control for approval
3. Only be reflected in A31 §6 after A12 shows Approved status
Document the change, its rationale, and the A12 reference in A31 §6.

### Step 8 — Cross-Reference Procurement Risks
Review A19 risk register for all procurement-related risks. For each:
- Add or update A31 §8 with the A19 Risk ID
- Confirm that the risk owner in A19 is aligned with the contract manager for that supplier

---

## Outputs

| Output | Artifact | Section |
|---|---|---|
| Procurement register | A31 | §4 |
| Supplier evaluation log | A31 | §5 |
| Contract management log | A31 | §6 |
| Contract financial summary | A31 | §7 |
| Contracted costs | A16 | §4 cost estimates |
| External resource records | A26 | Acquisition log |
| Supplier performance issues | A18 | Issue log (At risk / In default) |

---

## Operating Rules

1. No contract is signed without an A31 §4 procurement register entry at status = Approved.
2. All contract changes route through A12 before A31 §6 is updated — no exceptions.
3. Supplier performance reviews are mandatory at the cadence defined in A31 §6.
4. At-risk or In-default supplier status must create an A18 issue within 48 hours of assessment.
5. Procurement risks must be cross-referenced in both A19 and A31 §8 — single-artifact recording is incomplete.
6. Sole-source justification must be documented in A06 before a sole-source procurement proceeds.

---

## Failure Modes

| Failure mode | Detection signal | Corrective action |
|---|---|---|
| Contract without A31 entry | Contract in place but no A31 §4 record | Retroactive A31 entry; review A06 compliance |
| Supplier performance not reviewed | A31 §6 review dates passed with no entry | Conduct overdue review; document in A31 §6 |
| Contract change without A12 | A31 §6 change with no A12 Approved reference | Retroactive A12 entry; assess if change was authorized |
| Procurement risk not in A19 | A31 §8 has no A19 cross-reference | Identify procurement risks; log in A19 and cross-reference |
| Supplier insolvency or sudden incapacity | Supplier unable to perform mid-contract; no contingency plan in A31 or A19 | Log in A18 as High priority; activate A19 procurement risk response; assess replacement options; raise A12 if baseline affected |
| Contract dispute with no escalation path | Supplier challenges deliverable acceptance or payment; no dispute resolution clause referenced in A31 §6 | Engage contract manager and legal counsel; document dispute in A31 §6; escalate per A06; do not unilaterally withhold payment |

---

## Tests

| Test ID | Test description | Pass condition | Fail condition |
|---|---|---|---|
| T-1 | A31 entry before contract | Every contract has an A31 §4 procurement register entry before signing | Contract signed with no A31 §4 entry |
| T-2 | Evaluation documented | Every awarded contract has a completed A31 §5 evaluation log entry | Contract awarded with no evaluation log |
| T-3 | Approval threshold respected | Contracts above A06 threshold have required approvals documented in A31 §5 | Contract signed without documented approval |
| T-4 | A16 updated | All contracted costs reflected in A16 §4 cost estimates | Contracted cost not in A16 |
| T-5 | A26 updated | All external resources resulting from contracts entered in A26 | External resource not in A26 |
| T-6 | Performance reviews conducted | A31 §6 has performance status entries at each scheduled review date | Scheduled review date passed with no A31 §6 entry |
| T-7 | At-risk escalated | At-risk or In-default supplier status logged in A18 within 48 hours | At-risk supplier assessment with no A18 entry |
| T-8 | Contract changes via A12 | All contract changes have A12 change request with Approved status before A31 update | Contract modified without A12 Approved entry |
| T-9 | Risk cross-reference | A31 §8 references A19 Risk IDs for all procurement-related risks | Procurement risk in A19 with no A31 §8 cross-reference |

---

## Change Log

| Version | Date | Change description |
|---|---|---|
| 1.0.0 | 2026-05-29 | Initial build |
| 1.1.0 | 2026-05-30 | Expanded failure modes from 4 to 6: added supplier insolvency/incapacity and contract dispute with no escalation path |

---

*Authority: PMBOK8 Guide §2.8 Procurement Management*
*Source type: PMI-derived*
