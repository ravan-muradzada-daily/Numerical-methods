import numpy as np

# Given data

x = np.array([1, 1.5, 1.6, 2.5, 3.5], dtype=float)
y = np.array([0.6767, 0.3734, 0.3261, 0.08422, 0.01596], dtype=float)

#----------------------------------------------------#
# Define the function and its true derivative

def f(x):
    return 5 * np.exp(-2 * x) * x

def true_derivative(x):
    return np.exp(-2 * x) * (5 - 10 * x)

#----------------------------------------------------#
# Numerical Differentiation Methods

def forward_difference(i):
    return (y[i+1] - y[i]) / (x[i+1] - x[i])
    

def backward_difference(i):
    return (y[i] - y[i-1]) / (x[i] - x[i-1])

def central_difference(i):
    return (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])


def calculate_true_percent_relative_error(exact, approx):
    return np.abs((exact - approx) / exact) * 100


print()
print("I tried to use mostly central difference, because it is the best one, when it is not available to use it, I used forward or backward difference.\n")

n = len(x)
for i in range(n):
    if i == 0:
        current_derivative_approximation = forward_difference(i)
    elif i  == n-1:
        current_derivative_approximation = backward_difference(i)
    else:
        current_derivative_approximation = central_difference(i)
    
    current_exact_value = true_derivative(x[i])
    current_true_percent_relative_error = calculate_true_percent_relative_error(current_exact_value, current_derivative_approximation)

    print(f"Estimation for the derivative when x={x[i]}: {current_derivative_approximation:.3f}")
    print(f"True percent relative error when x={x[i]}: {current_true_percent_relative_error:.3f} %\n\n")
