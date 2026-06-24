"""
01_data_loading.py
Step 1: Load the dataset and perform initial inspection.
Run: python 01_data_loading.py
"""

import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import CSV_PATH, XLSX_PATH

def load_data(path=CSV_PATH):
    print("=" * 60)
    print("  STEP 1: DATA LOADING")
    print("=" * 60)

    df = pd.read_csv(path)

    print(f"\n✅ Dataset loaded from: {path}")
    print(f"\n📐 Shape: {df.shape[0]} rows × {df.shape[1]} columns")

    print("\n📋 First 5 rows:")
    print(df.head().to_string(index=False))

    print("\n📋 Column Names:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")

    print("\n📋 Data Types:")
    print(df.dtypes.to_string())

    print("\n📋 Basic Info:")
    df.info()

    print("\n📊 Statistical Summary:")
    print(df.describe().round(2).to_string())

    print("\n🏢 Unique Departments:")
    print(df["Department"].value_counts().to_string())

    print(f"\n👥 Unique Employees: {df['Employee_ID'].nunique()}")
    print(f"📅 Date Range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"🎯 Target Tasks: {df['Target_Tasks'].unique()} (all employees same target)")

    return df

if __name__ == "__main__":
    df = load_data()
    print("\n✅ Step 1 Complete.\n")
