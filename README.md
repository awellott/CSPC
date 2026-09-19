# CSPC - PW1 Lab A
I measured 3.766454 s for the loop version and  0.000359 for the NumPy version
on 200000 atoms, so NumPy is about 10481.6  times faster. All three tests pass (3 passed in pytest -v): test_starts_at_N0, test_rejects_negative_rate, test_matches_law.