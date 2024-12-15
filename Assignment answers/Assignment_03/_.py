import numpy as np
import matplotlib.pyplot as plt

errorValue = 10 ** (-15)
maxIterationCount = 100
delta = 10 ** (-5) # For modified secant method

f = lambda x: x*x - 4*x - (0.5**x) + 3
f_Derivative = lambda x: 2*x - 4 - (0.5**x) * np.log(0.5)

def calculateApproximatePercentRelativeError(currentValue, previousValue):
    if previousValue == None:
        return "-"
    return abs((currentValue - previousValue) / currentValue) * 100


def newtonRaphsonMethod(initialGuess):
    xn = initialGuess
    currentIteration = 0

    for i in range(maxIterationCount):
        f_n = f(xn)
        fD_n = f_Derivative(xn)
        currentIteration += 1
        
        if fD_n == 0:
            break
        xn_1 = xn - (f_n / fD_n)

        relativeError = calculateApproximatePercentRelativeError(xn_1, xn)
        print(f"NewtonRaphson, iteration: {currentIteration}, relative error: {relativeError} %")

        if abs(xn_1 - xn) < errorValue:
            return xn_1, currentIteration

        xn = xn_1
    print("Newton-Raphson method has failed!")
    return None

def secantMethod(x0, x1):
    xn_1 = x0
    xn = x1
    currentIteration = 0

    # xn means x(n)
    # xn_1 means x(n-1)
    # xn1 means x(n+1)
    
    for i in range(maxIterationCount):
        f_xn = f(xn)
        f_xn_1 = f(xn_1)
        currentIteration += 1
        xn1 = xn - ((f_xn * (xn_1 - xn)) / (f_xn_1 - f_xn))

        relativeError = calculateApproximatePercentRelativeError(xn1, xn)
        print(f"Secant, iteration: {currentIteration}, relative error: {relativeError} %")

 
        if abs(xn1 - xn) < errorValue:
            return xn1, currentIteration

        xn_1 = xn 
        xn = xn1 

    print("Secant method has failed!")
    return None 

def modifiedSecantMethod(initalGuess):
    xn = initalGuess
    currentIteration = 0

    for i in range(maxIterationCount):
        f_xn = f(xn)
        f_xn_delta = f(xn + delta)
        currentIteration += 1
        xn1 = xn - ((f_xn * delta) / (f_xn_delta - f_xn))

        relativeError = calculateApproximatePercentRelativeError(xn1, xn)
        print(f"ModifiedSecant, iteration: {currentIteration}, relative error: {relativeError} %")


        if abs(xn1 - xn) < errorValue:
            return xn1, currentIteration
        xn = xn1

    print("Modified Secant method has failed!")
    return None         



# ----------------------------------------------------------------------------- #

# Newton Raphson method part
resultFromNewtonRaphson, iterationCount1 = newtonRaphsonMethod(initialGuess=3.058) # Newton-Raphson part
print(f"*Result from Newton-Raphson method: {resultFromNewtonRaphson}, iterationCount: {iterationCount1}")

print(f"**Checking Newton Raphson method: {f(resultFromNewtonRaphson)}\n\n")

# ----------------------------------------------------------------------------- #

# Secant method part
resultFromSecantMethod, iterationCount2 = secantMethod(x0 = 3.058322957107139, x1 = 3.058322957107141)
print(f"*Result from Secant method: {resultFromSecantMethod}, iterationCount: {iterationCount2}")
print(f"**Checking Secant method: {f(resultFromSecantMethod)}\n\n")

# ----------------------------------------------------------------------------- #

# Modified Secant method part
resultFromModifiedSecantMethod, iterationCount3 = modifiedSecantMethod(initalGuess=3.058)
print(f"*Resulf from Modified Secant method: {resultFromModifiedSecantMethod}, iterationCount: {iterationCount3}")
print(f"**Checking Modified Secant method: {f(resultFromModifiedSecantMethod)}\n\n")

# ----------------------------------------------------------------------------- #

# Sketching the graph 

x = np.linspace(0.1, 5, 400)
y = f(x)
plt.plot(x, y, label=r'$x^2 - 4x + 0.5^x + 3$')
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.title('Graph of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

if resultFromNewtonRaphson is not None:
    plt.plot(resultFromNewtonRaphson, f(resultFromNewtonRaphson), 'ro', label='Newton-Raphson Root')
if resultFromSecantMethod is not None:
    plt.plot(resultFromSecantMethod, f(resultFromSecantMethod), 'go', label='Secant Root')
if resultFromModifiedSecantMethod is not None:
    plt.plot(resultFromModifiedSecantMethod, f(resultFromModifiedSecantMethod), 'bo', label='Modified Secant Root')

plt.legend()
plt.show()

# In the graph, the roots from each method overlaps
