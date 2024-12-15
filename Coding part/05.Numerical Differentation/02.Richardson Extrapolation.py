import numpy as np


'''
    Richardson Extrapolation is better version to approximate the derivative without having analytical solution. We need to have central difference to implement this algorithm.

    Step by step, we will approach the most exact result for our needings.
    We always use matrix to keep the approximation and then we select matrix[-1][-1] to get the better one.

    Imagine, we are given n, which represent matrix parameters, so our matrix is nxn. (It should be square matrix).
    Let's name the matrix "D".
    We will use central difference function, so let's name it "fc" function.

    Before all, we should fill the first column of the matrix:
    D[i][0] = fc(h / 2^i)
    
    To find other elements, we will use this formula:

    D[i][j] = D[i][j-1] + (D[i][j-1] - D[i-1][j-1]) / (4^j - 1)

    After all, we need to take D[-1][-1].
'''
def f(x):
    return np.sin(x)

def central_difference(x, h):
    return (f(x+h) - f(x-h)) / (2*h)

def richardson_extrapolation(x, h, n):
    approximations = np.zeros([n, n])

    for i in range(n):
        approximations[i][0] = central_difference(x, h / (2**i))

    for j in range(1, n): # Represents columns
        for i in range(n): # Represents rows
            approximations[i][j] = approximations[i][j-1] + (approximations[i][j-1] - approximations[i-1][j-1]) / ((4**j) - 1)

    return approximations[-1][-1]

x, h = np.pi / 4, np.pi / 12
n = 4

result = richardson_extrapolation(x, h, n)
print(f"Richardson Extrapolation: {result: 5.4f}")