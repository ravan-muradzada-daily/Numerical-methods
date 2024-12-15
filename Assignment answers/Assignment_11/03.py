import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# y' = x^2 * y - y
# y'' = 2x * y + x^2 * y' - y'
# y'''= 2 * y + 4xy' + x^2 *y'' - y''

def f(x, y):
    return x*x * y - y

def f_prime(x, y, y_prime):
    return 2 * x * y + x * x * y_prime - y_prime

def f_double_prime(x, y, y_pr, y_pr_pr):
    return 2 * y + 4 * x * y_pr + x * x * y_pr_pr - y_pr_pr


def taylor_series_method(x0, y0, delta, target):
    x_values = np.arange(x0, target+delta, delta)
    n = len(x_values)
    y_values_2nd = np.zeros(n)
    y_values_3rd = np.zeros(n)

    y_values_2nd[0] = y_values_3rd[0] = y0

    for i in range(1, n):
        x, y_2nd, y_3rd = x_values[i-1], y_values_2nd[i-1], y_values_3rd[i-1]

        # Second Order
        dy_dx = f(x, y_2nd)
        d2y_dx2 = f_prime(x, y_2nd, dy_dx)
        y_values_2nd[i] = y_2nd + dy_dx * delta + d2y_dx2 * delta * delta / 2

        # Third Order
        dy_dx = f(x, y_3rd)
        d2y_dx2 = f_prime(x, y_3rd, dy_dx)
        d3y_dx3 = f_double_prime(x, y_3rd, dy_dx, d2y_dx2)
        y_values_3rd[i] = y_3rd + dy_dx * delta + d2y_dx2 * delta * delta / 2 + d3y_dx3 * (delta**3) / 6

    return x_values, y_values_2nd, y_values_3rd

x0, y0 = 0, 1
delta = 0.1
target = 1

x_values, y_values_2nd, y_values_3rd = taylor_series_method(x0, y0, delta, target)

results = pd.DataFrame({
    'x:': x_values,
    '2nd Order: ': y_values_2nd,
    '3rd Order:': y_values_3rd
})

print()
print(results)

plt.figure(figsize=(10, 6))

plt.plot(x_values, y_values_2nd, label="Second Order Taylor Method")
plt.plot(x_values, y_values_3rd, label="Third Order Taylor Method")

plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Taylor Method Implementation')

plt.legend()
plt.grid(True)
plt.show()