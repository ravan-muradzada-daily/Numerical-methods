import numpy as np

# Differentiation 

def f(x):
    return x

def f_prime(x, y, dy_dx):
    return y

def f_double_prime(x, y, dy_dx, d2y_dx2):
    return dy_dx

def forward_difference(x, h):
    return (f(x+h) - f(x)) / h

def backward_difference(x, h):
    return (f(x) - f(x-h)) / h

def central_difference(x, h):
    return (f(x+h) - f(x-h)) / (2*h)

def richardson_extrapolation(x, h, n):
    approximations = np.zeros([n, n])

    for i in range(n):
        approximations[i][0] = central_difference(x, h / (2**i))

    for j in range(1, n):
        for i in range(n):
            approximations[i][j] = approximations[i][j-1] + (approximations[i][j-1] - approximations[i-1][j-1]) / ((4**j) - 1)
    
    return approximations[-1][-1]

# ----------------------------------------------- #

# Integration

def lower_upper_sums(a, b, n):
    h = (b - a) / n
    x = a
    lower, upper = 0, 0

    while x <= b:
        m = min(f(x), f(x+h))
        M = max(f(x), f(x+h))

        lower += m
        upper += M

        x += h 
    
    lower *= h
    upper *= h

    return (lower + upper) / 2.0

def trapezoid_1(a, b, n):
    h = (b - a) / n
    x_i = a + h
    Sum = 0.5 * (f(a) + f(b))

    while x_i < b:
        Sum += f(x_i)
        x_i += h

    Sum *= h

    return Sum

def trapezoid_2(x, y):
    res = 0
    n = len(x)
    for i in range(n-1):
        res += (x[i+1] - x[i]) * (y[i+1] + y[i])
    
    res *= 0.5

    return res

def recursive_trapezoid(a, b, n):
    approximations = np.zeros([n, n])

    approximations[0][0] = (b-a) * (f(a) + f(b)) / 2.0

    for i in range(1, n):
        s = 0
        h = (b - a) / (2**i)

        for k in range(1, 2**(i-1)+1):
            s += f(a + (2*k - 1)*h)
        
        approximations[i][0] = 0.5*approximations[i-1][0] + h * s

    return approximations

def romberg(approxs, n):
    for i in range(1, n):
        for j in range(1, i+1):
            approxs[i][j] = ((4**j) * approxs[i][j-1] - approxs[i-1][j-1]) / ((4**j) - 1)

    return approxs


# ----------------------------------------------- #

# ODE

def euler_method(x0, y0, delta, target):
    x, y = x0, y0

    x_values = np.arange(x0, target+delta, delta)
    y_values = np.zeros(len(x_values))
    y_values[0] = y0

    for i in range(1, len(x_values)):
        x, y = x_values[i-1], y_values[i-1]

        y_values[i] = y + delta * f(x, y)

    return x_values, y_values

def taylor_series_method(x0, y0, delta, target):
    x_values = np.arange(x0, target+delta, delta)
    n = len(x_values)
    y_values = np.zeros(n)
    y_values[0] = y0

    for i in range(1, n):
        x, y = x_values[i-1], y_values[i-1]

        dy_dx = f(x, y)
        d2y_dx2 = f_prime(x, y, dy_dx)

        y_values[i] = y + delta * dy_dx + (delta*delta / 2) * d2y_dx2
    
    return x_values, y_values


def taylor_series_method(x0, y0, delta, target):
    x_values = np.arange(x0, target+delta, delta)
    n = len(x_values)
    y_values = np.zeros(n)
    y_values[0] = y0

    for i in range(1, n):
        x, y = x_values[i-1], y_values[i-1]

        dy_dx = f(x, y)
        d2y_dx2 = f_prime(x, y, dy_dx)
        d3y_dx3 = f_double_prime(x, y, dy_dx, d2y_dx2)

        y_values[i] = y + dy_dx * delta + d2y_dx2 * (delta*delta / 2.0) + d3y_dx3 * (delta**3 / 6)

    return x_values, y_values