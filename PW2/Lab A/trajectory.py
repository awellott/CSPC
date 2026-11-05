import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
t = data[:, 0]
x = data[:, 1]
y = data[:, 2]

vx = np.gradient(x, t)
vy = np.gradient(y, t)
speed = np.sqrt(vx**2 + vy**2)

fig, axes = plt.subplots(2, 1, figsize=(8, 9))

axes[0].plot(x, y)
axes[0].set_xlabel("x (m)")
axes[0].set_ylabel("y (m)")
axes[0].set_title("Tracked path")
axes[0].set_aspect("equal", adjustable="datalim")

axes[1].plot(t, speed)
axes[1].set_xlabel("time (s)")
axes[1].set_ylabel("speed (m/s)")

fig.tight_layout()
fig.savefig("trajectory.png", dpi=150)
print("Mean speed:", np.mean(speed))
print("Max speed:", np.max(speed))