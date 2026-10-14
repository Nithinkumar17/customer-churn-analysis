# Customer Churn Analysis — Business Insights

## 1. Executive Summary

This project analyzes customer churn in a telecommunications dataset to identify customer segments associated with churn and develop data-driven retention recommendations.

The analysis was performed using Python, SQL Server, and Power BI. The workflow included data inspection, data cleaning, exploratory data analysis, SQL-based analysis, and interactive dashboard development.

### Overall Customer Metrics

| Metric                  | Result |
| ----------------------- | -----: |
| Total Customers         |  7,043 |
| Churned Customers       |  1,869 |
| Retained Customers      |  5,174 |
| Overall Churn Rate      | 26.54% |
| Customer Retention Rate | 73.46% |

The results indicate that approximately 26.54% of customers in the analyzed dataset had churned.

## 2. Project Objectives

* Measure the overall customer churn rate.
* Identify customer segments with different churn patterns.
* Analyze the relationship between contract type and churn.
* Investigate tenure, subscribed services, and billing preferences.
* Examine payment methods and monthly charges.
* Build an interactive Power BI dashboard to communicate findings.
* Recommend potential retention strategies based on the observed data.

## 3. Key Areas of Analysis

### Contract Analysis

Customer churn was compared across month-to-month, one-year, and two-year contracts.

**Business implication:** Contract segments with higher churn rates may benefit from targeted retention initiatives. Any contract incentives should be evaluated against customer lifetime value, profitability, and customer needs.

### Customer Tenure

Customers were grouped by tenure to compare churn patterns across different stages of the customer relationship.

**Business implication:** If early-tenure customers show higher churn, the business could investigate onboarding, service activation, customer expectations, and early support experiences.

### Service Analysis

Churn rates were compared across internet service, online security, technical support, online backup, device protection, and streaming services.

**Business implication:** Differences between service groups may help identify areas for further investigation. The company should examine service satisfaction, product fit, and support needs before changing its service strategy.

### Payment and Billing Analysis

The analysis compared payment methods, paperless billing, monthly charges, and total charges.

**Business implication:** Payment or billing segments with elevated churn may warrant investigation into payment friction, billing clarity, affordability, and customer experience.

### Customer Demographics

The analysis compared churn patterns across gender, senior-citizen status, partner status, and dependent status.

**Business implication:** Demographic differences should be interpreted carefully. Retention programs should focus on customer needs and service experience rather than making unsupported assumptions about individuals.

## 4. Retention Recommendations

### Recommendation 1: Investigate High-Churn Contract Segments

Compare churn rates and customer counts across contract types. Test appropriate contract incentives where the data indicates a retention opportunity.

### Recommendation 2: Improve Early Customer Engagement

If newer customers have higher churn, evaluate onboarding communications, service setup, and early customer support.

### Recommendation 3: Review Technical Support and Security Services

Investigate whether customers without technical support or online security show higher churn. Use customer feedback and service-quality data to understand the underlying reasons.

### Recommendation 4: Examine Billing and Payment Experience

Review payment-related churn patterns and investigate billing complaints, failed payments, and payment convenience where relevant.

### Recommendation 5: Measure Retention Program Performance

Track churn rate, customer counts, and retention outcomes over time. Compare results before and after retention initiatives while accounting for differences between customer groups.

## 5. Tools and Technologies

* **Python:** Data inspection, cleaning, and exploratory data analysis.
* **Pandas and NumPy:** Data manipulation and validation.
* **Matplotlib and Seaborn:** Exploratory visualizations.
* **SQL Server:** Data validation, segmentation, and churn analysis.
* **Power BI:** Interactive dashboards, DAX measures, KPI cards, slicers, and visual reporting.
* **Jupyter Notebook:** Interactive Python analysis.

## 6. Project Deliverables

The project includes:

* Raw and cleaned datasets.
* Python data-cleaning scripts.
* Exploratory data analysis notebook.
* SQL scripts for data validation and churn analysis.
* Six-page Power BI dashboard.
* Business insights and retention recommendations.

## 7. Conclusion

This project demonstrates an end-to-end customer churn analysis workflow using Python, SQL Server, and Power BI.

The analysis establishes an overall churn rate of 26.54% in the dataset and provides an interactive way to investigate churn across contracts, tenure, services, demographics, and billing characteristics.

The dashboard supports data-driven investigation and retention planning. Further analysis using customer feedback, service-quality data, and longitudinal outcomes would help determine why customers leave and evaluate the effectiveness of retention initiatives.

## 8. Analytical Limitations

* The analysis identifies associations, not necessarily causal relationships.
* The dataset does not independently establish the reasons each customer churned.
* Segment-level findings should be verified against the actual analysis results before being presented as business conclusions.
* Retention initiatives should be tes
