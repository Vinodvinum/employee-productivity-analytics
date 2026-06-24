"""
06_employee_analysis.py
Step 6: Individual employee analysis — top, bottom, consistent performers.
Run: python 06_employee_analysis.py
"""

import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CSV_PATH, DATA_PROCESSED, OUTPUTS_REPORTS

def employee_analysis(df=None):
    print("=" * 60)
    print("  STEP 6: EMPLOYEE ANALYSIS")
    print("=" * 60)

    if df is None:
        p = os.path.join(DATA_PROCESSED, "data_with_kpis.csv")
        df = pd.read_csv(p if os.path.exists(p) else CSV_PATH)
        df["Date"] = pd.to_datetime(df["Date"])
        if "Productivity_Pct" not in df.columns:
            df["Productivity_Pct"] = (df["Tasks_Completed"] / df["Target_Tasks"] * 100).round(2)
        if "Efficiency" not in df.columns:
            df["Efficiency"] = (df["Tasks_Completed"] / df["Hours_Worked"]).round(2)

    # ── Employee Summary ──────────────────────────────────────
    emp = df.groupby(["Employee_ID","Employee_Name","Department"]).agg(
        Avg_Productivity = ("Productivity_Pct","mean"),
        Avg_Quality      = ("Quality_Score",   "mean"),
        Avg_Efficiency   = ("Efficiency",       "mean"),
        Avg_Hours        = ("Hours_Worked",     "mean"),
        Total_Tasks      = ("Tasks_Completed",  "sum"),
        Records          = ("Employee_ID",      "count"),
    ).round(2).reset_index()

    # ── Top 10 Performers ─────────────────────────────────────
    top10 = emp.sort_values("Avg_Productivity", ascending=False).head(10)
    print("\n🏆 TOP 10 EMPLOYEES (by Avg Productivity %):")
    print(top10[["Employee_Name","Department","Avg_Productivity","Avg_Quality","Avg_Efficiency"]].to_string(index=False))

    # ── Bottom 10 Performers ──────────────────────────────────
    bot10 = emp.sort_values("Avg_Productivity", ascending=True).head(10)
    print("\n⚠️  BOTTOM 10 EMPLOYEES (Needs Training):")
    print(bot10[["Employee_Name","Department","Avg_Productivity","Avg_Quality","Avg_Efficiency"]].to_string(index=False))

    # ── Top 10 by Quality ─────────────────────────────────────
    top10q = emp.sort_values("Avg_Quality", ascending=False).head(10)
    print("\n🏆 TOP 10 EMPLOYEES (by Quality %):")
    print(top10q[["Employee_Name","Department","Avg_Quality","Avg_Productivity"]].to_string(index=False))

    # ── Top 10 by Efficiency ──────────────────────────────────
    top10e = emp.sort_values("Avg_Efficiency", ascending=False).head(10)
    print("\n🏆 TOP 10 EMPLOYEES (by Efficiency - Tasks/Hour):")
    print(top10e[["Employee_Name","Department","Avg_Efficiency","Avg_Productivity"]].to_string(index=False))

    # ── Consistent High Performers (>100% avg) ────────────────
    consistent = emp[emp["Avg_Productivity"] >= 100].sort_values("Avg_Productivity", ascending=False)
    print(f"\n✅ CONSISTENT HIGH PERFORMERS (Avg >= 100%): {len(consistent)} employees")
    print(consistent[["Employee_Name","Department","Avg_Productivity"]].to_string(index=False))

    # ── Employees Needing Attention (<85%) ───────────────────
    attention = emp[emp["Avg_Productivity"] < 85].sort_values("Avg_Productivity")
    print(f"\n🚨 EMPLOYEES NEEDING COACHING (<85%): {len(attention)} employees")
    if len(attention) > 0:
        print(attention[["Employee_Name","Department","Avg_Productivity","Avg_Quality"]].to_string(index=False))

    # ── Save ──────────────────────────────────────────────────
    out = os.path.join(OUTPUTS_REPORTS, "03_employee_summary.csv")
    emp.sort_values("Avg_Productivity", ascending=False).to_csv(out, index=False)
    print(f"\n✅ Employee summary saved to: {out}")

    return df, emp

if __name__ == "__main__":
    employee_analysis()
    print("\n✅ Step 6 Complete.\n")
