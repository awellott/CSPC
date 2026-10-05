import numpy as np
from scipy.optimize import newton, minimize


# ---------- helper: gradient descent ----------
def gradient_descent(fprime, x0, lr=0.01, n_iter=10000, tol=1e-10):
    x = x0
    for _ in range(n_iter):
        step = lr * fprime(x)
        x = x - step
        if abs(step) < tol:
            break
    return x


# ---------- 2A: f(x) = (x-3)^2 + 1 ----------
def f(x):   return (x - 3)**2 + 1
def df(x):  return 2 * (x - 3)
def d2f(x): return 2.0

x0 = 0.0
x_gd  = gradient_descent(df, x0, lr=0.1)
x_new = newton(df, x0, fprime=d2f)          # корень f'(x), настоящий Ньютон
x_sl  = minimize(lambda v: f(v[0]), [x0], method="SLSQP").x[0]

print("2A  gradient descent:", x_gd)
print("2A  Newton on f'    :", x_new)
print("2A  SLSQP           :", x_sl)


# ---------- 2B: g(x) = x^4 - 3x^2 + x + 5 ----------
def g(x):       return x**4 - 3*x**2 + x + 5
def gprime(x):  return 4*x**3 - 6*x + 1
def gsecond(x): return 12*x**2 - 6

for x0 in (0.0, 2.0):
    x_gd  = gradient_descent(gprime, x0, lr=0.01)
    x_new = newton(gprime, x0, fprime=gsecond)   # Ньютон: нужна g''
    x_sl  = minimize(lambda v: g(v[0]), [x0], method="SLSQP").x[0]

    print(f"\n2B  x0 = {x0}")
    for name, x in [("gradient descent", x_gd), ("Newton", x_new), ("SLSQP", x_sl)]:
        kind = "minimum" if gsecond(x) > 0 else "maximum"
        print(f"  {name:17s} x = {x:.6f}  g(x) = {g(x):.6f}  g'' = {gsecond(x):+.3f}  -> {kind}")

    