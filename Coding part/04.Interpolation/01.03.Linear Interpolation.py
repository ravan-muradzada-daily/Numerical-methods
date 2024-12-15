from math import *
# Stopping criteria:
# Until the difference of current and previous values is less than
# error value.
def f(x):
    return sin(x) - (x/2)

def linearInterpolation(low, high, errorValue):
    if f(low) * f(high) >= 0:
        print("Linear Interpolation method has failed!")
        return None

    mid = low

    while True:
        fLow, fHigh = f(low), f(high)
        previousMid = mid
        mid = (low * fHigh - high * fLow) / (fHigh - fLow)

        if abs(mid - previousMid) < errorValue:
            break

        fMid = f(mid)
        if fMid == 0:
            #mid is exact value
            break
        elif fLow * fMid > 0:
            low = mid
        else:
            high = mid

    return mid

low, high = 1, 2
errorValue = 0.0001

result = linearInterpolation(low, high, errorValue)

print(f"Result is {result}")