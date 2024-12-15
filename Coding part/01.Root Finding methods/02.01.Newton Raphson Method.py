import numpy as np
'''
    Newton-Raphson method always need initial guess, so using this we try to find better approximations for the root.

    The given error value is for our stopping criteria. According to statement, we should break the loop.

    How to calculate the stopping criteria?

    Stopping criteria for the loop:

    if abs(f(current_approximation)) < given_error_value:
        break

    -------------------

    In each iteration, we should check whether the derivative of the function in the current approximation is zero or not. If yes, we should stop the process, so that means there is something wrong.

    Our purpose is to find better approximations in each iteration, so for that we use special formula:

    new_approximation = current_approximation - (f(current_approximation) / f'(current_approximation))

    You need to learn by heart this formula.

'''

def f(x):
    # The given function
    return np.sin(x) - (x/2)

def f_derivative(x):
    # The derivative of the given function
    return np.cos(x) - 0.5

def newton_raphson(initial_Guess, error_value):
    x_n = initial_Guess
    # x_n is current approximation

    while True:
        f_xn = f(x_n)
        if abs(f(x_n)) < error_value:
            break

        f_derivative_xn = f_derivative(x_n)
        
        if f_derivative_xn == 0:
            print("Derivative is zero, method fails!")
            return None

        x_n = x_n - (f_xn / f_derivative_xn)       

    return x_n

initial_Guess = 1.5
error_value = 0.0001 # We can write it as 1e-3

result = newton_raphson(initial_Guess, error_value)

print(f"Result is {result}")

