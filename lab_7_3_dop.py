import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 5
R_out, R_in = 12, 2
angles = np.linspace(0, 2*np.pi, 2*n+1)
radii = np.array([R_out, R_in]*n + [R_out])
x = radii * np.cos(angles)
y = radii * np.sin(angles)

fig, ax = plt.subplots(figsize=(8,8))
ax.set(xlim=(-25,25), ylim=(-25,25), aspect='equal')
line, = ax.plot([], [], 'r-', lw=3)
fill = ax.fill([], [], 'gold', alpha=0.7)[0]

def animate(i):
    a = i * 0.02
    X = x*np.cos(a) - y*np.sin(a)
    Y = y*np.cos(a) + x*np.sin(a)
    line.set_data(X, Y)
    fill.set_xy(np.column_stack([X, Y]))
    return line, fill

ani = animation.FuncAnimation(fig, animate, frames=300, interval=20, blit=False)
plt.show()
ani.save('animation_9.gif', writer="pillow")