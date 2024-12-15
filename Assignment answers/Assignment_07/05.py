import numpy as np

def divided_differences(x_values, y_values):
    n = len(y_values)
    table = np.zeros((n, n))
    table[:, 0] = y_values


    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (x_values[i + j] - x_values[i])
    
    coefficients = [table[0][i] for i in range(n)]

    return coefficients


def newton_interpolation(x_values, coefficients, x):
    n = len(x_values)
    
    result = coefficients[0]
    p = 1
    for i in range(1, n):
        p *= (x - x_values[i - 1])
        result += p * coefficients[i]
    
    return result


x_values = np.array([0, 1, 2, 5.5, 11, 13, 16, 18])
y_values = np.array([0.5, 3.134, 5.3, 9.9, 10.2, 9.35, 7.2, 6.2])

x = 8

coefficients = divided_differences(x_values, y_values)

print(f"Coefficients:\n{coefficients}\n\n")

calculated_result = newton_interpolation(x_values, coefficients, x)
print(f"Calculated result:\n{calculated_result}")