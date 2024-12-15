import numpy as np
import matplotlib.pyplot as plt

exactRoot = 5.62859017617954 # max exact root
trueErrors, estimatedErrors = [], []

def f(x):
    return -0.6 * (x**2) + 2.4 * x + 5.5


def FindEstimatedAbsolutePercentRelativeError(currVal, previousVal): # For estimated error
    if previousVal == None: 
        return "-" 
    else:
        return abs((currVal - previousVal) / currVal) * 100

def FindTrueAbsolutePercentRelativeError(approximateValue): # For true error
    return abs((exactRoot - approximateValue) / exactRoot) * 100

def bisectionMethod(a, b, iterationCount):
    if f(a) * f(b) >= 0:
        print("Bisection method has failed!")
        return None
    mid = 0 # initialize

    previous = None

    for i in range(iterationCount):
        mid = (a + b) / 2.0
        fmid = f(mid)
        
        trueErrors.append(FindTrueAbsolutePercentRelativeError(mid))

        estimatedErrors.append(FindEstimatedAbsolutePercentRelativeError(mid, previous))

        if f(mid) == 0:
            # mid is exact root
            break
        elif f(a) * fmid > 0:
            a = mid
        else:
            b = mid

        previous = mid

    return mid

def graphicalPart():
    x = np.linspace(-10, 15, 400)
    y = f(x)

    plt.plot(x, y, label = 'f(x) = -0.6x^2 - 2.4x + 5.5',color='blue')

    plt.axhline(0, color='black', lw=2)
    plt.axvline(0, color='black', lw=2)
    plt.title('Graph of f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.scatter(exactRoot, 0, color='red', zorder=5, label=f'Highest root: {exactRoot:.5f}')
    plt.legend()
    plt.show()

a, b = 5, 10
iterationCount = 3

result = bisectionMethod(a, b, iterationCount)
graphicalPart()

for i in range(len(trueErrors)):
    print(f"Iteration: {i}, True Error: {trueErrors[i]}, Estimated Error: {estimatedErrors[i]}")

print(f"\n\nResult is {result}")