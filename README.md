# Strategic Analytics & Decision Frameworks
**Sai Vineeth Reddy Suravi | Senior Data Analyst**

This repository contains high-impact business intelligence projects focused on revenue optimization, risk mitigation, and product growth. Each project is structured as a case study focused on converting complex datasets into actionable executive decisions.

---

## 01. Hotel Revenue Recovery: Tackling High Cancellation Rates
**The Challenge:** High cancellation volumes were creating significant inventory instability, leading to unutilized room capacity and projected revenue loss.

- **Dataset:** 119,000+ booking records across 30+ features including lead time, market segments, and deposit history.
- **Primary Metric:** Cancellation Rate (%) & Revenue at Risk ($).
- **Analytical Strategy:** Performed a deep-dive correlation analysis and built a predictive model to isolate high-risk booking profiles.
- **Revenue Impact:** Identified that the "Transient" market segment, when combined with a lead time exceeding 90 days, accounted for 40% of all cancellations. This represents a ~$1.2M revenue leak.
- **Business Decision:** Recommended a dynamic deposit framework. By implementing non-refundable requirements for high-risk lead-time buckets, the organization can recover an estimated 25% of at-risk revenue.
- **Tradeoffs:** Stricter policies may impact initial booking velocity; recommended a phased rollout via A/B testing to monitor top-of-funnel impact.

---

## 02. Marketing ROI: Propensity Modeling for Loan Conversion
**The Challenge:** Current personal loan marketing campaigns suffered from low conversion rates, resulting in inefficient ad spend and high cost-per-acquisition (CPA).

- **Dataset:** 5,000+ customer records including demographic data, professional income levels, and historical campaign response.
- **Primary Metric:** Campaign Conversion Rate (%).
- **Analytical Strategy:** Developed a propensity scoring model (Logistic Regression & Decision Trees) to rank customers based on their likelihood to convert.
- **Revenue Impact:** Analysis revealed that high-income professionals (>100k) had a 2.4x higher conversion probability. Re-targeting this segment is projected to increase campaign ROI by 18%.
- **Business Decision:** Reallocated 50% of the quarterly marketing budget to the top-quartile propensity scores to maximize conversion yield.
- **Tradeoffs:** Heavy reliance on income-based targeting; required a fallback strategy to ensure the model remains robust during economic shifts.

---

## 03. Product Analytics: Onboarding Funnel Leakage
**The Challenge:** Significant user attrition was identified during the product onboarding phase, resulting in lost subscriber lifetime value (LTV).

- **Dataset:** Event-level logs for 10,000 users progressing through the Acquisition-Activation-Retention journey.
- **Primary Metric:** Onboarding Completion Rate (%).
- **Analytical Strategy:** Built a granular funnel model to isolate the specific interaction points causing user drop-off.
- **Revenue Impact:** Pinpointed a 65% drop-off at the "Payment Method" step. This friction point is estimated to cost $500k in Annualized Run Rate (ARR).
- **Business Decision:** Proposed a "Value-First" onboarding experiment—delaying payment collection until after core product activation or integrating 1-click payment (Apple/Google Pay).
- **Tradeoffs:** Shifting payment collection further down the funnel increases the risk of day-30 churn; recommended monitoring the 90-day retention cohort.

---

## 04. Growth Experimentation: Checkout UI Conversion Lift
**The Challenge:** Stakeholders needed to validate whether a new Checkout UI design statistically outperformed the legacy version before a global rollout.

- **Dataset:** 20,000 user sessions randomized into Control (A) and Variant (B) groups.
- **Primary Metric:** Checkout Conversion Rate (%).
- **Analytical Strategy:** Executed a two-sample proportion Z-test to measure conversion lift with 95% statistical power.
- **Revenue Impact:** Variant B demonstrated a 2.1% absolute lift (p-value = 0.012), projecting an incremental $250k in annualized revenue.
- **Business Decision:** Approved 100% rollout of the new UI based on statistical significance.
- **Tradeoffs:** Acknowledged potential "Novelty Effect"; mandated a 14-day holdout analysis to confirm the lift persists post-launch.

---

## Technical Stack & Governance
- **Languages:** SQL (Snowflake, dbt), Python (Pandas, Scikit-Learn, Statsmodels)
- **BI Tools:** Power BI (Expert DAX), Tableau, Excel (Advanced Modeling)
- **Frameworks:** CI/CD for Data Quality (GitHub Actions), Reproducible Notebooks

---
[LinkedIn](https://www.linkedin.com/in/saivineethreddysuravi) | [GitHub](https://github.com/saivineethreddysuravi) | [Portfolio](https://vineeeth.com)
