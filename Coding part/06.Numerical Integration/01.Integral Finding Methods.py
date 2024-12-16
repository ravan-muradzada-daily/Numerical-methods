import numpy as np

'''
    There are multiple numerical ways to calculate the given finite integral.
    ----------------------
    Lower - Upper sums:

    m_i = min(f(x), f(x+h))
    M_i = max(f(x), f(x+h))

    L = h * sum(m_i)
    U = h * sum(M_i)

    Result: (L + U) / 2
    Error <= (U - L) / 2
    ----------------------
    Trapezoid:

    result = h * (0.5 * (f(a) + f(b)) + sum(f(x_i)))
    1 <= i < n-1
    ----------------------
    Recursive Trapezoid:

    R[0][0] = (b-a)*(f(a) + f(b)) / 2
    R[i][0] = 0.5*R[i-1][0] + h * sum(f(a + (2k-1)*h))
    1 <= i <= 2^(n-1)
    ----------------------
    Romberg:
    
    First, we need R from recursive trapezoid. Then:

    R[i][j] = (4**j * R[i][j-1] - R[i-1][j-1]) / (4**j - 1)
    1 <= i < n
    1 <= j <= i
'''

def f(x):
    return x*x - 2*x

def exact_integration(a, b):
    return ((b**3 / 3) - b*b) - ((a**3 / 3) - a*a)

def lower_upper_sums(a, b, n):
    h = (b - a) / n
    x = a
    lower, upper = 0, 0

    while x <= b:
        m = min(f(x), f(x+h))
        M = max(f(x), f(x+h))

        lower += m
        upper += M

        x += h 
    
    lower *= h
    upper *= h

    return (lower + upper) / 2.0

def trapezoid(a, b, n):
    h = (b - a) / n
    x_i = a + h
    Sum = 0.5 * (f(a) + f(b))

    while x_i < b:
        Sum += f(x_i)
        x_i += h

    Sum *= h

    return Sum

def recursive_trapezoid(a, b, n):
    approximations = np.zeros([n, n])

    approximations[0][0] = (b-a) * (f(a) + f(b)) / 2.0

    for i in range(1, n):
        s = 0
        h = (b - a) / (2**i)

        for k in range(1, 2**(i-1)+1):
            s += f(a + (2*k - 1)*h)
        
        approximations[i][0] = 0.5*approximations[i-1][0] + h * s

    return approximations

def romberg(approxs, n):
    for i in range(1, n):
        for j in range(1, i+1):
            approxs[i][j] = ((4**j) * approxs[i][j-1] - approxs[i-1][j-1]) / ((4**j) - 1)

    return approxs

def calculate_true_relative_error(exact, approx):
    return np.abs((exact - approx) / exact) * 100

a, b, n = 1, 21, 10

l_u = lower_upper_sums(a, b, n)
tr = trapezoid(a, b, n)
rec_tr = recursive_trapezoid(a, b, n)
rmb = romberg(rec_tr, n)
exact_result = exact_integration(a, b)

results = {
    "Lower-Upper Sums:": l_u,
    "Trapezoid:": tr,
    "Recursive Trapezoid:": rec_tr[-1][0],
    "Romberg:": rmb[-1][-1]
}
print(rmb)
#print(f"{"Exact Result:":20} {exact_result:10.3f}\n")

for i in results:
    curr_error = calculate_true_relative_error(exact_result, results[i])

    #print(f"{i:20} {results[i]:10.3f}\t{curr_error:10.5f} %")