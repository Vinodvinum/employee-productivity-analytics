"""
04_eda_analysis.py
Step 4: Exploratory Data Analysis — distributions, company-level stats.
Run: python 04_eda_analysis.py
"""

import pandas as pd
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CSV_PATH, DATA_PROCESSED, OUTPUTS_REPORTS

def eda_analysis(df=None):
    print("=" * 60)
    print("  STEP 4: EXPLORATORY DATA ANALYSIS (EDA)")
    print("=" * 60)

    if df is None:
        p = os.path.join(DATA_PROCESSED, "data_with_kpis.csv")
        df = pd.read_csv(p) if os.path.exists(p) else pd.read_csv(CSV_PATH)
        df["Date"] = pd.to_datetime(df["Date"])
        if "Productivity_Pct" not in df.columns:
            df["Productivity_Pct"] = (df["Tasks_Completed"] / df["Target_Tasks"] * 100).round(2)
        if "Efficiency" not in df.columns:
            df["Efficiency"] = (df["Tasks_Completed"] / df["Hours_Worked"]).round(2)

    # ── Company-Level KPIs ────────────────────────────────────
    print("\n📊 COMPANY-LEVEL KPIs:")
    print(f"  Avg Productivity : {df['Productivity_Pct'].mean():.2f}%")
    print(f"  Avg Quality      : {df['Quality_Score'].mean():.2f}%")
    print(f"  Avg Efficiency   : {df['Efficiency'].mean():.2f} tasks/hr")
    print(f"  Total Employees  : {df['Employee_ID'].nunique()}")
    print(f"  Total Records    : {len(df):,}")
    print(f"  Total Tasks Done : {df['Tasks_Completed'].sum():,}")
    print(f"  Total Hours      : {df['Hours_Worked'].sum():,}")

    # ── Distribution Analysis ─────────────────────────────────
    print("\n📊 PRODUCTIVITY DISTRIBUTION:")
    bins = [0, 70, 80, 90, 100, 110, 120, 999]
    labels = ["<70%", "70-80%", "80-90%", "90-100%", "100-110%", "110-120%", ">120%"]
    df["Prod_Range"] = pd.cut(df["Productivity_Pct"], bins=bins, labels=labels)
    print(df["Prod_Range"].value_counts().sort_index().to_string())

    print("\n📊 QUALITY DISTRIBUTION:")
    qbins   = [0, 80, 85, 90, 95, 101]
    qlabels = ["<80% (Poor)", "80-85%", "85-90%", "90-95%", ">=95% (High)"]
    df["Qual_Range"] = pd.cut(df["Quality_Score"], bins=qbins, labels=qlabels)
    print(df["Qual_Range"].value_counts().sort_index().to_string())

    print("\n📊 HOURS WORKED DISTRIBUTION:")
    print(df["Hours_Worked"].value_counts().sort_index().to_string())

    # ── Percentile Analysis ───────────────────────────────────
    print("\n📊 PRODUCTIVITY PERCENTILES:")
    percs = [10, 25, 50, 75, 90, 95]
    for p in percs:
        val = np.percentile(df["Productivity_Pct"], p)
        print(f"  {p:3d}th percentile : {val:.2f}%")

    # ── High/Low Quality Records ──────────────────────────────
    high_q = (df["Quality_Score"] >= 95).sum()
    low_q  = (df["Quality_Score"] <  90).sum()
    print(f"\n📊 QUALITY RECORDS:")
    print(f"  High Quality (>=95%) : {high_q:,} records ({high_q/len(df)*100:.1f}%)")
    print(f"  Low  Quality (<90%)  : {low_q:,}  records ({low_q/len(df)*100:.1f}%)")
    print(f"  Max Quality Achieved : {df['Quality_Score'].max():.1f}%")
    print(f"  Min Quality Achieved : {df['Quality_Score'].min():.1f}%")

    # ── Save Summary Report ───────────────────────────────────
    summary = {
        "Metric": ["Avg Productivity %", "Avg Quality %", "Avg Efficiency",
                   "Total Employees", "Total Records", "Total Tasks", "Total Hours",
                   "High Quality Records", "Low Quality Records"],
        "Value": [
            f"{df['Productivity_Pct'].mean():.2f}%",
            f"{df['Quality_Score'].mean():.2f}%",
            f"{df['Efficiency'].mean():.2f}",
            df["Employee_ID"].nunique(),
            len(df),
            df["Tasks_Completed"].sum(),
            df["Hours_Worked"].sum(),
            high_q,
            low_q,
        ]
    }
    out = os.path.join(OUTPUTS_REPORTS, "01_company_summary.csv")
    pd.DataFrame(summary).to_csv(out, index=False)
    print(f"\n✅ Summary report saved to: {out}")

    return df

if __name__ == "__main__":
    eda_analysis()
    print("\n✅ Step 4 Complete.\n")
