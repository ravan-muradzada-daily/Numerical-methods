import numpy as np
import matplotlib.pyplot as plt

error_value = 1e-8

def f(x):
    return np.cos(x) - x * np.exp(x)

def bisection_method(a, b):
    if f(a) * f(b) > 0:
        print("Bisection method failed!")
        return None
    
    while True:
        mid = (a + b) / 2

        f_mid = f(mid)
        if abs(f_mid) < error_value:
            break

        if f_mid == 0:
            # mid is exact root
            break
        elif f(a) * f_mid > 0:
            a = mid
        else:
            b = mid

    return mid


x_for_plotting = np.linspace(-4, 1, 200)
plt.plot(x_for_plotting, f(x_for_plotting))
plt.axhline(0, color="black")
plt.axvline(0, color="black")
# -1.8642  -1.8638
plt.grid(True)
plt.legend()
#plt.show()