import numpy as np
from numpy.linalg import norm, inv
import matplotlib.pyplot as plt

errorValue = 1e-4

def f(X):
    x, y = X
    return np.array([
        x*x - y + x * np.cos(np.pi * x),
        y*x + np.exp(-x) - (1/x) 
    ])

def j(X):
    x, y = X

    return np.array([
        [2*x + np.cos(np.pi * x) - np.pi * x * np.sin(np.pi * x), -1],
        [y - np.exp(-x) + 1/(x*x), x]
    ]) 


def newtonRaphson(initalGuess):
    X = initalGuess
    iterationCounter = 0
    while True:
        F = f(X)
        iterationCounter += 1
        if norm(F) < errorValue:
            print(f"Iteration count is {iterationCounter}")
            return X 
        
        J = j(X)
        J_inv = inv(J)
        X = X - J_inv @ F
    
    return None 

intialGuess = np.array([
    1.25, 0.75
])

#------------------------------------------
# Newton Raphson result

result = newtonRaphson(intialGuess)

print(result)

#------------------------------------------
#Checking

print(f"Checking: {f(result)}")

#------------------------------------------

def sketchGraph():
    def f1(x):
       return x**2 + x * np.cos(np.pi * x)  

    def f2(x):
        return (1/x*x) - np.exp(-x)/x

    x_values = np.linspace(0.1, 10, 100)  

    y1_values = f1(x_values)
    y2_values = f2(x_values)

    plt.plot(x_values, y1_values, label='y = x^2 + x cos(πx)', color='blue')
    plt.plot(x_values, y2_values, label='y = (e^(-x) / x) - (1 / x^2)', color='orange')
    x_root, y_root = result[0], result[1]
    plt.plot(x_root, y_root, 'ro',
             label =f'root: ({x_root:.3f}, {y_root:.3f})')

    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.axvline(0, color='black', lw=0.5, ls='--')
    plt.title('Graphical Representation of Nonlinear Equations')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.xlim(0, 5)
    plt.ylim(-5, 5)  
    plt.show()

#------------------------------------------
# Sketching graph

# If you want to sketch the graph, you should use newtonRaphson method,
# because I have used roots from the method in the graph. 

sketchGraph()