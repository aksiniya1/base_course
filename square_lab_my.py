import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

total_frames = 200
fps = 30
cube_size = 1.0
room_size = 4.0  

gravity = -0.05
bounce_damping = 0.7
initial_velocity_z = 0.3

color_gradient = [
    (0.5, 0.5, 0.5, 1.0),    
    (0.9, 0.7, 0.7, 1.0),   
    (0.9, 0.5, 0.5, 1.0),   
    (0.9, 0.3, 0.3, 1.0),    
    (1.0, 0.0, 0.0, 1.0),    
    (1.0, 0.0, 0.2, 1.0),   
    (0.6, 0.0, 0.1, 1.0),   
    (0.4, 0.0, 0.1, 1.0),    
    (0.2, 0.0, 0.1, 1.0),    
    (0.1, 0.1, 0.1, 1.0),    
]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Прыгающий куб с изменением цвета при столкновениях')
ax.set_xlim(-room_size/2, room_size/2)
ax.set_ylim(-room_size/2, room_size/2)
ax.set_zlim(0, room_size)
ax.grid(True, alpha=0.3)

collision_count = 0
current_color_index = 0

cube_position = np.array([0.0, 0.0, cube_size/2], dtype=np.float64)
cube_velocity = np.array([
    np.random.uniform(-0.1, 0.1), 
    np.random.uniform(-0.1, 0.1),  
    initial_velocity_z             
], dtype=np.float64)

rotation_angles = np.array([0.0, 0.0, 0.0], dtype=np.float64)

def create_cube(center=(0, 0, 0), size=1, rotation_angles=(0, 0, 0)):
    """Создает вершины и грани куба с вращением"""
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
    
    rx, ry, rz = rotation_angles
    
    if rx != 0:
        cos_rx = np.cos(rx)
        sin_rx = np.sin(rx)
        Rx = np.array([
            [1, 0, 0],
            [0, cos_rx, -sin_rx],
            [0, sin_rx, cos_rx]
        ])
        vertices = vertices @ Rx.T
    
    if ry != 0:
        cos_ry = np.cos(ry)
        sin_ry = np.sin(ry)
        Ry = np.array([
            [cos_ry, 0, sin_ry],
            [0, 1, 0],
            [-sin_ry, 0, cos_ry]
        ])
        vertices = vertices @ Ry.T
    
    if rz != 0:
        cos_rz = np.cos(rz)
        sin_rz = np.sin(rz)
        Rz = np.array([
            [cos_rz, -sin_rz, 0],
            [sin_rz, cos_rz, 0],
            [0, 0, 1]
        ])
        vertices = vertices @ Rz.T
    
    vertices += np.array(center)
    
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # задняя
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # передняя
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # нижняя
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # верхняя
        [vertices[0], vertices[3], vertices[7], vertices[4]],  # левая
        [vertices[1], vertices[2], vertices[6], vertices[5]]   # правая
    ]
    
    return vertices, faces

def create_room(size=5.0):
    half_size = size / 2
    walls = []
    
    walls.append(Poly3DCollection([[
        [-half_size, -half_size, 0],
        [half_size, -half_size, 0],
        [half_size, half_size, 0],
        [-half_size, half_size, 0]
    ]], alpha=0.2, color='gray', edgecolors='black', linewidths=0.5))
    
    wall_alpha = 0.1
    wall_color = 'lightblue'
    
    walls.append(Poly3DCollection([[
        [-half_size, -half_size, 0],
        [half_size, -half_size, 0],
        [half_size, -half_size, size],[-half_size, -half_size, size]
    ]], alpha=wall_alpha, color=wall_color, linewidths=0.5))
    
    walls.append(Poly3DCollection([[
        [-half_size, half_size, 0],
        [half_size, half_size, 0],
        [half_size, half_size, size],
        [-half_size, half_size, size]
    ]], alpha=wall_alpha, color=wall_color, linewidths=0.5))
    
    walls.append(Poly3DCollection([[
        [-half_size, -half_size, 0],
        [-half_size, half_size, 0],
        [-half_size, half_size, size],
        [-half_size, -half_size, size]
    ]], alpha=wall_alpha, color=wall_color, linewidths=0.5))
    
    walls.append(Poly3DCollection([[
        [half_size, -half_size, 0],
        [half_size, half_size, 0],
        [half_size, half_size, size],
        [half_size, -half_size, size]
    ]], alpha=wall_alpha, color=wall_color, linewidths=0.5))
    
    return walls

room_walls = create_room(room_size)
for wall in room_walls:
    ax.add_collection3d(wall)

cube = Poly3DCollection([], alpha=0.8, linewidths=1, edgecolors='black')
cube.set_facecolor(color_gradient[current_color_index])
ax.add_collection3d(cube)

info_text = ax.text2D(0.02, 0.98, '', transform=ax.transAxes,
                      bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

def update_physics():
 
    global cube_position, cube_velocity, rotation_angles, collision_count, current_color_index
    
    cube_velocity[2] += gravity
    
    cube_position += cube_velocity
    
    rotation_speed = 0.1
    rotation_angles[0] += cube_velocity[2] * rotation_speed
    rotation_angles[1] += cube_velocity[0] * rotation_speed
    rotation_angles[2] += cube_velocity[1] * rotation_speed
    
    half_room = room_size / 2
    half_cube = cube_size / 2
    collision_happened = False
    
    if cube_position[0] - half_cube < -half_room:
        cube_velocity[0] = -cube_velocity[0] * bounce_damping
        cube_position[0] = -half_room + half_cube
        collision_happened = True
    elif cube_position[0] + half_cube > half_room:
        cube_velocity[0] = -cube_velocity[0] * bounce_damping
        cube_position[0] = half_room - half_cube
        collision_happened = True
    
    if cube_position[1] - half_cube < -half_room:
        cube_velocity[1] = -cube_velocity[1] * bounce_damping
        cube_position[1] = -half_room + half_cube
        collision_happened = True
    elif cube_position[1] + half_cube > half_room:
        cube_velocity[1] = -cube_velocity[1] * bounce_damping
        cube_position[1] = half_room - half_cube
        collision_happened = True
    
    if cube_position[2] - half_cube < 0: 
        cube_velocity[2] = -cube_velocity[2] * bounce_damping
        cube_position[2] = half_cube
        
       
        if abs(cube_velocity[2]) < 0.1:
            cube_velocity[2] = np.random.uniform(0.15, 0.3)
            cube_velocity[0] += np.random.uniform(-0.05, 0.05)
            cube_velocity[1] += np.random.uniform(-0.05, 0.05)
        
        collision_happened = True
    elif cube_position[2] + half_cube > room_size:  # Потолок
        cube_velocity[2] = -cube_velocity[2] * bounce_damping
        cube_position[2] = room_size - half_cube
        collision_happened = True
    
    if collision_happened:
        collision_count += 1
        current_color_index = collision_count % len(color_gradient)

    max_speed = 0.5
    speed = np.linalg.norm(cube_velocity)
    if speed > max_speed:
        cube_velocity = cube_velocity / speed * max_speed

def init():
  
    cube.set_verts([])
    info_text.set_text('')
    return cube, info_text

def animate(frame):
   

    update_physics()
    vertices, faces = create_cube(
        center=cube_position,
        size=cube_size,
        rotation_angles=rotation_angles
    )
    
    cube.set_verts(faces)
    
    cube.set_facecolor(color_gradient[current_color_index])
    
    info = (f"Столкновений: {collision_count}\n"
            f"Цвет: {current_color_index}\n"
            f"Позиция: ({cube_position[0]:.2f}, "
            f"{cube_position[1]:.2f}, {cube_position[2]:.2f})\n"
            f"Скорость: ({cube_velocity[0]:.2f}, "
            f"{cube_velocity[1]:.2f}, {cube_velocity[2]:.2f})")
    
    info_text.set_text(info)
    
    if frame % 5 == 0:
        ax.view_init(elev=20, azim=frame*0.5)
    
    return cube, info_text

ani = FuncAnimation(
    fig, 
    animate, 
    frames=total_frames * 10, 
    init_func=init, 
    blit=False, 
    interval=1000/fps,
    repeat=True
)

legend_text = "Цвета при столкновениях:\n"
for i, color in enumerate(color_gradient[:7]):
    color_names = ["Серый", "Еле роз.", "Розовый", "Св. красный", 
                   "Красный", "Ярк. красный", "Бордовый"]
    legend_text += f"{i}: {color_names[i]}\n"

ax.text2D(0.72, 0.98, legend_text, transform=ax.transAxes,
          fontsize=9, verticalalignment='top',
          bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

plt.tight_layout()

plt.show()

try:
    from matplotlib.animation import PillowWriter
    writer = PillowWriter(fps=fps)
    ani.save('jumping_cube_collisions.gif', writer=writer)
    print("Анимация сохранена как 'jumping_cube_collisions.gif'")
except Exception as e:
    print(f"Не удалось сохранить анимацию: {e}")
    print("Для сохранения установите: pip install pillow")
