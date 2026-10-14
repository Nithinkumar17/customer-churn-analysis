# Customer Churn Analysis | Python, SQL Server & Power BI

## Project Overview

Customer churn is a significant challenge for businesses that depend on recurring customer relationships.

This project analyzes telecommunications customer data to understand churn patterns, identify customer segments that warrant further investigation, and develop data-driven retention recommendations.

The project uses **Python, SQL Server, and Power BI** to demonstrate an end-to-end data analytics workflow, from data cleaning and validation to exploratory analysis, SQL querying, dashboard development, and business reporting.

## Business Problem

The business needs to understand:

* What proportion of customers have churned?
* How does churn vary across contract types and tenure groups?
* How are subscribed services associated with churn?
* How do payment methods and billing characteristics relate to churn?
* Which customer segments should be investigated for potential retention improvements?

The goal is to turn customer data into actionable insights that support retention planning.

## Dataset Overview

**Dataset:** Telco Customer Churn

The dataset contains 7,043 customer records and 21 columns, covering customer demographics, account information, subscribed services, billing details, and churn status.

Important columns include:

| Column            | Description                           |
| ----------------- | ------------------------------------- |
| `customerID`      | Unique customer identifier            |
| `gender`          | Customer gender                       |
| `SeniorCitizen`   | Senior-citizen indicator              |
| `tenure`          | Customer tenure in months             |
| `InternetService` | Internet service type                 |
| `Contract`        | Customer contract type                |
| `PaymentMethod`   | Payment method                        |
| `MonthlyCharges`  | Monthly customer charges              |
| `TotalCharges`    | Total customer charges                |
| `Churn`           | Whether the customer left the service |

## Technologies Used

| Technology       | Application                            |
| ---------------- | -------------------------------------- |
| Python           | Data cleaning and analysis             |
| Pandas           | Data manipulation                      |
| NumPy            | Numerical operations                   |
| Matplotlib       | Visualization                          |
| Seaborn          | Statistical visualization              |
| Jupyter Notebook | Exploratory analysis                   |
| SQL Server       | Data validation and analytical queries |
| Power BI         | Interactive dashboard                  |
| DAX              | KPI calculations                       |
| Git and GitHub   | Version control and portfolio hosting  |

## Project Workflow

### 1. Data Inspection and Cleaning

* Inspected dataset structure, data types, and category distributions.
* Examined missing values and duplicate records.
* Cleaned and validated the dataset.
* Prepared the cleaned data for further analysis.

### 2. Exploratory Data Analysis

* Examined overall customer churn.
* Investigated tenure and contract patterns.
* Analyzed customer demographics and subscribed services.
* Explored billing and payment characteristics.

### 3. SQL Analysis

Developed SQL scripts to perform:

* Database table creation and preparation.
* Data-quality validation.
* Overall churn analysis.
* Customer segmentation.
* Retention insight analysis.

### 4. Power BI Dashboard

Created a six-page interactive dashboard.

| Page | Dashboard                            | Purpose                                           |
| ---- | ------------------------------------ | ------------------------------------------------- |
| 1    | Executive Overview                   | Overall customer KPIs and churn                   |
| 2    | Customer Demographics                | Churn patterns across demographic groups          |
| 3    | Contract & Tenure Analysis           | Contract and tenure comparisons                   |
| 4    | Services & Churn Analysis            | Churn across subscribed services                  |
| 5    | Payment & Billing Analysis           | Payment methods and billing characteristics       |
| 6    | Retention Insights & Recommendations | Retention analysis and potential business actions |

The dashboard includes KPI cards, bar charts, column charts, matrix visuals, and interactive slicers.

## Key Results

The validated dataset contains the following overall metrics:

| Metric             | Result |
| ------------------ | -----: |
| Total Customers    |  7,043 |
| Churned Customers  |  1,869 |
| Retained Customers |  5,174 |
| Churn Rate         | 26.54% |
| Retention Rate     | 73.46% |

These figures establish the baseline for examining churn across different customer segments.

Segment-level findings should be taken from the completed analysis and validated against the underlying data.

## Example DAX Measure

The churn-rate measure calculates the proportion of customers who have churned within the current filter context.

```dax
Churn Rate =
DIVIDE(
    [Churned Customers],
    [Total Customers],
    0
)
```

## Business Recommendations

The analysis supports further investigation into:

1. **Contract retention:** Evaluate customer groups with elevated churn and test appropriate retention offers.
2. **Early customer engagement:** Investigate onboarding and support improvements for tenure groups with higher churn.
3. **Service experience:** Examine support and service patterns associated with customer churn.
4. **Billing experience:** Investigate payment friction and billing concerns in relevant customer segments.
5. **Performance monitoring:** Track churn and retention KPIs to evaluate the effectiveness of retention initiatives.

These are recommendations for investigation and testing. Observed relationships do not independently establish causation.

## Repository Structure

```text
Customer_Churn_Analysis/
│
├── data/
│   ├── raw/
│   │   └── Telco-Customer-Churn.csv
│   └── cleaned/
│       └── telco_churn_cleaned.csv
│
├── notebooks/
│   └── customer_churn_analysis.ipynb
│
├── scripts/
│   └── clean_customer_churn.py
│
├── sql/
│   ├── 01_create_table.sql
│   ├── 02_data_validation.sql
│   ├── 03_churn_analysis.sql
│   ├── 04_customer_segmentation.sql
│   └── 05_retention_insights.sql
│
├── reports/
│   ├── Business_Insights.md
│   └── Project_Summary.md
│
├── visualizations/
│
├── powerbi/
│   └── Customer_Churn_Dashboard.pbix
│
└── README.md
```

*Update the structure if your actual folder or file names differ.*

## How to Explore the Project

1. Review the cleaned dataset and Python notebook.
2. Explore the SQL scripts to understand the analytical queries.
3. Open the Power BI dashboard to examine churn patterns interactively.
4. Read `reports/Business_Insights.md` for business recommendations.
5. Read `reports/Project_Summary.md` for the project methodology and deliverables.

## Skills Demonstrated

* Data cleaning and data validation
* Exploratory data analysis
* Python and Pandas
* SQL querying and aggregation
* Customer segmentation
* Power BI dashboard development
* DAX measures and KPI reporting
* Business insight generation
* Analytical documentation

## Conclusion

This project demonstrates how Python, SQL Server, and Power BI can be combined to analyze customer churn and communicate findings through interactive dashboards.

It provides a foundation for investigating customer retention opportunities and demonstrates practical data analytics skills relevant to entry-level Data Analyst roles.
