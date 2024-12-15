import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def model(x, a, b):
    return a * b**x / x

def solution_1(x, y):
    n = len(x)
    matrix = np.array([[n, sum(x)], [sum(x), sum(x*x)]])

    X = np.log(x)
    Y = np.log(y)

    right = np.array([sum(X) + sum(Y), sum(x*Y) + sum(x*X)]) 

    res = np.linalg.solve(matrix, right)
    res = np.exp(res)
    
    return res


def solution_2(x, y):
    result = curve_fit(model, x, y)[0]
    return result

x = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7], dtype=float)
y = np.array([7, 6, 6, 7, 8, 10, 13, 15, 19, 25, 33, 43, 54], dtype=float)

res1 = solution_1(x, y)
res2 = solution_2(x, y)

print(res1)
print(res2)