import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig1, ax1 = plt.subplots(figsize=(8, 8))
fig1.patch.set_facecolor('black')
ax1.set_facecolor('black')

t1 = np.linspace(0, 12*np.pi, 3000)
common_term = np.exp(np.cos(t1)) - 2*np.cos(4*t1) + (np.sin(t1/12))**5
x1 = np.sin(t1) * common_term
y1 = np.cos(t1) * common_term

ax1.set_xlim(-5, 5)
ax1.set_ylim(-5, 5)
ax1.set_title('Анимация бабочки', fontsize=16, color='pink', pad=20)
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)


colors1 = plt.cm.rainbow(np.linspace(0, 1, len(t1)))


scatter1 = ax1.scatter([], [], s=30, alpha=0.7)
line1, = ax1.plot([], [], lw=1.5, color='cyan', alpha=0.8)

def init1():
    scatter1.set_offsets(np.empty((0, 2)))
    line1.set_data([], [])
    return scatter1, line1

def animate1(i):
    idx = i * 20
    if idx > len(t1):
        idx = len(t1)
    
    scatter1.set_offsets(np.column_stack([x1[:idx], y1[:idx]]))
    scatter1.set_color(colors1[:idx])
    scatter1.set_sizes([30] * idx)
    
    line1.set_data(x1[:idx], y1[:idx])
    return scatter1, line1

ani1 = animation.FuncAnimation(fig1, animate1, init_func=init1,
                              frames=150, interval=20, blit=True)


fig2, ax2 = plt.subplots(figsize=(8, 8))
fig2.patch.set_facecolor('black')
ax2.set_facecolor('black')

t2 = np.linspace(0, 2*np.pi, 1000)
x2 = 16 * (np.sin(t2) ** 3)
y2 = 13*np.cos(t2) - 5*np.cos(2*t2) - 2*np.cos(3*t2) - np.cos(4*t2)

ax2.set_xlim(-20, 20)
ax2.set_ylim(-20, 20)
ax2.set_title('Анимация сердца', fontsize=16, color='red', pad=20)
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)

colors2 = plt.cm.Reds(np.linspace(0.3, 1, len(t2)))

scatter2 = ax2.scatter([], [], s=40, alpha=0.8)
line2, = ax2.plot([], [], lw=2, color='#FF2255', alpha=0.9)

def init2():
    scatter2.set_offsets(np.empty((0, 2)))
    line2.set_data([], [])
    return scatter2, line2

def animate2(i):
    idx = i * 10
    if idx > len(t2):
        idx = len(t2)
    
    scatter2.set_offsets(np.column_stack([x2[:idx], y2[:idx]]))
    scatter2.set_color(colors2[:idx])
    scatter2.set_sizes([40] * idx)
    
    line2.set_data(x2[:idx], y2[:idx])
    return scatter2, line2

ani2 = animation.FuncAnimation(fig2, animate2, init_func=init2,
                              frames=100, interval=30, blit=True)

plt.show()
ani1.save('animation_7.gif', writer="pillow")
ani2.save('animation_6.gif', writer="pillow")