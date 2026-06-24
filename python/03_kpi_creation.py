"""
03_kpi_creation.py
Step 3: Create KPI columns — Productivity %, Efficiency, Performance Category.
Run: python 03_kpi_creation.py
"""

import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CSV_PATH, DATA_PROCESSED, TARGET_PRODUCTIVITY, TARGET_QUALITY

def create_kpis(df=None):
    print("=" * 60)
    print("  STEP 3: KPI CREATION")
    print("=" * 60)

    if df is None:
        df = pd.read_csv(CSV_PATH)
        df["Date"] = pd.to_datetime(df["Date"])

    # ── KPI 1: Productivity % ─────────────────────────────────
    df["Productivity_Pct"] = (
        df["Tasks_Completed"] / df["Target_Tasks"] * 100
    ).round(2)
    print("\n✅ KPI 1 — Productivity %")
    print(f"   Formula : Tasks_Completed / Target_Tasks × 100")
    print(f"   Mean    : {df['Productivity_Pct'].mean():.2f}%")
    print(f"   Min     : {df['Productivity_Pct'].min():.2f}%")
    print(f"   Max     : {df['Productivity_Pct'].max():.2f}%")

    # ── KPI 2: Efficiency (Tasks per Hour) ────────────────────
    df["Efficiency"] = (
        df["Tasks_Completed"] / df["Hours_Worked"]
    ).round(2)
    print("\n✅ KPI 2 — Efficiency (Tasks / Hour)")
    print(f"   Formula : Tasks_Completed / Hours_Worked")
    print(f"   Mean    : {df['Efficiency'].mean():.2f}")
    print(f"   Min     : {df['Efficiency'].min():.2f}")
    print(f"   Max     : {df['Efficiency'].max():.2f}")

    # ── KPI 3: Performance Category ───────────────────────────
    def categorize(p):
        if p >= 110:  return "Excellent"
        elif p >= 100: return "Good"
        elif p >= 90:  return "Average"
        elif p >= 80:  return "Below Average"
        else:          return "Poor"

    df["Performance_Category"] = df["Productivity_Pct"].apply(categorize)
    print("\n✅ KPI 3 — Performance Category")
    print(df["Performance_Category"].value_counts().to_string())

    # ── KPI 4: Quality Category ───────────────────────────────
    def quality_cat(q):
        if q >= 95:   return "High Quality"
        elif q >= 90: return "Good Quality"
        elif q >= 85: return "Average Quality"
        elif q >= 80: return "Below Average"
        else:         return "Poor Quality"

    df["Quality_Category"] = df["Quality_Score"].apply(quality_cat)
    print("\n✅ KPI 4 — Quality Category")
    print(df["Quality_Category"].value_counts().to_string())

    # ── KPI 5: Target Achievement Flag ───────────────────────
    df["Hit_Target"] = df["Productivity_Pct"] >= TARGET_PRODUCTIVITY
    pct_hit = df["Hit_Target"].mean() * 100
    print(f"\n✅ KPI 5 — Target Hit Rate: {pct_hit:.1f}% of daily records hit 100% target")

    # ── Summary ───────────────────────────────────────────────
    print("\n📊 KPI Summary:")
    print(f"   Avg Productivity : {df['Productivity_Pct'].mean():.2f}%  (Target: {TARGET_PRODUCTIVITY}%)")
    print(f"   Avg Quality      : {df['Quality_Score'].mean():.2f}%    (Target: {TARGET_QUALITY}%)")
    print(f"   Avg Efficiency   : {df['Efficiency'].mean():.2f} tasks/hr")
    print(f"   Total Tasks Done : {df['Tasks_Completed'].sum():,}")
    print(f"   Total Hours      : {df['Hours_Worked'].sum():,}")

    # ── Save ──────────────────────────────────────────────────
    out = os.path.join(DATA_PROCESSED, "data_with_kpis.csv")
    df.to_csv(out, index=False)
    print(f"\n✅ Dataset with KPIs saved to: {out}")

    return df

if __name__ == "__main__":
    df = create_kpis()
    print("\n✅ Step 3 Complete.\n")
