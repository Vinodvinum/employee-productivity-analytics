"""
config.py — Shared paths and settings for the project.
All Python scripts import from here.
"""

import os

# ── BASE PATHS ────────────────────────────────────────────────────
BASE_DIR        = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_RAW        = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED  = os.path.join(BASE_DIR, "data", "processed")
OUTPUTS_CHARTS  = os.path.join(BASE_DIR, "outputs", "charts")
OUTPUTS_REPORTS = os.path.join(BASE_DIR, "outputs", "reports")

CSV_PATH  = os.path.join(DATA_RAW, "employee_productivity_dataset.csv")
XLSX_PATH = os.path.join(DATA_RAW, "employee_productivity_dataset.xlsx")

# ── KPI TARGETS ───────────────────────────────────────────────────
TARGET_PRODUCTIVITY = 100.0   # %
TARGET_QUALITY      = 95.0    # %
TARGET_TASKS        = 50      # tasks/day

# ── DEPARTMENTS ───────────────────────────────────────────────────
DEPARTMENTS = ["AI", "Data", "QA", "Operations"]

# ── COLORS (for charts) ───────────────────────────────────────────
DEPT_COLORS = {
    "AI":         "#1565C0",
    "Data":       "#6D28D9",
    "QA":         "#0D9488",
    "Operations": "#EA580C",
}
CHART_PALETTE  = ["#1565C0", "#6D28D9", "#0D9488", "#EA580C"]
COLOR_GREEN    = "#16A34A"
COLOR_RED      = "#DC2626"
COLOR_GOLD     = "#F59E0B"
COLOR_NAVY     = "#0A1628"

# ── CHART SETTINGS ────────────────────────────────────────────────
FIGSIZE_WIDE   = (14, 6)
FIGSIZE_SQUARE = (10, 8)
FIGSIZE_TALL   = (10, 12)
DPI            = 150

print(f"[config] BASE_DIR: {BASE_DIR}")
print(f"[config] CSV_PATH: {CSV_PATH}")
