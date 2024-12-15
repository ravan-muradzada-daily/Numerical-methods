import numpy as np
import matplotlib.pyplot as plt

def divided_differences(x_values, y_values):
    n = len(y_values)

    table = [[0 for i in range(n)]for i in range(n)]

    for i in range(n):
        table[i][0] = y_values[i]
    
    for j in range(1, n):
        for i in range(n-j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x_values[i+j] - x_values[i])

    coefficients = [table[0][i] for i in range(n)]

    return coefficients

def newton_interpolation(x_values, coefficients, x):
    n = len(x_values)

    result = coefficients[0]
    p = 1

    for i in range(1, n):
        p *= (x - x_values[i-1])
        result += coefficients[i] * p 
    
    return result

def sketch_graph(x_values, y_values, coefficients, x, f_x):
    plt.plot(x_values, y_values, "*b", label="The given data")
    plt.plot(x, f_x, "*r", label=f"x={x} and f(x)={f_x:.3f}")
    plt.title("Newton Interpolation")
    plt.xlabel('x')
    plt.ylabel('y')

    plt.grid(True)
    plt.legend()
    plt.show()

x_values = np.array([1.6, 2, 2.5, 3.2, 4, 4.5], dtype=float)
y_values = np.array([2, 8, 14, 15, 8, 2], dtype=float)
x = 2.8

coefficients = divided_differences(x_values, y_values)
print(f"Polynomial coefficients:\n{coefficients}\n\n")

calculated_result = newton_interpolation(x_values, coefficients, x)
print(f"Calculated f({x}) from interpolation:\n{calculated_result}")

sketch_graph(x_values, y_values, coefficients, x, calculated_result)


