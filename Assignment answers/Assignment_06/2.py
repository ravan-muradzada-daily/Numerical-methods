import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def model(x, a, b, c, d):
    return a * (x**3) + b * (x**2) + c * x + d

def solution_1(x, y):
    n = len(x)

    matrix = np.array([
        [sum(x**6), sum(x**5), sum(x**4), sum(x**3)], 

        [sum(x**5), sum(x**4), sum(x**3), sum(x**2)],
        
        [sum(x**4), sum(x**3), sum(x**2), sum(x)],

        [sum(x**3), sum(x**2), sum(x), n]])


    right_hand_side = np.array(
        [sum(y*(x**3)), sum(y*(x**2)), sum(y*x), sum(y)])
    

    result_list = np.linalg.solve(matrix, right_hand_side)

    return result_list

def solution_2(x, y):
    result_list = curve_fit(model, x, y)[0]

    return result_list

def sketch_graph(x, y, predicated_values_for_y, xn, yn):
    plt.scatter(x, y, label="data")
    plt.plot(x, predicated_values_for_y, label="least squares")
    plt.grid()
    plt.legend()
    plt.plot(xn, yn, "*r")
    plt.show()


# Inputs
x = np.array([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5])
y = np.array([-1, -0.7, 0.2, 1.5, 2.1, 3.2, 3.5, 3.6, 3.3, 
              3.6, 4.2, 5.7])


# Solution using Ax=B
result_list_1 = solution_1(x, y)
print(f"Parameters from solution 1:\n{result_list_1}\n\n")


# Solution using curve_fit model
result_list_2 = solution_2(x, y)
print(f"Parameters from solution 2:\n{result_list_2}\n\n")


# Predicted values for y
predicated_values_for_y = model(x, *result_list_2)


# Finding residuals
residuals = abs(predicated_values_for_y - y)
print(f"Residuals:\n{residuals}")


# Giving a value
xn = 1.2
yn = model(xn, *result_list_2)


#Sketching graph
sketch_graph(x, y, predicated_values_for_y, xn, yn)