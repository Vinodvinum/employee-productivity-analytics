"""
02_data_cleaning.py
Step 2: Check data quality, handle issues, convert types.
Run: python 02_data_cleaning.py
"""

import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CSV_PATH, DATA_PROCESSED

def clean_data(df=None):
    print("=" * 60)
    print("  STEP 2: DATA CLEANING & QUALITY CHECK")
    print("=" * 60)

    if df is None:
        df = pd.read_csv(CSV_PATH)

    # ── 1. Missing Values ──────────────────────────────────────
    print("\n🔍 Missing Values:")
    missing = df.isnull().sum()
    if missing.sum() == 0:
        print("  ✅ No missing values found — dataset is complete!")
    else:
        print(missing[missing > 0])
        df = df.dropna()
        print(f"  ⚠️  Rows after dropping nulls: {len(df)}")

    # ── 2. Duplicate Records ──────────────────────────────────
    print("\n🔍 Duplicate Records:")
    dupes = df.duplicated().sum()
    if dupes == 0:
        print("  ✅ No duplicate records found!")
    else:
        print(f"  ⚠️  Found {dupes} duplicates. Removing...")
        df = df.drop_duplicates()
        print(f"  ✅ Rows after removing duplicates: {len(df)}")

    # ── 3. Data Type Conversion ───────────────────────────────
    print("\n🔄 Converting Data Types:")
    df["Date"] = pd.to_datetime(df["Date"])
    print("  ✅ 'Date' column converted to datetime")

    df["Employee_ID"]   = df["Employee_ID"].astype(str)
    df["Employee_Name"] = df["Employee_Name"].astype(str)
    df["Department"]    = df["Department"].astype(str)
    print("  ✅ String columns confirmed")

    # ── 4. Add Time Columns ───────────────────────────────────
    df["Year"]  = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Month_Name"] = df["Date"].dt.strftime("%b %Y")
    print("  ✅ Year, Month, Month_Name columns added")

    # ── 5. Value Validation ───────────────────────────────────
    print("\n🔍 Value Range Checks:")
    print(f"  Tasks_Completed: min={df['Tasks_Completed'].min()}, max={df['Tasks_Completed'].max()}")
    print(f"  Quality_Score:   min={df['Quality_Score'].min()}, max={df['Quality_Score'].max()}")
    print(f"  Hours_Worked:    min={df['Hours_Worked'].min()}, max={df['Hours_Worked'].max()}")
    print(f"  Target_Tasks:    {df['Target_Tasks'].unique()} (fixed for all)")

    # ── 6. Save Cleaned File ──────────────────────────────────
    out_path = os.path.join(DATA_PROCESSED, "cleaned_data.csv")
    df.to_csv(out_path, index=False)
    print(f"\n✅ Cleaned dataset saved to: {out_path}")
    print(f"   Final shape: {df.shape}")

    return df

if __name__ == "__main__":
    df_clean = clean_data()
    print("\n✅ Step 2 Complete.\n")
