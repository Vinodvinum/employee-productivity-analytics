-- ============================================================
-- 00_create_table.sql
-- Create the Employee_Productivity table in MySQL
-- Run this FIRST before any other SQL query
-- ============================================================

CREATE DATABASE IF NOT EXISTS employee_productivity_db;
USE employee_productivity_db;

DROP TABLE IF EXISTS Employee_Productivity;

CREATE TABLE Employee_Productivity (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    Employee_ID     VARCHAR(10)    NOT NULL,
    Employee_Name   VARCHAR(50)    NOT NULL,
    Department      VARCHAR(20)    NOT NULL,
    Date            DATE           NOT NULL,
    Tasks_Completed INT            NOT NULL,
    Target_Tasks    INT            NOT NULL DEFAULT 50,
    Quality_Score   DECIMAL(5,2)   NOT NULL,
    Hours_Worked    INT            NOT NULL,
    -- Computed columns (MySQL 5.7+)
    Productivity_Pct AS (ROUND((Tasks_Completed * 100.0) / Target_Tasks, 2)) STORED,
    Efficiency       AS (ROUND(Tasks_Completed / Hours_Worked, 2))            STORED
);

-- Load data from CSV (update path to your local file)
-- LOAD DATA INFILE '/path/to/employee_productivity_dataset.csv'
-- INTO TABLE Employee_Productivity
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS
-- (Employee_ID, Employee_Name, Department, Date,
--  Tasks_Completed, Target_Tasks, Quality_Score, Hours_Worked);

SELECT 'Table created successfully!' AS Status;
