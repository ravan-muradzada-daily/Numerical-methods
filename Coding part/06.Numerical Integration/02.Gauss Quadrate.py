import numpy as np

def determine_cardinal(i, x, x_values):
    result = 1
    n = len(x_values)

    for j in range(n):
        if i != j:
            current = (x - x_values[j]) / (x_values[i] - x_values[j])
            result *= current

    return result

