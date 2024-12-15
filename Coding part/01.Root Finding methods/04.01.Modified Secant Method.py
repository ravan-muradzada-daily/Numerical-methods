import numpy as np

'''
    Modified secant method is another version of Secant Method. The difference is that, to find a new approximation,
    we use another formula:

    x(new) = x(pr) - x(pr)*delta*f(x) / (f(x(pr) + delta * x(pr)) * f(x(pr)))

    As you can see, to start the process we just need one initial guess.
    
    Stopping criteria:
    if abs(f(x)) <= given_error_value:
        break 

'''

def f(x):
    return x**3-(np.exp(-2*x)-2)

def modified_secant_method(initial_guess, delta, error_value):
    x = initial_guess

    while True:
        x = x - x*delta*f(x) / (f(x+delta*x) - f(x))

        if abs(f(x)) < error_value:
            break 

    return x

delta = 0.5
error_value = 1e-15
initial_guess = -1

result = modified_secant_method(initial_guess, delta, error_value)
print(f"Result: {result}")

checking = f(result)
print(f"Checking: {checking}")