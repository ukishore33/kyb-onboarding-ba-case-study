# Process Mapping: As-Is vs To-Be Analysis

**Project Name:** NovaPay KYB Risk Scoring Engine  
**Document Type:** Process Mapping Document  
**Version:** 1.0 | **Date:** April 2026  
**Author:** Kishore U. | [LinkedIn](https://linkedin.com/in/kishore-techie) | 6303308133

---

## 1. Executive Overview

This document provides a detailed comparison between the current manual KYB onboarding process (As-Is) and the proposed automated process (To-Be). The analysis highlights pain points, improvement opportunities, and quantified benefits.

---

## 2. As-Is Process: Manual KYB Onboarding

### 2.1 Current Process Flow

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           AS-IS: MANUAL KYB PROCESS                                  │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐       │
│  │ Entity   │───▶│ Document │───▶│ Analyst  │───▶│ World-   │───▶│ Risk     │       │
│  │ Submission│    │ Collection│    │ Screening│    │ Check    │───▶│ Assessment│      │
│  └──────────┘    └──────────┘    └──────────┘    │ Screening│    └──────────┘       │
│       │              │              │              └──────────┘         │            │
│       │              │              │                                       │          │
│       ▼              ▼              ▼                                       ▼          │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                         MANUAL ACTIVITIES                                   │   │
│  │  • Entity fills PDF forms (3-5 days)                                      │   │
│  │  • Email documents to compliance@novapay.com                                │   │
│  │  • Analyst downloads, organizes documents                                  │   │
│  │  • Manual World-Check search (30-45 min per entity)                        │   │
│  │  • Manual adverse media search (20-30 min)                                 │   │
│  │  • Manual UBO tracing from declaration forms                               │   │
│  │  • Manual jurisdiction risk assessment                                      │   │
│  │  • Team lead review (1-2 days)                                              │   │
│  │  • MLRO sign-off for high-risk cases (1-2 days)                            │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                    │                                               │
│                                    ▼                                               │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐                     │
│  │ Approve │    │ Reject   │    │ Request  │    │ Escalate │                     │
│  │ (40%)   │    │ (15%)    │    │ Additional│   │ to MLRO  │                     │
│  └──────────┘    └──────────┘    │ Info (45%)│   │ (10%)    │                     │
│                                  └──────────┘    └──────────┘                     │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Step-by-Step Process Details

| Step | Activity | Owner | Time | Pain Point |
|------|----------|-------|------|------------|
| 1 | Entity submits application form | Business Entity | 3-5 days | ⏱ Slow form completion |
| 2 | Documents received via email | Operations | 15 min | 📧 Manual email handling |
| 3 | Document verification | Compliance Analyst | 2 hours | ⚠️ 35% incomplete submissions |
| 4 | World-Check screening | Compliance Analyst | 45 min | 🔍 Manual search |
| 5 | Adverse media search | Compliance Analyst | 30 min | 🔍 Manual search |
| 6 | UBO identification | Compliance Analyst | 1 hour | 👤 Complex ownership structures |
| 7 | Jurisdiction risk assessment | Compliance Analyst | 30 min | 🌍 Manual FATF list lookup |
| 8 | Sector risk evaluation | Compliance Analyst | 20 min | 📊 Manual classification |
| 9 | Risk assessment report | Compliance Analyst | 1 hour | 📝 Manual report writing |
| 10 | Team lead review | Team Lead | 1-2 days | ⏳ Bottleneck |
| 11 | MLRO approval (if required) | MLRO | 1-2 days | ⏳ Additional delay |
| 12 | Final decision & notification | Operations | 4 hours | 📧 Manual email |

**Total Average Time: 5-7 business days**

### 2.3 As-Is Process Metrics

| Metric | Value | Issue |
|--------|-------|-------|
| Total Steps | 12 | Too many manual handoffs |
| Average TAT | 5-7 days | Above industry benchmark |
| Analyst Time per Entity | 4 hours | High manual effort |
| Rework Rate | 35% | Document issues |
| Decision Consistency | 60% | Subjective judgments |
| High-Risk Detection | 40% | Missed entities |

---

## 3. To-Be Process: Automated Risk Scoring

### 3.1 Proposed Process Flow

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                        TO-BE: AUTOMATED KYB PROCESS                                  │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐                       │
│  │ Entity   │───▶│ API      │───▶│ Document │───▶│ Auto     │                       │
│  │ Submission│    │ Ingestion│    │ Validation│   │ Risk     │                       │
│  └──────────┘    └──────────┘    └──────────┘    │ Scoring  │                       │
│       │              │              │              └──────────┘                       │
│       │              │              │                   │                             │
│       ▼              ▼              ▼                   ▼                             │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                      AUTOMATED PROCESSING (<2 minutes)                       │   │
│  │  • JSON payload validation                                                   │   │
│  │  • Document type/size check                                                 │   │
│  │  • ML model scoring across 9 dimensions                                     │   │
│  │  • External API calls (World-Check, Dow Jones)                             │   │
│  │  • Risk classification (Low/Medium/High)                                   │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                    │                                               │
│                    ┌───────────────┼───────────────┐                               │
│                    ▼               ▼               ▼                               │
│            ┌──────────┐    ┌──────────┐    ┌──────────┐                          │
│            │  LOW     │    │ MEDIUM   │    │  HIGH    │                          │
│            │  RISK    │    │  RISK    │    │  RISK    │                          │
│            │ (0-30)   │    │ (31-60)  │    │ (61-100) │                          │
│            └────┬─────┘    └────┬─────┘    └────┬─────┘                          │
│                 │              │              │                                 │
│                 ▼              ▼              ▼                                 │
│         ┌────────────┐  ┌────────────┐  ┌────────────┐                            │
│         │ AUTO-      │  │ ANALYST   │  │   EDD     │                            │
│         │ APPROVE    │  │  REVIEW   │  │  WORKFLOW │                            │
│         │ (Same day) │  │  (1 day)  │  │ (3-5 days)│                            │
│         └────────────┘  └────────────┘  └────────────┘                            │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Step-by-Step Process Details

| Step | Activity | Owner | Time | Improvement |
|------|----------|-------|------|-------------|
| 1 | Entity submits via portal | Business Entity | Real-time | ⚡ Same process |
| 2 | API receives JSON payload | System | <1 sec | ⚡ Automated |
| 3 | Document validation | System | <30 sec | ⚡ Auto validation |
| 4 | External API calls | System | <30 sec | ⚡ Parallel calls |
| 5 | ML Risk Scoring | System | <2 min | ⚡ Automated |
| 6 | Risk Classification | System | <1 sec | ⚡ Auto tiering |
| 7 | Route to workflow | System | <1 sec | ⚡ Auto routing |
| 8 | Processing (varies by tier) | System/Analyst | Same/1/3-5 days | ⚡ Tiered SLA |

**Total Average Time: Same day to 5 days (based on risk tier)**

### 3.3 Risk Tier Processing

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         RISK TIER PROCESSING MATRIX                                  │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │  LOW RISK (0-30) ────▶ AUTO-APPROVE WORKFLOW                                │   │
│   │  ┌────────────────────────────────────────────────────────────────────┐    │   │
│   │  │ Step 1: Score calculated                                          │    │   │
│   │  │ Step 2: All documents complete? ──YES──▶ Auto-approve             │    │   │
│   │  │ Step 3: Email notification sent                                    │    │   │
│   │  │ Step 4: Entity status = "APPROVED"                               │    │   │
│   │  │ Total Time: <15 minutes                                          │    │   │
│   │  └────────────────────────────────────────────────────────────────────┘    │   │
│   └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │  MEDIUM RISK (31-60) ──▶ ANALYST REVIEW WORKFLOW                           │   │
│   │  ┌────────────────────────────────────────────────────────────────────┐    │   │
│   │  │ Step 1: Added to review queue                                     │    │   │
│   │  │ Step 2: Case assigned to analyst (highest score first)            │    │   │
│   │  │ Step 3: Review entity details + risk dimensions                   │    │   │
│   │  │ Step 4: Approve / Reject / Escalate                                │    │   │
│   │  │ Step 5: Decision recorded with reason                             │    │   │
│   │  │ Total Time: 1 business day                                        │    │   │
│   │  └────────────────────────────────────────────────────────────────────┘    │   │
│   └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │  HIGH RISK (61-100) ──▶ ENHANCED DUE DILIGENCE (EDD) WORKFLOW             │   │
│   │  ┌────────────────────────────────────────────────────────────────────┐    │   │
│   │  │ Step 1: Alert generated immediately                               │    │   │
│   │  │ Step 2: Email notification to MLRO + Compliance Head              │    │   │
│   │  │ Step 3: Deep dive: UBO tracing, source of funds, references        │    │   │
│   │  │ Step 4: Additional document requests if needed                    │    │   │
│   │  │ Step 5: Committee review (if score > 80)                          │    │   │
│   │  │ Step 6: Final decision: Approve / Reject / Escalate               │    │   │
│   │  │ Total Time: 3-5 business days                                     │    │   │
│   │  └────────────────────────────────────────────────────────────────────┘    │   │
│   └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Comparative Analysis

### 4.1 Time Comparison by Risk Tier

| Risk Tier | As-Is Time | To-Be Time | Reduction |
|-----------|------------|------------|-----------|
| Low Risk (70%) | 5-7 days | Same day | 85% |
| Medium Risk (25%) | 5-7 days | 1-2 days | 70% |
| High Risk (5%) | 7-10 days | 3-5 days | 50% |
| **Portfolio Average** | **5-7 days** | **1-2 days** | **70%** |

### 4.2 Process Comparison Table

| Dimension | As-Is (Manual) | To-Be (Automated) | Improvement |
|-----------|----------------|------------------|-------------|
| **Total Steps** | 12 | 8 | 33% reduction |
| **Manual Touchpoints** | 10 | 2 | 80% reduction |
| **Average TAT** | 5-7 days | 1-2 days | 70% faster |
| **Analyst Time per Entity** | 4 hours | 15 min (medium only) | 94% reduction |
| **Rework Rate** | 35% | 8% | 77% reduction |
| **Decision Consistency** | 60% | 95% | 58% improvement |
| **High-Risk Detection** | 40% | 92% | 130% improvement |
| **Cost per Onboarding** | ₹2,800 | ₹900 (avg) | 68% reduction |

### 4.3 Pain Point Resolution

| # | As-Is Pain Point | To-Be Solution | Impact |
|---|------------------|----------------|--------|
| 1 | 5-7 day TAT | Automated scoring | 70% faster |
| 2 | 35% rework rate | Document validation | 77% reduction |
| 3 | Manual screening (75 min) | API integration | <2 min |
| 4 | Subjective decisions | ML model | Consistent |
| 5 | No risk differentiation | 3-tier classification | Targeted |
| 6 | 40% high-risk detection | 9-dimension scoring | 130% improvement |
| 7 | No audit trail | Immutable logging | Compliant |
| 8 | Scalability constraints | Auto-scaling | Future-ready |

---

## 5. Process Decision Gates

### 5.1 Decision Gate Flow

```
                              ┌─────────────────┐
                              │   NEW ENTITY    │
                              │   SUBMISSION    │
                              └────────┬────────┘
                                       │
                                       ▼
                         ┌────────────────────────┐
                         │  DATA VALIDATION       │
                         │  (API Schema Check)   │
                         └────────┬───────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
               PASS (95%)                   FAIL (5%)
                    │                           │
                    ▼                           ▼
         ┌─────────────────┐         ┌─────────────────┐
         │ DOCUMENT        │         │ REJECT WITH     │
         │ VALIDATION      │         │ ERROR MESSAGE   │
         └────────┬────────┘         └─────────────────┘
                  │
       ┌─────────┴─────────┐
       │                   │
  COMPLETE (85%)      INCOMPLETE (15%)
       │                   │
       ▼                   ▼
┌─────────────┐    ┌─────────────────┐
│ ML RISK     │    │ REQUEST ADDITIONAL│
│ SCORING     │    │ DOCUMENTS        │
│ (<2 min)    │    └─────────────────┘
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────────┐
│      RISK CLASSIFICATION                │
│  ┌─────────┬─────────┬─────────┐       │
│  │  LOW   │ MEDIUM  │  HIGH   │       │
│  │ 0-30   │ 31-60   │ 61-100  │       │
│  └────┬────┴────┬────┴────┬────┘       │
└───────┼─────────┼─────────┼────────────┘
        │         │         │
        ▼         ▼         ▼
   ┌────────┐ ┌────────┐ ┌────────┐
   │  AUTO  │ │ REVIEW │ │   EDD  │
   │APPROVE │ │ QUEUE  │ │ALERT   │
   └────────┘ └────────┘ └────────┘
```

---

## 6. Implementation Considerations

### 6.1 Change Management Impact

| Stakeholder | Impact | Mitigation |
|-------------|--------|-------------|
| Compliance Analysts | Role evolves from screener to reviewer | Training on new workflow |
| MLRO | Enhanced oversight role | Dashboard training |
| Operations | Reduced document handling | Redeployment planning |
| Business | Faster onboarding | Communication on SLAs |

### 6.2 Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Model accuracy issues | Medium | High | 90-day validation period |
| Integration failures | Low | High | Fallback to manual process |
| User adoption resistance | Medium | Medium | Training + change champions |
| Regulatory changes | Low | Medium | Quarterly model review |

---

## 7. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 2026 | Kishore U. | Initial release |

**Contact:** Kishore U. | github.com/ukishore33 | linkedin.com/in/kishore-techie | 6303308133