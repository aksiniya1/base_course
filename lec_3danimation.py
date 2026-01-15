import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
 
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
 
N = 100
edge = 10
phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, np.pi, 100)
 
def animate(R):

    x = R * np.outer(np.sin(phi), np.cos(theta))
    y = R * np.outer(np.sin(phi), np.sin(theta))
    z = R * np.outer(np.cos(phi), np.ones(np.size(theta)))
    return x, y, z
 
for i in range(N):
 
  ax.set_xlim3d([-edge, edge])
  ax.set_xlabel('X')
 
  ax.set_ylim3d([-edge, edge])
  ax.set_ylabel('Y')

  ax.set_zlim3d([-edge, edge])
  ax.set_zlabel('Z')
 
  x = animate(edge/N*i)[0]
  y = animate(edge/N*i)[1]
  z = animate(edge/N*i)[2]
  ax.plot_surface(x, y, z, color='b')
  plt.savefig(f'pic_{i}')

  images = []
filenames = [f'pic_{i}.png' for i in range(N)]
for filename in filenames:
  images.append(imageio.imread(filename))
  os.remove(filename)
imageio.mimsave('movie.gif', images)