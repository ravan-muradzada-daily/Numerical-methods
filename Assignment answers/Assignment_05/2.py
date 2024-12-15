import numpy as np

def f(b, d, c, rhs):
    n = len(d)
    c_prime = np.zeros(n - 1)
    d_prime = np.zeros(n)
    rhs_prime = np.zeros(n)
    x = np.zeros(n)

    d_prime[0] = d[0]
    rhs_prime[0] = rhs[0]
    for i in range(1, n):
        c_prime[i - 1] = c[i - 1] / d_prime[i - 1]
        d_prime[i] = d[i] - b[i] * c_prime[i - 1]
        rhs_prime[i] = rhs[i] - b[i] * rhs_prime[i - 1] / d_prime[i - 1]

    x[-1] = rhs_prime[-1] / d_prime[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (rhs_prime[i] - c[i] * x[i + 1]) / d_prime[i]

    return x

b = np.array([0, 5, 6, 7, 8])  # sub-diagonal elements
d = np.array([10, 20, 30, 40, 50])  # main diagonal elements
c = np.array([1, 2, 3, 4, 0])  # super-diagonal elements
rhs = np.array([1, 2, 1, -1, 1])  # right-hand side vector

solution = f(b, d, c, rhs)
print("Solution:", solution)
