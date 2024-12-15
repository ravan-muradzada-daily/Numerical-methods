import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0

    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= ((x - x_values[j]) / (x_values[i] - x_values[j]))
        
        result += y_values[i] * p

    return result


#----------------------------------------------------#
# Input data

x_values = np.array([1, 3, 5, 7, 13], dtype=float) # Time
y_values = np.array([800, 2310, 3090, 3940, 4755], dtype=float) # Measured velocity v

x = 10 # t = 10

#----------------------------------------------------#
# Calculating the result and print it

calculated_result = lagrange_interpolation(x_values, y_values, x) # f(t)

print(f"Calculated result: {calculated_result} cm/s")

#----------------------------------------------------#
# Sketching the graph

x_for_plotting = np.linspace(0, 15, 200)
y_for_plotting = lagrange_interpolation(x_values, y_values, x_for_plotting)

plt.plot(x_for_plotting, y_for_plotting, color="blue", label="The graph of the function")
plt.title('The velocity of the parachutist')
plt.xlabel('Time')
plt.ylabel('Velocity')

plt.scatter(x_values, y_values, color="red", label="Given data")

plt.scatter(x, calculated_result, color="black", label=f"Calculated point when t = {x}")

plt.grid(True)
plt.legend()
plt.show()