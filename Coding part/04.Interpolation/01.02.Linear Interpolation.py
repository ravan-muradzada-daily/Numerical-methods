from math import *
# If the exact root is given

def function(x):
    return x**3 - 2*(x**2) - 5

def linearInterpolationMethod(low, high, exactValue, errorValue):
    if function(low) * function(high) >= 0:
        print("Linear Interpolation method has failed!")
        return None

    currentValue = 0
    n = 0 # iteration count

    while True:
        fLow, fHigh = function(low), function(high)
        currentValue = (low * fHigh - high * fLow) / (fHigh - fLow)
        n += 1
        fCurrent = function(currentValue)

        print(f"Iteration: {n}, Boundaries: [{low}, {high}], currValue={currentValue}, f(currValue) = {fCurrent}")
        if fCurrent == 0:
            # currentValue is the exact root
            break
        elif fLow * fCurrent > 0:
            low = currentValue
        else:
            high = currentValue

        if abs(currentValue - exactValue) < errorValue:
            break

    return currentValue

low, high = 2, 3
errorValue = 0.01
exactValue = 2.69064744802878

result = linearInterpolationMethod(low, high, exactValue, errorValue)

print(f"\n\nResult is {result}")