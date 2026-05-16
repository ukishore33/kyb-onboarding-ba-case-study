# Business Requirements Document (BRD)

**Project Name:** NovaPay KYB Risk Scoring Engine  
**Document Type:** BRD  
**Version:** 1.0 | **Date:** April 2026  
**Author:** Kishore U. | [LinkedIn](https://linkedin.com/in/kishore-techie) | 6303308133

---

## 1. Introduction

### 1.1 Purpose of Document

This Business Requirements Document (BRD) defines the functional and non-functional requirements for the KYB Onboarding Process Automation project at NovaPay Financial Services. The document serves as the primary reference for all stakeholders during the development, testing, and implementation phases.

### 1.2 Project Objectives

| Objective | Success Criteria |
|-----------|------------------|
| Reduce KYB onboarding TAT | From 5-7 days to 1-2 days for 70% of entities |
| Lower cost per onboarding | From ₹2,800 to ₹900 for low-risk entities |
| Improve risk detection | From 40% to 92% high-risk entity identification |
| Ensure RBI compliance | Zero regulatory findings in audits |

### 1.3 Scope Definition

**In Scope:**
- Automated risk scoring using ML model
- Integration with existing document management system
- Risk-tiered processing workflow (Auto-Approve / Review / EDD)
- Real-time dashboard and reporting
- Alert management for high-risk entities

**Out of Scope:**
- Customer-facing portal changes
- Changes to core payment gateway systems
- Real-time transaction monitoring
- Credit risk assessment
- AML transaction scanning (separate project)

---

## 2. Stakeholders

### 2.1 Stakeholder Register

| Stakeholder | Role | Department | Interest | Influence |
|-------------|------|------------|----------|------------|
| Priya Sharma | MLRO | Compliance | High | High |
| Rajesh Kumar | Compliance Head | Compliance | High | High |
| Amit Verma | Technology Lead | IT/Technology | Medium | High |
| Sneha Reddy | Business Head | Payments Business | High | Medium |
| Vikram Singh | Operations Manager | Operations | Medium | Medium |
| Finance Team | Cost Center Owner | Finance | Medium | Low |

### 2.2 RACI Matrix

| Activity | MLRO | Compliance Head | Tech Lead | Business Head | Operations | Finance |
|----------|------|------------------|------------|---------------|------------|---------|
| Requirements Gathering | A | R | C | C | I | I |
| BRD Approval | I | A | C | C | I | I |
| Functional Spec Development | C | R | A | C | I | I |
| Non-Functional Spec | C | C | A | I | I | I |
| UAT Sign-off | A | R | C | C | R | I |
| Go-Live Approval | R | A | C | C | I | C |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## 3. Functional Requirements

### 3.1 Requirements Overview

All functional requirements are prioritized using MoSCoW methodology:

- **Must Have (M):** Critical for project success; non-negotiable
- **Should Have (S):** Important for business value; strongly desired
- **Could Have (C):** Nice to have; enhances user experience
- **Won't Have (W):** Explicitly excluded from current scope

---

### FR-01: Entity Data Ingestion

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-01 |
| **Priority** | Must Have |
| **Description** | System must accept entity registration data via API from the onboarding portal |
| **Business Rule** | All mandatory fields (entity name, registration number, address, UBO details) must be captured before processing |
| **Validation** | JSON schema validation with error response for invalid payloads |

**Acceptance Criteria:**
- [ ] API endpoint accepts POST request with entity JSON payload
- [ ] Valid payload creates new entity record in system
- [ ] Invalid payload returns 400 error with field-level validation messages
- [ ] System generates unique Entity ID for tracking

---

### FR-02: Document Upload & Validation

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-02 |
| **Priority** | Must Have |
| **Description** | System must accept and validate supporting documents (certificate of incorporation, address proof, UBO declarations) |
| **Business Rule** | Minimum 4 documents required: COI, address proof, PAN, UBO declaration |
| **Validation** | File type: PDF, JPG, PNG only; max 10MB per file |

**Acceptance Criteria:**
- [ ] File upload API accepts multipart/form-data
- [ ] System validates file type and size before accepting
- [ ] Document completeness score calculated (0-100%)
- [ ] Incomplete submissions flagged for user notification

---

### FR-03: Risk Dimension Scoring

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-03 |
| **Priority** | Must Have |
| **Description** | ML model must score entity across 9 risk dimensions |
| **Business Rule** | Each dimension scored 0-100; weighted aggregate determines final risk score |

**Risk Dimensions & Weights:**

| Dimension | Weight | Data Source |
|-----------|--------|--------------|
| UBO Transparency | 15% | Entity declaration + D&B |
| Jurisdiction Risk | 20% | FATF, Basel Index |
| Sector Risk | 10% | NAICS classification |
| Sanctions Exposure | 20% | OFAC, EU, UN lists |
| Adverse Media | 10% | Dow Jones |
| PEP Association | 10% | World-Check |
| Shell Company Indicators | 5% | Incorporation patterns |
| Financial Red Flags | 5% | Internal transaction data |
| Document Completeness | 5% | Automated validation |

**Acceptance Criteria:**
- [ ] All 9 dimensions scored for each entity
- [ ] Weighted aggregate calculated within 2 minutes
- [ ] Dimension-level scores visible in entity detail view
- [ ] Model version tracked for audit trail

---

### FR-04: Risk Classification Engine

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-04 |
| **Priority** | Must Have |
| **Description** | System must classify entities into risk tiers based on aggregate score |
| **Business Rule** | Classification determines processing workflow |

| Risk Tier | Score Range | Processing Path | SLA |
|-----------|-------------|------------------|-----|
| Low | 0-30 | Auto-Approve | Same day |
| Medium | 31-60 | Light Review | 1 day |
| High | 61-100 | Enhanced Due Diligence | 3-5 days |

**Acceptance Criteria:**
- [ ] Entities automatically classified upon score calculation
- [ ] Correct workflow triggered based on classification
- [ ] Manual override capability for MLRO (with audit trail)
- [ ] Classification history maintained

---

### FR-05: Auto-Approval Workflow

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-05 |
| **Priority** | Must Have |
| **Description** | Low-risk entities must be auto-approved without manual intervention |
| **Business Rule** | Only entities scoring 0-30 with all mandatory documents complete qualify |

**Acceptance Criteria:**
- [ ] Auto-approval triggered within 5 minutes of score finalization
- [ ] Approval notification sent to entity via email
- [ ] Entity status updated to "Approved" in system
- [ ] No human intervention required for low-risk entities

---

### FR-06: Alert Generation for High-Risk Entities

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-06 |
| **Priority** | Must Have |
| **Description** | System must generate immediate alerts for high-risk entities requiring EDD |
| **Business Rule** | Alert must include risk score, dimension breakdown, and recommended actions |

**Acceptance Criteria:**
- [ ] Alert generated within 2 minutes of scoring for high-risk entities
- [ ] Email notification sent to Compliance team
- [ ] Alert visible on dashboard with priority indicator
- [ ] Alert includes: entity name, risk score, top 3 risk factors, recommended action

---

### FR-07: Case Management for Review Queue

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-07 |
| **Priority** | Should Have |
| **Description** | Medium-risk entities must be routed to analyst review queue with all relevant information |
| **Business Rule** | Each case must include entity summary, risk score, dimension breakdown, and document links |

**Acceptance Criteria:**
- [ ] Cases automatically added to review queue upon classification
- [ ] Cases sorted by score (highest risk first)
- [ ] Analyst can view all entity details in single screen
- [ ] Analyst can approve, reject, or escalate case

---

### FR-08: Reporting & Analytics Dashboard

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-08 |
| **Priority** | Should Have |
| **Description** | Real-time dashboard must display KYB operations metrics |
| **Business Rule** | Dashboard must be accessible to Compliance Head, MLRO, and Business Head |

**Required Metrics:**
- Total entities onboarded (daily/weekly/monthly)
- Risk tier distribution
- Average TAT by risk tier
- Approval/Rejection rates
- Analyst workload distribution

**Acceptance Criteria:**
- [ ] Dashboard loads within 3 seconds
- [ ] Data refreshes every 15 minutes
- [ ] Export to Excel/PDF available
- [ ] Date range filter available

---

### FR-09: Audit Trail & Compliance Logging

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-09 |
| **Priority** | Must Have |
| **Description** | All system actions must be logged for RBI audit compliance |
| **Business Rule** | Logs must be immutable and retained for 7 years |

**Acceptance Criteria:**
- [ ] Every API call logged with timestamp, user, action, result
- [ ] Score calculation inputs and outputs logged
- [ ] Manual override actions logged with reason
- [ ] Log export available for audit purposes

---

### FR-10: User Access Management

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-10 |
| **Priority** | Should Have |
| **Description** | Role-based access control must be implemented |
| **Business Rule** | Access based on job function; no shared credentials |

| Role | Permissions |
|------|-------------|
| MLRO | Full access, override capability, system config |
| Compliance Analyst | View all, approve/reject medium risk, view documents |
| Technology Lead | System config, API access, no approval rights |
| Business Head | Dashboard only, no approval rights |

**Acceptance Criteria:**
- [ ] SSO integration with corporate AD
- [ ] Role-based menu visibility
- [ ] Session timeout after 30 minutes inactivity
- [ ] Failed login attempts logged and locked after 5 attempts

---

### FR-11: Integration with External Data Providers

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-11 |
| **Priority** | Could Have |
| **Description** | System must integrate with external screening services |
| **Business Rule** | API-based integration; fallback to manual lookup if service unavailable |

**External Providers:**
- Dow Jones (Adverse Media)
- World-Check (PEP, Sanctions)
- Dun & Bradstreet (Company data)

**Acceptance Criteria:**
- [ ] API integration functional for all 3 providers
- [ ] Timeout handling (5 second max wait)
- [ ] Fallback process defined for service outage
- [ ] Cost per query tracked for reporting

---

### FR-12: Notification Engine

| Attribute | Details |
|-----------|---------|
| **Requirement ID** | FR-12 |
| **Priority** | Could Have |
| **Description** | Automated notifications for key workflow events |
| **Business Rule** | Email and in-app notifications for stakeholders |

**Notification Triggers:**
- Entity submitted for processing
- Risk score calculated
- Classification assigned
- Alert generated (high risk)
- Case assigned to analyst
- Approval/Rejection decision made

**Acceptance Criteria:**
- [ ] Email notifications sent for all triggers
- [ ] In-app notification center with unread count
- [ ] Notification preferences configurable per user
- [ ] Notification history retained for 90 days

---

## 4. Non-Functional Requirements

### 4.1 Performance Requirements

| Requirement | Target | Measurement |
|-------------|--------|-------------|
| API Response Time | <500ms (p95) | APM tool |
| Risk Score Calculation | <2 minutes | End-to-end timing |
| Dashboard Load Time | <3 seconds | Browser timing |
| Concurrent Users | 50 | Load testing |
| Daily Processing Capacity | 1,000 entities | Stress testing |

### 4.2 Security Requirements

| Requirement | Specification |
|-------------|----------------|
| Data Encryption | AES-256 at rest, TLS 1.3 in transit |
| API Authentication | OAuth 2.0 with JWT tokens |
| PII Protection | Tokenization of entity data |
| Access Control | RBAC with AD integration |
| Vulnerability Scanning | Monthly automated scans |

### 4.3 Availability Requirements

| Requirement | Target |
|-------------|--------|
| System Uptime | 99.5% (excluding planned maintenance) |
| Recovery Time Objective (RTO) | 4 hours |
| Recovery Point Objective (RPO) | 1 hour |
| Maintenance Window | Sundays 2AM-6AM IST |

### 4.4 Compliance Requirements

| Requirement | Standard |
|-------------|----------|
| Data Retention | 7 years (RBI mandate) |
| Audit Trail | Immutable logs |
| Regulatory Reporting | Monthly RBI compliance report |
| Model Governance | Annual model validation |

---

## 5. Assumptions & Constraints

### 5.1 Assumptions

1. External data provider APIs (Dow Jones, World-Check, D&B) will be available during implementation
2. Existing IT infrastructure can support the new system without major upgrades
3. Stakeholders will be available for requirements review sessions
4. Training data for ML model will be provided by Compliance team
5. VPN access will be provided for remote development team

### 5.2 Constraints

1. **Budget:** Project must be completed within allocated budget of ₹45 Lakhs
2. **Timeline:** Go-live target is Q2 2026 (12-week implementation)
3. **Resource:** Only 2 developers available for build phase
4. **Integration:** Cannot modify core banking systems; only API integration
5. **Regulatory:** All changes must be approved by MLRO before production deployment

---

## 6. Dependencies

| Dependency | Impact | Owner |
|------------|--------|-------|
| External screening API access | Blocking | Technology Lead |
| Entity onboarding portal API | Blocking | Product Team |
| ML model training data | Blocking | Compliance Head |
| UAT environment setup | Non-blocking | Technology Lead |
| User training materials | Non-blocking | Business Analyst |

---

## 7. Acceptance Criteria Summary

| Requirement ID | Requirement | Acceptance Criteria Met? |
|----------------|-------------|--------------------------|
| FR-01 | Entity Data Ingestion | ☐ |
| FR-02 | Document Upload & Validation | ☐ |
| FR-03 | Risk Dimension Scoring | ☐ |
| FR-04 | Risk Classification Engine | ☐ |
| FR-05 | Auto-Approval Workflow | ☐ |
| FR-06 | Alert Generation | ☐ |
| FR-07 | Case Management | ☐ |
| FR-08 | Reporting Dashboard | ☐ |
| FR-09 | Audit Trail | ☐ |
| FR-10 | User Access Management | ☐ |
| FR-11 | External Integration | ☐ |
| FR-12 | Notification Engine | ☐ |

---

## 8. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 2026 | Kishore U. | Initial release |

**Approved By:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| MLRO | Priya Sharma | __________ | __________ |
| Compliance Head | Rajesh Kumar | __________ | __________ |
| Technology Lead | Amit Verma | __________ | __________ |

**Contact:** Kishore U. | github.com/ukishore33 | linkedin.com/in/kishore-techie | 6303308133