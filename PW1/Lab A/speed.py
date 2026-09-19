import time
from decay import simulate_loop, simulate

N = 200_000
LAM = 0.4

t0 = time.perf_counter()
simulate_loop(N, LAM)
t_loop = time.perf_counter() - t0

t0 = time.perf_counter()
simulate(N, LAM)
t_numpy = time.perf_counter() - t0

print(f"Loop:  {t_loop:.4f} s")
print(f"NumPy: {t_numpy:.4f} s")
print(f"NumPy is {t_loop / t_numpy:.1f} times faster")