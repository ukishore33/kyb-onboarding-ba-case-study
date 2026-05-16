# Business Impact Analysis: Quantified Benefits

**Project Name:** NovaPay KYB Risk Scoring Engine  
**Document Type:** Business Impact Analysis  
**Version:** 1.0 | **Date:** April 2026  
**Author:** Kishore U. | [LinkedIn](https://linkedin.com/in/kishore-techie) | 6303308133

---

## 1. Executive Summary

This document provides a comprehensive quantification of the business impact expected from implementing the KYB Risk Scoring Engine. All figures are based on NovaPay's current operational data and projected improvements from automation.

**Key Takeaways:**
- **Monthly Savings:** ₹7,47,500 (53% reduction in KYB operational costs)
- **Annual Savings:** ₹89,70,000 (approximately ₹90 Lakhs)
- **Payback Period:** 4 months
- **Risk Detection Improvement:** 130% (from 40% to 92%)

---

## 2. Before vs After Comparison

### 2.1 Operational Metrics (12-Month Comparison)

| # | Metric | Before (Manual) | After (Automated) | Change | % Improvement |
|---|--------|-----------------|------------------|--------|---------------|
| 1 | Average TAT (days) | 5-7 | 1-2 | -5 days | 70% faster |
| 2 | Cost per onboarding (₹) | 2,800 | 900 (avg) | -1,900 | 68% reduction |
| 3 | Analyst time per entity (hours) | 4 | 0.25 (low) / 2 (med) | -3.75 | 94% reduction |
| 4 | Rework rate (%) | 35 | 8 | -27 pts | 77% reduction |
| 5 | Decision consistency (%) | 60 | 95 | +35 pts | 58% improvement |
| 6 | High-risk detection rate (%) | 40 | 92 | +52 pts | 130% improvement |
| 7 | False negative rate (%) | 2 | 0.1 | -1.9 pts | 95% reduction |
| 8 | Auto-approval rate (%) | 0 | 70 | +70 pts | New capability |
| 9 | Document processing time (min) | 120 | 5 | -115 min | 96% reduction |
| 10 | External screening time (min) | 75 | 0.5 | -74.5 min | 99% reduction |
| 11 | Monthly capacity (entities) | 500 | 1,500 | +1,000 | 3x scalability |
| 12 | Compliance audit findings | 2/year | 0/year | -2 | 100% reduction |

### 2.2 Financial Metrics

| Metric | Monthly | Annual |
|--------|---------|--------|
| **Current KYB Cost** | ₹14,00,000 | ₹1,68,00,000 |
| **Projected KYB Cost** | ₹6,52,500 | ₹78,30,000 |
| **Net Savings** | ₹7,47,500 | ₹89,70,000 |

---

## 3. Detailed Savings Calculation

### 3.1 Monthly Cost Breakdown (Post-Implementation)

| Risk Tier | % of Portfolio | Volume | Cost/Entity | Total Cost |
|------------|----------------|--------|-------------|------------|
| **Low Risk** | 70% | 350 | ₹900 | ₹3,15,000 |
| **Medium Risk** | 25% | 125 | ₹1,800 | ₹2,25,000 |
| **High Risk** | 5% | 25 | ₹4,500 | ₹1,12,500 |
| **Total** | 100% | 500 | - | **₹6,52,500** |

### 3.2 Savings Calculation Assumptions

| Assumption | Value | Source |
|------------|-------|--------|
| Monthly onboarding volume | 500 entities | Operations data |
| Low-risk cost (auto-approve) | ₹900 | System estimate |
| Medium-risk cost (analyst review) | ₹1,800 | 50% of manual |
| High-risk cost (EDD) | ₹4,500 | 60% of manual |
| Risk tier distribution | 70/25/5 | ML model projection |
| Analyst fully-loaded cost | ₹75,000/month | HR data |

### 3.3 ROI Calculation

```
INVESTMENT REQUIRED:
- Development cost: ₹35,00,000
- Integration cost: ₹5,00,000
- Training cost: ₹2,00,000
- Contingency (10%): ₹4,20,000
- TOTAL INVESTMENT: ₹46,20,000

MONTHLY SAVINGS:
- Cost reduction: ₹7,47,500

ANNUAL SAVINGS:
- First year: ₹89,70,000
- Subsequent years: ₹89,70,000 (recurring)

PAYBACK PERIOD:
- Investment ÷ Monthly Savings = 46,20,000 ÷ 7,47,500 = 6.2 months
- With implementation timeline: ~4 months (after go-live)

3-YEAR ROI:
- Total savings (3 years): ₹2,69,10,000
- Net benefit (3 years): ₹2,22,90,000
- ROI: 483%
```

---

## 4. Risk Reduction Metrics

### 4.1 Compliance Risk Improvement

| Metric | Before | After | Impact |
|--------|--------|-------|--------|
| **High-Risk Entity Detection** | 40% | 92% | 130% improvement |
| **False Negative Rate** | 2% | 0.1% | 95% reduction |
| **FATF Jurisdiction Misses** | 2 cases (2023) | 0 expected | 100% prevention |
| **Regulatory Audit Findings** | 2/year | 0/year | 100% reduction |

### 4.2 Risk Tier Distribution (Projected)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    EXPECTED RISK DISTRIBUTION (Post-Implementation)             │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│   Low Risk (0-30)      ████████████████████████████████████ 70% (350 entities)  │
│   Medium Risk (31-60)  ████████████████                   25% (125 entities)  │
│   High Risk (61-100)   █████                                5% (25 entities)   │
│                                                                                  │
│   Processing Path:                                                                  │
│   • Low Risk: Auto-Approve (same day) - 350 entities/month                      │
│   • Medium Risk: Analyst Review (1 day) - 125 entities/month                     │
│   • High Risk: Enhanced DD (3-5 days) - 25 entities/month                        │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 4.3 Risk Dimension Impact

| Risk Dimension | Detection Method | Improvement |
|----------------|------------------|-------------|
| UBO Transparency | ML model + D&B | Automated tracing |
| Jurisdiction Risk | FATF API integration | Real-time monitoring |
| Sector Risk | NAICS classification | Consistent scoring |
| Sanctions Exposure | World-Check API | Instant screening |
| Adverse Media | Dow Jones API | Comprehensive search |
| PEP Association | World-Check API | Instant matching |
| Shell Company Indicators | ML pattern detection | 85% accuracy |
| Financial Red Flags | Transaction analysis | New capability |
| Document Completeness | Auto-validation | 100% coverage |

---

## 5. Operational Efficiency Gains

### 5.1 Time Savings by Activity

| Activity | Before (min) | After (min) | Savings |
|----------|--------------|-------------|---------|
| Document verification | 120 | 5 | 115 min |
| World-Check screening | 45 | 0.5 | 44.5 min |
| Adverse media search | 30 | 0.5 | 29.5 min |
| UBO tracing | 60 | 5 | 55 min |
| Risk assessment | 45 | 0 (auto) | 45 min |
| Report writing | 60 | 0 (auto) | 60 min |
| **Total per entity** | **360 min** | **11 min** | **349 min** |

### 5.2 Analyst Workload Transformation

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Entities reviewed per analyst/month | 167 | 42 | -75% |
| Time on low-risk entities | 70% | 10% | -60 pts |
| Time on high-risk entities | 10% | 50% | +40 pts |
| Focus on value-adding work | 30% | 90% | +60 pts |

### 5.3 Scalability Improvement

| Metric | Current Limit | Projected Capacity | Growth |
|--------|---------------|-------------------|--------|
| Monthly entities | 500 | 1,500 | 3x |
| With same headcount | 500 | 1,500 | 3x |
| Cost per additional entity | ₹2,800 | ₹900 | -68% |

---

## 6. 12-Month P&L Impact

### 6.1 Monthly P&L Projection

| Month | Volume | Savings | Cumulative |
|-------|--------|---------|------------|
| Month 1 (Implementation) | - | -₹46,20,000 | -₹46,20,000 |
| Month 2 (Go-Live) | 500 | ₹7,47,500 | -₹38,72,500 |
| Month 3 | 500 | ₹7,47,500 | -₹31,25,000 |
| Month 4 | 500 | ₹7,47,500 | -₹23,77,500 |
| Month 5 | 500 | ₹7,47,500 | -₹16,30,000 |
| Month 6 | 500 | ₹7,47,500 | -₹8,82,500 |
| Month 7 | 500 | ₹7,47,500 | -₹1,35,000 |
| **Month 8** | 500 | ₹7,47,500 | **₹6,12,500** |
| Month 9 | 500 | ₹7,47,500 | ₹13,60,000 |
| Month 10 | 500 | ₹7,47,500 | ₹21,07,500 |
| Month 11 | 500 | ₹7,47,500 | ₹28,55,000 |
| Month 12 | 500 | ₹7,47,500 | ₹36,02,500 |

### 6.2 Year 2-3 Projections

| Year | Annual Savings | Cumulative | Notes |
|------|----------------|------------|-------|
| Year 1 | ₹89,70,000 | ₹36,02,500 | Partial year (8 months) |
| Year 2 | ₹89,70,000 | ₹1,25,72,500 | Full year |
| Year 3 | ₹89,70,000 | ₹2,15,42,500 | Full year |

---

## 7. Intangible Benefits

### 7.1 Quantifiable Intangibles

| Benefit | Description | Estimated Value |
|---------|-------------|-----------------|
| **Brand Protection** | Avoided regulatory penalties | ₹10,00,000/year |
| **Faster Onboarding** | Improved merchant acquisition | ₹25,00,000/year |
| **Competitive Advantage** | Differentiated service offering | ₹15,00,000/year |
| **Employee Satisfaction** | Reduced manual repetitive work | Improved retention |

### 7.2 Strategic Benefits

| Benefit | Impact |
|---------|--------|
| **Regulatory Confidence** | Stronger RBI relationship |
| **Scalability** | Support 3x growth without headcount |
| **Audit Readiness** | Complete audit trail |
| **Future-Proofing** | Foundation for AI/ML expansion |

---

## 8. Sensitivity Analysis

### 8.1 Best Case / Worst Case

| Scenario | Monthly Savings | Annual Savings | Payback |
|----------|-----------------|----------------|---------|
| **Best Case** (+20% volume) | ₹8,97,000 | ₹1,07,64,000 | 5 months |
| **Base Case** | ₹7,47,500 | ₹89,70,000 | 6 months |
| **Worst Case** (-20% volume) | ₹5,98,000 | ₹71,76,000 | 8 months |

### 8.2 Key Assumptions Sensitivity

| Variable | Sensitivity | Impact on ROI |
|----------|-------------|---------------|
| Volume changes ±20% | Medium | ±₹15L/year |
| Cost per entity ±10% | Low | ±₹7L/year |
| Risk distribution shifts | High | ±₹20L/year |

---

## 9. Implementation Risks & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Model accuracy <90% | Medium | High | 90-day validation period |
| Integration delays | Low | Medium | Buffer in timeline |
| User adoption resistance | Medium | Medium | Training + champions |
| External API costs higher | Low | Low | Budget contingency |

---

## 10. Conclusion

The business case demonstrates a strong financial and operational impact:

- **Payback Period:** 6 months (4 months post-implementation)
- **3-Year Net Benefit:** ₹2.23 Crores
- **Risk Detection:** 130% improvement
- **Operational Efficiency:** 70% faster TAT

**Recommendation:** Proceed with implementation as the project meets all financial and strategic criteria.

---

## 11. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | April 2026 | Kishore U. | Initial release |

**Contact:** Kishore U. | github.com/ukishore33 | linkedin.com/in/kishore-techie | 6303308133