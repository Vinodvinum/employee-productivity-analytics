-- ============================================================
-- Q6: Which Department Performs Best?
-- Business Reason: Compare departments across all KPIs.
-- ============================================================
USE employee_productivity_db;

SELECT
    Department,
    COUNT(DISTINCT Employee_ID)                              AS Employees,
    ROUND(AVG((Tasks_Completed * 100.0) / Target_Tasks), 2) AS Avg_Productivity_Pct,
    ROUND(AVG(Quality_Score), 2)                             AS Avg_Quality_Pct,
    ROUND(AVG(Tasks_Completed * 1.0 / Hours_Worked), 2)     AS Avg_Efficiency,
    ROUND(AVG(Hours_Worked), 2)                              AS Avg_Hours_Worked,
    SUM(Tasks_Completed)                                     AS Total_Tasks,
    SUM(Hours_Worked)                                        AS Total_Hours,
    CASE
        WHEN AVG((Tasks_Completed * 100.0)/Target_Tasks) >= 100 THEN 'Above Target ✅'
        WHEN AVG((Tasks_Completed * 100.0)/Target_Tasks) >= 95  THEN 'Near Target ⚠️'
        ELSE 'Below Target ❌'
    END AS Status
FROM Employee_Productivity
GROUP BY Department
ORDER BY Avg_Productivity_Pct DESC;
