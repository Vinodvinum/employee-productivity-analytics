# 📊 Employee Productivity & Quality Analysis Project

### Presenter: Vinod M | Data Analyst

This repository contains a complete data analysis project on employee productivity. It includes data cleaning and analysis using Python (Pandas), database queries using SQL, and a 5-page interactive dashboard guide for Power BI.

---

## 🗂️ Project Structure

> **Note:** The structure below is a complete representation. Some files like the Jupyter Notebook or specific output reports are part of the full project but may not be included in every context.

```
EmployeeProductivity_Project/
│
├── data/
│   ├── raw/                          ← Original dataset files
│   │   ├── employee_productivity_dataset.csv
│   │   └── employee_productivity_dataset.xlsx
│   └── processed/                    ← Cleaned output from Python scripts
│
├── sql/                              ← All SQL queries (10 business questions)
│   ├── 00_create_table.sql
│   ├── 01_total_employees.sql
│   ├── 02_dept_distribution.sql
│   ├── 03_avg_productivity.sql
│   ├── 04_top_performers.sql
│   ├── 05_bottom_performers.sql
│   ├── 06_dept_performance.sql
│   ├── 07_quality_analysis.sql
│   ├── 08_hours_vs_output.sql
│   ├── 09_monthly_trend.sql
│   ├── 10_consistent_performers.sql
│   └── all_queries_combined.sql
│
├── python/                           ← Complete Python analysis pipeline
│   ├── config.py                     ← Shared paths & settings
│   ├── 01_data_loading.py
│   ├── 02_data_cleaning.py
│   ├── 03_kpi_creation.py
│   ├── 04_eda_analysis.py
│   ├── 05_dept_analysis.py
│   ├── 06_employee_analysis.py
│   ├── 07_trend_analysis.py
│   ├── 08_correlation_outliers.py
│   ├── 09_generate_charts.py
│   └── run_all.py                    ← Run everything in one go
│
├── notebooks/
│   └── Employee_Productivity_Analysis.ipynb  ← Full Jupyter Notebook
│
├── powerbi/
│   ├── 01_setup_guide.md             ← Step-by-step Power BI build guide
│   ├── 02_dax_measures.dax           ← All DAX measures (copy-paste)
│   ├── 03_powerquery_m_code.m        ← Power Query M transformations
│   └── 04_data_model.md              ← Data model & relationships
│
├── outputs/
│   ├── charts/                       ← Auto-generated PNG charts
│   └── reports/                      ← CSV summary reports
│
├── requirements.txt                  ← Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 How to Use This Repository

### 1. Prerequisites

- Python 3.8+
- MySQL Server (or another SQL database)
- Power BI Desktop

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 2 — Run full Python analysis

```bash
cd python
python run_all.py
```

### Step 3 — Open SQL queries

Open any `.sql` file in MySQL Workbench, DBeaver, or VS Code SQL extension.

### Step 4 — Build Power BI Dashboard

Follow `powerbi/01_setup_guide.md` step by step.

---

## 📋 Dataset Overview

| Property    | Value                             |
| ----------- | --------------------------------- |
| File        | employee_productivity_dataset.csv |
| Rows        | 4,500                             |
| Columns     | 8                                 |
| Employees   | 50                                |
| Departments | AI, Data, QA, Operations          |
| Period      | Q1 2026 (Jan–Mar)                 |

### Columns

| Column          | Type    | Description                 |
| --------------- | ------- | --------------------------- |
| Employee_ID     | String  | Unique ID (E001–E050)       |
| Employee_Name   | String  | Employee display name       |
| Department      | String  | AI / Data / QA / Operations |
| Date            | Date    | Daily entry date            |
| Tasks_Completed | Integer | Actual tasks done           |
| Target_Tasks    | Integer | Daily target (50)           |
| Quality_Score   | Float   | Work quality %              |
| Hours_Worked    | Integer | Hours worked that day       |

---

## 📐 KPIs Created

| KPI            | Formula                                | Business Meaning   |
| -------------- | -------------------------------------- | ------------------ |
| Productivity % | (Tasks_Completed / Target_Tasks) × 100 | Target achievement |
| Quality %      | Quality_Score (already in data)        | Work accuracy      |
| Efficiency     | Tasks_Completed / Hours_Worked         | Tasks per hour     |

---

## 🔑 Key Results

| Metric           | Value                 | Target |
| ---------------- | --------------------- | ------ |
| Avg Productivity | 98.76%                | 100%   |
| Avg Quality      | 94.21%                | 95%    |
| Avg Efficiency   | 6.21 tasks/hr         | -      |
| Total Tasks      | 225,134               | -      |
| Best Dept        | AI (103.21%)          | -      |
| Worst Dept       | Operations (94.27%)   | -      |
| Top Employee     | Employee_07 (118.67%) | -      |
| Lowest Employee  | Employee_45 (72.31%)  | -      |

---

## 🛠️ Tools Used

| Tool     | Purpose                                       |
| -------- | --------------------------------------------- |
| SQL      | Extract, aggregate, answer business questions |
| Python   | Clean data, create KPIs, statistical analysis |
| Power BI | Interactive 5-page dashboard                  |
| Excel    | Initial validation                            |

---

_Project by Vinod M | Q1 2026 Employee Productivity Analysis_
