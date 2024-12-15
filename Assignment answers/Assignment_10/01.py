import numpy as np

#---------------------------------------------#
# Functions

def f1(x):
    return np.log(x-3)

def f2(x):
    return np.sqrt(100 - np.sqrt(x))

def low_upper_sums(f, a, b, n):
    lower, upper = 0.0, 0.0
    h = (b - a) / n 
    current_term = a

    while current_term <= b:
        m = min(f(current_term), f(current_term+h))
        M = max(f(current_term), f(current_term+h))
        
        lower += m 
        upper += M 

        current_term += h
    
    lower *= h 
    upper *= h

    return (lower + upper) / 2.0

def trapezoid(f, a, b, n):
    h = (b - a) / n
    sum = (f(a) + f(b)) / 2.0
    current_term = a + h

    while current_term < b:
        sum += f(current_term)
        current_term += h 

    sum *= h 

    return sum

#---------------------------------------------#
# Input Data

n1, n2 = 10, 100
a1, b1 = 4, 5
a2, b2 = 2, 10

#---------------------------------------------#

# First equation: ln(x-3)

print("\n**************************************\n")
print("-Results for the first equation: ln(x-3)\n")


print(f"N = {n1}")

result_1_lower_upper = low_upper_sums(f1, a1, b1, n1)
result_1_trapezoid = trapezoid(f1, a1, b1, n1)

print(f"Result from lower-upper sums: {result_1_lower_upper:.3f}")
print(f"Result from trapezoid method: {result_1_trapezoid:.3f}\n\n")

print(f"N = {n2}")

result_1_lower_upper = low_upper_sums(f1, a1, b1, n2)
result_1_trapezoid = trapezoid(f1, a1, b1, n2)

print(f"Result from lower-upper sums: {result_1_lower_upper:.3f}")
print(f"Result from trapezoid method: {result_1_trapezoid:.3f}")
print("\n**************************************\n")


#---------------------------------------------#

# Second equation: sqrt(100 - sqrt(x))

print("-Results from the second equation: sqrt(100 - sqrt(x))\n")

print(f"N = {n1}")

result_2_lower_upper = low_upper_sums(f2, a2, b2, n1)
result_2_trapezoid = trapezoid(f2, a2, b2, n1)

print(f"Result from lower-upper sums: {result_2_lower_upper:.3f}")
print(f"Result from trapezoid method: {result_2_trapezoid:.3f}\n\n")

print(f"N = {n2}")

result_2_lower_upper = low_upper_sums(f2, a2, b2, n2)
result_2_trapezoid = trapezoid(f2, a2, b2, n2)

print(f"Result from lower-upper sums: {result_2_lower_upper:.3f}")
print(f"Result from trapezoid method: {result_2_trapezoid:.3f}")
print("\n**************************************")
