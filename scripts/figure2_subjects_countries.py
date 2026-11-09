"""Figure 2: subject areas (a) and countries (b) of the Scopus core records."""
import csv, pathlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
def load(name):
    return [(r[0], int(r[1])) for r in list(csv.reader(open(ROOT / "data" / name, encoding="utf-8")))[1:]]

SUBJ_SHOWN = ["Computer Science", "Social Sciences", "Engineering", "Medicine",
              "Business, Management and Accounting", "Decision Sciences", "Mathematics",
              "Economics, Econometrics and Finance"]
subj_all = dict(load("scopus_core_subject_areas.csv"))
subj = [(s, subj_all[s]) for s in SUBJ_SHOWN]
ctry_all = load("scopus_core_countries.csv")
ctry = ctry_all[:10] + [c for c in ctry_all if c[0] == "Croatia"]
WRAP = {"Business, Management and Accounting": "Business, Management\nand Accounting",
        "Economics, Econometrics and Finance": "Economics, Econometrics\nand Finance"}
HIGHLIGHT = {"Business, Management and Accounting", "Economics, Econometrics and Finance", "Croatia"}

plt.rcParams["font.family"] = "DejaVu Serif"
fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 3.5), dpi=300)
def hbar(ax, data, title, col):
    data = data[::-1]
    labels = [WRAP.get(d[0], d[0]) for d in data]; vals = [d[1] for d in data]
    cols = ["#c0392b" if d[0] in HIGHLIGHT else col for d in data]
    bars = ax.barh(labels, vals, color=cols, height=0.65)
    for r, v in zip(bars, vals):
        ax.text(v + 1.5, r.get_y() + r.get_height() / 2, str(v), va="center", fontsize=7)
    ax.set_title(title, fontsize=9, loc="left"); ax.tick_params(labelsize=7)
    ax.spines[["top", "right"]].set_visible(False); ax.set_xlabel("Number of records", fontsize=7.5)
    ax.set_xlim(0, max(vals) * 1.18)
hbar(a, subj, "(a) Subject areas", "#3b5b92")
hbar(b, ctry, "(b) Countries/territories", "#c9a227")
fig.tight_layout(w_pad=1.5)
out = ROOT / "figures" / "Figure2.png"
fig.savefig(out, dpi=300)
Image.open(out).convert("RGB").save(out.with_suffix(".tif"), dpi=(300, 300), compression="tiff_lzw")
print("saved", out)
