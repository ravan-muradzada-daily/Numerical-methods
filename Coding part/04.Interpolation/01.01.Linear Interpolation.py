import numpy as np

exactValue = 0.69897

def f(x):
    return np.log10(x)

def linear_interpolation(x, x0, x1):
    f_x = f(x0) + ((f(x1) - f(x0)) / (x1 - x0)) * (x - x0)

    return f_x
def find_relative_error(exactValue, calculatedValue):
    return (exactValue - calculatedValue)*100 / exactValue

result_1 = linear_interpolation(5, 4, 6) # Using 4 and 6
print(f"Result 1: {result_1}")
print(f"Relative error 1: {find_relative_error(exactValue, result_1)}\n\n")


result_2 = linear_interpolation(5, 4.5, 5.5) # Using 4.5 and 5.5
print(f"Result 2: {result_2}")
print(f"Relative error 2: {find_relative_error(exactValue, result_2)}")