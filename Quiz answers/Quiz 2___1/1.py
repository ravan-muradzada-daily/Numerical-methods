import numpy as np
from scipy.optimize import curve_fit

def model(x, a, b):
    return a*x / np.exp(b*x)

def solution_1(x, y):
    matrix = np.array([[len(x), sum(x)], [sum(x), sum(x*x)]])
    X = np.log(x)
    Y = np.log(y)
    right = np.array([sum(Y) - sum(X), sum(x*Y) - sum(x*X)])

    res = np.linalg.solve(matrix, right)

    return np.exp(res)

def solution_2(x, y):
    return curve_fit(model, x, y)[0]

x = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5], dtype=float)
y = np.array([12, 14, 15, 14, 13, 12, 11, 9, 8, 7, 6, 5], dtype=float)

res_1 = solution_1(x, y)
res_2 = solution_2(x, y)

print(res_1)
print(res_2)