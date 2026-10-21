"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv
data = np.loadtxt("freefall.csv", delimiter=",", skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: velocity and acceleration by differentiation
v = np.gradient(y, t)
a = np.gradient(v, t)
print("Mean acceleration:", np.mean(a))
print("Std of acceleration:", np.std(a))

# TODO 3: integrate back
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]
print("Max error of recovered velocity:", np.max(np.abs(v_rec - v)))
print("Max error of recovered position:", np.max(np.abs(y_rec - y)))
print("Median acceleration:", np.median(a))
print("Mean acceleration (without 5 edge points on each side):", np.mean(a[5:-5]))

# TODO 4: figure with 3 stacked panels
fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

axes[0].plot(t, y, label="measured y")
axes[0].plot(t, y_rec, "--", label="recovered y")
axes[0].set_ylabel("position (m)")
axes[0].legend()

axes[1].plot(t, v, label="v from gradient")
axes[1].plot(t, v_rec, "--", label="recovered v")
axes[1].set_ylabel("velocity (m/s)")
axes[1].legend()

axes[2].plot(t, a, label="a from gradient")
axes[2].axhline(-9.81, color="red", linestyle="--", label="true -9.81")
axes[2].set_ylabel("acceleration (m/s²)")
axes[2].set_xlabel("time (s)")
axes[2].legend()

plt.tight_layout()
plt.savefig("motion.png", dpi=150)