"""
run_all.py — Run the COMPLETE analysis pipeline in one command.
Usage (from python/ folder): python run_all.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("\n" + "="*60)
print("  EMPLOYEE PRODUCTIVITY — FULL ANALYSIS PIPELINE")
print("  Presented by: Vinod M | Data Analyst")
print("="*60)

import importlib, types

steps = [
    ("01_data_loading",      "load_data",          []),
    ("02_data_cleaning",     "clean_data",         ["df"]),
    ("03_kpi_creation",      "create_kpis",        ["df"]),
    ("04_eda_analysis",      "eda_analysis",       ["df"]),
    ("05_dept_analysis",     "dept_analysis",      ["df"]),
    ("06_employee_analysis", "employee_analysis",  ["df"]),
    ("07_trend_analysis",    "trend_analysis",     ["df"]),
    ("08_correlation_outliers","correlation_outliers",["df"]),
    ("09_generate_charts",   "generate_all_charts",[]),
]

results = {}
df = None

for module_name, func_name, arg_keys in steps:
    print(f"\n▶  Running {module_name}.py ...")
    spec   = importlib.util.spec_from_file_location(
        module_name,
        os.path.join(os.path.dirname(__file__), f"{module_name}.py")
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fn   = getattr(mod, func_name)
    args = [results.get(k, df) for k in arg_keys] if arg_keys else []
    out  = fn(*args) if args else fn()
    # If function returns a tuple, first element is df
    if isinstance(out, tuple):
        df = out[0]
        for i, k in enumerate(["df","extra1","extra2"]):
            if i < len(out): results[k] = out[i]
    elif out is not None:
        df = out
        results["df"] = df

print("\n" + "="*60)
print("  ✅ ALL STEPS COMPLETE!")
print("  📊 Charts  → outputs/charts/   (11 PNG files)")
print("  📋 Reports → outputs/reports/  (5 CSV files)")
print("  📁 Data    → data/processed/   (cleaned CSVs)")
print("="*60 + "\n")
