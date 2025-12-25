

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

phi = np.linspace(0, 2*np.pi, 200)  
alpha = 0.15  

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)


line, = ax.plot([], [], 'b-', linewidth=2)


def init():
    line.set_data([], [])
    return line,


def animate(frame):

    t = frame * 0.1
    r = alpha * t
    
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    
    line.set_data(x, y)
    
    if r > 8:  
        new_limit = r * 1.2
        ax.set_xlim(-new_limit, new_limit)
        ax.set_ylim(-new_limit, new_limit)
    
    return line,

ani = FuncAnimation(fig, animate, frames=150, 
                    init_func=init, blit=True, interval=50)

plt.tight_layout()
plt.show()

ani.save('animation_5.gif', writer="pillow")
