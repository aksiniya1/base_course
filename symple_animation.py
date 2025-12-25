import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Создание пространства и подпространства для анимации
fig, ax = plt.subplots()

# Объект анимации
anim_object, = plt.plot([], [], '-', lw=2)

x, y = [], [] # Координаты объекта анимации
frames_interval = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(0, 2*np.pi) # Пределы изменения переменной Х
ax.set_ylim(-1, 1) # Пределы изменения переменной У

# Функция подстановки параметра в объект анимации
def update(frame):
    x.append(frame) # Расчет координаты Х
    y.append(np.sin(frame)) # Расчет координаты У
    
    # Передача координат объекту анимации
    anim_object.set_data(x, y)

    return anim_object


ani = FuncAnimation(fig, # Вызов пространства для анимации
                    update, # Вызов функции подстановки координат
                    frames=frames_interval, # Интервал значений
                    interval=50) # Интервал между кадрами,
                                 # по умолчанию 200 милисекунд

ani.save('animation_1.gif', writer="pillow")
