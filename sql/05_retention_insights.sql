USE CustomerChurnDB;
GO

-- 1. Identify customer groups with high churn rates

SELECT
    Contract,

    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END AS TenureGroup,

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
    Contract,
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END

ORDER BY
    ChurnRatePercentage DESC,
    TotalCustomers DESC;
GO

-- 2. Calculate monthly charges associated with churn

SELECT
    Churn,

    COUNT(*) AS TotalCustomers,

    CAST(
        SUM(MonthlyCharges)
        AS DECIMAL(12,2)
    ) AS TotalMonthlyCharges,

    CAST(
        AVG(MonthlyCharges)
        AS DECIMAL(10,2)
    ) AS AverageMonthlyCharge

FROM dbo.CustomerChurn

GROUP BY Churn

ORDER BY Churn;
GO

-- 3. Analyze churn by online security and technical support

SELECT
    OnlineSecurity,
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

GROUP BY
    OnlineSecurity,
    TechSupport

ORDER BY
    ChurnRatePercentage DESC,
    TotalCustomers DESC;
GO


-- 4. Analyze churn by payment method

SELECT
    PaymentMethod,

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

GROUP BY PaymentMethod

ORDER BY ChurnRatePercentage DESC;
GO


-- 5. Create a retention priority summary by contract

WITH ContractSummary AS
(
    SELECT
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

    GROUP BY Contract
)

SELECT
    Contract,
    TotalCustomers,
    ChurnedCustomers,
    ChurnRatePercentage,

    CASE
        WHEN ChurnRatePercentage >= 40
            THEN 'High Churn Rate'

        WHEN ChurnRatePercentage >= 20
            THEN 'Moderate Churn Rate'

        ELSE 'Lower Churn Rate'
    END AS ChurnCategory

FROM ContractSummary

ORDER BY
    ChurnRatePercentage DESC,
    ChurnedCustomers DESC;
GO