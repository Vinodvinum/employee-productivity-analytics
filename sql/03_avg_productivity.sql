-- ============================================================
-- Q3: What is the overall average productivity?
-- Business Reason: Measure company-level performance.
-- Expected: ~98.76%
-- ============================================================
USE employee_productivity_db;

SELECT
    ROUND(AVG((Tasks_Completed * 100.0) / Target_Tasks), 2) AS Avg_Productivity_Pct,
    ROUND(AVG(Quality_Score), 2)                             AS Avg_Quality_Pct,
    ROUND(AVG(Tasks_Completed * 1.0 / Hours_Worked), 2)     AS Avg_Efficiency,
    SUM(Tasks_Completed)                                     AS Total_Tasks_Completed,
    SUM(Hours_Worked)                                        AS Total_Hours_Worked,
    100 AS Target_Productivity_Pct,
    95  AS Target_Quality_Pct
FROM Employee_Productivity;
