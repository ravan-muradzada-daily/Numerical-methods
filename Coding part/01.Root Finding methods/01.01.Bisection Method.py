import numpy as np

def function(x):
    # The given function in the problem
    return (x**3) - (7 * (x**2)) + 14 * x - 6

def bisectionMethod(lowerBound, upperBound, exactValue, errorValue):
    if function(lowerBound) * function(upperBound) >= 0:
        print("Bisection method has failed!")
        return None
    
    while True:
        mid_point = (lowerBound + upperBound) / 2.0
  

        if function(mid_point) == 0:
            # mid_point is exact root
            break
        elif function(mid_point) * function(lowerBound) > 0:
            # Checking "Intermediate Value Theorem" each iteration
            lowerBound = mid_point
        else:
            upperBound = mid_point

        if abs(exactValue - mid_point) < errorValue:
            # If the current error value is less that given error value,
            # that means, we should stop the process.
            break

    return mid_point


lowerBound, upperBound = 0, 1
exactValue = 2 - np.sqrt(2) # It is given in the problem statement
errorValue = 0.01

result = bisectionMethod(lowerBound, upperBound, exactValue, errorValue)

print(f"\n\nThe result is {result}")