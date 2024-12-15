# curve fitting with least squares
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def function(x, a, b):
    return a*x + b 

def solution_1(x, y):
    n = len(x)
    matrix = np.array([[sum(x**2), sum(x)], [sum(x), n]])
    right_hand_side = np.array([sum(x*y), sum(y)])
    result_list = np.linalg.solve(matrix, right_hand_side)

    return result_list

def solution_2(x, y):
    result_list = curve_fit(function, x, y)[0]
    return result_list

def graphical_part(x, y, predicted_values_for_y):
    plt.scatter(x, y, label="data")
    plt.plot(x, predicted_values_for_y, label="least squares")
    plt.grid()
    plt.legend()
    plt.show()


# ----------------------------------------------------------#
# Inputs
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([0.5, 0.6, 0.8, 1.0, 1.2, 1.7])
# ----------------------------------------------------------#



# ----------------------------------------------------------#
# Result 1
result_list__1 = solution_1(x, y)
print(f"Result list from solution 1:\n{result_list__1}\n")
# ----------------------------------------------------------#



# ----------------------------------------------------------#
# Result 2
result_list__2 = solution_2(x, y)
print(f"Result list from solution 2:\n{result_list__2}\n\n")
# ----------------------------------------------------------#



# ----------------------------------------------------------#
# Predicted values for y
predicted_values_for_y = function(x, *result_list__2)
print(f"Predicted values for y:\n{predicted_values_for_y}\n\n")
# ----------------------------------------------------------#



# ----------------------------------------------------------#
# Residuals
residuals = abs(y - predicted_values_for_y)
print(f"Residuals:\n{residuals}\n\n")
# ----------------------------------------------------------#



# ----------------------------------------------------------#
# Error Function (FI)
errorFunction = sum(residuals**2)
print(f"Error function:\n{errorFunction}\n\n")
# ----------------------------------------------------------#



# ----------------------------------------------------------#
# As mathematical function
print(f"f(x) ={result_list__2[0]:6.2g}*x +{result_list__2[1]:6.2g}", sep="")
# ----------------------------------------------------------#



# ----------------------------------------------------------#
# Graphical part
graphical_part(x, y, predicted_values_for_y)
# ----------------------------------------------------------#

