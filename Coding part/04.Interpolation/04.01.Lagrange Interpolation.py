import numpy as np

'''
    For each step we need to calculate the cardinal. So I have created a function which is called in each iteration to calculate cardinal properly.
'''

def calculate_cardinal(x_values, i, x):
    result = 1
    n = len(x_values)

    for j in range(n):
        if i != j:
            result *= ((x - x_values[j]) / (x_values[i] - x_values[j]))
        
    return result


def lagrange_interpolation(x_values, y_values, x):
    result  = 0
    n = len(x_values)

    for i in range(n):
        result += y_values[i] * calculate_cardinal(x_values, i, x)
    
    return result

x_values = np.array([1, 3, 5, 7, 13], dtype=float)
y_values = np.array([800, 2310, 3090, 3940, 4755], dtype=float)
y_to_interpolation = 4192.72705078125

calculated_result = lagrange_interpolation(y_values, x_values, y_to_interpolation)

print(calculated_result)