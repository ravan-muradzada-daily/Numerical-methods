import numpy as np
import matplotlib.pyplot as plt

# Define the original function
def original_function(x):
    return np.cos((x ** (2 / 3)) / np.sqrt(2))

# Define the Taylor series approximation (5 nonzero terms)
def taylor_series_approximation(x):
    u = (x ** (2 / 3)) / np.sqrt(2)
    return (1 - (u**2) / 2 + (u**4) / 24 - (u**6) / 720 + (u**8) / 40320)

# Define the range of x values
x_values = np.linspace(-2, 2, 500)
original_values = original_function(x_values)
taylor_values = taylor_series_approximation(x_values)

# Plot the original function and Taylor series approximation
plt.figure(figsize=(10, 6))
plt.plot(x_values, original_values, label="Original Function", color="blue")
plt.plot(x_values, taylor_values, label="Taylor Series (5 terms)", color="orange", linestyle="--")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Add horizontal line at y=0

# Add grid, title, and labels
plt.grid(True, linestyle="--", alpha=0.7)
plt.title("Comparison of Original Function and Taylor Series Approximation", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.legend(fontsize=12)
plt.show()

# Compute and print values for each x
print(f"{'x':>10} {'Original f(x)':>20} {'Taylor Approximation':>25} {'Absolute Error':>20}")
for x in x_values:
    original = original_function(x)
    taylor = taylor_series_approximation(x)
    error = abs(original - taylor)
    print(f"{x:>10.5f} {original:>20.10f} {taylor:>25.10f} {error:>20.10f}")
