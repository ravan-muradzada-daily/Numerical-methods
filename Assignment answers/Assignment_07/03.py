import numpy as np
import matplotlib.pyplot as plt

def divided_difference(x_values, y_values):
    n = len(x_values)

    table = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        table[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n-j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x_values[i+j] - x_values[i])

    coefficients = [table[0][i] for i in range(n)]
    
    return coefficients

def newton_interpolation(x_values, y_values, x):
    coefficients = divided_difference(x_values, y_values)
    n = len(x_values)

    result = coefficients[0]
    p = 1

    for i in range(1, n):
        p *= (x - x_values[i-1])
        result += p * coefficients[i]
    
    return result



x_values = np.array([0, 1.8, 5, 6, 8.2, 9.2, 12])
y_values = np.array([26, 16.415, 5.375, 3.5, 2.015, 2.54, 8])
x = 3.5

calculated_result = newton_interpolation(x_values, y_values, x)
print(f"Calculated result: {calculated_result}")

x_interval = np.linspace(min(x_values), max(x_values), 500)
y_interval = np.array([newton_interpolation(x_values, y_values, x_i) for x_i in x_interval])

plt.plot(x_interval, y_interval, color="green", label="Interpolation Polynomial")


plt.plot(x_values, y_values, "*r", label="Given data")
plt.plot(x, calculated_result, "*b", label=f"x={x} and f(x)={calculated_result}")

plt.grid(True)
plt.legend()
plt.show()