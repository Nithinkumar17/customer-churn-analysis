USE CustomerChurnDB;
GO


/*Overall Customer Churn*/

SELECT
    COUNT(*) AS TotalCustomers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS ChurnedCustomers,

    SUM(CASE
        WHEN Churn = 'No' THEN 1
        ELSE 0
    END) AS RetainedCustomers,

    CAST(
        100.0 * SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercentage

FROM dbo.CustomerChurn;
GO

/*Analyzing Churn by Contract Type*/
SELECT
    Contract,

    COUNT(*) AS TotalCustomers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS ChurnedCustomers,

    CAST(
        100.0 * SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercentage

FROM dbo.CustomerChurn

GROUP BY Contract

ORDER BY ChurnRatePercentage DESC;
GO

/* Analyzing Churn by Tenure */
SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END AS TenureGroup,

    COUNT(*) AS TotalCustomers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS ChurnedCustomers,

    CAST(
        100.0 * SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercentage

FROM dbo.CustomerChurn

GROUP BY
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END

ORDER BY MIN(tenure);
GO

/* Analyzing Churn by Monthly Charges */

SELECT
    CASE
        WHEN MonthlyCharges < 35 THEN 'Low Charges'
        WHEN MonthlyCharges < 70 THEN 'Medium Charges'
        ELSE 'High Charges'
    END AS MonthlyChargeGroup,

    COUNT(*) AS TotalCustomers,

    SUM(CASE
        WHEN Churn = 'Yes' THEN 1
        ELSE 0
    END) AS ChurnedCustomers,

    CAST(
        100.0 * SUM(CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END) / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercentage

FROM dbo.CustomerChurn

GROUP BY
    CASE
        WHEN MonthlyCharges < 35 THEN 'Low Charges'
        WHEN MonthlyCharges < 70 THEN 'Medium Charges'
        ELSE 'High Charges'
    END

ORDER BY MIN(MonthlyCharges);
GO