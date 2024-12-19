# recursive Trapezoid method
import numpy as np

def f(x):
    return np.cos(x + x**3)

def Trapezoid(f,a,b):
    return (f(a)+f(b))*(b-a)/2

def Recur_trapezoid(f,a,b,n):
    R=np.zeros([n,n])
    R[0,0]=Trapezoid(f,a,b)


    for i in range (1,n):
        s=0
        h=(b-a)/(2**i)
        
        for k in range (1, 2**(i-1)+1):
            s+=f(a+(2*k-1)*h)
        R[i,0]=R[i-1,0]/2+h*s
    return R
  
a=0
b=1
n=5
R=Recur_trapezoid(f,a,b,n)
print("Integrals estimates: \n", R)