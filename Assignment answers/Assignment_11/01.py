import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''

y' = -1.2y + 7 * e^(-0.3x)

'''

def f(x, y):
    return -1.2 * y + 7 * np.exp(-0.3 * x)

def euler_method(x0, y0, delta, target):
    x_values = np.arange(x0, target+delta, delta)
    n = len(x_values)
    y_values = np.zeros(n)
    y_values[0] = y0

    for i in range(1, n):
        x, y = x_values[i-1], y_values[i-1]

        dy_dx = f(x, y)

        y_values[i] = y + dy_dx * delta
    
    return x_values, y_values

def find_exact_solution(x_values, y_values):
    n = len(x_values)
    exact_solutions = np.zeros(n)
    error_values = np.zeros(n)

    for i in range(n):
        exact_solutions[i] = (70*np.exp(-0.3*x_values[i]) / 9.0) - (43 * np.exp(-1.2 * x_values[i]) / 9.0)
        error_values[i] = np.abs(exact_solutions[i] - y_values[i])

    return exact_solutions, error_values

x0, y0 = 0, 3
delta = 0.1
target = 2.5

x_values, y_values = euler_method(x0, y0, delta, target)
exact_solutions, error_values = find_exact_solution(x_values, y_values)

results = pd.DataFrame({
    'x:': x_values,
    'y_true:': exact_solutions,
    'y_Euler:': y_values,
    'abs_error:': error_values
})

print()
print(results)

plt.figure(figsize=(10, 6))

plt.plot(x_values, y_values, label='Euler method')
plt.plot(x_values, exact_solutions, label='Exact solution')

plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Euler method implementation')
plt.legend()
plt.grid(True)
plt.show()