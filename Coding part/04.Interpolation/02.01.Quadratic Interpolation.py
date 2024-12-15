import numpy as np

exactValue = 0.69897

def f(x):
    return np.log10(x)

def quadratic_interpolation(x, x0, x1, x2):
    y0, y1, y2 = f(x0), f(x1), f(x2)
    b0 = y0

    b1 = (y1 - y0) / (x1 - x0)

    b2 = ((y2-y1) / (x2-x1) - b1) / (x2 - x0)

    f_x = b0 + b1 * (x - x0) + b2 * (x - x0) * (x - x1)

    return f_x

def find_relative_error(exactValue, calculatedValue):
    return (exactValue - calculatedValue)*100 / exactValue

x = 5

x0, x1, x2 = 3, 4, 6

result_1 = quadratic_interpolation(x, x0, x1, x2)
print(f"Result: {result_1}")
print(f"Relative error 1: {find_relative_error(exactValue, result_1)}\n\n")


x0, x1, x2 = 3.5, 4.5, 5.5
result_2 = quadratic_interpolation(x, x0, x1, x2)
print(f"Relative error 2: {find_relative_error(exactValue, result_2)}\n\n")
