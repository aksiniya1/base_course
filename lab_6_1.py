import numpy as np
import matplotlib.pyplot as plt

def plot_hyperbola(x_limits, N, a=1, b=1, save_path=None):

    x_left = np.linspace(x_limits[0], -a, N // 2)
    x_right = np.linspace(a, x_limits[1], N // 2)
    
 
    y_left_upper = b * np.sqrt((x_left**2) / a**2 - 1)
    y_left_lower = -b * np.sqrt((x_left**2) / a**2 - 1)

    y_right_upper = b * np.sqrt((x_right**2) / a**2 - 1)
    y_right_lower = -b * np.sqrt((x_right**2) / a**2 - 1)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_left, y_left_upper, 'b', label='Верхняя ветвь (левая)')
    plt.plot(x_left, y_left_lower, 'b', label='Нижняя ветвь (левая)')
    plt.plot(x_right, y_right_upper, 'r', label='Верхняя ветвь (правая)')
    plt.plot(x_right, y_right_lower, 'r', label='Нижняя ветвь (правая)')
    
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title(f'Гипербола: $x^2/{a}^2 - y^2/{b}^2 = 1$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.axis('equal')
    plt.savefig('fig_4.png')
