-- ============================================================
-- Q7: Which Department Has Highest Quality?
-- Business Reason: Quality is as important as productivity.
-- ============================================================
USE employee_productivity_db;

SELECT
    Department,
    ROUND(AVG(Quality_Score), 2)           AS Avg_Quality_Pct,
    ROUND(MAX(Quality_Score), 2)           AS Max_Quality,
    ROUND(MIN(Quality_Score), 2)           AS Min_Quality,
    COUNT(CASE WHEN Quality_Score >= 95 THEN 1 END) AS High_Quality_Records,
    COUNT(CASE WHEN Quality_Score <  90 THEN 1 END) AS Low_Quality_Records,
    95 AS Target_Quality,
    ROUND(AVG(Quality_Score) - 95, 2)     AS Vs_Target
FROM Employee_Productivity
GROUP BY Department
ORDER BY Avg_Quality_Pct DESC;
