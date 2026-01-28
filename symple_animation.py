import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

x, y = [], [] 
frames_interval = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(0, 2*np.pi) 
ax.set_ylim(-1, 1) 

def update(frame):
    x.append(frame) 
    y.append(np.sin(frame)) 
    
   
    anim_object.set_data(x, y)

    return anim_object


ani = FuncAnimation(fig, 
                    update, 
                    frames=frames_interval, 
                    interval=50) 
                                 

ani.save('animation_1.gif', writer="pillow")
