-- ============================================================
-- Q9: Monthly Productivity Trend — Is it Improving?
-- Business Reason: Track performance changes over time.
-- ============================================================
USE employee_productivity_db;

SELECT
    YEAR(Date)  AS Year,
    MONTH(Date) AS Month_Num,
    DATE_FORMAT(Date, '%b %Y')                               AS Month_Name,
    COUNT(DISTINCT Employee_ID)                              AS Active_Employees,
    ROUND(AVG((Tasks_Completed * 100.0) / Target_Tasks), 2) AS Avg_Productivity_Pct,
    ROUND(AVG(Quality_Score), 2)                             AS Avg_Quality_Pct,
    ROUND(AVG(Tasks_Completed * 1.0 / Hours_Worked), 2)     AS Avg_Efficiency,
    SUM(Tasks_Completed)                                     AS Total_Tasks,
    SUM(Hours_Worked)                                        AS Total_Hours,
    100                                                      AS Target_Productivity,
    95                                                       AS Target_Quality
FROM Employee_Productivity
GROUP BY YEAR(Date), MONTH(Date), DATE_FORMAT(Date, '%b %Y')
ORDER BY YEAR(Date), MONTH(Date);
