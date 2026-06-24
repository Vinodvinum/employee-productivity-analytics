"""
08_correlation_outliers.py
Step 8: Correlation analysis & outlier detection using IQR method.
Run: python 08_correlation_outliers.py
"""

import pandas as pd
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CSV_PATH, DATA_PROCESSED, OUTPUTS_REPORTS

def correlation_outliers(df=None):
    print("=" * 60)
    print("  STEP 8: CORRELATION & OUTLIER ANALYSIS")
    print("=" * 60)

    if df is None:
        p = os.path.join(DATA_PROCESSED, "data_with_kpis.csv")
        df = pd.read_csv(p if os.path.exists(p) else CSV_PATH)
        df["Date"] = pd.to_datetime(df["Date"])
        if "Productivity_Pct" not in df.columns:
            df["Productivity_Pct"] = (df["Tasks_Completed"] / df["Target_Tasks"] * 100).round(2)
        if "Efficiency" not in df.columns:
            df["Efficiency"] = (df["Tasks_Completed"] / df["Hours_Worked"]).round(2)

    numeric_cols = ["Tasks_Completed","Target_Tasks","Quality_Score",
                    "Hours_Worked","Productivity_Pct","Efficiency"]

    # ── Correlation Matrix ────────────────────────────────────
    print("\n📊 CORRELATION MATRIX:")
    corr = df[numeric_cols].corr().round(3)
    print(corr.to_string())

    # ── Key Correlation: Hours vs Tasks ───────────────────────
    r_hours_tasks = df["Hours_Worked"].corr(df["Tasks_Completed"])
    print(f"\n🔍 Hours Worked vs Tasks Completed:")
    print(f"   Correlation Coefficient : {r_hours_tasks:.3f}")
    if abs(r_hours_tasks) < 0.3:
        interp = "WEAK — working more hours does NOT significantly increase tasks"
    elif abs(r_hours_tasks) < 0.7:
        interp = "MODERATE — some relationship between hours and tasks"
    else:
        interp = "STRONG — hours worked strongly affects task completion"
    print(f"   Interpretation          : {interp}")

    # ── Hours vs Tasks by Group ───────────────────────────────
    print("\n📊 AVG TASKS BY HOURS WORKED:")
    hrs_tasks = df.groupby("Hours_Worked")["Tasks_Completed"].mean().round(2)
    for hrs, tasks in hrs_tasks.items():
        bar = "█" * int(tasks / 5)
        print(f"   {hrs} hrs : {tasks:.2f} tasks  {bar}")

    # ── Productivity vs Quality Correlation ───────────────────
    r_prod_qual = df["Productivity_Pct"].corr(df["Quality_Score"])
    print(f"\n🔍 Productivity vs Quality:")
    print(f"   Correlation : {r_prod_qual:.3f}")
    print(f"   Meaning     : {'Positive' if r_prod_qual > 0 else 'Negative'} relationship")

    # ── IQR Outlier Detection ─────────────────────────────────
    print("\n📊 OUTLIER DETECTION (IQR Method):")
    for col in ["Productivity_Pct", "Quality_Score", "Efficiency"]:
        Q1  = df[col].quantile(0.25)
        Q3  = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        out   = df[(df[col] < lower) | (df[col] > upper)]
        print(f"\n  {col}:")
        print(f"    Q1={Q1:.2f}  Q3={Q3:.2f}  IQR={IQR:.2f}")
        print(f"    Bounds : [{lower:.2f}, {upper:.2f}]")
        print(f"    Outliers: {len(out)} records ({len(out)/len(df)*100:.1f}%)")

    # ── High Efficiency, Low Quality Employees ────────────────
    print("\n🔍 HIGH PRODUCTIVITY BUT LOW QUALITY EMPLOYEES:")
    risk = df.groupby(["Employee_Name","Department"]).agg(
        Avg_Prod=("Productivity_Pct","mean"),
        Avg_Qual=("Quality_Score","mean")
    ).reset_index()
    risk_emp = risk[(risk["Avg_Prod"] >= 100) & (risk["Avg_Qual"] < 90)]
    if len(risk_emp):
        print(risk_emp.round(2).to_string(index=False))
    else:
        print("  ✅ No employees found with high productivity but low quality.")

    # ── Save correlation ──────────────────────────────────────
    out = os.path.join(OUTPUTS_REPORTS, "05_correlation.csv")
    corr.to_csv(out)
    print(f"\n✅ Correlation matrix saved to: {out}")

    return df

if __name__ == "__main__":
    correlation_outliers()
    print("\n✅ Step 8 Complete.\n")
