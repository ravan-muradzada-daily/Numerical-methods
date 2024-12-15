import numpy as np
from random import randint

def f(x):
    return np.sin(x) + np.cos(x) + x*x + 4

def divided_differences(x_values, y_values):
    n = len(y_values)

    table = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        table[i][0] = y_values[i]
    
    for j in range(1, n):
        for i in range(n-j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x_values[i+j] - x_values[i])
    
    b = [table[0][i] for i in range(n)]

    return b

def newton_interpolation_method(x_values, y_values, x):
    b = divided_differences(x_values, y_values)
    n = len(x_values)
    result = b[0]

    p = 1
    for i in range(1, n):
        p *= (x - x_values[i-1])
        result += b[i] * p 

    return result

def find_relative_error(exactValue, calculatedValue):
    return abs(exactValue - calculatedValue)*100 / exactValue

x_values = np.array([1, 2, 3, 4, 5])
y_values = np.array([1, 8, 27, 64, 125])

x = 3.5 
exact_root = 42.875

result = newton_interpolation_method(x_values, y_values, x)

print(f"Calculated result: {result}")
print(f"Relative error: {find_relative_error(exact_root, result)} %")