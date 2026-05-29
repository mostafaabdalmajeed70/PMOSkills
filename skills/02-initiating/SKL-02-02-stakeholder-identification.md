# SKL-02-02 — Stakeholder Identification
**Skill ID:** SKL-02-02  
**Skill Name:** Stakeholder Identification  
**Version:** 1.0.0-draft  
**Lifecycle Pack:** 02-Initiating  
**Status:** Draft · Untested  
**Source Type:** PMI-derived  
**File Path:** `skills/02-initiating/SKL-02-02-stakeholder-identification.md`

---

## Purpose

Identify all individuals, groups, and organizations that have a stake in the project, and document their interests, involvement, influence, interdependencies, and potential impact on project success into **A07 — Stakeholder Register and Engagement Strategy**. This skill produces the foundational stakeholder view that drives requirements elicitation, communications planning, and engagement throughout the project lifecycle.

This skill is first executed during **initiation**, immediately after the Project Charter (A04) is approved. It is then **re-executed periodically** throughout the project as the environment evolves, new stakeholders emerge, or existing stakeholder dynamics shift.

---

## Scope

**In scope:**
- Identifying all internal and external stakeholders
- Documenting stakeholder interests, influence, impact, and interdependencies
- Producing the initial Stakeholder Register and Engagement Strategy (A07)
- Assigning an initial engagement level classification (Unaware → Leading)
- Triggering downstream engagement and communications planning skills

**Out of scope:**
- Developing detailed engagement plans → use SKL-03-07 (Plan Stakeholder Engagement)
- Planning communications channels and cadence → use SKL-03-08 (Plan Communications Management)
- Active stakeholder management and communications execution → Planning and Executing pack skills
- Monitoring and adjusting engagement → Monitoring and Controlling pack skills

---

## Authority and Governance

| Field | Value |
|-------|-------|
| **Primary PMI Source** | PMBOK8 |
| **Exact Section** | Guide §2.5.2.1 Identify Stakeholders · Guide Figure 2-33 · Guide §2.5.1 Key Concepts |
| **Purpose of Citation** | Establish stakeholder identification as a continuing, iterative project management process within the Stakeholders Performance Domain |
| **Source Type** | PMI-derived |
| **Governance Layer** | Project Governance |
| **Artifact Produced** | A07 — Stakeholder Register and Engagement Strategy |
| **Owner** | Project Manager |
| **Approval Authority** | Sponsor (initial strategic alignment); ongoing updates managed by PM |
| **Threshold Band** | T2 — changes affecting key sponsor or governance-body stakeholder classification require sponsor awareness |
| **Escalate When** | New stakeholders emerge who hold decision or veto authority affecting scope, budget, or delivery approach |

---

## Performance Domains and Principles

**Performance Domains:** Stakeholders · Governance  
**Focus Areas:** Initiating · Planning · Executing · Monitoring and Controlling

| Principle | Application in This Skill |
|-----------|--------------------------|
| P1 Adopt a Holistic View | Stakeholder identification must capture internal and external stakeholders, supportive and resistant parties, and those impacted regardless of their visibility |
| P2 Focus on Value | Stakeholder identification anchors value delivery — the right stakeholders must be known before scope, requirements, and success criteria can be validated |
| P5 Engage Stakeholders | Active, ongoing identification is the prerequisite for any engagement; missing a key stakeholder is a project risk |
| P7 Embrace Adaptability | Re-run this skill when the project environment changes; the register is never a static snapshot |

---

## PMBOK 8 Process: Identify Stakeholders

### Inputs (per PMBOK8 Guide Figure 2-33)

| Input | Artifact / Source | Mandatory? | Notes |
|-------|------------------|-----------|-------|
| Project charter | A04 | Yes | Primary trigger and source of initial named stakeholders: sponsor, PM, key parties |
| Business case | A01 | Yes | Identifies business owners, benefit recipients, impacted business functions |
| Benefits management plan | A02 | Recommended | Identifies benefit owners and their organizational context |
| Communications management plan | A28 | Conditional | Available on re-runs; existing comm plan informs stakeholder re-analysis |
| Stakeholder engagement plan | A07 (prior version) | Conditional | Available on re-runs; prior engagement strategy reviewed before update |
| Change log | A12 | Conditional | Re-runs triggered by change events may surface new or altered stakeholder positions |
| Issue log | A18 | Conditional | Active issues often reveal previously hidden or under-weighted stakeholders |
| Requirements documentation | A08 | Conditional | Planning-phase re-runs use scope and requirements as a stakeholder discovery lens |
| Agreements | Pre-existing contracts/MOUs | Conditional | Supplier, partner, or regulatory agreements identify additional external stakeholders |
| Enterprise environmental factors (EEFs) | A05 — Context Register | Yes | Organizational culture, industry context, regulatory environment, market factors |
| Organizational process assets (OPAs) | A05 — Context Register | Yes | Templates, historical stakeholder registers, lessons, communication standards |

### Tools and Techniques (per PMBOK8 Guide Figure 2-33)

| Tool / Technique | When to Use | Key Output |
|-----------------|------------|-----------|
| Expert judgment | Always — PM, sponsor, and domain experts name stakeholders from organizational knowledge | Initial stakeholder candidates |
| Data gathering — Questionnaires and surveys | When large or distributed organizations require structured input | Consolidated stakeholder nominations |
| Data gathering — Brainstorming | When starting a new project with unclear stakeholder boundaries | Broad candidate list for filtering |
| Data analysis — Stakeholder analysis | Always — assess each stakeholder's interests, influence, power, and engagement level | Populated A07 fields |
| Data analysis — Document analysis | Always — mine charter, business case, agreements, and prior records for named parties | Stakeholder candidate list |
| Data representation — Stakeholder mapping/representation | When visualizing power/interest or salience is needed to communicate the engagement picture | Stakeholder grid or salience model |
| Meetings | Initial identification session with sponsor; re-runs as part of status or governance reviews | Validated stakeholder list |

#### Stakeholder Analysis Models (data representation options)

| Model | Use Case |
|-------|----------|
| **Power/Interest Grid** | Classic two-axis map; classify by power to influence and interest in outcomes |
| **Power/Influence Grid** | Substitutes active involvement for interest where behavioral engagement matters more |
| **Influence/Impact Grid** | Focuses on who can change outcomes and who is most affected |
| **Salience Model** | Three-attribute model: Power, Legitimacy, Urgency — used for complex stakeholder landscapes |
| **Directions of Influence** | Maps upward (governing bodies), downward (team), outward (suppliers), and sideward (peers) |

### Outputs (per PMBOK8 Guide Figure 2-33)

| Output | Artifact ID | Description |
|--------|------------|-------------|
| **Stakeholder register** | A07 | Primary output — stakeholder identities, attributes, interests, influence, and initial engagement classification |
| **Change requests** | A12 | When identification reveals scope, risk, or plan impacts requiring formal change |
| **Project management plan updates** | — | Requirements management plan, communications management plan, risk management plan, and stakeholder engagement plan may all require updates |
| **Project document updates** | — | Assumption log (A05), issue log (A18), risk register (A19) updated when identification reveals new issues or risks |

---

## Instructions

Execute this skill in the following sequence. On first execution, the PM leads the identification session with sponsor input. On re-runs, the PM reviews and updates A07 using all available inputs.

### Step 1 — Confirm Prerequisites

Before starting, verify:

- [ ] Project Charter (A04) has been signed and approved
- [ ] Business Case (A01) is accessible
- [ ] Context Register (A05) is available (EEFs and OPAs)
- [ ] On re-runs: prior A07 version is the starting point, not a blank slate

If A04 is not signed, **do not proceed**. Return to SKL-02-01.

### Step 2 — Generate the Initial Candidate List

Use document analysis and expert judgment to extract stakeholder candidates from all available inputs. Start with the charter — it names the sponsor, PM, and key parties by definition. Then extend outward:

**Internal stakeholder categories to consider:**
- Sponsor(s) and steering committee members
- Project manager and project management team
- Project team members and functional contributors
- PMO leads (where engaged)
- Business owners, process owners, and benefit owners
- Senior management affected by project outcomes
- Internal audit, legal, and compliance functions (where relevant)
- Finance and procurement functions (where relevant)

**External stakeholder categories to consider:**
- Customers and end users
- Suppliers, vendors, and contractors
- Regulatory bodies and government agencies
- Partner organizations and joint venture parties
- Industry groups, standard-setting bodies
- Community groups, affected public (for infrastructure and public-sector projects)
- Media (for high-visibility or public-interest projects)

> Apply the holistic view principle (P1): include stakeholders who are neutral or resistant, not only those who are supportive. Missing a resistant stakeholder is a project risk.

### Step 3 — Apply Stakeholder Analysis

For each identified stakeholder or stakeholder group, complete the following analysis fields for A07:

| Analysis Field | Description | Source |
|---------------|-------------|--------|
| Stakeholder identity | Name, role, organization, contact | Charter, document analysis |
| Interest / stake | What outcome, deliverable, or decision affects them | Expert judgment, document analysis |
| Power / influence level | Ability to affect project decisions, resources, or outcomes | Stakeholder analysis |
| Impact level | Degree to which project outcomes affect the stakeholder | Stakeholder analysis |
| Current engagement level | Unaware / Resistant / Neutral / Supportive / Leading | Stakeholder analysis |
| Target engagement level | Where the PM needs engagement to be for project success | Expert judgment |
| Engagement gap | Difference between current and target — drives engagement strategy | Derived |
| Communication needs | Frequency, format, level of detail required | Stakeholder analysis, document analysis |
| Interdependencies | Other stakeholders this party is connected to or influenced by | Stakeholder mapping |
| Risk flag | Yes/No — does the gap or position create a project risk? | Stakeholder analysis |

#### Engagement Level Definitions (PMI-aligned)

| Level | Description |
|-------|-------------|
| **Unaware** | Not aware of the project or its potential impacts |
| **Resistant** | Aware but opposed to the project or its outcomes |
| **Neutral** | Aware but neither supportive nor resistant |
| **Supportive** | Aware of the project and supportive of its outcomes |
| **Leading** | Actively engaged and helping drive project success |

### Step 4 — Apply a Stakeholder Mapping Model

Select one mapping model appropriate to the project's complexity. For most projects, the **Power/Interest Grid** is sufficient. For complex stakeholder landscapes (large transformation projects, regulated industries, multi-organizational programs), consider the **Salience Model**.

Record the selected model and the resulting classification in A07. The mapping model output does not need to be a separate document — embed the classification result in A07 as an engagement context note.

**Do not maintain a separate salience canvas or stakeholder mapping worksheet if it only duplicates A07 fields.** (Waste Rule — A05 v1.0.3 §3.2)

### Step 5 — Populate A07 — Stakeholder Register and Engagement Strategy

Complete all mandatory fields of A07 using the analysis output from Steps 2–4. Refer to the **Core Fields** section below.

Apply the following constraint: A07 is a **living record**, not a point-in-time report. Build it for updatability — structured so that re-runs in Steps 6–8 are incremental updates, not rewrites.

### Step 6 — Identify Downstream Impacts

After completing A07, scan for items that require other project artifacts to be updated or created:

| Trigger | Action |
|---------|--------|
| New stakeholder reveals an unrecorded assumption | Update A05 Assumption Log |
| New stakeholder introduces a project risk | Add entry to A19 Risk Management Record |
| Engagement gap is significant and creates delivery risk | Raise a risk flag in A19 |
| Identification reveals a scope boundary issue | Raise a change request (A12) |
| Communications planning needs to be revised | Flag for A28 update |
| Stakeholder has regulatory or compliance authority | Escalate to sponsor and update A06 Tailoring Decision Record if governance implications exist |

### Step 7 — Present Initial A07 to Sponsor

On first execution, present the initial A07 to the sponsor for strategic alignment review. The sponsor confirms:

- Named stakeholders at the executive and governance level are correct
- Engagement approach for high-power stakeholders is appropriate
- No critical stakeholders have been omitted

This does **not** require formal approval for every re-run. Routine updates managed by the PM.

### Step 8 — Trigger Downstream Skills

Once A07 is baselined, immediately trigger:

| Skill | What It Does |
|-------|-------------|
| SKL-03-07 | Plan Stakeholder Engagement — develops detailed strategies for each engagement gap |
| SKL-03-08 | Plan Communications Management — translates stakeholder information needs into a communications record |
| SKL-02-03 | Create Context Register (A05) — if not yet initiated, stakeholder data feeds EEF and OPA compilation |

---

## Core Fields — A07 Stakeholder Register and Engagement Strategy

| Field | Mandatory? | Guidance |
|-------|-----------|---------|
| **Stakeholder identity** | Yes | Name or group name, role, organization, contact method |
| **Stake / interest** | Yes | What the stakeholder cares about: outcomes, deliverables, decisions, timing |
| **Influence level** | Yes | High / Medium / Low — ability to affect project direction, funding, or team |
| **Impact level** | Yes | High / Medium / Low — degree the project affects the stakeholder |
| **Current engagement level** | Yes | Unaware / Resistant / Neutral / Supportive / Leading |
| **Target engagement level** | Yes | Where engagement needs to be for the project to succeed |
| **Engagement gap** | Yes | Derived from current vs. target — drives strategy |
| **Engagement approach** | Yes | Key actions: inform, consult, involve, collaborate, empower |
| **Communication needs** | Yes | Frequency, channel, format, and level of detail for this stakeholder |
| **Interdependencies** | Recommended | Other stakeholders who influence or are influenced by this party |
| **Risk flag** | Recommended | Flag when the gap or resistance level creates a project risk |
| **Last reviewed date** | Yes | Tracks currency of the record — required for audit and re-run control |

---

## Tailoring Guidance

| Context | Tailoring Decision |
|---------|-------------------|
| Small, low-risk internal project | A07 may be a simple table in the project charter or a lightweight register; full salience analysis is optional |
| Agile/adaptive project | A07 is still required — identify stakeholders before the first sprint; re-run each iteration as needed; product owner is a primary stakeholder interface |
| Large transformation or regulatory project | Full stakeholder analysis with salience model; separate engagement strategies per group; sponsor review of A07 is mandatory |
| External contract project | Include contractual parties (client, sub-contractors, oversight bodies) as named stakeholders; legal and compliance functions flagged explicitly |
| Multi-phase predictive project | Re-run this skill at each phase gate; A07 must be updated before planning for the new phase begins |
| Public-sector or community-impact project | External community groups, advocacy organizations, and elected representatives must be explicitly identified |

**Do not tailor away:**
- Stakeholder identification itself (P5 — mandatory for any project)
- Sponsor identification and engagement classification (governance anchor — non-negotiable)
- Re-run cadence at phase transitions (P7 — required for adaptability)

---

## Failure Cases

| Failure | Indicator | Corrective Action |
|---------|-----------|-----------------|
| Charter not approved before execution | A07 drafted without a signed A04 | Halt; return to SKL-02-01 |
| Only supportive stakeholders identified | Register contains no Neutral or Resistant entries on a complex change project | Conduct facilitated stakeholder discovery session; include explicit "who might oppose or be affected negatively?" question |
| A07 never re-run after initial creation | Register is dated from initiation, project is mid-execution | Schedule immediate re-run; flag as a governance gap |
| Salience canvas and A07 maintained separately with duplicate content | Two artifacts contain the same stakeholder rows | Merge into A07; retire the canvas (waste rule) |
| Key regulatory or compliance stakeholder missing | Regulatory body or audit function not listed | Add immediately; assess if a change request or governance escalation is needed |
| Engagement gaps not acted upon | High-influence, Resistant stakeholders with no engagement action | Raise risk flag in A19; escalate engagement gap to sponsor |
| A07 approval routed to PM instead of sponsor | PM self-approves initial strategic classification | Sponsor review is mandatory for initial release |

---

## Outputs Produced by This Skill

| Output | Location | Notes |
|--------|---------- |-------|
| Stakeholder Register and Engagement Strategy | `artifacts/templates/A07-stakeholder-register.md` (filled) | Primary deliverable |
| Risk register updates | A19 (Risk Management Record) | Risk flags from engagement gaps |
| Assumption log updates | A05 (Context Register) | New assumptions surfaced during identification |
| Downstream skill trigger list | Internal record | SKL-03-07 and SKL-03-08 triggered |

---

## Re-Run Schedule

| Trigger | Re-Run Type |
|---------|------------|
| End of each project phase (predictive) | Full re-run; update all fields |
| Start of each sprint or iteration (adaptive) | Lightweight re-run; confirm no new stakeholders; update engagement levels if changed |
| Major change request approved (A12) | Targeted re-run; assess whether the change introduces or affects stakeholders |
| New agreement or supplier engaged | Targeted re-run; add external stakeholders from the agreement |
| Significant stakeholder behavior change observed | Immediate targeted update; reassess current engagement level |
| Project enters deployment or transition phase | Full re-run; end-user and operational stakeholders become primary |

---

## Integration Points

| Connected Artifact or Skill | Relationship |
|----------------------------|-------------|
| A04 Project Charter | Input — primary trigger; charter names the sponsor, PM, and key parties |
| A01 Business Case | Input — identifies business owners and benefit recipients |
| A02 Benefits Record | Input — identifies benefit owners |
| A05 Context Register | Bidirectional — EEFs and OPAs feed identification; new assumptions feed back to A05 |
| A12 Change and Exception Decision Log | Conditional input on re-runs; output when identification triggers a change |
| A18 Issue, Impediment, and Action Log | Conditional input on re-runs; issues often reveal hidden stakeholders |
| A19 Risk Management Record | Output — engagement gaps with risk implications are logged here |
| A28 Communications and Reporting Record | Downstream — stakeholder communication needs from A07 feed A28 |
| A07 (itself — prior version) | Input on all re-runs — always update from the prior state, never blank-slate |
| SKL-02-01 | Upstream prerequisite — charter must be signed before this skill runs |
| SKL-03-07 | Downstream — Plan Stakeholder Engagement consumes A07 as its primary input |
| SKL-03-08 | Downstream — Plan Communications Management uses A07 stakeholder information needs |

---

## Tests

### Test T-1: Minimum Valid A07 at Initiation
**Given:** A signed Project Charter (A04) and approved Business Case (A01)  
**When:** SKL-02-02 is executed at project initiation  
**Then:** A07 must contain at minimum: sponsor, PM, and at least three other named stakeholder groups; all mandatory fields populated; current and target engagement levels assigned; last reviewed date recorded

### Test T-2: Missing Charter Prerequisite
**Given:** No signed Project Charter exists  
**When:** Step 1 prerequisite check is run  
**Then:** Skill must halt and return "Return to SKL-02-01 — Project Charter not approved"

### Test T-3: Only Supportive Stakeholders
**Given:** A07 draft contains only Supportive and Leading entries  
**When:** The PM reviews a complex organizational change project  
**Then:** Skill must flag this as a likely identification gap and prompt a facilitated discovery session to surface Neutral and Resistant stakeholders

### Test T-4: Re-Run at Phase Gate
**Given:** A predictive project completing Phase 1 and entering Phase 2  
**When:** SKL-02-02 is re-run at the phase gate  
**Then:** A07 must be updated with the last reviewed date; new phase stakeholders (e.g., operational teams, end users) must be assessed; engagement levels must be revised based on phase progression

### Test T-5: Engagement Gap Risk Flag
**Given:** A key decision-maker stakeholder is classified as Resistant with a target of Supportive  
**When:** Step 6 downstream impact check is run  
**Then:** A risk entry must be created in A19 referencing the engagement gap, with an assigned owner and target engagement action

### Test T-6: Waste Rule — Duplicate Salience Canvas
**Given:** A separate salience canvas exists alongside A07 with identical stakeholder rows  
**When:** Waste test is applied  
**Then:** Skill must flag the duplicate; recommend merging salience classification into A07 and retiring the canvas

### Test T-7: Adaptive Project Re-Run
**Given:** An adaptive (Scrum) project entering Sprint 3  
**When:** A lightweight re-run of SKL-02-02 is performed  
**Then:** A07 must confirm no new external stakeholders have emerged; engagement levels for product owner and key users must be confirmed or updated; last reviewed date updated

---

## Examples

### Example A — Internal IT System Migration (Predictive, Medium Complexity)

Initial A07 identifies the following stakeholder groups:

| Stakeholder | Interest | Influence | Impact | Current | Target |
|------------|---------|----------|--------|---------|--------|
| VP Operations (Sponsor) | Project success, cost adherence | High | High | Leading | Leading |
| IT Director | Technical delivery, team capacity | High | High | Supportive | Leading |
| Finance Team Lead | Data integrity in migration | Medium | High | Neutral | Supportive |
| End Users — Operations Staff | Minimal disruption to daily work | Low | High | Resistant | Neutral |
| Procurement Manager | Vendor contracts and SLAs | Medium | Medium | Neutral | Supportive |
| Compliance Officer | Data privacy and audit trail | High | Medium | Unaware | Supportive |

> Note: End Users (Resistant) and Compliance Officer (Unaware) are flagged as engagement risks → entries added to A19.

### Example B — Adaptive Software Product (Scrum, 3 Sprints Completed)

Re-run after Sprint 3 reveals:

- A new product compliance requirement from a regulatory team not previously identified → added to A07 as Neutral (target: Supportive) → risk flag raised in A19
- Product Owner engagement remains Leading → confirmed, no change
- Two end-user groups have shifted from Neutral to Supportive after demo → A07 updated; risk flag closed

---

## Companion References

| Alias | Source | Relevant Section |
|-------|--------|-----------------|
| PMBOK8 | PMBOK Guide 8th Edition | §2.5 Stakeholders Performance Domain · §2.5.1 Key Concepts · §2.5.2.1 Identify Stakeholders · Figure 2-33 |
| PMBOK8 | The Standard for Project Management | §3.7 P5 Engage Stakeholders · §3.1 P1 Holistic View · §3.9 P7 Embrace Adaptability |
| Process-Groups | Process Groups Practice Guide | Initiating Process Group · Identify Stakeholders |
| PMI-BA | Business Analysis Practice Guide | Stakeholder identification and analysis |
| Forms-Book | PMI Practice Standard Forms | Stakeholder register template reference |

---

*Source Type: PMI-derived*  
*Governance Layer: Project Governance*  
*Authority: PMBOK8 §2.5.2.1 · Figure 2-33 · Standard §3.7 P5*  
*Linked Artifact: A07 — Stakeholder Register and Engagement Strategy*  
*Related Skills: SKL-02-01 · SKL-03-07 · SKL-03-08*  
*Re-run: Yes — periodic throughout project lifecycle*
