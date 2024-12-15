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

#----------------------------------------------------#
# Input data

x_values = np.array([1, 4, 6], dtype=float)
y_values = np.array([0, 1.386294, 1.791760], dtype=float)
x = 2

#----------------------------------------------------#
# Calculating results and print them

calculated_result_order_1 = lagrange_interpolation(x_values[:-1], y_values[:-1], x)

calculated_result_order_2 = lagrange_interpolation(x_values, y_values, x)


print(f"Calculated result from order 1: {calculated_result_order_1}\n\n")

print(f"Calculated result from order 2: {calculated_result_order_2}\n\n")

#----------------------------------------------------#
# Sketching the graph

plt.plot(x_values, y_values, "bo", label="Given data")
plt.plot(x, calculated_result_order_1, "*r", label="Calculated data from order 1")
plt.plot(x, calculated_result_order_2, "*g", label="Calculated data from order 2")

plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Lagrange Interpolation')
plt.legend()
plt.show()