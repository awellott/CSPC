
# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:

    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A radioactive decay simulation in two versions (a pure-Python loop and a NumPy version), a conda environment file, and pytest tests, all under PW1/Lab A, plus a script that compares the speed of the two versions.

**Speed comparison (loop vs NumPy):**
- loop  : 3.766454 s
- numpy : 0.000359 s
- speed-up: 10481.6 x faster

**Tests:** all passing? yes (3 passed in pytest -v)

**Conclusion:**
- All three tests pass, and the simulation agrees with the analytical law N0 * exp(-lam * t). The NumPy version is about 10,000 times faster than the loop, because the loop runs Python code for every atom, while NumPy does the work on the whole array at once in compiled code. I had some problems with a wrong import path in the tests, running files with the wrong Python instead of pytest, and the time step in my law test, and fixing them taught me to read error messages carefully.

---

## PW2 - Lab B: Optimisation Warm-up

**What I built:**
- `PW2/Lab B/warmup.py`: minimises f(x) = (x-3)^2 + 1 (2A) and g(x) = x^4 - 3x^2 + x + 5 (2B) with three methods: gradient descent by hand, `scipy.optimize.newton` on the derivative, and `minimize(..., method="SLSQP")`. For 2B, I checked the sign of g'' at each answer (g'' > 0 = minimum, g'' < 0 = maximum).

**2B results (g has three stationary points: x = -1.3009 global min, 0.1699 local max, 1.1309 local min):**

| x0 | Method           | x         | g(x)     | g''    | Type    |
|----|------------------|-----------|----------|--------|---------|
| 0  | Gradient descent | -1.300840 | 1.486095 | +14.31 | minimum |
| 0  | Newton           |  0.169938 | 5.084135 | -5.65  | maximum |
| 0  | SLSQP            | -1.300857 | 1.486095 | +14.31 | minimum |
| 2  | Gradient descent |  1.130901 | 3.929770 | +9.35  | minimum |
| 2  | Newton           |  1.130901 | 3.929770 | +9.35  | minimum |
| 2  | SLSQP            | -1.300639 | 1.486095 | +14.30 | minimum |

**Do the methods agree?** Not always. From x0 = 0, Newton disagrees with the other two; from x0 = 2, SLSQP disagrees with the other two.

**Did Newton land on a minimum or another stationary point?** From x0 = 0 it landed on a maximum (g'' < 0), because Newton on g' only finds roots of g' and does not distinguish minima from maxima. From x0 = 2 it landed on the local minimum at 1.1309.

**How did the starting point change the result?** From x0 = 2, gradient descent and Newton fall into the nearest basin (a local minimum, not the global one). From x0 = 0, gradient descent reaches the global minimum, but Newton goes to the maximum.

**Conclusion:**
- On the easy convex function all methods agree. On the harder landscape all three methods are local, so the result depends on both the algorithm and the starting point. Checking the sign of g'' is necessary before trusting a stationary point as a minimum.


**Part 3: fitting a reaction rate (`kinetics.py`)**

I read `kinetics.csv` (time, concentration), set C0 to the first measured value, and minimised the sum of squared errors between the data and C0·exp(-k·t) with `minimize(..., method="SLSQP", bounds=[(0, 5)], x0=0.5)`.

- Fitted k = 0.2493 (expected: close to 0.25)
- The fitted curve passes through the data points (plot saved as `kinetics.png`).

**Part 4: chemical equilibrium (`equilibrium.py`)**

I wrote `k_imbalance(x)` = (2x)^2 / ((1-x)(1-x)) - K with K = 16 and solved it two ways: `scipy.optimize.newton` (root-finding) and `minimize` of `k_imbalance(x)**2` with `method="SLSQP"`.

- Both methods agree: x = 0.6667.
- Equilibrium amounts: H2 = 0.3333 mol, I2 = 0.3333 mol, HI = 1.3333 mol.
- The plot of H2, I2 and HI against x shows the reactants falling and the product rising, with the equilibrium marked (plot saved as `equilibrium.png`).

**Part 5 (bonus): titration equivalence point (`titration.py`)**

I read `titration.csv` (volume_base, pH), computed the slope of the pH curve with `np.gradient(pH, V)` and took the volume where the slope is largest with `np.argmax`.

- Equivalence point: V = ___ mL (expected: about 50 mL).
- The left plot shows the pH jump and the right plot shows the slope peaking at the same volume (plot saved as `titration.png`).
