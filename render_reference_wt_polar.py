"""Regenerate Figure 4 in the manuscript's Matplotlib plot style.

Uses the original pointwise wind-tunnel coefficients and propagated
uncertainty magnitudes in figures_revision_measured_uncertainty_data.csv.
No smoothing or statistical re-estimation is performed.

Usage: python render_reference_wt_polar.py
Requirements: matplotlib, pandas
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd

root = Path(__file__).resolve().parent
df = pd.read_csv(root / "figures_revision_measured_uncertainty_data.csv")
assert len(df) == 27 and df["x"].is_unique

plt.rcParams.update({
    "font.family": "DejaVu Serif",
    "mathtext.fontset": "stix",
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "lines.linewidth": 1.1,
})
fig, axes = plt.subplots(1, 2, figsize=(6.6, 3.35))
fig.subplots_adjust(left=.09, right=.986, bottom=.263, top=.885, wspace=.27)
colors = ["#0072B2", "#D55E00", "#009E73", "#8B55A3"]
markers = ["o", "s", "^", "D"]
for ax, group in zip(axes, ["a", "b"]):
    for delta, color, marker in zip([0, 10, 20, 30], colors, markers):
        ax.errorbar(df["x"], df[f"{group}{delta}"],
                    yerr=df[f"e{group}{delta}"],
                    color=color, marker=marker, markersize=2.35,
                    markeredgewidth=.35, linewidth=1.05,
                    elinewidth=1.05, capsize=2.4, capthick=1.0, zorder=3)
    ax.set_xlim(-26, 26)
    ax.set_xticks([-20, -10, 0, 10, 20])
    ax.set_xlabel(r"$\alpha$ (deg)")
    ax.grid(alpha=.15, linewidth=.65)
    ax.axhline(0, color="0.50", lw=.7, zorder=0)
axes[0].set_ylim(-.95, 1.2)
axes[0].set_ylabel(r"$C_L$")
axes[0].set_title("(a) Lift")
axes[1].set_ylim(-.23, .065)
axes[1].set_ylabel(r"$C_M^A$")
axes[1].set_title("(b) Pitching moment")
handles = [Line2D([], [], color=c, marker=m, ms=4, lw=1.1)
           for c, m in zip(colors, markers)]
legend = fig.legend(handles, [rf"$\delta={d}^\circ$" for d in [0, 10, 20, 30]],
                    loc="lower center", bbox_to_anchor=(.5, .008),
                    ncol=4, frameon=False, handlelength=1.8,
                    columnspacing=1.2, handletextpad=.45)
fig.canvas.draw()
canvas = fig.canvas.get_renderer()
rect = legend.get_window_extent(canvas)
for ax in axes:
    if rect.overlaps(ax.get_tightbbox(canvas)):
        raise RuntimeError("Legend overlaps the plot or axes")
if rect.x0 < 0 or rect.x1 > fig.bbox.width or rect.y0 < 0:
    raise RuntimeError("Legend exceeds the figure boundary")
fig.savefig(root / "figures_revision_measured_baseline.pdf")
plt.close(fig)
