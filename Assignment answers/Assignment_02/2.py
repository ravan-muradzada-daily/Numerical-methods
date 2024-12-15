import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * x * np.abs(np.cos(np.sqrt(x))) - 5

def checkStoppingCriteria(currVal, previousVal):
    if previousVal == None: return False
    return abs((currVal - previousVal) / currVal) < 0.01
        

def bisectionMethod(a, b):
    if f(a) * f(b) >= 0:
        print("Bisection method has failed!")
        return None
    mid = 0 # initialize
    previous = None

    while True:
        mid = (a + b) / 2.0
        fmid = f(mid)

        if checkStoppingCriteria(mid, previous):
            break

        if f(mid) == 0:
            # mid is exact root
            break
        elif f(a) * f(mid) > 0:
            a = mid
        else:
            b = mid
        previous = mid

    return mid

def sketchGraph():
    x = np.linspace(0.1, 5, 400)
    y = f(x)
    plt.plot(x, y, label=r'$x^2 \cdot |\cos \sqrt{x}| - 5$')
    plt.axhline(0, color='black', lw=2)
    plt.axvline(0, color='black', lw=2)
    plt.title('Graph of f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()


a, b = 0, 5

res = bisectionMethod(a, b)
sketchGraph()
print(f"\n\nResult: {res}")
print(f"\n\nChecking {f(res)}") # checking

