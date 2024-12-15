import numpy as np
import pandas as pd

# y' = 1 - 2y^2 - x

def f(x, y):
    return 1 - 2 * y * y - x

# y'' = - 4 * y * y' - 1

def f_prime(x, y, y_prime):
    return -4 * y * y_prime - 1

def taylor_series_method(x0, y0, delta, target):
    x_values = np.arange(x0, target+delta, delta)
    n = len(x_values)
    y_values = np.zeros(n)
    y_values[0] = y0

    for i in range(1, n):
        x, y = x_values[i-1], y_values[i-1]

        dy_dx = f(x, y)
        d2y_dx2 = f_prime(x, y, dy_dx)

        y_values[i] = y + delta * dy_dx + (delta*delta / 2) * d2y_dx2
    
    return x_values, y_values

x0, y0 = 0, 1
delta = 0.1
target = 1

x_values, y_values = taylor_series_method(x0, y0, delta, target)

results = pd.DataFrame({
    't': x_values,
    '2nd Order Taylor': y_values,
})

print(results)