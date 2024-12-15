import numpy as np
'''
    In secant_method method we do not use derivative. However, here we use two elements as initial guess.
    We need x(0) and x(1) as initial guesses. So using that we find better approximations.

    How to find new approximation for secant_method Method?

    Imagine, currently we are in n'th approximation and want to find (n+1)th.
    The formula for that is:

    x(n+1) = x(n) - (( x(n) - x(n-1)) / ( f(x(n)) - f(xn_1) )) * f(x(n))
    You just need to learn it by heart.
    
    Stopping criteria is too similar to Newton Raphson method:

    if abs(f(x(n+1))) < given_error_value:
        break

'''
def f(x):
    return (np.exp(x) / x) - (np.sin(x) / (x**2)) + 2 * x - 10

def secan_method(x0, x1, errorValue):

    # x0 means x(n-1) 
    # x1 means x(n) 
    # x2 means x(n+1) 

    while True:
        f_x0 = f(x0)
        f_x1 = f(x1)

        x2 = x0 - (x1-x0) * f(x0) / (f(x1) - f(x0)) 

        x0 = x1
        x1 = x2

        if abs(f(x2)) < errorValue:
            break

    return x2

x0 = 1
x1 = 2
error_value = 10 ** (-7)

result = secan_method(x0, x1, error_value)
checking = f(result)

print(f"Result: {result}")
print(f"Checking: {checking}")
