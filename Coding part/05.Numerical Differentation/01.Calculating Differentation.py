import numpy as np


'''
    Forward, Backward and Cetral Differences are the methods to calculate the derivative without needing analytical solution.
    The most preciese one is Central Difference, so if we are wanted the best one, we should use it.
'''

def f(x):
    return np.sin(x)

def exact_derivative(x):
    return np.cos(x)


def forward_difference(x, h):
    return (f(x+h) - f(x)) / h

def backward_difference(x, h):
    return (f(x) - f(x-h)) / h

def central_difference(x, h):
    return (f(x+h) - f(x-h)) / (2*h)

x, h = np.pi / 4, np.pi / 12


results = {
        "Exact Derivative:": exact_derivative(x),
        "Forward Difference:": forward_difference(x, h),
       "Backward Difference:": backward_difference(x, h),
       "Central Difference:": central_difference(x, h)           
}

for i in results:
   print(f"{i:20}\t{results[i]:.4f}")
