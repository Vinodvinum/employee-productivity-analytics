-- ============================================================
-- Q8: Does Working More Hours Increase Productivity?
-- Business Reason: Understand effort vs output relationship.
-- ============================================================
USE employee_productivity_db;

SELECT
    Hours_Worked,
    COUNT(*)                                                  AS Records,
    ROUND(AVG(Tasks_Completed), 2)                           AS Avg_Tasks_Completed,
    ROUND(AVG((Tasks_Completed * 100.0) / Target_Tasks), 2) AS Avg_Productivity_Pct,
    ROUND(AVG(Tasks_Completed * 1.0 / Hours_Worked), 2)     AS Avg_Efficiency,
    ROUND(AVG(Quality_Score), 2)                             AS Avg_Quality
FROM Employee_Productivity
GROUP BY Hours_Worked
ORDER BY Hours_Worked;
