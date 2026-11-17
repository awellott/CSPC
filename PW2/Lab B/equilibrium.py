"""
PW2 Lab B Part 4 -- chemical equilibrium of H2 + I2 <-> 2 HI.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 16.0  # equilibrium constant (use the value from your skeleton if it has one)


def k_imbalance(x):
    """Left side of (2x)^2 / ((1-x)(1-x)) - K; zero at equilibrium."""
    x = np.ravel(x)[0]
    return (2 * x) ** 2 / ((1 - x) * (1 - x)) - K


# (1) root-finding with Newton
x_newton = newton(k_imbalance, 0.5)
print("Newton x:", x_newton)

# (2) minimise k_imbalance(x)**2 with SLSQP
res = minimize(lambda x: k_imbalance(x) ** 2, x0=0.5,
               method="SLSQP", bounds=[(0, 0.99)])
x_slsqp = res.x[0]
print("SLSQP x:", x_slsqp)

x_eq = x_newton
print("Equilibrium amounts (mol):")
print("  H2 =", 1 - x_eq)
print("  I2 =", 1 - x_eq)
print("  HI =", 2 * x_eq)

# plot amounts versus extent x
xs = np.linspace(0, 1, 200)
plt.figure(figsize=(7, 5))
plt.plot(xs, 1 - xs, label="H2")
plt.plot(xs, 1 - xs, "--", label="I2 (same as H2)")
plt.plot(xs, 2 * xs, label="HI")
plt.axvline(x_eq, color="k", linestyle=":", label=f"equilibrium x = {x_eq:.3f}")
plt.xlabel("extent of reaction x")
plt.ylabel("amount (mol)")
plt.legend()
plt.tight_layout()
plt.savefig("equilibrium.png", dpi=150)