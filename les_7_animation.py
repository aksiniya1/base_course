import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

t = np.arange(0.01, 4*np.pi, 0.01)
R = 1

x = R * np.cos(t)
y= R * np.sin(t)
z = R * np.log10(t)

ax.plot(x, y, z, label='Dich')

ax.legend()
	
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D Test')
 
plt.savefig('fig_1.png')