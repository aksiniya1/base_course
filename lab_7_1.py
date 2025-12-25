import numpy as np
import matplotlib.pyplot as plt

R1 = 1  
t1 = np.linspace(0, 4*np.pi, 500) 
x1 = R1 * (t1 - np.sin(t1))
y1 = R1 * (1 - np.cos(t1))

R2 = 2  
t2 = np.linspace(0, 2*np.pi, 500)  
x2 = R2 * np.cos(t2)**3
y2 = R2 * np.sin(t2)**3

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(x1, y1, 'b', linewidth=2)

ax1.set_aspect('equal')

ax2.plot(x2, y2, 'r', linewidth=2)

ax2.set_aspect('equal')

plt.tight_layout()
plt.show()
plt.savefig('fig_5.png')