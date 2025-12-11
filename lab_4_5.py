import numpy as np  
def area(figure, *arg):
    if figure == "circle":
        return np.pi * arg[0]**2
    elif figure == "triangle":
        return 0.5 * arg[0]* arg[1]
    else:
        return arg[0]**2
    
    S_circle = area ("triangle", 4, 7, 8)
    print(S_circle)