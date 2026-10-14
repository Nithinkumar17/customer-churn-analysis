USE CustomerChurnDB;
GO

-- Customer Segmentation by Tenure and Contract

SELECT
    CASE
        WHEN tenure <= 12 THEN 'New Customers (0-12 Months)'
        WHEN tenure <= 24 THEN 'Growing Customers (13-24 Months)'
        WHEN tenure <= 48 THEN 'Established Customers (25-48 Months)'
        ELSE 'Loyal Customers (49+ Months)'
    END AS CustomerSegment,

    Contract,

    COUNT(*) AS TotalCustomers,

    SUM(
        CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END
    ) AS ChurnedCustomers,

    CAST(
        100.0 * SUM(
            CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END
        ) / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercentage

FROM dbo.CustomerChurn

GROUP BY
    CASE
        WHEN tenure <= 12 THEN 'New Customers (0-12 Months)'
        WHEN tenure <= 24 THEN 'Growing Customers (13-24 Months)'
        WHEN tenure <= 48 THEN 'Established Customers (25-48 Months)'
        ELSE 'Loyal Customers (49+ Months)'
    END,
    Contract

ORDER BY
    MIN(tenure),
    ChurnRatePercentage DESC;
GO


-- Customer Segmentation by Internet Service

SELECT
    InternetService,

    COUNT(*) AS TotalCustomers,

    SUM(
        CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END
    ) AS ChurnedCustomers,

    SUM(
        CASE
            WHEN Churn = 'No' THEN 1
            ELSE 0
        END
    ) AS RetainedCustomers,

    CAST(
        100.0 * SUM(
            CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END
        ) / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercentage

FROM dbo.CustomerChurn

GROUP BY InternetService

ORDER BY ChurnRatePercentage DESC;
GO

-- Customer Segmentation by Technical Support

SELECT
    TechSupport,

    COUNT(*) AS TotalCustomers,

    SUM(
        CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END
    ) AS ChurnedCustomers,

    CAST(
        100.0 * SUM(
            CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END
        ) / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercentage

FROM dbo.CustomerChurn

GROUP BY TechSupport

ORDER BY ChurnRatePercentage DESC;
GO


-- Customer Segmentation by Family Status

SELECT
    Partner,
    Dependents,

    COUNT(*) AS TotalCustomers,

    SUM(
        CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END
    ) AS ChurnedCustomers,

    CAST(
        100.0 * SUM(
            CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END
        ) / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercentage

FROM dbo.CustomerChurn

GROUP BY
    Partner,
    Dependents

ORDER BY ChurnRatePercentage DESC;
GO

-- Customer Segmentation by Senior Citizen Status

SELECT
    CASE
        WHEN SeniorCitizen = 1 THEN 'Senior Citizen'
        ELSE 'Non-Senior Citizen'
    END AS CustomerSegment,

    COUNT(*) AS TotalCustomers,

    SUM(
        CASE
            WHEN Churn = 'Yes' THEN 1
            ELSE 0
        END
    ) AS ChurnedCustomers,

    CAST(
        100.0 * SUM(
            CASE
                WHEN Churn = 'Yes' THEN 1
                ELSE 0
            END
        ) / NULLIF(COUNT(*), 0)
        AS DECIMAL(5,2)
    ) AS ChurnRatePercentage

FROM dbo.CustomerChurn

GROUP BY SeniorCitizen

ORDER BY ChurnRatePercentage DESC;
GO