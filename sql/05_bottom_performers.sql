-- ============================================================
-- Q5: Who are the Bottom 10 Employees (Needs Training)?
-- Business Reason: Find employees needing support or coaching.
-- ============================================================
USE employee_productivity_db;

SELECT
    Employee_ID,
    Employee_Name,
    Department,
    ROUND(AVG((Tasks_Completed * 100.0) / Target_Tasks), 2) AS Avg_Productivity_Pct,
    ROUND(AVG(Quality_Score), 2)                             AS Avg_Quality_Pct,
    ROUND(AVG(Tasks_Completed * 1.0 / Hours_Worked), 2)     AS Avg_Efficiency,
    SUM(Tasks_Completed)                                     AS Total_Tasks,
    100 - ROUND(AVG((Tasks_Completed * 100.0) / Target_Tasks), 2) AS Gap_To_Target
FROM Employee_Productivity
GROUP BY Employee_ID, Employee_Name, Department
ORDER BY Avg_Productivity_Pct ASC
LIMIT 10;
