-- ============================================================
-- Q10: Who Are Consistent High Performers (Avg > 100%)?
-- Business Reason: Find reliable, always-above-target employees.
-- ============================================================
USE employee_productivity_db;

SELECT
    Employee_ID,
    Employee_Name,
    Department,
    ROUND(AVG((Tasks_Completed * 100.0) / Target_Tasks), 2) AS Avg_Productivity_Pct,
    ROUND(AVG(Quality_Score), 2)                             AS Avg_Quality_Pct,
    ROUND(AVG(Tasks_Completed * 1.0 / Hours_Worked), 2)     AS Avg_Efficiency,
    COUNT(*)                                                 AS Days_Recorded,
    COUNT(CASE WHEN (Tasks_Completed*100.0/Target_Tasks) >= 100
               THEN 1 END)                                   AS Days_Above_Target,
    ROUND(COUNT(CASE WHEN (Tasks_Completed*100.0/Target_Tasks) >= 100
                     THEN 1 END) * 100.0 / COUNT(*), 1)     AS Consistency_Pct
FROM Employee_Productivity
GROUP BY Employee_ID, Employee_Name, Department
HAVING AVG((Tasks_Completed * 100.0) / Target_Tasks) >= 100
ORDER BY Avg_Productivity_Pct DESC;
