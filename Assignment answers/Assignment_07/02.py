import numpy as np

def divided_differences(x_values, y_values):
    n = len(y_values)

    table = [[0 for i in range(n)]for i in range(n)]

    for i in range(n):
        table[i][0] = y_values[i]
    
    for j in range(1, n):
        for i in range(n-j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x_values[i+j] - x_values[i])
        
    coefficients = [table[0][i] for i in range(n)]

    return coefficients

def newton_interpolation(x_values, y_values, x):
    coefficients = divided_differences(x_values, y_values)

    n = len(x_values)

    result = coefficients[0]
    p = 1

    for i in range(1, n):
        p *= (x - x_values[i-1])
        result += p * coefficients[i]
    
    return result


all_calculated_results = np.zeros(4, dtype=float)
x = 4

#---------------------------------------------------------#
# First order

x_1 = np.array([3, 5], dtype=float)
y_1 = np.array([19, 99], dtype=float)

all_calculated_results[0] = newton_interpolation(x_1, y_1, x)

#---------------------------------------------------------#
# Second order

x_2 = np.array([2, 3, 5], dtype=float)
y_2 = np.array([6, 19, 99], dtype=float)

all_calculated_results[1] = newton_interpolation(x_2, y_2, x)

#---------------------------------------------------------#
# Third order

x_3 = np.array([2, 3, 5, 7], dtype=float)
y_3 = np.array([6, 19, 99, 291], dtype=float)

all_calculated_results[2] = newton_interpolation(x_3, y_3, x)

#---------------------------------------------------------#
# Fourth order

x_4 = np.array([1, 2, 3, 5, 7], dtype=float)
y_4 = np.array([3, 6, 19, 99, 291], dtype=float)

all_calculated_results[3] = newton_interpolation(x_4, y_4, x)


#---------------------------------------------------------#
# Printing all results

for i in range(4):
    print(f"Result in {i+1}'th order: {all_calculated_results[i]}\n")

#---------------------------------------------------------#

print("As the polynomial order increases, the result at x = 4 should get closer to the true value. Higher-order polynomials generally provide more accurate approximations.\nIn our example, we can notice that while order is increasing, the calculated result is approaching to 48. Even if we increase the order more, it will continue like that. So, it also shows us to increase order properly will increase accuracy.")