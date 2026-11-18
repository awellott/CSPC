"""PW3 - Session 1: load heart.csv and look at the distribution of each continuous variable.

Run from your CSPC/PW3 folder (heart.csv must be in the same folder):
    conda activate cspc
    python session1.py
"""
import pandas as pd
import matplotlib.pyplot as plt

# ---- 1. Load the data ----
df = pd.read_csv("heart.csv")
print("Shape (rows, columns):", df.shape)
print(df.head())

continuous = ["age", "chol", "trestbps", "thalach"]
cont = df[continuous]
print()
print(cont.describe())

# ---- 2. Shape of each variable ----
labels = {
    "age": "Age (years)",
    "chol": "Cholesterol (mg/dl)",
    "trestbps": "Resting blood pressure (mm Hg)",
    "thalach": "Max heart rate (bpm)",
}

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.ravel(), continuous):
    ax.hist(cont[col], bins=20, edgecolor="black")
    ax.axvline(cont[col].mean(), linestyle="--", label="mean")
    ax.axvline(cont[col].median(), linestyle=":", label="median")
    ax.set_title(col)
    ax.set_xlabel(labels[col])
    ax.set_ylabel("Count")
    ax.legend()

fig.suptitle("Distributions of the continuous variables (Cleveland heart data)")
fig.tight_layout()
fig.savefig("distributions.png", dpi=150)
plt.show()

# Numbers that help you describe the shapes in the README
# (skew > 0: long right tail, skew < 0: long left tail)
print()
print("Skewness:\n", cont.skew())