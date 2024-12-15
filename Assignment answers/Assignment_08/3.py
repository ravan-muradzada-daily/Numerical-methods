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

x_values = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)
y_values = np.array([1, 0.5, 0.3333, 0.25, 0.2, 0.1667, 0.1429], dtype=float)
y_searching = 0.3


#-----------------------------------------------------------#
# Finding the x using inversing the inputs technique.

print("\nTo find inverse, we need to reverse x_values and y_values when we send them to the function as parameters..")
calculated_result = lagrange_interpolation(y_values, x_values, y_searching)
print(f"\nCalculated result for x:\n{calculated_result:.3f}\n\n")

#-----------------------------------------------------------#
# Checking part

print("We can check the value sending it to the function:")
print(f"Checking: \n{lagrange_interpolation(x_values, y_values, calculated_result):.1f}\n\n")

#-----------------------------------------------------------#
# Conclusion part

print(f"So we can eaily say:\nf({calculated_result:.3f}) = {y_searching}\n")

#-----------------------------------------------------------#
# Sketching the graph

x_for_plotting = np.linspace(0, 8, 200)
y_for_plotting = lagrange_interpolation(x_values, y_values, x_for_plotting)

plt.plot(x_for_plotting, y_for_plotting, color="blue", label="The graph of the function")
plt.scatter(x_values, y_values, color="red", label="Given data")
plt.plot(calculated_result, y_searching, "go", label=f"f({calculated_result:.3f}) = {y_searching}")
plt.title("Implementing inverse interpolation")
plt.xlabel('x')
plt.ylabel('f(x)')

plt.grid(True)
plt.legend()
plt.show()