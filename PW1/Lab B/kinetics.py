from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

here = Path(__file__).parent

# kinetics.csv: columns time, concentration (first row is a header)
data = np.genfromtxt(here / "kinetics.csv", delimiter=",", names=True)
t = data["time"]
c_meas = data["concentration"]

C0 = c_meas[0]   # C0 = first measured value


def total_error(k):
    k = float(np.atleast_1d(k)[0])
    return np.sum((c_meas - C0 * np.exp(-k * t)) ** 2)


res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
k_fit = res.x[0]
print(f"Fitted k = {k_fit:.4f}  (error = {res.fun:.6f})")

t_fine = np.linspace(t.min(), t.max(), 200)
plt.scatter(t, c_meas, label="data")
plt.plot(t_fine, C0 * np.exp(-k_fit * t_fine), "r-", label=f"fit, k = {k_fit:.3f}")
plt.xlabel("time")
plt.ylabel("concentration")
plt.legend()
plt.savefig(here / "kinetics.png", dpi=150)