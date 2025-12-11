import numpy as np

def multiply_array_elements(arr):
    
    return np.prod(arr) 

arr1 = np.array([2, 3, 4])
result1 = multiply_array_elements(arr1)
print(f"Массив: {arr1}")
print(f"Произведение элементов: {result1}")
