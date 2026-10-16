from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

here = Path(__file__).parent

K = 16.0   # equilibrium constant


def k_imbalance(x):
    return (2 * x) ** 2 / ((1 - x) * (1 - x)) - K


# (1) root-finding
x_newton = newton(k_imbalance, 0.5)

# (2) minimise k_imbalance^2
res = minimize(lambda v: k_imbalance(v[0]) ** 2, [0.5],
               method="SLSQP", bounds=[(0, 0.99)], options={"ftol": 1e-12})
x_slsqp = res.x[0]

print(f"Newton: x = {x_newton:.6f}")
print(f"SLSQP : x = {x_slsqp:.6f}")
print(f"Equilibrium amounts: H2 = {1 - x_newton:.4f} mol, "
      f"I2 = {1 - x_newton:.4f} mol, HI = {2 * x_newton:.4f} mol")

x = np.linspace(0, 0.99, 200)
plt.plot(x, 1 - x, label="H2")
plt.plot(x, 1 - x, "--", label="I2")
plt.plot(x, 2 * x, label="HI")
plt.axvline(x_newton, color="gray", linestyle=":", label=f"equilibrium x = {x_newton:.3f}")
plt.xlabel("extent x (mol)")
plt.ylabel("amount (mol)")
plt.legend()
plt.savefig(here / "equilibrium.png", dpi=150)