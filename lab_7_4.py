import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def fractal_points(x0, y0, C, D, n=1000):
    x, y = np.zeros(n), np.zeros(n)
    x[0], y[0] = x0, y0
    for i in range(1, n):
        x[i] = x[i-1]**2 - y[i-1]**2 + C
        y[i] = 2 * x[i-1] * y[i-1] + D
    return x, y

x0, y0, C, D = 0.1, 0.1, 0.3, 0.33
x, y = fractal_points(x0, y0, C, D, 1000)

fig, ax = plt.subplots(figsize=(8, 6))
scat = ax.scatter([], [], s=10, c='blue')
ax.set_xlim(min(x)-0.1, max(x)+0.1)
ax.set_ylim(min(y)-0.1, max(y)+0.1)

def update(frame):
    scat.set_offsets(np.column_stack((x[:frame+1], y[:frame+1])))
    return scat,

ani = FuncAnimation(fig, update, frames=1000, interval=20, blit=True)
plt.show()

params = [
    (0.1, 0.1, 0.3, 0.33, "Базовый"),
    (0.0, 0.0, 0.3, 0.33, "Начало (0,0)"),
    (0.5, 0.5, 0.3, 0.33, "Начало (0.5,0.5)"),
    (0.1, 0.1, -0.7, 0.27, "Небазовый"),
    (0.1, 0.1, 0.36, 0.1, "C=0.36, D=0.1"),
    (0.1, 0.1, 0.0, 0.0, "C=0, D=0")
]

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
for idx, (x0p, y0p, Cp, Dp, title) in enumerate(params):
    ax = axes[idx//3, idx%3]
    xp, yp = fractal_points(x0p, y0p, Cp, Dp, 500)
    ax.scatter(xp, yp, s=5, alpha=0.6)
    ax.set_title(title)
plt.tight_layout()
plt.show()

ani.save('animation_8.gif', writer="pillow")