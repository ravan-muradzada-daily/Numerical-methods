import numpy as np

#---------------------------------------------------#
# Functions

def f(x):
    return np.sin(x)

def forward_difference(x, h):
    return (f(x+h) - f(x)) / h

def backward_difference(x, h):
    return (f(x) - f(x-h)) / h

def central_difference(x, h):
    return (f(x+h) - f(x-h)) / (2*h)

def calculate_exact_result(x):
    return np.cos(x)

def calculate_true_percent_relative_error(exact, approx):
    return np.abs((exact - approx) / exact) * 100

#---------------------------------------------------#
# Input data

x = np.pi / 4
h = np.pi / 12
exact_value = calculate_exact_result(x)
print(f"\nExact value: {exact_value:.3f}\n\n")

#---------------------------------------------------#
# Forward difference

estimation_1 = forward_difference(x, h)
error_1 = calculate_true_percent_relative_error(exact_value, estimation_1)

print(f"Estimation using Forward Difference: {estimation_1:.3f}")
print(f"Error in Forward Difference: {error_1:.3f} %\n\n")

#---------------------------------------------------#
# Backward difference

estimation_2 = backward_difference(x, h)
error_2 = calculate_true_percent_relative_error(exact_value, estimation_2)

print(f"Estimation using Bakward Difference: {estimation_2:.3f}")
print(f"Error in Bakward Difference: {error_2:.3f} %\n\n")

#---------------------------------------------------#
# Central difference

estimation_3 = central_difference(x, h)
error_3 = calculate_true_percent_relative_error(exact_value, estimation_3)

print(f"Estimation using Central Difference: {estimation_3:.3f}")
print(f"Error in Central Difference: {error_3:.3f} %\n\n")