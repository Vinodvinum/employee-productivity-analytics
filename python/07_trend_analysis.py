"""
07_trend_analysis.py
Step 7: Monthly trend analysis — Productivity, Quality, Efficiency over time.
Run: python 07_trend_analysis.py
"""

import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CSV_PATH, DATA_PROCESSED, OUTPUTS_REPORTS, TARGET_PRODUCTIVITY, TARGET_QUALITY

def trend_analysis(df=None):
    print("=" * 60)
    print("  STEP 7: TREND ANALYSIS")
    print("=" * 60)

    if df is None:
        p = os.path.join(DATA_PROCESSED, "data_with_kpis.csv")
        df = pd.read_csv(p if os.path.exists(p) else CSV_PATH)
        df["Date"] = pd.to_datetime(df["Date"])
        if "Productivity_Pct" not in df.columns:
            df["Productivity_Pct"] = (df["Tasks_Completed"] / df["Target_Tasks"] * 100).round(2)
        if "Efficiency" not in df.columns:
            df["Efficiency"] = (df["Tasks_Completed"] / df["Hours_Worked"]).round(2)

    df["Month"]      = df["Date"].dt.month
    df["Month_Name"] = df["Date"].dt.strftime("%b %Y")
    month_order      = ["Jan 2026", "Feb 2026", "Mar 2026"]

    # ── Monthly KPI Trend ─────────────────────────────────────
    monthly = df.groupby(["Month","Month_Name"]).agg(
        Avg_Productivity = ("Productivity_Pct","mean"),
        Avg_Quality      = ("Quality_Score",   "mean"),
        Avg_Efficiency   = ("Efficiency",       "mean"),
        Total_Tasks      = ("Tasks_Completed",  "sum"),
        Total_Hours      = ("Hours_Worked",     "sum"),
    ).round(2).reset_index().sort_values("Month")

    print("\n📊 MONTHLY KPI TREND:")
    print(monthly[["Month_Name","Avg_Productivity","Avg_Quality","Avg_Efficiency","Total_Tasks","Total_Hours"]].to_string(index=False))

    # ── Month-over-Month Change ───────────────────────────────
    print("\n📊 MONTH-OVER-MONTH CHANGE:")
    for i in range(1, len(monthly)):
        prev = monthly.iloc[i-1]
        curr = monthly.iloc[i]
        p_chg = curr["Avg_Productivity"] - prev["Avg_Productivity"]
        q_chg = curr["Avg_Quality"]      - prev["Avg_Quality"]
        e_chg = curr["Avg_Efficiency"]   - prev["Avg_Efficiency"]
        print(f"\n  {prev['Month_Name']} → {curr['Month_Name']}:")
        print(f"    Productivity : {p_chg:+.2f}%  {'⬆️' if p_chg>0 else '⬇️'}")
        print(f"    Quality      : {q_chg:+.2f}%  {'⬆️' if q_chg>0 else '⬇️'}")
        print(f"    Efficiency   : {e_chg:+.2f}    {'⬆️' if e_chg>0 else '⬇️'}")

    # ── Target Comparison ─────────────────────────────────────
    print(f"\n📊 VS TARGET ({TARGET_PRODUCTIVITY}% Productivity, {TARGET_QUALITY}% Quality):")
    for _, row in monthly.iterrows():
        p_vs = row["Avg_Productivity"] - TARGET_PRODUCTIVITY
        q_vs = row["Avg_Quality"]      - TARGET_QUALITY
        print(f"  {row['Month_Name']}: Prod={p_vs:+.2f}%  Quality={q_vs:+.2f}%")

    # ── Department Monthly Trend ──────────────────────────────
    dept_monthly = df.groupby(["Department","Month_Name"])["Productivity_Pct"].mean().round(2).unstack()
    print("\n📊 DEPARTMENT PRODUCTIVITY TREND (Monthly):")
    print(dept_monthly.to_string())

    # ── Best Month ────────────────────────────────────────────
    best = monthly.loc[monthly["Avg_Productivity"].idxmax()]
    print(f"\n🏆 Best Month: {best['Month_Name']} → {best['Avg_Productivity']:.2f}%")

    # ── Save ──────────────────────────────────────────────────
    out = os.path.join(OUTPUTS_REPORTS, "04_monthly_trend.csv")
    monthly.to_csv(out, index=False)
    print(f"\n✅ Monthly trend saved to: {out}")

    return df, monthly

if __name__ == "__main__":
    trend_analysis()
    print("\n✅ Step 7 Complete.\n")
