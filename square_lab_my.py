import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

total_frames = 100
fps = 30
cube_size = 1.0
initial_z = 0
jump_height = 3.0
rotation_speed = 180

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Прыгающий куб')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-0.5, 4)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.grid(False)

def create_cube(center=(0, 0, 0), size=1, rotation=0):
    vertices = np.array([
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ]) * size / 2
    
    if rotation != 0:
        theta = np.radians(rotation)
        rotation_matrix = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])
        vertices = vertices @ rotation_matrix.T
    
    vertices += np.array(center)
    
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[0], vertices[3], vertices[7], vertices[4]]
    ]
    
    return vertices, faces

face_colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

cube = Poly3DCollection([], alpha=0.8, linewidths=1, edgecolors='black')
for color in face_colors:
    cube.set_facecolor(color)
ax.add_collection3d(cube)

floor = Poly3DCollection([[
    [-2, -2, -0.01],
    [2, -2, -0.01],
    [2, 2, -0.01],
    [-2, 2, -0.01]
]], alpha=0.3, color='gray')
ax.add_collection3d(floor)

def jump_height_at_frame(frame):
    t = frame / total_frames
    if t < 0.5:
        return 4 * jump_height * t * (1 - t)
    else:
        return 4 * jump_height * t * (1 - t)

def init():
    cube.set_verts([])
    return cube,

def animate(frame):
    height = jump_height_at_frame(frame % total_frames)
    rotation = rotation_speed * (frame % total_frames) / total_frames
    
    vertices, faces = create_cube(
        center=(0, 0, initial_z + height),
        size=cube_size,
        rotation=rotation
    )
    
    cube.set_verts(faces)
    
    colors = []
    for i, color in enumerate(face_colors):
        factor = 0.8 + 0.2 * (height / jump_height)
        colors.append(color)
    cube.set_facecolor(colors)
    
    return cube,

ani = FuncAnimation(
    fig, 
    animate, 
    frames=total_frames * 3,
    init_func=init, 
    blit=True, 
    interval=1000/fps
)

plt.tight_layout()
plt.show()

try:
    ani.save('jumping_cube.gif', writer='pillow', fps=fps)
    print("Сохранено как 'jumping_cube.gif'")
except:
    print("Установите pillow: pip install pillow")