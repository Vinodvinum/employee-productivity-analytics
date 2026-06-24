# 📊 Power BI Dashboard — Complete Setup Guide
## Employee Productivity & Quality Analysis
### Vinod M | Data Analyst

---

> **How to use this guide:**
> Open Power BI Desktop → follow each step exactly.
> All DAX measures are in `02_dax_measures.dax` — copy-paste directly.
> Power Query code is in `03_powerquery_m_code.m`.

---

## STEP 1 — Load the Data

1. Open **Power BI Desktop**
2. Click **Home → Get Data → Text/CSV**
3. Select: `data/raw/employee_productivity_dataset.csv`
4. Click **Transform Data** (opens Power Query Editor)

---

## STEP 2 — Power Query Transformations

In Power Query Editor, apply these steps:

1. **Change Type:**
   - `Date` → Date
   - `Tasks_Completed`, `Target_Tasks`, `Hours_Worked` → Whole Number
   - `Quality_Score` → Decimal Number

2. **Add Column → Custom Column:**

   **Productivity_Pct:**
   ```
   = [Tasks_Completed] / [Target_Tasks] * 100
   ```

   **Efficiency:**
   ```
   = [Tasks_Completed] / [Hours_Worked]
   ```

   **Month_Name:**
   ```
   = Date.ToText([Date], "MMM yyyy")
   ```

   **Month_Num:**
   ```
   = Date.Month([Date])
   ```

3. Click **Close & Apply**

---

## STEP 3 — Create DAX Measures

In the **Data pane**, right-click the table → **New Measure**
Copy each measure from `02_dax_measures.dax`

### Key Measures to Create:
- `Avg Productivity %`
- `Avg Quality %`
- `Avg Efficiency`
- `Total Tasks Completed`
- `Total Hours Worked`
- `Total Employees`
- `High Quality Records`
- `Low Quality Records`

---

## STEP 4 — Create Report Pages

### PAGE 1 — Executive Overview

**Title:** "1. EXECUTIVE OVERVIEW — Company Performance At A Glance"

**Slicers (top-right):**
- Date Range slicer → Field: `Date`
- Department slicer → Field: `Department`
- Employee slicer → Field: `Employee_Name`

**KPI Cards (top row — 6 cards):**

| Card | Measure | Format |
|------|---------|--------|
| Total Employees | `Total Employees` | Number |
| Avg Productivity % | `Avg Productivity %` | % (2 decimals) |
| Avg Quality % | `Avg Quality %` | % (2 decimals) |
| Avg Efficiency | `Avg Efficiency` | Decimal (2) |
| Total Tasks Completed | `Total Tasks Completed` | Number |
| Total Hours Worked | `Total Hours Worked` | Number |

**Visuals (bottom 2 rows):**

1. **Clustered Bar Chart** — Productivity % by Department
   - X-axis: `Department`
   - Y-axis: `Avg Productivity %`
   - Colors: Blue (#1565C0)
   - Add constant line at 100% (red dashed)

2. **Clustered Bar Chart** — Quality % by Department
   - X-axis: `Department`
   - Y-axis: `Avg Quality %`
   - Colors: Purple (#7C3AED)
   - Add constant line at 95%

3. **Line Chart** — Monthly Productivity % Trend
   - X-axis: `Month_Name` (sort by Month_Num)
   - Y-axis: `Avg Productivity %`
   - Add constant line at 100%

4. **Bar Chart** — Total Tasks by Department
   - X-axis: `Total Tasks Completed`
   - Y-axis: `Department`

5. **Bar Chart** — Efficiency by Department
   - X-axis: `Avg Efficiency`
   - Y-axis: `Department`
   - Colors: Orange (#EA580C)

6. **Donut Chart** — Employee Count by Department
   - Values: `Total Employees`
   - Legend: `Department`

**Key Takeaway text box (bottom):**
> "Overall productivity is close to target. AI department is the top performer while Operations needs improvement."

---

### PAGE 2 — Employee Analysis

**Title:** "2. EMPLOYEE ANALYSIS — Individual Performance Overview"

**KPI Cards (top row — 6 cards):**
- Total Employees
- Top Performer name + % (use card with conditional formatting)
- Lowest Performer name + %
- Avg Productivity %
- Avg Quality %
- Avg Efficiency

**Visuals:**

1. **Bar Chart** — Top 10 Employees by Avg Productivity %
   - Y-axis: `Employee_Name` (Top N filter: 10, by Avg Productivity %)
   - X-axis: `Avg Productivity %`
   - Color: Blue

2. **Bar Chart** — Bottom 10 Employees
   - Same setup, but Bottom N filter
   - Color: Red (#DC2626)

3. **Column Chart** — Productivity Distribution (Histogram)
   - Use bins: <70, 70-80, 80-90, 90-100, 100-110, 110-120, >120
   - Color: Teal (#0D9488)

4. **Bar Chart** — Top 10 by Efficiency
   - Color: Green (#16A34A)

5. **Bar Chart** — Top 10 by Quality %
   - Color: Purple (#7C3AED)

6. **Table** — Employee Performance Summary
   - Columns: Employee_Name, Avg Productivity %, Avg Quality %, Avg Efficiency, Total Tasks
   - Sort by Avg Productivity % descending
   - Conditional formatting: Green for high, Red for low

---

### PAGE 3 — Department Analysis

**Title:** "3. DEPARTMENT ANALYSIS — Compare Department Performance Across Key Metrics"

**KPI Cards:** Avg Productivity %, Avg Quality %, Avg Efficiency, Total Tasks, Total Hours

**Visuals:**

1. **Clustered Column Chart** — Productivity % by Department (with 100% line)
2. **Clustered Column Chart** — Quality % by Department (with 95% line)
3. **Bar Chart** — Efficiency by Department
4. **Table** — Department Performance Summary
   - Columns: Department, Avg Productivity, Avg Quality, Avg Efficiency, Total Tasks, Total Hours
   - Color-code productivity: Green ≥100%, Red <95%

5. **Matrix/Table** — Productivity Heatmap (Department × Month)
   - Rows: Department | Columns: Month_Name | Values: Avg Productivity %
   - Conditional formatting: Red→Yellow→Green scale (88% to 110%)

6. **Donut Chart** — Total Tasks by Department

7. **Scatter Chart** — Quality vs Productivity by Department
   - X-axis: Avg Productivity % | Y-axis: Avg Quality %
   - Size: Total Tasks

8. **Line Chart** — Dept Productivity Trend (Monthly)
   - X-axis: Month | Y-axis: Avg Productivity % | Legend: Department

---

### PAGE 4 — Quality Analysis

**Title:** "4. QUALITY ANALYSIS — Monitor Quality Performance and Identify Improvement Areas"

**KPI Cards:**
- Average Quality % (vs 95% target)
- High Quality Records (≥95%)
- Low Quality Records (<90%)
- Total Quality Checks
- Max Quality %
- Min Quality %

**Visuals:**

1. **Bar Chart** — Avg Quality % by Department (with 95% target line)
2. **Line Chart** — Quality Trend Over Time (Monthly)
3. **Donut Chart** — Quality Distribution by category
   - Categories: ≥95% Excellent, 90-95% Good, 85-90% Average, 80-85% Below Avg, <80% Poor

4. **Scatter Chart** — Quality % vs Productivity %
   - X-axis: Productivity % | Y-axis: Quality %
   - Add quadrant lines at 100% and 95%

5. **Table** — Quality by Department × Month
   - With conditional formatting

6. **Table** — Quality Alerts (Employees/Departments Needing Attention)
   - Filter: Quality < 90 or Productivity < 85
   - Show: Employee, Issue, Quality %, vs Target, Recommendation

---

### PAGE 5 — Trend Analysis

**Title:** "5. TREND ANALYSIS — Performance Trends Over Time"

**KPI Cards:** Avg Productivity %, Avg Quality %, Avg Efficiency, Total Tasks, Total Hours, Total Employees

**Visuals:**

1. **Line Chart** — Monthly Productivity % Trend (with 100% target line)
2. **Line Chart** — Monthly Quality % Trend (with 95% target line)
3. **Line Chart** — Monthly Efficiency Trend
4. **Area Chart** — Total Tasks Completed Trend (Monthly)
5. **Line Chart** — Productivity % by Department (Monthly, 4 lines)

6. **Table** — Monthly Performance Summary
   - Columns: Month | Productivity Actual | vs Target | Quality Actual | vs Target | Efficiency | Total Tasks | vs Prev Month

---

## STEP 5 — Formatting Tips

### Color Theme:
| Element | Color |
|---------|-------|
| AI Dept | #1565C0 (Blue) |
| Data Dept | #7C3AED (Purple) |
| QA Dept | #0D9488 (Teal) |
| Operations | #EA580C (Orange) |
| Above Target | #16A34A (Green) |
| Below Target | #DC2626 (Red) |
| Target Lines | #DC2626 dashed |
| Background | White |
| Page Headers | Dark Navy #0A1628 |

### Canvas Settings:
- Canvas size: 1366 × 768 (16:9)
- Background: White
- Font: Segoe UI

### Navigation:
- Add 5 buttons (one per page) in a left sidebar
- Use icons: Home, Person, Building, Star, Trend
- Set action: Page Navigation to each respective page

---

## STEP 6 — Publish

1. Click **File → Publish → Publish to Power BI**
2. Sign in with your Microsoft account
3. Choose workspace
4. Access via: app.powerbi.com

---

*Setup guide for: Vinod M | Employee Productivity Dashboard | Q1 2026*
