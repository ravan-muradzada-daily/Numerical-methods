import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''

    y' = y^3 + 2
    y'' = 3*y^2 * y'

'''
def f(x, y):
    return y**3 + 2

def f_prime(x, y, y_prime):
    return 3 * y * y * y_prime

def taylor_series_method(x0, y0, delta, target):
    x_values = np.arange(x0, target+delta, delta)
    n = len(x_values)
    y_values = np.zeros(n)
    y_values[0] = y0

    for i in range(1, n):
        x, y = x_values[i-1], y_values[i-1]

        dy_dx = f(x, y)
        d2y_dx2 = f_prime(x, y, dy_dx)

        y_values[i] = y + dy_dx * delta + d2y_dx2 * delta * delta / 2

    return x_values, y_values

x0, y0 = 0, 3
target = 4
delta = 0.2

x_values, y_values = taylor_series_method(x0, y0, delta, target)

results = pd.DataFrame({
    'x:': x_values,
    '2nd Order Taylor: ': y_values
})

print()
print(results)

plt.figure(figsize=(10, 6))


plt.plot(x_values, y_values, label="Second Order Taylor Series Method",color="red")
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Taylor series method implementation')

plt.legend()
plt.grid(True)
plt.show()