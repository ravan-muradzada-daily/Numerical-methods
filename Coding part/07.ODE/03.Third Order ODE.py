import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# y' = 1 - 2 * y**2 - x
# y'' = -4 * y * y' - 1
# y''' = -4 * (y' * y' + y * y'')

# y(x+h) = y(x) + y'(x) * delta + y''(x) * (delta^2 / 2!) + y'''(x) * (delta^3 / 3!)

def f(x, y):
    return 1 - 2 * y * y - x

def f_prime(x, y, y_prime):
    return -4 * y * y_prime - 1

def f_double_prime(x, y, y_prime, y_pr_pr):
    return -4 * (y_prime**2 + y * y_pr_pr)

def taylor_series_method(x0, y0, delta, target):
    x_values = np.arange(x0, target+delta, delta)
    n = len(x_values)
    y_values = np.zeros(n)
    y_values[0] = y0

    for i in range(1, n):
        x, y = x_values[i-1], y_values[i-1]

        dy_dx = f(x, y)
        d2y_dx2 = f_prime(x, y, dy_dx)
        d3y_dx3 = f_double_prime(x, y, dy_dx, d2y_dx2)

        y_values[i] = y + dy_dx * delta + d2y_dx2 * (delta*delta / 2.0) + d3y_dx3 * (delta**3 / 6)

    return x_values, y_values

x0, y0 = 0, 1
delta = 0.1
target = 1
x_values, y_values = taylor_series_method(x0, y0, delta, target)

results = pd.DataFrame({
    'x:': x_values,
    '3rd Order Taylor': y_values
})

print(results)