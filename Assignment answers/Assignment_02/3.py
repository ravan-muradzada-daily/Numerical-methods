import numpy as np
import matplotlib.pyplot as plt

exactRoot = 5.60979
trueErrors, estimatedErrors = [], []
allApproximations = []

def f(x):
    return (x**4) - 8 * (x**3) - 35 * x**2 + 450 * x -1001
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
    previous = None
    mid = 0
    for i in range(iterationCount):
        mid = (a + b) / 2.0
        fMid = f(mid)
        allApproximations.append(mid)
        trueErrors.append(FindTrueAbsolutePercentRelativeError(mid))
        estimatedErrors.append(FindEstimatedAbsolutePercentRelativeError(mid, previous))

        f_a, f_b = f(a), f(b)
        if fMid == 0:
            # mid is exact root
            break
        elif f_a * fMid > 0:
            a = mid
        else:
            b = mid 

        previous = mid

    return mid 

def sketchGraph():
    x = np.linspace(4, 6.5, 400)
    y = f(x)
    plt.plot(x, y, label=r'$f(x) = x^4 - 8x^3 - 35x^2 + 450x - 1001$', color='blue')

    plt.axhline(0, color='black', lw=2)
    plt.axvline(exactRoot, color='green', linestyle='--', label=f'True Root: {exactRoot}')

    plt.scatter(allApproximations, [f(mid) for mid in allApproximations], color = "red", label='Bisection Iterations', zorder=5)

    plt.title('Graph of f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

a, b = 4.5, 6
iterationCount = 5

result = bisectionMethod(a, b, iterationCount)

for i in range(len(trueErrors)):
    print(f"Iteration: {i}, True error: {trueErrors[i]}, Estimated error: {estimatedErrors[i]}")

print(f"\n\nResult: {result}")

sketchGraph()