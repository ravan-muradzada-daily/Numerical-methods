# Richardson extrapolation for Differentiation
import numpy as np
def f(x):
    return -0.1*x**4-0.15*x**3-0.5*x**2-0.25*x+1.2

def FI(f, x, h):
    return (f(x+h)-f(x-h))/(2*h)

def Richardson(f, x, h, n):
    D=np.zeros([n,n])
    for i in range (n):
        D[i, 0]=FI(f, x, h/2**i)
    for j in range (1,n):
        for i in range (n):
            D[i,j]=D[i, j-1]+(D[i, j-1]-D[i-1, j-1])/(4**j-1)
    print(D)
    return D[n-1, n-1]

x=0.5
h=0.5
n=4
true_value=-0.9125
estimation=Richardson(f,x,h,n)
print (f"Richardson extrapolation is {estimation}")
relative_error=np.abs(true_value-estimation)/true_value*100
print(f"Relative error is {relative_error}")

