# 📐 Data Model Documentation
## Employee Productivity Dashboard

---

## Table: Employee_Productivity (Main Fact Table)

| Column | Type | Description |
|--------|------|-------------|
| Employee_ID | Text | Unique identifier (E001–E050) |
| Employee_Name | Text | Employee display name |
| Department | Text | AI / Data / QA / Operations |
| Date | Date | Daily record date |
| Tasks_Completed | Integer | Daily tasks completed |
| Target_Tasks | Integer | Daily target (50) |
| Quality_Score | Decimal | Quality percentage |
| Hours_Worked | Integer | Hours worked that day |
| Productivity_Pct | Decimal | **CALCULATED** Tasks/Target×100 |
| Efficiency | Decimal | **CALCULATED** Tasks/Hours |
| Month_Name | Text | **CALCULATED** "Jan 2026" |
| Month_Num | Integer | **CALCULATED** 1,2,3 |
| Year | Integer | **CALCULATED** 2026 |
| Performance_Category | Text | **CALCULATED** Excellent/Good/Average/Below/Poor |
| Quality_Category | Text | **CALCULATED** High/Good/Average/Below/Poor |

---

## Date Table (Recommended to Add)

Create a Date Table in Power BI for proper time intelligence:

```dax
Date Table =
ADDCOLUMNS(
    CALENDAR(DATE(2026,1,1), DATE(2026,3,31)),
    "Year",       YEAR([Date]),
    "Month_Num",  MONTH([Date]),
    "Month_Name", FORMAT([Date], "MMM YYYY"),
    "Quarter",    "Q" & QUARTER([Date]),
    "Week_Num",   WEEKNUM([Date])
)
```

Then create relationship:
- **Employee_Productivity[Date]** → **Date Table[Date]** (Many to One)

---

## Key Relationships

```
Employee_Productivity  →  (No external dimension tables)
                          All analysis done within one table
```

For a more advanced model, you could create:
- **Dim_Employee** (Employee_ID, Employee_Name, Department)
- **Dim_Date** (Date table as above)
- **Fact_Productivity** (daily metrics only)

---

## Measures Table

Create a dedicated **Measures** table (blank table, no data) to organize all DAX measures cleanly:

```
📁 Measures/
   ├── 📊 KPI - Avg Productivity %
   ├── 📊 KPI - Avg Quality %
   ├── 📊 KPI - Avg Efficiency
   ├── 📊 KPI - Total Tasks Completed
   ├── 📊 KPI - Total Hours Worked
   ├── 📊 KPI - Total Employees
   ├── 🏆 Top Performer Name
   ├── 🏆 Top Performer %
   ├── ⚠️  Lowest Performer Name
   ├── ⚠️  Lowest Performer %
   ├── 📈 MoM Productivity Change
   ├── 📈 MoM Quality Change
   ├── 🎯 Target Hit Rate %
   └── 🎨 Productivity Color
```
