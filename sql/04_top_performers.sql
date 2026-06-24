-- ============================================================
-- Q4: Who are the Top 10 Employees by Productivity?
-- Business Reason: Identify star performers for recognition.
-- ============================================================
USE employee_productivity_db;

SELECT
    Employee_ID,
    Employee_Name,
    Department,
    ROUND(AVG((Tasks_Completed * 100.0) / Target_Tasks), 2) AS Avg_Productivity_Pct,
    ROUND(AVG(Quality_Score), 2)                             AS Avg_Quality_Pct,
    ROUND(AVG(Tasks_Completed * 1.0 / Hours_Worked), 2)     AS Avg_Efficiency,
    SUM(Tasks_Completed)                                     AS Total_Tasks
FROM Employee_Productivity
GROUP BY Employee_ID, Employee_Name, Department
ORDER BY Avg_Productivity_Pct DESC
LIMIT 10;
