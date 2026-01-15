import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
Theta, Phi = np.meshgrid(theta, phi)

phi_vals = np.linspace(0, 2, 50)
theta_vals = np.linspace(0, 2*np.pi, 50)
Phi_par, Theta_par = np.meshgrid(phi_vals, theta_vals)

X_par = Phi_par * np.cos(Theta_par)
Y_par = Phi_par * np.sin(Theta_par)
Z_par = Phi_par**2

a, b, c = 1, 1, 1
X_hyp = a * np.cos(Phi) * np.sinh(Theta)
Y_hyp = b * np.sin(Phi) * np.sinh(Theta)
Z_hyp = c * np.sinh(Theta)

h = 0.5
phi_vals = np.linspace(0, 2, 50)
theta_vals = np.linspace(0, 4*np.pi, 50)
Phi_hel, Theta_hel = np.meshgrid(phi_vals, theta_vals)

X_hel = Phi_hel * np.cos(Theta_hel)
Y_hel = Phi_hel * np.sin(Theta_hel)
Z_hel = h * Theta_hel

l, m, n = 0.5, 0.5, 1
def f(theta):
    return np.sin(theta)

X_con = Phi * np.cos(Theta) + l * f(Theta)
Y_con = Phi * np.sin(Theta) + m * f(Theta)
Z_con = n * f(Theta)

fig = plt.figure(figsize=(16, 12))

ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X_par, Y_par, Z_par, cmap='viridis', alpha=0.8)
ax1.set_title('Параболид')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X_hyp, Y_hyp, Z_hyp, cmap='plasma', alpha=0.8)
ax2.set_title('Гиперболид')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

ax3 = fig.add_subplot(223, projection='3d')
ax3.plot_surface(X_hel, Y_hel, Z_hel, cmap='coolwarm', alpha=0.8)
ax3.set_title('Геликоид')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

ax4 = fig.add_subplot(224, projection='3d')
ax4.plot_surface(X_con, Y_con, Z_con, cmap='summer', alpha=0.8)
ax4.set_title('Коноид (f(θ) = sin θ)')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')

plt.tight_layout()
plt.show()

plt.savefig('figures.png',)