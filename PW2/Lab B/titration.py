"""
PW2 Lab B Part 5 (bonus) -- titration equivalence point.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]
pH = data[:, 1]

slope = np.gradient(pH, V)
i = np.argmax(slope)
V_eq = V[i]
print("Equivalence point (mL):", V_eq)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

axes[0].plot(V, pH)
axes[0].axvline(V_eq, color="r", linestyle="--", label=f"equivalence {V_eq:.1f} mL")
axes[0].set_xlabel("volume of base (mL)")
axes[0].set_ylabel("pH")
axes[0].legend()

axes[1].plot(V, slope)
axes[1].axvline(V_eq, color="r", linestyle="--")
axes[1].set_xlabel("volume of base (mL)")
axes[1].set_ylabel("slope dpH/dV")

fig.tight_layout()
fig.savefig("titration.png", dpi=150)