-- ============================================================
-- Q1: How many total employees are there?
-- Business Reason: Management wants to know workforce size.
-- Expected Result: 50
-- ============================================================
USE employee_productivity_db;

SELECT
    COUNT(DISTINCT Employee_ID)   AS Total_Employees,
    COUNT(DISTINCT Department)    AS Total_Departments,
    COUNT(*)                      AS Total_Records,
    MIN(Date)                     AS Start_Date,
    MAX(Date)                     AS End_Date,
    DATEDIFF(MAX(Date), MIN(Date)) + 1 AS Total_Days
FROM Employee_Productivity;
