"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

here = Path(__file__).parent

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
data = np.genfromtxt(here / "titration.csv", delimiter=",", names=True)
V = data["volume_base"]
pH = data["pH"]

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope = np.gradient(pH, V)
i = np.argmax(slope)
V_eq = V[i]
print(f"Equivalence point: V = {V_eq:.2f} mL")

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(V, pH)
ax1.axvline(V_eq, color="gray", linestyle=":", label=f"equivalence V = {V_eq:.1f} mL")
ax1.set_xlabel("volume of base (mL)")
ax1.set_ylabel("pH")
ax1.set_title("pH curve")
ax1.legend()

ax2.plot(V, slope)
ax2.axvline(V_eq, color="gray", linestyle=":")
ax2.set_xlabel("volume of base (mL)")
ax2.set_ylabel("dpH/dV")
ax2.set_title("slope of pH curve")

plt.tight_layout()
plt.savefig(here / "titration.png", dpi=150)