"""
05_dept_analysis.py
Step 5: Department-level analysis across all KPIs.
Run: python 05_dept_analysis.py
"""

import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CSV_PATH, DATA_PROCESSED, OUTPUTS_REPORTS

def dept_analysis(df=None):
    print("=" * 60)
    print("  STEP 5: DEPARTMENT ANALYSIS")
    print("=" * 60)

    if df is None:
        p = os.path.join(DATA_PROCESSED, "data_with_kpis.csv")
        df = pd.read_csv(p if os.path.exists(p) else CSV_PATH)
        df["Date"] = pd.to_datetime(df["Date"])
        if "Productivity_Pct" not in df.columns:
            df["Productivity_Pct"] = (df["Tasks_Completed"] / df["Target_Tasks"] * 100).round(2)
        if "Efficiency" not in df.columns:
            df["Efficiency"] = (df["Tasks_Completed"] / df["Hours_Worked"]).round(2)

    # ── Department Performance Summary ────────────────────────
    dept_summary = df.groupby("Department").agg(
        Employees       = ("Employee_ID",     "nunique"),
        Records         = ("Employee_ID",     "count"),
        Avg_Productivity= ("Productivity_Pct","mean"),
        Avg_Quality     = ("Quality_Score",   "mean"),
        Avg_Efficiency  = ("Efficiency",      "mean"),
        Avg_Hours       = ("Hours_Worked",    "mean"),
        Total_Tasks     = ("Tasks_Completed", "sum"),
        Total_Hours     = ("Hours_Worked",    "sum"),
    ).round(2).reset_index()

    dept_summary = dept_summary.sort_values("Avg_Productivity", ascending=False)

    print("\n📊 DEPARTMENT PERFORMANCE SUMMARY:")
    print(dept_summary.to_string(index=False))

    # ── Productivity Ranking ──────────────────────────────────
    print("\n🏆 PRODUCTIVITY RANKING:")
    for i, row in dept_summary.iterrows():
        flag = "🥇" if row["Avg_Productivity"] >= 100 else "⚠️"
        print(f"  {flag} {row['Department']:12} → {row['Avg_Productivity']:.2f}%")

    # ── Quality Ranking ───────────────────────────────────────
    print("\n🏆 QUALITY RANKING:")
    q_rank = dept_summary.sort_values("Avg_Quality", ascending=False)
    for _, row in q_rank.iterrows():
        flag = "✅" if row["Avg_Quality"] >= 95 else "❌"
        print(f"  {flag} {row['Department']:12} → {row['Avg_Quality']:.2f}%")

    # ── Efficiency Ranking ────────────────────────────────────
    print("\n🏆 EFFICIENCY RANKING (Tasks/Hour):")
    e_rank = dept_summary.sort_values("Avg_Efficiency", ascending=False)
    for _, row in e_rank.iterrows():
        print(f"  🔹 {row['Department']:12} → {row['Avg_Efficiency']:.2f} tasks/hr")

    # ── Monthly Dept Trend ────────────────────────────────────
    df["Month_Name"] = df["Date"].dt.strftime("%b %Y")
    monthly_dept = df.groupby(["Department","Month_Name"])["Productivity_Pct"].mean().round(2).unstack()
    print("\n📊 DEPT PRODUCTIVITY HEATMAP (Monthly):")
    print(monthly_dept.to_string())

    # ── Save ──────────────────────────────────────────────────
    out = os.path.join(OUTPUTS_REPORTS, "02_dept_summary.csv")
    dept_summary.to_csv(out, index=False)
    print(f"\n✅ Department summary saved to: {out}")

    return df, dept_summary

if __name__ == "__main__":
    dept_analysis()
    print("\n✅ Step 5 Complete.\n")
