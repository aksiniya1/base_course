import numpy as np
import matplotlib.pyplot as plt

def plot_hyperbola(x_min, x_max, N, a=2, b=3):
  
    x_left = np.linspace(x_min, -a, N//2)
    x_right = np.linspace(a, x_max, N//2)
    
    
    y_left_upper = (b/a) * np.sqrt(x_left**2 - a**2)
    y_left_lower = -y_left_upper
    
    y_right_upper = (b/a) * np.sqrt(x_right**2 - a**2)
    y_right_lower = -y_right_upper
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_left, y_left_upper, 'b', label='Ветвь +')
    plt.plot(x_left, y_left_lower, 'b')
    plt.plot(x_right, y_right_upper, 'r', label='Ветвь +')
    plt.plot(x_right, y_right_lower, 'r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Гипербола: $x^2/{a}^2 - y^2/{b}^2 = 1$')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.axis('equal')
    plt.show()


plot_hyperbola(-5, 5, 500)