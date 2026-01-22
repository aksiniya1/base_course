import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


t = np.arange(0.01, 16*np.pi, 0.01)

x1 = np.sin(2*t)
y1 = 1 - np.cos(2*t)
z1 = 2*np.cos(t)

x2 = (2**(-0.1*t)) * np.cos(2*t)
y2 = (2**(-0.1*t)) * np.sin(2*t)
z2 = -t

R = 1
x3 = R * (np.cos(t))**3
y3 = R * (np.sin(t))**3
z3 = np.cos(2*t)

fig = plt.figure(figsize=(10, 15))

ax1 = fig.add_subplot(311, projection='3d')
ax1.plot(x1, y1, z1, linewidth=2, color='blue')
ax1.set_title('а) Непонятная кривая', fontsize=12)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.view_init(elev=20, azim=45) 

ax2 = fig.add_subplot(312, projection='3d')
ax2.plot(x2, y2, z2, linewidth=2, color='red')
ax2.set_title('б) Кривая, напоминающая пружинку', fontsize=12)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.view_init(elev=20, azim=45)

ax3 = fig.add_subplot(313, projection='3d')
ax3.plot(x3, y3, z3, linewidth=2, color='green')
ax3.set_title('в) Крутая кривая', fontsize=12)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.view_init(elev=20, azim=45)

plt.tight_layout()
plt.show()

plt.savefig('figures2.png',)