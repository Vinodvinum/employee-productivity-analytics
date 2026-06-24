-- ============================================================
-- all_queries_combined.sql
-- All 10 business questions in one file.
-- Vinod M | Employee Productivity Analysis | Q1 2026
-- ============================================================
USE employee_productivity_db;

-- ── Q1: Total Employees ──────────────────────────────────────
SELECT 'Q1: Total Employees' AS Query;
SELECT COUNT(DISTINCT Employee_ID) AS Total_Employees FROM Employee_Productivity;

-- ── Q2: Department Distribution ──────────────────────────────
SELECT 'Q2: Department Distribution' AS Query;
SELECT Department, COUNT(DISTINCT Employee_ID) AS Employees
FROM Employee_Productivity GROUP BY Department ORDER BY Employees DESC;

-- ── Q3: Average Productivity ──────────────────────────────────
SELECT 'Q3: Average Productivity' AS Query;
SELECT ROUND(AVG((Tasks_Completed*100.0)/Target_Tasks),2) AS Avg_Productivity_Pct,
       ROUND(AVG(Quality_Score),2) AS Avg_Quality_Pct,
       ROUND(AVG(Tasks_Completed*1.0/Hours_Worked),2) AS Avg_Efficiency
FROM Employee_Productivity;

-- ── Q4: Top 10 Performers ─────────────────────────────────────
SELECT 'Q4: Top 10 Performers' AS Query;
SELECT Employee_Name, Department,
       ROUND(AVG((Tasks_Completed*100.0)/Target_Tasks),2) AS Avg_Productivity_Pct
FROM Employee_Productivity
GROUP BY Employee_ID, Employee_Name, Department
ORDER BY Avg_Productivity_Pct DESC LIMIT 10;

-- ── Q5: Bottom 10 Performers ──────────────────────────────────
SELECT 'Q5: Bottom 10 Performers' AS Query;
SELECT Employee_Name, Department,
       ROUND(AVG((Tasks_Completed*100.0)/Target_Tasks),2) AS Avg_Productivity_Pct
FROM Employee_Productivity
GROUP BY Employee_ID, Employee_Name, Department
ORDER BY Avg_Productivity_Pct ASC LIMIT 10;

-- ── Q6: Best Department ───────────────────────────────────────
SELECT 'Q6: Department Performance Ranking' AS Query;
SELECT Department,
       ROUND(AVG((Tasks_Completed*100.0)/Target_Tasks),2) AS Avg_Productivity_Pct,
       ROUND(AVG(Quality_Score),2) AS Avg_Quality_Pct,
       ROUND(AVG(Tasks_Completed*1.0/Hours_Worked),2) AS Avg_Efficiency
FROM Employee_Productivity
GROUP BY Department ORDER BY Avg_Productivity_Pct DESC;

-- ── Q7: Quality by Department ─────────────────────────────────
SELECT 'Q7: Quality Analysis by Department' AS Query;
SELECT Department, ROUND(AVG(Quality_Score),2) AS Avg_Quality_Pct
FROM Employee_Productivity
GROUP BY Department ORDER BY Avg_Quality_Pct DESC;

-- ── Q8: Hours vs Output ───────────────────────────────────────
SELECT 'Q8: Hours Worked vs Tasks Completed' AS Query;
SELECT Hours_Worked, ROUND(AVG(Tasks_Completed),2) AS Avg_Tasks,
       ROUND(AVG(Tasks_Completed*1.0/Hours_Worked),2) AS Efficiency
FROM Employee_Productivity
GROUP BY Hours_Worked ORDER BY Hours_Worked;

-- ── Q9: Monthly Trend ─────────────────────────────────────────
SELECT 'Q9: Monthly Productivity Trend' AS Query;
SELECT DATE_FORMAT(Date,'%b %Y') AS Month,
       ROUND(AVG((Tasks_Completed*100.0)/Target_Tasks),2) AS Avg_Productivity_Pct,
       ROUND(AVG(Quality_Score),2) AS Avg_Quality_Pct
FROM Employee_Productivity
GROUP BY YEAR(Date), MONTH(Date), DATE_FORMAT(Date,'%b %Y')
ORDER BY YEAR(Date), MONTH(Date);

-- ── Q10: Consistent High Performers ──────────────────────────
SELECT 'Q10: Consistent High Performers (>100%)' AS Query;
SELECT Employee_Name, Department,
       ROUND(AVG((Tasks_Completed*100.0)/Target_Tasks),2) AS Avg_Productivity_Pct
FROM Employee_Productivity
GROUP BY Employee_ID, Employee_Name, Department
HAVING AVG((Tasks_Completed*100.0)/Target_Tasks) > 100
ORDER BY Avg_Productivity_Pct DESC;
