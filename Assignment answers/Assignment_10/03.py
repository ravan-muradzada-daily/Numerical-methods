import numpy as np

def f1(x):
    return (np.sqrt(x*x - 0.16)) / x

def f2(x):
    return np.arcsin(np.sqrt(x / (1+x)))

def f3(x):
    return (np.sin(0.1*x + 0.5)) / (1.7 + np.cos(x**3 + 3))


def recursive_trapezoid(f,a,b,n):
    R=np.zeros([n,n])
    R[0,0] = (f(a) + f(b)) * (b - a) / 2

    for i in range (1, n):
        s = 0
        h = (b - a) / (2**i)

        for k in range (1, 2**(i-1)+1):
            s += f(a + (2*k-1) * h)

        R[i,0] = R[i-1,0] / 2 + h * s
        
    return R

def romberg(approximations, N):
    for n in range (1, N):
        for m in range (1, n+1):
            approximations[n,m]=(4**m*approximations[n, m-1]-approximations[n-1, m-1])/(4**m-1)

    return approximations

a1, b1 = 1, 2
a2, b2 =  0, 3
a3, b3 = 0, 1.2
n = 5

print("\nThe first integral:")
R1 = recursive_trapezoid(f1, a1, b1, n)
R1 = romberg(R1, n)
print(f"R[3][3]: {R1[3][3]:.4f}")

print("\nThe second integral:")
R2 = recursive_trapezoid(f2, a2, b2, n)
R2 = romberg(R2, n)
print(f"R[3][3]: {R2[3][3]:.4f}")

print("\nThe third integral:")
R3 = recursive_trapezoid(f3, a3, b3, n)
R3 = romberg(R3, n)
print(f"R[3][3]: {R3[3][3]:.4f}")


