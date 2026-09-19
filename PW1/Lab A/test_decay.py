"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate,simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)

def test_matches_law():
    n0, lam = 10_000, 0.4
    runs = [simulate(n0, lam, seed=s) for s in range(50)]
    mean_curve = np.mean(runs, axis=0)
    t = np.arange(len(mean_curve)) *0.05  # временная сетка, проверьте по decay.py
    expected = n0 * np.exp(-lam * t)
    assert mean_curve == pytest.approx(expected, rel=0.05)