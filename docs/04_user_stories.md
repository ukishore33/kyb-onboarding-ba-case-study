# Agile User Stories: KYB Risk Scoring Engine

**Project Name:** NovaPay KYB Risk Scoring Engine  
**Document Type:** User Stories (Agile)  
**Version:** 1.0 | **Date:** April 2026  
**Author:** Kishore U. | [LinkedIn](https://linkedin.com/in/kishore-techie) | 6303308133

---

## 1. Introduction

This document contains 12 user stories organized into 4 Epics for the KYB Onboarding Process Automation project. Each story follows the standard format: "As a [role], I want [feature] so that [benefit]."

---

## 2. Epic Overview

| Epic | Description | # Stories | Total Points |
|------|-------------|-----------|---------------|
| EPIC-01 | Data Ingestion | 3 | 13 |
| EPIC-02 | Risk Scoring | 4 | 21 |
| EPIC-03 | Alert Management | 3 | 11 |
| EPIC-04 | Reporting | 2 | 8 |
| **Total** | | **12** | **53** |

---

## 3. Epic 1: Data Ingestion

### US-01: Entity Submission API

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-01                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As a Business Relationship Manager,                                          │
│  I want to submit entity registration data through an API                      │
│  so that the onboarding process starts immediately without manual entry."      │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-01 - Data Ingestion                    Priority: MUST HAVE          │
│ Story Points: 5                 Sprint: 1                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] API accepts POST request with entity JSON payload                         │
│ [ ] Valid payload creates entity record with unique Entity ID                 │
│ [ ] Invalid payload returns 400 error with field-level validation messages     │
│ [ ] API responds within 500ms (p95)                                            │
│ [ ] Request logged in audit trail                                               │
│                                                                                  │
│ Technical Notes:                                                                │
│ - Endpoint: POST /api/v1/entities                                               │
│ - Authentication: OAuth 2.0 JWT                                                 │
│ - Payload size limit: 5MB                                                       │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### US-02: Document Upload & Storage

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-02                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As a Compliance Analyst,                                                     │
│  I want to upload supporting documents (COI, address proof, UBO declaration)  │
│  so that they are stored securely and linked to the entity record."             │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-01 - Data Ingestion                    Priority: MUST HAVE          │
│ Story Points: 5                 Sprint: 1                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] File upload accepts PDF, JPG, PNG formats only                             │
│ [ ] Maximum file size: 10MB per file                                           │
│ [ ] Files stored in encrypted blob storage                                      │
│ [ ] Document linked to entity via Entity ID                                     │
│ [ ] Upload confirmation with file ID returned                                   │
│ [ ] Duplicate file detection (hash comparison)                                │
│                                                                                  │
│ Technical Notes:                                                                │
│ - Endpoint: POST /api/v1/entities/{id}/documents                              │
│ - Storage: Azure Blob with AES-256 encryption                                  │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### US-03: Document Validation Engine

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-03                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As a Compliance Analyst,                                                     │
│  I want the system to automatically validate uploaded documents                │
│  so that incomplete submissions are identified immediately."                    │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-01 - Data Ingestion                    Priority: SHOULD HAVE        │
│ Story Points: 3                 Sprint: 1                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] System checks for required document types (COI, address, PAN, UBO)        │
│ [ ] Completeness score calculated (0-100%)                                      │
│ [ ] Missing documents flagged with specific message                            │
│ [ ] Validation result included in entity detail response                       │
│ [ ] Incomplete entities blocked from scoring                                   │
│                                                                                  │
│ Business Rule:                                                                  │
│ Minimum required: Certificate of Incorporation, Address Proof, PAN, UBO Form   │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Epic 2: Risk Scoring

### US-04: ML Risk Scoring Engine

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-04                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As a Compliance Analyst,                                                     │
│  I want the system to calculate a risk score using the ML model                 │
│  so that entities are objectively assessed across 9 risk dimensions."          │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-02 - Risk Scoring                     Priority: MUST HAVE           │
│ Story Points: 8                Sprint: 2                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] Model scores entity across all 9 risk dimensions                           │
│ [ ] Weighted aggregate score calculated (0-100)                               │
│ [ ] Scoring completes within 2 minutes                                         │
│ [ ] Dimension-level scores visible in response                                 │
│ [ ] Model version tracked for audit                                            │
│ [ ] Score calculation logged with all inputs                                   │
│                                                                                  │
│ Risk Dimensions:                                                                │
│ 1. UBO Transparency (15%)    2. Jurisdiction Risk (20%)                       │
│ 3. Sector Risk (10%)         4. Sanctions Exposure (20%)                       │
│ 5. Adverse Media (10%)       6. PEP Association (10%)                          │
│ 7. Shell Company Indicators (5%)  8. Financial Red Flags (5%)                  │
│ 9. Document Completeness (5%)                                                   │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### US-05: Risk Classification Engine

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-05                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As a Technology Lead,                                                        │
│  I want entities to be automatically classified into risk tiers                │
│  so that the appropriate processing workflow is triggered."                     │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-02 - Risk Scoring                     Priority: MUST HAVE           │
│ Story Points: 5                Sprint: 2                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] Entities scored 0-30 classified as LOW RISK                                │
│ [ ] Entities scored 31-60 classified as MEDIUM RISK                           │
│ [ ] Entities scored 61-100 classified as HIGH RISK                              │
│ [ ] Correct workflow triggered based on classification                          │
│ [ ] Classification timestamp recorded                                          │
│ [ ] Classification history maintained                                          │
│                                                                                  │
│ Business Rules:                                                                 │
│ - Score 0-30: Auto-Approve workflow (same day SLA)                             │
│ - Score 31-60: Analyst Review workflow (1 day SLA)                              │
│ - Score 61-100: EDD workflow (3-5 day SLA)                                     │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### US-06: External Data Integration

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-06                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As a Compliance Analyst,                                                     │
│  I want the system to query external screening services                        │
│  so that sanctions, PEP, and adverse media checks are performed automatically."│
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-02 - Risk Scoring                     Priority: SHOULD HAVE        │
│ Story Points: 5                Sprint: 2                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] World-Check API called for PEP/sanctions screening                         │
│ [ ] Dow Jones API called for adverse media search                               │
│ [ ] D&B API called for company verification                                    │
│ [ ] API results incorporated into risk dimensions                              │
│ [ ] Timeout handling (5 second max wait)                                       │
│ [ ] Fallback to manual lookup if service unavailable                            │
│ [ ] Cost per query tracked for reporting                                       │
│                                                                                  │
│ External Services:                                                              │
│ - World-Check (Refinitiv)                                                      │
│ - Dow Jones Risk & Compliance                                                   │
│ - Dun & Bradstreet                                                             │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### US-07: Manual Override Capability

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-07                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As an MLRO,                                                                  │
│  I want to be able to manually override risk classifications                    │
│  so that exceptional cases can be processed with appropriate justification."    │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-02 - Risk Scoring                     Priority: SHOULD HAVE        │
│ Story Points: 3                Sprint: 2                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] MLRO can override any classification                                       │
│ [ ] Override requires mandatory reason entry                                   │
│ [ ] Override logged in audit trail with timestamp and user                      │
│ [ ] Original score preserved for comparison                                    │
│ [ ] Override report available for monthly review                               │
│ [ ] More than 5% overrides flagged for management review                      │
│                                                                                  │
│ Business Rules:                                                                 │
│ - Only MLRO role has override permission                                       │
│ - Reason field minimum 20 characters                                           │
│ - Monthly override report to Compliance Head                                   │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Epic 3: Alert Management

### US-08: High-Risk Alert Generation

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-08                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As a Compliance Analyst,                                                     │
│  I want immediate alerts generated for high-risk entities                       │
│  so that enhanced due diligence can be initiated without delay."               │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-03 - Alert Management                 Priority: MUST HAVE          │
│ Story Points: 5                Sprint: 3                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] Alert generated within 2 minutes of scoring for score > 60               │
│ [ ] Email notification sent to Compliance team                                 │
│ [ ] Alert visible on dashboard with HIGH priority indicator                     │
│ [ ] Alert includes: entity name, risk score, top 3 risk factors              │
│ [ ] Alert includes recommended action                                          │
│ [ ] Alert acknowledgment tracking                                              │
│                                                                                  │
│ Alert Content:                                                                  │
│ - Entity Name & ID                                                              │
│ - Risk Score & Classification                                                  │
│ - Top 3 Risk Factors (dimension + score)                                      │
│ - Recommended Action                                                            │
│ - Link to full entity details                                                   │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### US-09: Case Management Queue

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-09                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As a Compliance Analyst,                                                     │
│  I want medium-risk cases to appear in a review queue                          │
│  so that I can process them efficiently with all relevant information."         │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-03 - Alert Management                 Priority: SHOULD HAVE        │
│ Story Points: 3                Sprint: 3                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] Medium-risk cases automatically added to review queue                      │
│ [ ] Cases sorted by score (highest risk first)                                 │
│ [ ] Single screen shows all entity details                                      │
│ [ ] Dimension breakdown visible                                                │
│ [ ] Document viewer integrated                                                  │
│ [ ] One-click approve/reject buttons                                            │
│ [ ] Rejection requires reason selection                                        │
│                                                                                  │
│ Queue Management:                                                               │
│ - Daily capacity indicator                                                      │
│ - SLA countdown timer                                                           │
│ - Workload distribution visible to Team Lead                                   │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### US-10: Auto-Approval Workflow

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-10                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As a Technology Lead,                                                        │
│  I want low-risk entities to be auto-approved without manual intervention     │
│  so that resources are focused on high-risk cases."                             │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-03 - Alert Management                 Priority: MUST HAVE           │
│ Story Points: 3                Sprint: 3                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] Auto-approval triggered within 5 minutes of scoring                       │
│ [ ] Only entities with score 0-30 qualify                                      │
│ [ ] All mandatory documents must be complete                                    │
│ [ ] Approval notification sent to entity via email                              │
│ [ ] Entity status updated to "APPROVED"                                        │
│ [ ] No human intervention required                                              │
│ [ ] Auto-approval rate tracked (target: 70% of portfolio)                     │
│                                                                                  │
│ Business Rules:                                                                 │
│ - Score range: 0-30                                                            │
│ - Document completeness: 100%                                                  │
│ - No external data provider errors                                              │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Epic 4: Reporting

### US-11: Operations Dashboard

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-11                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As a Compliance Head,                                                         │
│  I want a real-time dashboard showing KYB operations metrics                   │
│  so that I can monitor performance and identify issues quickly."               │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-04 - Reporting                         Priority: SHOULD HAVE        │
│ Story Points: 5                Sprint: 4                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] Dashboard displays total entities onboarded (daily/weekly/monthly)        │
│ [ ] Risk tier distribution chart (pie or bar)                                  │
│ [ ] Average TAT by risk tier displayed                                          │
│ [ ] Approval/Rejection rates shown                                              │
│ [ ] Analyst workload distribution visible                                       │
│ [ ] Dashboard loads within 3 seconds                                            │
│ [ ] Data refreshes every 15 minutes                                             │
│ [ ] Date range filter available                                                │
│ [ ] Export to Excel available                                                   │
│                                                                                  │
│ Metrics:                                                                       │
│ - Total Volume: Daily, Weekly, Monthly                                          │
│ - TAT: Average by tier                                                         │
│ - Quality: Approval rate, Rejection rate, Rework rate                          │
│ - Resources: Analyst workload, Queue depth                                      │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### US-12: Compliance Reporting

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER STORY: US-12                                                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│ "As an MLRO,                                                                  │
│  I want monthly compliance reports generated automatically                     │
│  so that regulatory submissions and board reviews are supported."               │
│                                                                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Epic: EPIC-04 - Reporting                         Priority: SHOULD HAVE        │
│ Story Points: 3                Sprint: 4                                         │
│                                                                                  │
│ Acceptance Criteria:                                                            │
│ [ ] Monthly report generated on 1st of each month                              │
│ [ ] Report includes: total onboarded, risk distribution, TAT                  │
│ [ ] Report includes: high-risk cases summary                                   │
│ [ ] Report includes: override statistics                                        │
│ [ ] Report includes: model performance metrics                                  │
│ [ ] PDF export available                                                       │
│ [ ] Report auto-emailed to MLRO and Compliance Head                            │
│ [ ] 7-year report archive maintained                                           │
│                                                                                  │
│ Report Sections:                                                                │
│ 1. Executive Summary                                                            │
│ 2. Volume & TAT Metrics                                                         │
│ 3. Risk Distribution                                                           │
│ 4. High-Risk Case Summary                                                       │
│ 5. Model Performance                                                           │
│ 6. Compliance Exceptions                                                       │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Story Summary Table

| Epic | US ID | Title | Priority | Points | Sprint |
|------|-------|-------|----------|--------|--------|
| EPIC-01 | US-01 | Entity Submission API | MUST | 5 | 1 |
| EPIC-01 | US-02 | Document Upload | MUST | 5 | 1 |
| EPIC-01 | US-03 | Document Validation | SHOULD | 3 | 1 |
| EPIC-02 | US-04 | ML Risk Scoring | MUST | 8 | 2 |
| EPIC-02 | US-05 | Risk Classification | MUST | 5 | 2 |
| EPIC-02 | US-06 | External Integration | SHOULD | 5 | 2 |
| EPIC-02 | US-07 | Manual Override | SHOULD | 3 | 2 |
| EPIC-03 | US-08 | High-Risk Alert | MUST | 5 | 3 |
| EPIC-03 | US-09 | Case Queue | SHOULD | 3 | 3 |
| EPIC-03 | US-10 | Auto-Approval | MUST | 3 | 3 |
| EPIC-04 | US-11 | Dashboard | SHOULD | 5 | 4 |
| EPIC-04 | US-12 | Compliance Report | SHOULD | 3 | 4 |

### Sprint Allocation

| Sprint | Stories | Points | Focus |
|--------|---------|--------|-------|
| Sprint 1 | US-01, US-02, US-03 | 13 | Data Ingestion |
| Sprint 2 | US-04, US-05, US-06, US-07 | 21 | Risk Scoring |
| Sprint 3 | US-08, US-09, US-10 | 11 | Alert Management |
| Sprint 4 | US-11, US-12 | 8 | Reporting |

---

## 8. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 2026 | Kishore U. | Initial release |

**Contact:** Kishore U. | github.com/ukishore33 | linkedin.com/in/kishore-techie | 6303308133