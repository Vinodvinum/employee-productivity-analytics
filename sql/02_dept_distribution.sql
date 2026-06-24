-- ============================================================
-- Q2: How many employees are in each department?
-- Business Reason: Understand workforce distribution.
-- ============================================================
USE employee_productivity_db;

SELECT
    Department,
    COUNT(DISTINCT Employee_ID)                    AS Employee_Count,
    COUNT(*)                                       AS Total_Records,
    ROUND(COUNT(DISTINCT Employee_ID) * 100.0 /
          (SELECT COUNT(DISTINCT Employee_ID)
           FROM Employee_Productivity), 1)          AS Pct_Of_Workforce
FROM Employee_Productivity
GROUP BY Department
ORDER BY Employee_Count DESC;
