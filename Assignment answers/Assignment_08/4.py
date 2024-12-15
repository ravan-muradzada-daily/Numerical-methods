import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0
    
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= ((x - x_values[j]) / (x_values[i] - x_values[j]))
        
        result += p * y_values[i]
    
    return result

# Input part
x_values = np.array([0, 1, 2, 3, 4, 5], dtype=float)
y_values = np.array([0, 0.5, 0.8, 0.9, 0.941176, 0.961538], dtype=float)
y_searching = 0.85


#-----------------------------------------------------------#
# Finding the x using inversing the inputs technique.
print("\nTo find inverse, we need to reverse x_values and y_values when we send them to the function as parameters..")
calculated_result = lagrange_interpolation(y_values, x_values, y_searching)
print(f"\nCalculated result for x:\n{calculated_result:.3f}")



