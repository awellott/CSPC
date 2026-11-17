"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration), C0 = first value
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)
t = data[:, 0]
C = data[:, 1]
C0 = C[0]


# TODO 2: total error = sum of (measured - C0*exp(-k*t))^2
def total_error(k):
    k = np.ravel(k)[0]
    return np.sum((C - C0 * np.exp(-k * t)) ** 2)


# TODO 3: minimise the error with SLSQP, bounds [(0, 5)], start x0=0.5
res = minimize(total_error, x0=0.5, method="SLSQP", bounds=[(0, 5)])
k_fit = res.x[0]
print("Fitted k:", k_fit)
print("Final error:", res.fun)

# TODO 4: plot measured data (points) and fitted curve (line)
tt = np.linspace(t.min(), t.max(), 200)
plt.figure(figsize=(7, 5))
plt.plot(t, C, "o", label="measured data")
plt.plot(tt, C0 * np.exp(-k_fit * tt), label=f"fit, k = {k_fit:.4f}")
plt.xlabel("time")
plt.ylabel("concentration")
plt.legend()
plt.tight_layout()
plt.savefig("kinetics.png", dpi=150)