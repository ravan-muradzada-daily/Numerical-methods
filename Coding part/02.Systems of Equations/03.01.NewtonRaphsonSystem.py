import numpy as np
from numpy.linalg import norm, inv

def f(X):
    x, y, z = X

    return np.array([
        x*x + y*y + z*z - 3,
        x*x + y*y - z - 1, 
        x + y + z - 3
    ])

def j(X):
    x, y, z = X

    return np.array([
        [2*x, 2*y, 2*z],
        [2*x, 2*y, -1],
        [1, 1, 1]
    ])

def newtonRaphson(InitialGuess, errorValue, maxIteration):
    X = InitialGuess

    for i in range(maxIteration):
        F = f(X)
        if norm(F) < errorValue:
            return X
        
        J = j(X)
        J_inv = inv(J)

        X = X - J_inv @ F 
    
    print("The process diverged in the given iteration count!")
    return None 

initialGuess = np.array([1.0, 0.0, 1.0])
errorValue = 1e-7
maxIteration = 20

result = newtonRaphson(initialGuess, errorValue, maxIteration)

print(result)

#Checking
print(f"Checking: {f(result)}")