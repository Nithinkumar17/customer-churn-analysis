# Customer Churn Analysis — Project Summary

## 1. Project Overview

**Project Name:** Customer Churn Analysis
**Project Type:** End-to-End Data Analytics Project
**Domain:** Telecommunications
**Primary Objective:** Analyze customer churn patterns and identify opportunities to improve customer retention.

This project analyzes customer churn using Python, SQL Server, and Power BI. It covers the complete analytics workflow, from data cleaning and validation to exploratory analysis, SQL-based segmentation, interactive dashboards, and business recommendations.

## 2. Business Problem

Customer churn occurs when customers stop using a company's services. High churn can reduce recurring revenue, increase customer acquisition costs, and affect long-term business growth.

The objective of this project is to understand churn patterns across customer demographics, contract types, tenure, subscribed services, and billing characteristics.

The analysis helps identify customer segments that warrant further investigation and supports data-driven retention planning.

## 3. Dataset Overview

**Dataset:** Telco Customer Churn

The dataset contains customer information, subscribed services, billing details, and churn status.

| Attribute                  | Description                                    |
| -------------------------- | ---------------------------------------------- |
| Total Customer Records     | 7,043                                          |
| Total Columns              | 21                                             |
| Target Variable            | `Churn`                                        |
| Customer Identifier        | `customerID`                                   |
| Key Numeric Variables      | `tenure`, `MonthlyCharges`, `TotalCharges`     |
| Key Segmentation Variables | `Contract`, `InternetService`, `PaymentMethod` |

The original dataset contains 7,043 customer records and 21 columns.

## 4. Tools and Technologies

| Technology       | Purpose                                     |
| ---------------- | ------------------------------------------- |
| Python           | Data cleaning and exploratory analysis      |
| Pandas           | Data manipulation and transformation        |
| NumPy            | Numerical operations                        |
| Matplotlib       | Data visualization                          |
| Seaborn          | Statistical visualization                   |
| Jupyter Notebook | Interactive analysis                        |
| SQL Server       | Data validation, segmentation, and analysis |
| Power BI         | Interactive dashboard development           |
| DAX              | KPI measures and analytical calculations    |
| Git and GitHub   | Version control and portfolio presentation  |

## 5. Project Workflow

### Phase 1: Data Inspection

* Examined the dataset structure and column data types.
* Reviewed missing values and duplicate records.
* Investigated unique values and category distributions.
* Identified data-quality issues requiring attention.

### Phase 2: Data Cleaning

* Cleaned and prepared the dataset for analysis.
* Validated numeric and categorical columns.
* Checked missing values and duplicate records.
* Prepared the cleaned dataset for SQL Server and Power BI.

### Phase 3: Exploratory Data Analysis

* Analyzed overall churn distribution.
* Investigated customer tenure and contract types.
* Examined monthly charges and customer characteristics.
* Compared churn patterns across customer segments.

### Phase 4: SQL Analysis

Created SQL scripts for:

1. Table creation and database preparation.
2. Data-quality validation.
3. Overall churn and segment analysis.
4. Customer segmentation.
5. Retention insights and prioritization.

### Phase 5: Power BI Dashboard Development

Developed a six-page interactive dashboard.

| Page | Dashboard                            |
| ---- | ------------------------------------ |
| 1    | Executive Overview                   |
| 2    | Customer Demographics                |
| 3    | Contract & Tenure Analysis           |
| 4    | Services & Churn Analysis            |
| 5    | Payment & Billing Analysis           |
| 6    | Retention Insights & Recommendations |

The dashboard includes KPI cards, churn-rate comparisons, customer segmentation, matrix visuals, and interactive slicers.

### Phase 6: Business Insights

Prepared a business insights report summarizing the analysis, potential retention opportunities, and recommended areas for further investigation.

## 6. Key Results

The validated dataset contains the following overall customer metrics:

| Metric             | Result |
| ------------------ | -----: |
| Total Customers    |  7,043 |
| Churned Customers  |  1,869 |
| Retained Customers |  5,174 |
| Overall Churn Rate | 26.54% |
| Retention Rate     | 73.46% |

These metrics provide the baseline for investigating churn across different customer segments.

The dashboard allows users to explore differences in churn by contract, tenure, demographics, services, and billing characteristics.

## 7. Key DAX Measures

The Power BI model includes measures for total customers, churned customers, retained customers, churn rate, and average monthly charges.

Example churn-rate calculation:

```dax
Churn Rate =
DIVIDE(
    [Churned Customers],
    [Total Customers],
    0
)
```

The measure supports interactive analysis by recalculating the rate in response to report filters.

## 8. Business Recommendations

Based on the observed segment-level patterns, the business can investigate:

* Retention strategies for customer groups with elevated churn.
* Onboarding improvements for customers in higher-risk tenure groups.
* Customer support and service-related retention opportunities.
* Payment and billing experience improvements.
* Ongoing monitoring of churn and retention KPIs.

Recommendations should be prioritized using actual segment-level results and validated through further analysis or controlled experiments.

## 9. Skills Demonstrated

This project demonstrates practical skills in:

* Data cleaning and validation.
* Exploratory data analysis.
* SQL querying and aggregation.
* Customer segmentation.
* KPI development using DAX.
* Interactive dashboard development.
* Business insight generation.
* Analytical reporting.
* Communicating findings to business stakeholders.

## 10. Conclusion

The Customer Churn Analysis project demonstrates an end-to-end data analytics workflow using Python, SQL Server, and Power BI.

It combines data preparation, exploratory analysis, SQL-based segmentation, interactive visualization, and business recommendations in a single portfolio project.

The resulting dashboard provides a foundation for understanding customer churn patterns and identifying opportunities to improve retention.

## 11. Project Files

The project contains:

* Raw and cleaned datasets.
* Python analysis notebook and cleaning script.
* SQL analysis scripts.
* Power BI dashboard.
* Business insights report.
* Project summary.
* README documentation.
