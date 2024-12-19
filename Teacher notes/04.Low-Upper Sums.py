import numpy as np

def f1(x):
    return np.log(x-3)

def f2(x):
    return np.sqrt(100 - np.sqrt(x))

def low_upper_sums(f, a, b, n):
    h = (b - a) / n
    x = a
    low, upper = 0, 0

    while x <= b:
        m = min(f(x), f(x+h))
        M = max(f(x), f(x+h))
        low += m
        upper += M
        x += h

    low *= h
    upper *= h
    return (low + upper) / 2

def trapezoid(f, a, b, n):
    h = (b - a) / n
    S = (f(a) + f(b)) / 2
    x = a + h
    while x < b:
       S += f(x)
       x += h
    S *= h
    
    return S

n1, n2 = 10, 100

a1, b1 = 4, 5
a2, b2 = 2, 10

result_1_low_upper_n1 = low_upper_sums(f1, a1, b1, n1)
result_1_low_upper_n2 = low_upper_sums(f1, a1, b1, n2)
result_1_trapezoid_n1 = trapezoid(f1, a1, b1, n1)
result_1_trapezoid_n2 = trapezoid(f1, a1, b1, n2)

result_2_low_upper_n1 = low_upper_sums(f2, a2, b2, n1)
result_2_low_upper_n2 = low_upper_sums(f2, a2, b2, n2)
result_2_trapezoid_n1 = trapezoid(f2, a2, b2, n1)
result_2_trapezoid_n2 = trapezoid(f2, a2, b2, n2)


# print(f"\nWhen N={n1}:\n\n")
# # print("For first integral:")
# # print(f"Result from low upper sums: {result_1_low_upper_n1}")
# # print(f"Result from trapezoid: {result_1_trapezoid_n1}")
print("\nFor the second integral:")
print(f"Result from low upper sums: {result_2_low_upper_n1}")
print(f"Result from trapezoid: {result_2_trapezoid_n2}\n")

# print(f"\n\nWhen N={n2}\n\n")
# print("For first integral:")
# print(f"Result from low upper sums: {result_1_low_upper_n2}")
# print(f"Result from trapezoid: {result_1_trapezoid_n2}")
# print("\nFor the second integral:")
# print(f"Result from low upper sums: {result_2_low_upper_n2}")
# print(f"Result from trapezoid: {result_2_low_upper_n2}\n")