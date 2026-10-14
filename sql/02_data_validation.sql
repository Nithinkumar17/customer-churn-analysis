SELECT COUNT(*) AS TotalCustomers
FROM dbo.CustomerChurn;

SELECT TOP 10 *
FROM dbo.CustomerChurn;

SELECT
    customerID,
    COUNT(*) AS DuplicateCount
FROM dbo.CustomerChurn
GROUP BY customerID
HAVING COUNT(*) > 1;

SELECT
    Churn,
    COUNT(*) AS CustomerCount,
    CAST(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM dbo.CustomerChurn)
        AS DECIMAL(5,2)
    ) AS Percentage
FROM dbo.CustomerChurn
GROUP BY Churn
ORDER BY Churn;