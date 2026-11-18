
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

## PW1 - Lab B: Optimisation Warm-up

**What I built:**
- `PW1/Lab B/warmup.py`: minimises f(x) = (x-3)^2 + 1 (2A) and g(x) = x^4 - 3x^2 + x + 5 (2B) with three methods: gradient descent by hand, `scipy.optimize.newton` on the derivative, and `minimize(..., method="SLSQP")`. For 2B, I checked the sign of g'' at each answer (g'' > 0 = minimum, g'' < 0 = maximum).

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

- Equivalence point: V = 50 mL (expected: about 50 mL).
- The left plot shows the pH jump and the right plot shows the slope peaking at the same volume (plot saved as `titration.png`).

### Summary (Part 6)

**Three methods compared (Part 2).** I minimised the same functions with gradient descent, `scipy.optimize.newton` (applied to the derivative) and `minimize(..., method="SLSQP")`. On the convex function f(x) = (x-3)^2 + 1 all three methods agree. On g(x) = x^4 - 3x^2 + x + 5, which has a global minimum at x = -1.3009, a local maximum at x = 0.1699 and a local minimum at x = 1.1309, the results depend on the method and on the starting point. From x0 = 0, gradient descent and SLSQP find the global minimum (x ≈ -1.3008), while Newton converges to the local maximum (x = 0.1699, g'' = -5.65), because it only finds roots of g'. From x0 = 2, gradient descent and Newton fall into the nearest local minimum (x = 1.1309), while SLSQP reaches the global minimum. All methods are local, so the result depends on both the algorithm and the starting point, and the sign of g'' must be checked before trusting a stationary point as a minimum.

**Fitted rate constant.** Fitting C0·exp(-k·t) to `kinetics.csv` with SLSQP gives k = 0.2493 (expected: close to 0.25). The fitted curve passes through the data points (`kinetics.png`).

**Equilibrium composition.** Solving (2x)^2 / ((1-x)(1-x)) = K with K = 16, both with `newton` and with `minimize`, gives x = 0.6667. Equilibrium amounts: H2 = 0.3333 mol, I2 = 0.3333 mol, HI = 1.3333 mol (`equilibrium.png`).

**Titration equivalence point.** The slope of the pH curve, computed with `np.gradient(pH, V)`, peaks at V = 50 mL (expected: about 50 mL), where the pH curve jumps (`titration.png`).

## PW2 - Lab A: Motion from Tracking Data

**What I built:** `PW2/Lab A/analysis.py` reads the noisy free-fall measurements in `freefall.csv`, computes velocity and acceleration with `np.gradient` (applied once and twice), integrates the acceleration back with `cumulative_trapezoid` and plots position, velocity and acceleration in `motion.png`.

**Results:**
- Mean acceleration: -8.58 m/s^2 (expected: about -9.81). The standard deviation is 28.7 m/s^2, so the acceleration is very noisy.
- Excluding the 5 edge points on each side, the mean is -10.03 m/s^2, close to -9.81. The edge points are the noisiest, because `np.gradient` uses one-sided differences there.
- The median (-5.74 m/s^2) is not close to -9.81, which also shows how scattered the acceleration values are.
- Integrating the acceleration back recovers the velocity and position with maximum errors of 4.45 m/s and 0.78 m.

**Why is the acceleration so noisy? (Part 3)** Each derivative divides the small random errors in the measured position by the small time step (0.1 s), so differentiating twice amplifies the noise enormously, while the position itself only contains the original, small noise.


**Conclusion:** differentiation amplifies noise (each derivative is noisier than the previous one: position -> velocity -> acceleration), while integration suppresses it, so the recovered velocity and position follow smooth curves.

![Position, velocity and acceleration](PW2/Lab%20A/motion.png)

**Bonus: 2D trajectory.** trajectory.csv contains a noisy tracked path (time, x, y).
I differentiated x and y separately with np.gradient and computed the speed
sqrt(vx^2 + vy^2). The mean speed is 23.65 and the maximum speed is 38.69.

![Tracked path and speed](PW2/Lab%20A/trajectory.png)


## Part 2 — Three routes to a minimum

Code: `PW2/Lab B/warmup.py`. Three methods were compared: gradient descent (written by hand, step size 0.05), Newton's method (`scipy.optimize.newton` applied to f'(x) = 0, with f'' as the derivative) and SLSQP (`scipy.optimize.minimize(..., method="SLSQP")`).

### 2A. Easy convex function: f(x) = (x - 3)^2 + 1

Start point x0 = 0.

| Method | x | f(x) |
|---|---|---|
| Gradient descent | 3.000000 | 1.000000 |
| Newton | 3.000000 | 1.000000 |
| SLSQP | 3.000000 | 1.000000 |

All three methods reach x ≈ 3. f is convex with a single global minimum, so every method finds it and the differences between the methods are hidden.

### 2B. Harder landscape: g(x) = x^4 - 3x^2 + x + 5

g'(x) = 4x^3 - 6x + 1 has three roots, so g has several stationary points (two minima and one maximum).

| Start | Method | x | g(x) | g''(x) | Type |
|---|---|---|---|---|---|
| x0 = 0 | Gradient descent | -1.3008 | 1.4861 | - | minimum (global) |
| x0 = 0 | Newton | 0.1699 | 5.0841 | -5.65 | **maximum** |
| x0 = 0 | SLSQP | -1.3009 | 1.4861 | - | minimum (global) |
| x0 = 2 | Gradient descent | 1.1309 | 3.9298 | - | minimum (local) |
| x0 = 2 | Newton | 1.1309 | 3.9298 | 9.35 | minimum (local) |
| x0 = 2 | SLSQP | -1.3006 | 1.4861 | - | minimum (global) |

**Do the methods agree?**
No, not in general. From x0 = 0, gradient descent and SLSQP agree (x ≈ -1.30), but Newton ends at a different point. From x0 = 2, gradient descent and Newton agree (x ≈ 1.13), but SLSQP ends at x ≈ -1.30. The result depends on the method and on the starting point.

**Did Newton land on a minimum?**
- From x0 = 0: **no**. Newton converged to x ≈ 0.17, where g'' < 0, so this is a maximum (g = 5.08, higher than the nearby points).
- From x0 = 2: **yes**. It converged to x ≈ 1.13, where g'' > 0, so it is a minimum, but only a local one (g = 3.93 versus 1.49 at x ≈ -1.30).

**Conclusions**
- Newton's method here solves g'(x) = 0. It finds any stationary point, whether minimum or maximum, so the sign of g'' must be checked at the answer (g'' > 0 minimum, g'' < 0 maximum).
- g has two minima, at x ≈ -1.30 (global) and x ≈ 1.13 (local). Gradient descent and Newton end up in the basin of the start point, so a different x0 can give a different answer.
- On the easy convex function (2A) the methods are indistinguishable. The non-convex function (2B) shows their differences: sensitivity to the start point, and the need to verify that a stationary point is really a minimum.

## PW2 --- Lab B: Optimisation in chemistry

**Part 3 (reaction rate).** I fitted C(t) = C0 * exp(-k t) to the noisy
concentration data by minimising the sum of squared errors with SLSQP
(bounds 0 to 5, start 0.5). The fitted rate constant is k = 0.2618, and the
curve follows the measured points well despite the noise.

![Kinetics fit](PW2/Lab%20B/kinetics.png)

**Part 4 (equilibrium).** Solving (2x)^2 / ((1-x)^2) - K = 0 by root-finding
(Newton) and by minimising the squared imbalance (SLSQP) gives the same
extent x = 0.667. The equilibrium amounts are H2 = 0.333 mol, I2 = 0.333 mol
and HI = 1.333 mol.

![Equilibrium](PW2/Lab%20B/equilibrium.png)

Part 5 (bonus, titration).* The equivalence point is where the pH curve
is steepest, so I computed the slope with np.gradient(pH, V) and took the
volume where it is largest (np.argmax). The equivalence point is at 50.0 mL.

![Titration](PW2/Lab%20B/titration.png)

## PW2 --- Lab B: Optimisation in chemistry

**Part 2 (three methods).** On the easy convex function f(x) = (x-3)^2 + 1,
gradient descent, Newton's method and SLSQP all reach x = 3. On the harder
g(x) = x^4 - 3x^2 + x + 5 they disagree: starting from x0 = 0, gradient
descent and SLSQP find the minimum near x = -1.30, while Newton lands on a
stationary point near x = 0.17 where g'' < 0, which is a maximum. Starting
from x0 = 2, all three methods find the local minimum near x = 1.13. So on a
complicated landscape the starting point and the algorithm matter, and
Newton's method only finds a stationary point, not necessarily a minimum.

**Part 3 (rate constant).** Fitting C(t) = C0 * exp(-k t) to the noisy data
with SLSQP gives k = 0.2618.

![Kinetics fit](PW2/Lab%20B/kinetics.png)

**Part 4 (equilibrium).** Newton (root-finding) and SLSQP (minimising the
squared imbalance) agree on x = 0.667, giving H2 = 0.333 mol, I2 = 0.333 mol
and HI = 1.333 mol.

![Equilibrium](PW2/Lab%20B/equilibrium.png)

**Part 5 (titration, bonus).** The steepest point of the pH curve, found with
np.gradient and np.argmax, gives an equivalence point at 50.0 mL.

![Titration](PW2/Lab%20B/titration.png)

## PW3 – Session 1: Characterising the data

**Data source.** Heart Disease (Cleveland) dataset, from the UCI Machine Learning
Repository (https://archive.ics.uci.edu/ml/datasets/Heart+Disease), downloaded from
Kaggle (Ritwik B3, "Heart Disease Cleveland",
https://www.kaggle.com/datasets/ritwikb3/heart-disease-cleveland, CC BY-SA 4.0).

**Loading.** `heart.csv` has 303 rows (patients) and 14 columns. I isolated the
four continuous variables: age, chol, trestbps, thalach.

**Distributions.** See `distributions.png` (script: `session1.py`).

![distributions](distributions.png)

- **age:** (symmetric or skewed? where is the peak? range?)
- **chol:** (peak, direction of the tail, outliers?)
- **trestbps:** (...)
- **thalach:** (...)