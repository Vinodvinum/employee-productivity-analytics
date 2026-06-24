"""
09_generate_charts.py
Step 9: Generate all charts matching the Power BI dashboard — saved as PNG files.
Run: python 09_generate_charts.py
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import (CSV_PATH, DATA_PROCESSED, OUTPUTS_CHARTS,
                    DEPT_COLORS, CHART_PALETTE, COLOR_GREEN, COLOR_RED,
                    COLOR_GOLD, COLOR_NAVY, TARGET_PRODUCTIVITY, TARGET_QUALITY)

sns.set_theme(style="whitegrid", font_scale=1.1)
DEPTS = ["AI", "Data", "QA", "Operations"]

def load_df():
    p = os.path.join(DATA_PROCESSED, "data_with_kpis.csv")
    df = pd.read_csv(p if os.path.exists(p) else CSV_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    if "Productivity_Pct" not in df.columns:
        df["Productivity_Pct"] = (df["Tasks_Completed"] / df["Target_Tasks"] * 100).round(2)
    if "Efficiency" not in df.columns:
        df["Efficiency"] = (df["Tasks_Completed"] / df["Hours_Worked"]).round(2)
    df["Month_Name"] = df["Date"].dt.strftime("%b %Y")
    return df

def save(fig, name):
    path = os.path.join(OUTPUTS_CHARTS, name)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  ✅ Saved: {name}")

# ── CHART 1: Dept Productivity Bar Chart ──────────────────────────
def chart_dept_productivity(df):
    data = df.groupby("Department")["Productivity_Pct"].mean().reindex(DEPTS)
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(data.index, data.values, color=[DEPT_COLORS[d] for d in DEPTS], width=0.5, edgecolor="white")
    ax.axhline(TARGET_PRODUCTIVITY, color=COLOR_RED, ls="--", lw=1.5, label=f"Target {TARGET_PRODUCTIVITY}%")
    for bar in bars:
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
                f"{bar.get_height():.2f}%", ha="center", fontsize=10, fontweight="bold")
    ax.set_title("Productivity % by Department", fontsize=14, fontweight="bold", pad=12)
    ax.set_ylabel("Avg Productivity %"); ax.set_ylim(85, 110); ax.legend()
    save(fig, "01_dept_productivity.png")

# ── CHART 2: Dept Quality Bar Chart ───────────────────────────────
def chart_dept_quality(df):
    data = df.groupby("Department")["Quality_Score"].mean().reindex(DEPTS)
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(data.index, data.values, color="#7C3AED", width=0.5, edgecolor="white")
    ax.axhline(TARGET_QUALITY, color=COLOR_RED, ls="--", lw=1.5, label=f"Target {TARGET_QUALITY}%")
    for bar in bars:
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.2,
                f"{bar.get_height():.2f}%", ha="center", fontsize=10, fontweight="bold")
    ax.set_title("Quality % by Department", fontsize=14, fontweight="bold", pad=12)
    ax.set_ylabel("Avg Quality %"); ax.set_ylim(85, 105); ax.legend()
    save(fig, "02_dept_quality.png")

# ── CHART 3: Dept Efficiency Bar Chart ────────────────────────────
def chart_dept_efficiency(df):
    data = df.groupby("Department")["Efficiency"].mean().reindex(DEPTS)
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(data.index, data.values, color="#EA580C", edgecolor="white")
    for bar in bars:
        ax.text(bar.get_width()+0.05, bar.get_y()+bar.get_height()/2,
                f"{bar.get_width():.2f}", va="center", fontsize=10, fontweight="bold")
    ax.set_title("Avg Efficiency (Tasks/Hour) by Department", fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Tasks / Hour"); ax.set_xlim(0, 8.5)
    save(fig, "03_dept_efficiency.png")

# ── CHART 4: Monthly Productivity Trend ───────────────────────────
def chart_monthly_trend(df):
    monthly = df.groupby("Month_Name").agg(
        Productivity=("Productivity_Pct","mean"),
        Quality=("Quality_Score","mean"),
        Efficiency=("Efficiency","mean"),
    ).round(2).reindex(["Jan 2026","Feb 2026","Mar 2026"])
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    for ax, col, color, target, label in [
        (axes[0], "Productivity", "#1565C0", TARGET_PRODUCTIVITY, "Productivity %"),
        (axes[1], "Quality",      "#7C3AED", TARGET_QUALITY,      "Quality %"),
        (axes[2], "Efficiency",   "#EA580C", None,                "Tasks/Hour"),
    ]:
        ax.plot(monthly.index, monthly[col], marker="o", color=color, lw=2.5, ms=8)
        for i, (idx, val) in enumerate(monthly[col].items()):
            ax.annotate(f"{val:.2f}", (idx, val), textcoords="offset points",
                        xytext=(0, 10), ha="center", fontsize=10, fontweight="bold")
        if target:
            ax.axhline(target, color=COLOR_RED, ls="--", lw=1.2, label=f"Target {target}%")
            ax.legend(fontsize=9)
        ax.set_title(f"Monthly {col} Trend", fontsize=12, fontweight="bold")
        ax.set_ylabel(label); ax.tick_params(axis="x", rotation=15)

    fig.suptitle("Monthly Performance Trends — Q1 2026", fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()
    save(fig, "04_monthly_trends.png")

# ── CHART 5: Top 10 Employees ─────────────────────────────────────
def chart_top_employees(df):
    emp = df.groupby("Employee_Name")["Productivity_Pct"].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(emp.index[::-1], emp.values[::-1], color="#1565C0", edgecolor="white")
    for bar in bars:
        ax.text(bar.get_width()+0.3, bar.get_y()+bar.get_height()/2,
                f"{bar.get_width():.2f}%", va="center", fontsize=9.5, fontweight="bold")
    ax.axvline(TARGET_PRODUCTIVITY, color=COLOR_RED, ls="--", lw=1.5, label="100% Target")
    ax.set_title("Top 10 Employees by Avg Productivity %", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Avg Productivity %"); ax.legend(); ax.set_xlim(0, 135)
    save(fig, "05_top10_employees.png")

# ── CHART 6: Bottom 10 Employees ─────────────────────────────────
def chart_bottom_employees(df):
    emp = df.groupby("Employee_Name")["Productivity_Pct"].mean().sort_values(ascending=True).head(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(emp.index, emp.values, color=COLOR_RED, edgecolor="white")
    for bar in bars:
        ax.text(bar.get_width()+0.3, bar.get_y()+bar.get_height()/2,
                f"{bar.get_width():.2f}%", va="center", fontsize=9.5, fontweight="bold")
    ax.axvline(TARGET_PRODUCTIVITY, color=COLOR_GREEN, ls="--", lw=1.5, label="100% Target")
    ax.set_title("Bottom 10 Employees (Needs Training)", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Avg Productivity %"); ax.legend(); ax.set_xlim(0, 135)
    save(fig, "06_bottom10_employees.png")

# ── CHART 7: Productivity Distribution ───────────────────────────
def chart_prod_distribution(df):
    emp_avg = df.groupby("Employee_Name")["Productivity_Pct"].mean()
    bins = [0,70,80,90,100,110,120,999]
    labels = ["<70%","70-80%","80-90%","90-100%","100-110%","110-120%",">120%"]
    counts = pd.cut(emp_avg, bins=bins, labels=labels).value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(counts.index, counts.values, color="#0D9488", edgecolor="white", width=0.6)
    for bar in bars:
        if bar.get_height() > 0:
            ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.1,
                    str(int(bar.get_height())), ha="center", fontsize=11, fontweight="bold")
    ax.set_title("Employee Productivity Distribution", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Productivity % Range"); ax.set_ylabel("No. of Employees")
    save(fig, "07_productivity_distribution.png")

# ── CHART 8: Quality Distribution Pie ────────────────────────────
def chart_quality_pie(df):
    bins   = [0,80,85,90,95,101]
    labels = ["<80%\n(Poor)","80-85%\n(Below Avg)","85-90%\n(Average)","90-95%\n(Good)",">=95%\n(Excellent)"]
    counts = pd.cut(df["Quality_Score"], bins=bins, labels=labels).value_counts().sort_index()
    colors = [COLOR_RED,"#EA580C",COLOR_GOLD,"#16A34A","#0D9488"]
    fig, ax = plt.subplots(figsize=(8, 7))
    wedges, texts, autotexts = ax.pie(counts, labels=labels, autopct="%1.1f%%",
                                       colors=colors, startangle=140,
                                       wedgeprops=dict(edgecolor="white",linewidth=1.5))
    for t in autotexts: t.set_fontsize(9)
    ax.set_title("Quality Score Distribution", fontsize=13, fontweight="bold", pad=12)
    save(fig, "08_quality_distribution.png")

# ── CHART 9: Dept Productivity Monthly Heatmap ───────────────────
def chart_heatmap(df):
    pivot = df.pivot_table(index="Department", columns="Month_Name",
                           values="Productivity_Pct", aggfunc="mean")
    pivot = pivot.reindex(DEPTS)[["Jan 2026","Feb 2026","Mar 2026"]]
    fig, ax = plt.subplots(figsize=(9, 4))
    sns.heatmap(pivot, annot=True, fmt=".2f", cmap="RdYlGn",
                linewidths=0.5, linecolor="white", ax=ax,
                vmin=88, vmax=110, cbar_kws={"label": "Productivity %"})
    ax.set_title("Productivity % Heatmap — Department × Month", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Month"); ax.set_ylabel("Department")
    save(fig, "09_dept_month_heatmap.png")

# ── CHART 10: Hours vs Tasks Scatter ─────────────────────────────
def chart_hours_scatter(df):
    dept_avg = df.groupby(["Department","Hours_Worked"])["Tasks_Completed"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(9, 5))
    for dept in DEPTS:
        sub = dept_avg[dept_avg["Department"]==dept]
        ax.scatter(sub["Hours_Worked"], sub["Tasks_Completed"],
                   label=dept, color=DEPT_COLORS[dept], s=80, alpha=0.8)
    ax.set_title("Hours Worked vs Avg Tasks Completed", fontsize=13, fontweight="bold", pad=12)
    ax.set_xlabel("Hours Worked"); ax.set_ylabel("Avg Tasks Completed")
    ax.legend(); ax.grid(True, alpha=0.4)
    save(fig, "10_hours_vs_tasks.png")

# ── CHART 11: Dept Trend Lines ────────────────────────────────────
def chart_dept_trends(df):
    monthly_dept = df.groupby(["Department","Month_Name"])["Productivity_Pct"].mean().unstack()
    monthly_dept = monthly_dept[["Jan 2026","Feb 2026","Mar 2026"]]
    fig, ax = plt.subplots(figsize=(10, 6))
    for dept in DEPTS:
        vals = monthly_dept.loc[dept]
        ax.plot(vals.index, vals.values, marker="o", lw=2.5,
                color=DEPT_COLORS[dept], label=dept, ms=8)
        for x, y in zip(vals.index, vals.values):
            ax.annotate(f"{y:.2f}%", (x, y), textcoords="offset points",
                        xytext=(0, 8), ha="center", fontsize=9)
    ax.axhline(100, color=COLOR_RED, ls="--", lw=1.5, label="Target 100%")
    ax.set_title("Productivity % Trend by Department (Monthly)", fontsize=13, fontweight="bold", pad=12)
    ax.set_ylabel("Avg Productivity %"); ax.legend(); ax.set_ylim(85, 115)
    ax.tick_params(axis="x", rotation=15)
    save(fig, "11_dept_trend_lines.png")

# ── MAIN ──────────────────────────────────────────────────────────
def generate_all_charts():
    print("=" * 60)
    print("  STEP 9: GENERATING ALL CHARTS")
    print("=" * 60)
    df = load_df()
    print(f"\n📊 Generating 11 charts to: {OUTPUTS_CHARTS}\n")

    chart_dept_productivity(df)
    chart_dept_quality(df)
    chart_dept_efficiency(df)
    chart_monthly_trend(df)
    chart_top_employees(df)
    chart_bottom_employees(df)
    chart_prod_distribution(df)
    chart_quality_pie(df)
    chart_heatmap(df)
    chart_hours_scatter(df)
    chart_dept_trends(df)

    print(f"\n✅ All 11 charts saved to outputs/charts/")

if __name__ == "__main__":
    generate_all_charts()
    print("\n✅ Step 9 Complete.\n")
