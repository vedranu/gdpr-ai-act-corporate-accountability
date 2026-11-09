"""Figure 1: core records per publication year in Scopus and Web of Science."""
import csv, pathlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
rows = list(csv.DictReader(open(ROOT / "data" / "core_corpus_by_year.csv", encoding="utf-8")))
years = [r["year"] for r in rows]
scopus = [int(r["scopus"]) for r in rows]
wos = [int(r["wos"]) for r in rows]

plt.rcParams["font.family"] = "DejaVu Serif"
fig, ax = plt.subplots(figsize=(6.3, 3.0), dpi=300)
x = np.arange(len(years)); w = 0.36
b1 = ax.bar(x - w / 2, scopus, w, label=f"Scopus (n = {sum(scopus)})", color="#3b5b92")
b2 = ax.bar(x + w / 2, wos, w, label=f"Web of Science (n = {sum(wos)})", color="#c9a227")
for bars in (b1, b2):
    for r in bars:
        ax.annotate(str(int(r.get_height())), (r.get_x() + r.get_width() / 2, r.get_height()),
                    ha="center", va="bottom", fontsize=8, xytext=(0, 2), textcoords="offset points")
ax.set_xticks(x); ax.set_xticklabels(years, fontsize=9)
ax.set_ylabel("Number of records", fontsize=9); ax.set_xlabel("Publication year", fontsize=9)
ax.tick_params(axis="y", labelsize=8); ax.set_ylim(0, 140)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
out = ROOT / "figures" / "Figure1.png"
fig.savefig(out, dpi=300)
Image.open(out).convert("RGB").save(out.with_suffix(".tif"), dpi=(300, 300), compression="tiff_lzw")
print("saved", out)
