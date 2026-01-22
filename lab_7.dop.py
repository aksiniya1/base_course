import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

R = 2.0 
k = 0.8 

total_frames = 180

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, alpha=0.3)
ax.set_aspect('equal')

ax.set_xlim(-0.5, 4*np.pi*R + 0.5)
ax.set_ylim(-R*k - 1.5, R*k + 1.5)

def cycloid(t, R, k):
    x = R * (t - k * np.sin(t))
    y = R * (1 - k * np.cos(t))
    return x, y

t_background = np.linspace(0, 4*np.pi, 1000)
x_background, y_background = cycloid(t_background, R, k)

ax.plot(x_background, y_background, 'b-', linewidth=2, alpha=0.7)

point, = ax.plot([], [], 'ro', markersize=12)
trace, = ax.plot([], [], 'r-', linewidth=1.5, alpha=0.7)
circle = plt.Circle((0, R), R, fill=False, color='green', linewidth=1.5, alpha=0.5)
ax.add_patch(circle)

radius_line, = ax.plot([], [], 'g--', linewidth=1.5, alpha=0.7)

trace_x = []
trace_y = []

def init():
    point.set_data([], [])
    trace.set_data([], [])
    radius_line.set_data([], [])
    return point, trace, radius_line

def animate(frame):

    t = 4 * np.pi * frame / total_frames
 
    x_point, y_point = cycloid(t, R, k)

    point.set_data([x_point], [y_point])

    trace_x.append(x_point)
    trace_y.append(y_point)
    trace.set_data(trace_x, trace_y)

    circle.center = (R * t, R)

    x_circle_point = R * t - R * k * np.sin(t)
    y_circle_point = R - R * k * np.cos(t)
    radius_line.set_data([R * t, x_circle_point], [R, y_circle_point])
    
    return point, trace, circle, radius_line

ani = FuncAnimation(fig, animate, frames=total_frames,
                    init_func=init, blit=True, interval=50)

plt.tight_layout()
plt.show()
ani.save('animation_10.gif', writer="pillow")