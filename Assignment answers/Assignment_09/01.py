import numpy as np

#---------------------------------------------------#
# Functions

def f(x):
    return (-0.1 * (x**4) - 0.15 * (x**3) - 0.5 * x * x - 0.25*x + 1.2)

def FI(x, h):
    return (f(x+h) - f(x-h)) / (2*h)

def richardson_extrapolation(x, h, n):
    approximations = np.zeros([n, n])

    for i in range(n):
        approximations[i][0] = FI(x, h / (2**i))
    
    for j in range(1, n):
        for i in range(n):
            approximations[i][j] = approximations[i][j-1] + ((approximations[i][j-1] - approximations[i-1][j-1]) / ((4**j) - 1))

    return approximations[-1][-1]


#---------------------------------------------------#
# Input data

x = 0.5
h1 = 0.5
h2 = 0.25
n = 4
exact_value = -0.9125

#---------------------------------------------------#
# Central Differences

central_difference_h1 = FI(x, h1)
central_difference_h2 = FI(x, h2)

print(f"\nCentral difference when h1 = {h1}: {central_difference_h1}")
print(f"Central difference when h2 = {h2}: {central_difference_h2}\n\n")

#---------------------------------------------------#
# Richardson extrapolation for h1

estimation_h1 = richardson_extrapolation(x, h1, n)
error_h1 = abs((exact_value - estimation_h1) / exact_value) * 100

print(f"Result from h = {h1}: {estimation_h1}")
print(f"True Percent Relative Error when h = {h1}: {error_h1} %\n\n")

#---------------------------------------------------#
# Richardson extrapolation for h2

estimation_h2 = richardson_extrapolation(x, h2, n)
error_h2 = abs((exact_value - estimation_h2) / exact_value) * 100
print(f"Result from h = {h2}: {estimation_h2}")
print(f"True Percent Relative Error when h = {h2}: {error_h2} %\n\n")

#---------------------------------------------------#
# Exact result

print(f"Exact result: {exact_value}\n")
