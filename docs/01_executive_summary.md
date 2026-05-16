# Executive Summary: KYB Onboarding Process Automation

**Project Name:** NovaPay KYB Risk Scoring Engine  
**Document Type:** Business Case & Problem Statement  
**Version:** 1.0 | **Date:** April 2026  
**Author:** Kishore U. | [LinkedIn](https://linkedin.com/in/kishore-techie) | 6303308133

---

## 1. Executive Overview

NovaPay Financial Services, a leading payment gateway fintech onboarding 500+ business entities monthly, faces significant operational challenges in its Know Your Business (KYB) onboarding process. This document presents the business case for automating the KYB risk assessment workflow using a machine learning-powered Entity Risk Scoring Engine.

---

## 2. Problem Statement

### 2.1 Current State Challenges

| Metric | Current Value | Industry Benchmark |
|--------|---------------|-------------------|
| Average KYB Onboarding Time | 5-7 business days | 2-3 days |
| Manual Analyst Workforce | 3 FTE | N/A |
| Document Rework Rate | 35% | <15% |
| Cost Per Onboarding | ₹2,800 | ₹800-1,200 |
| Risk Differentiation | None (binary) | Tiered scoring |

### 2.2 Critical Business Risks

1. **Compliance Gap:** In 2023, two entities from FATF-grey-list jurisdictions were approved without enhanced due diligence, exposing the company to regulatory scrutiny.

2. **Operational Inefficiency:** Analysts spend 70% of time on low-risk entities that could be auto-processed, diverting resources from high-risk cases requiring deeper investigation.

3. **Inconsistent Decision-Making:** Manual screening introduces subjectivity; different analysts apply varying thresholds for sanctions hits and adverse media.

4. **Scalability Constraint:** Current process cannot support NovaPay's projected growth to 1,500 monthly onboardings by Q4 2026 without proportional headcount increase.

---

## 3. Proposed Solution

### 3.1 To-Be State: Automated Risk Scoring Engine

The solution implements a Gradient Boosting ML model that evaluates entities across 9 risk dimensions:

| Risk Dimension | Data Source | Weight |
|----------------|-------------|--------|
| UBO Transparency | Entity declaration + D&B data | 15% |
| Jurisdiction Risk | FATF lists, Basel AML Index | 20% |
| Sector Risk | NAICS code classification | 10% |
| Sanctions Exposure | OFAC, EU, UN sanctions lists | 20% |
| Adverse Media | Dow Jones, LexisNexis | 10% |
| PEP Association | World-Check database | 10% |
| Shell Company Indicators | Incorporation patterns | 5% |
| Financial Red Flags | Transaction pattern analysis | 5% |
| Document Completeness | Automated document validation | 5% |

### 3.2 Risk Tiering Logic

| Risk Score Range | Classification | Processing Path | SLA |
|------------------|-----------------|------------------|-----|
| 0-30 | **Low Risk** | Auto-Approve | Same day |
| 31-60 | **Medium Risk** | Light Review (1 analyst) | 1 day |
| 61-100 | **High Risk** | Enhanced Due Diligence (EDD) | 3-5 days |

---

## 4. Business Case & ROI Calculation

### 4.1 Monthly Savings Projection

```
Current State:
- Monthly onboarding volume: 500 entities
- Cost per onboarding: ₹2,800
- Total monthly KYB cost: 500 × ₹2,800 = ₹14,00,000

Projected State (Post-Implementation):
- Low Risk (70%): 350 entities × ₹900 = ₹3,15,000
- Medium Risk (25%): 125 entities × ₹1,800 = ₹2,25,000
- High Risk (5%): 25 entities × ₹4,500 = ₹1,12,500
- Total monthly cost: ₹6,52,500

Monthly Savings: ₹14,00,000 - ₹6,52,500 = ₹7,47,500
Annual Savings: ₹7,47,500 × 12 = ₹89,70,000 (≈ ₹90 Lakhs)
```

### 4.2 Risk Reduction Benefits

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| False Negative Rate (High-risk entities missed) | 2% | 0.1% | 95% reduction |
| High-Risk Entity Detection Rate | 40% | 92% | 130% improvement |
| Regulatory Finding Probability | High | Low | Significant reduction |

### 4.3 Efficiency Gains

| Metric | Before | After | Impact |
|--------|--------|-------|--------|
| Average TAT (Low/Medium Risk) | 5-7 days | 1-2 days | 70% reduction |
| Analyst Time per Low-Risk Entity | 4 hours | 15 minutes | 94% reduction |
| Rework Rate | 35% | 8% | 77% reduction |

---

## 5. Implementation Roadmap

| Phase | Timeline | Deliverable |
|-------|----------|--------------|
| Phase 1: Discovery & Requirements | Weeks 1-2 | BRD, Process Maps |
| Phase 2: Model Development | Weeks 3-6 | ML Model, API |
| Phase 3: Integration & Testing | Weeks 7-10 | System Integration |
| Phase 4: UAT & Training | Weeks 11-12 | User Training, Go-Live |

---

## 6. Recommendation

This business case demonstrates a clear ROI with payback period of 4 months. The solution addresses critical compliance gaps while delivering substantial operational savings. **Recommendation: Approve project initiation.**

---

## 7. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 2026 | Kishore U. | Initial release |

**Contact:** Kishore U. | github.com/ukishore33 | linkedin.com/in/kishore-techie | 6303308133