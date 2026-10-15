

SELECT*FROM telco_churn_cleaned;

SELECT COUNT(*) AS Total_Customer
FROM telco_churn_cleaned;

SELECT COUNT(*) AS Churned_Customer
FROM telco_churn_cleaned
WHERE [Churn_Label]='yes';

SELECT COUNT(*) AS Active_Customer
FROM telco_churn_cleaned
WHERE [Churn_Label]='No';


SELECT
    COUNT(*) AS Total_Customers,

    SUM(CASE
            WHEN [Churn_Label] = 'Yes' THEN 1
            ELSE 0
        END) AS Churned_Customers,

    ROUND(
        100.0 * SUM(CASE
                        WHEN [Churn_Label] = 'Yes' THEN 1
                        ELSE 0
                    END) / COUNT(*),
        2
    ) AS Churn_Rate

FROM telco_churn_cleaned;

SELECT 
    Contract,
    COUNT(*) AS Total_Customers,

    SUM(CASE
            WHEN [Churn_Label] = 'Yes' THEN 1
            ELSE 0
        END) AS Churned_Customers,

    ROUND(
        100.0 * SUM(CASE
                        WHEN [Churn_Label] = 'Yes' THEN 1
                        ELSE 0
                    END) / COUNT(*),
        2
    ) AS Churn_Rate

FROM telco_churn_cleaned
GROUP BY Contract
ORDER BY Churn_Rate DESC;

SELECT 
    Internet_Service,
    COUNT(*) AS Total_Customers,

    SUM(CASE
            WHEN [Churn_Label] = 'Yes' THEN 1
            ELSE 0
        END) AS Churned_Customers,

    ROUND(
        100.0 * SUM(CASE
                        WHEN [Churn_Label] = 'Yes' THEN 1
                        ELSE 0
                    END) / COUNT(*),
        2
    ) AS Churn_Rate

FROM telco_churn_cleaned
GROUP BY Internet_Service
ORDER BY Churn_Rate DESC;


SELECT 
    Payment_Method,
    COUNT(*) AS Total_Customers,

    SUM(CASE
            WHEN [Churn_Label] = 'Yes' THEN 1
            ELSE 0
        END) AS Churned_Customers,

    ROUND(
        100.0 * SUM(CASE
                        WHEN [Churn_Label] = 'Yes' THEN 1
                        ELSE 0
                    END) / COUNT(*),
        2
    ) AS Churn_Rate

FROM telco_churn_cleaned
GROUP BY Payment_Method
ORDER BY Churn_Rate DESC;


SELECT
    Tenure_Group,

    COUNT(*) AS Total_Customers,

    SUM(
        CASE
            WHEN [Churn_Label] = 'Yes' THEN 1
            ELSE 0
        END
    ) AS Churned_Customers,

    ROUND(
        100.0 * SUM(
            CASE
                WHEN [Churn_Label] = 'Yes' THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS Churn_Rate

FROM telco_churn_cleaned

GROUP BY Tenure_Group

ORDER BY Churn_Rate DESC;


SELECT
        Monthly_Charges_Group,
       COUNT(*) AS Total_Customer,
       
              SUM ( CASE
                       WHEN [Churn_Label]='yes' THEN 1 
                       ELSE 0 
                    END) AS Churned_Customer,
       ROUND(
             100.00*SUM(CASE
                            WHEN [Churn_Label]='yes' THEN 1 
                            ELSE 0 
                        END
                       )/COUNT(*),
                     2
              ) AS Churn_Rate
      
FROM telco_churn_cleaned
GROUP BY Monthly_Charges_Group
ORDER BY Churn_Rate DESC;



