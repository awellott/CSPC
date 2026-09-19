
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