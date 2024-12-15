import numpy as np
from numpy.linalg import norm, inv
import matplotlib.pyplot as plt

errorValue = 1e-7
maximumIterationCount = 50

def f(X):
    x, y, z = X 

    return np.array([
        2*x + y + 2*z*z - 5,
        y*y*y + 4*z - 4,
        x*y + z - np.exp(z)
    ])

def j(X):
    x, y, z = X

    return np.array([
        [2, 1, 4*z],
        [0, 3*y*y, 4],
        [y, x, 1 - np.exp(z)]
    ])

def newtonRaphson(initalGuess):
    X = initalGuess

    for i in range(maximumIterationCount):
        F = f(X)
        if norm(F) < errorValue:
            print(f"Result has been foun in {i+1} iterations!")
            return X 
        J = j(X)
        J_inv = inv(J)

        X = X - J_inv @ F 
    
    print("Failed! The result cannot found in this iteration count!")
    return None

#------------------------------------------
# Newton Raphson method

initalGuess = [1.0, 1.0, 0.0]

result = newtonRaphson(initalGuess)

print(f"Results list: {result}\n\n")

#------------------------------------------
# Checking

print(f"Checking: {f(result)}")