import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Functions
#------------------------------------------------------------#

def solution_2(model, x, y):
    result_list = curve_fit(model, x, y)[0]

    return result_list

# For model 1:

def model_1(x, a, b, c):
    return a * np.cos(x) + b * np.exp(x) + c

def solution_1__for_model_1(x, y): # Ax = B
    n = len(x)

    matrix = np.array([[sum(np.cos(x)**2), sum(np.cos(x)*np.exp(x)), sum(np.cos(x))], 
            [sum(np.cos(x)*np.exp(x)), sum(np.exp(2*x)), sum(np.exp(x))],[sum(np.cos(x)), sum(np.exp(x)), n]])

    right_hand_side = np.array([sum(y*np.cos(x)), sum(y*np.exp(x)), sum(y)])

    result_list = np.linalg.solve(matrix, right_hand_side)

    return result_list



# For model 2:

def model_2(x, a, b, c, d):
    return a * (x**3) + b * (x**2) + c * x + d

def solution_1__for_model_2(x, y):
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



# For model 3:

def model_3(x, a, b, c):
    return a + b * np.sin(x) + c * (x**3)

def solution_1__for_model_3(x, y):
    n = len(x)

    matrix = np.array([
            [n, sum(np.sin(x)), sum(x**3)],
            [sum(np.sin(x)), sum(np.sin(x)**2), sum((x**3)*np.sin(x))],
            [sum(x**3), sum((x**3) * np.sin(x)), sum(x**6)]
        ])


    right_hand_side = np.array(
        [sum(y), sum(y * np.sin(x)), sum(y * (x**3))])
    
    result_list = np.linalg.solve(matrix, right_hand_side)

    return result_list


#------------------------------------------------------------#

# Inputs:

x = np.array([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5])
y = np.array([-1, -0.7, 0.2, 1.5, 2.1, 3.2, 3.5, 3.6, 3.3, 
              3.6, 4.2, 5.7])

xn = 1.2
plt.scatter(x, y, label="input data")
plt.grid()

#------------------------------------------------------------#


# Solution for model 1:
print("For Model 1:\n")
# Solution using Ax=B
result_list_1__for_model_1 = solution_1__for_model_1(x, y)
print(f"Parameters from solution 1:\n{result_list_1__for_model_1}\n\n")


# Solution using curve_fit model
result_list_2__for_model_1 = solution_2(model_1, x, y)
print(f"Parameters from solution 2:\n{result_list_2__for_model_1}\n\n")


# Predicted values for y
predicated_values_for_y__for_model_1 = model_1(x, *result_list_2__for_model_1)


# Finding residuals
residuals__for_model_1 = abs(predicated_values_for_y__for_model_1 - y)
print(f"Residuals: {residuals__for_model_1}\n\n")


# Giving a value
yn__for_model_1 = model_1(xn, *result_list_2__for_model_1)

plt.plot(x, predicated_values_for_y__for_model_1, label="model 1")
plt.plot(xn, yn__for_model_1, "*r", label = "model 1, when xn = 1.2")




#------------------------------------------------------------#


# Solution for model 2:
print("For Model 2:\n")

# Solution using Ax=B
result_list_1__for_model_2 = solution_1__for_model_2(x, y)
print(f"Parameters from solution 1:\n{result_list_1__for_model_2}\n\n")


# Solution using curve_fit model
result_list_2__for_model_2 = solution_2(model_2, x, y)
print(f"Parameters from solution 2:\n{result_list_2__for_model_2}\n\n")


# Predicted values for y
predicated_values_for_y__for_model_2 = model_2(x, *result_list_2__for_model_2)


# Finding residuals
residuals__for_model_2 = abs(predicated_values_for_y__for_model_2 - y)
print(f"Residuals:\n{residuals__for_model_2}\n\n")


# Giving a value
yn__for_model_2 = model_2(xn, *result_list_2__for_model_2)

plt.plot(x, predicated_values_for_y__for_model_2, label="model 2")
plt.plot(xn, yn__for_model_2, "*b",  label = "model 2, when xn = 1.2")


#------------------------------------------------------------#

# Solution for model 3:
print("For Model 3:\n")

# Solution using Ax=B
result_list_1__for_model_3 = solution_1__for_model_3(x, y)
print(f"Parameters from solution 1:\n{result_list_1__for_model_3}\n\n")


# Solution using curve_fit model
result_list_2__for_model_3 = solution_2(model_3, x, y)
print(f"Parameters from solution 2:\n{result_list_2__for_model_3}\n\n")


# Predicted values for y
predicated_values_for_y__for_model_3 = model_3(x, *result_list_2__for_model_3)


# Finding residuals
residuals__for_model_3 = abs(predicated_values_for_y__for_model_3 - y)
print(f"Residuals:\n{residuals__for_model_3}")

plt.plot(x, predicated_values_for_y__for_model_3, label="model 3")


#------------------------------------------------------------#

plt.legend()
plt.show()

#------------------------------------------------------------#


print("\n\nFrom the graph, it can be easily said that the first model is the best.\n\n")

FI_1 = sum(residuals__for_model_1**2)
FI_2 = sum(residuals__for_model_2**2)
FI_3 = sum(residuals__for_model_3**2)

print(f"If we calculate erorr functions, we can say the first model is the best, too: \n\nF1={FI_1}\nF2={FI_2}\nF3={FI_3}")