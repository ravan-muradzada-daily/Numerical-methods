import numpy as np

def f(x):
    return np.cos(x + x**3)

print("If we use just recursive trapezoid method (not romberg), we can use an array instead of matrix.")

def recursive_trapezoid(f, a, b, n):
    approximations = np.zeros(n)
    approximations[0] = (f(a) + f(b)) * (b - a) / 2.0

    for i in range(1, n):
        current_sum = 0
        h = (b - a) / (2 ** i)

        for k in range(1, 2**(i-1) + 1):
            current_sum += f(a + (2*k - 1)*h)
        approximations[i] = approximations[i-1] / 2.0 + h * current_sum
    
    return approximations

a, b = 0, 1
n = 4

approximations = recursive_trapezoid(f, a, b, n)
print("\nAll approximations:")
for i in approximations:
    print(f"{i:.3f}", end="\t")

print(f"\n\nR[3] = {approximations[3]:.3f}\n")

f_max_2 = 1
h = (b - a) / n 
error_estimate = ((b-a) * h * h * f_max_2) / 12
print(f"Error estimate: {error_estimate}")