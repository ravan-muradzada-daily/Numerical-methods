import numpy as np

def f(x):
    return np.sin(x) + x*x - 2*x + 3

def exact_derivative(x):
    return np.cos(x) + 2*x - 2


def forward_difference(x, h):
    return (f(x+h) - f(x)) / h

def backward_difference(x, h):
    return (f(x) - f(x-h)) / h

def central_difference(x, h):
    return (f(x+h) - f(x-h)) / (2*h)

def richardson_extrapolation(x, h, n):
    approximations = np.zeros([n, n])

    for i in range(n):
        approximations[i][0] = central_difference(x, h / (2**i))

    for j in range(1, n):
        for i in range(n):
            approximations[i][j] = approximations[i][j-1] + (approximations[i][j-1] - approximations[i-1][j-1]) / ((4**j) - 1)
    
    return approximations[-1][-1]

def calculate_true_relative_error(exact, approx):
    return np.abs((exact - approx) / exact) * 100

x, h = np.pi / 5, np.pi / 12
n = 5

results = {
        "Exact Derivative:": exact_derivative(x),
        "Forward Difference:": forward_difference(x, h),
       "Backward Difference:": backward_difference(x, h),
       "Central Difference:": central_difference(x, h),
       "Richardson Extrapolation:": richardson_extrapolation(x, h, n)      
}
exact_result = results["Exact Derivative:"]

for i in results:
    print(f"{i:26}\t{results[i]:8.4f}\t{calculate_true_relative_error(exact_result, results[i]):.3f} %")

