import numpy as np
import matplotlib.pyplot as plt

def derivative(f, x, method='central'):
    n=len(x)
    deriv=[0]*n
    if method=='central':
        for i in range (1, n-1):
            deriv[i]=(f[i+1]-f[i-1])/(x[i+1]-x[i-1])
    elif method=='backward':
        for i in range (1,n):
            deriv[i]=(f[i]-f[i-1])/(x[i]-x[i-1])
    elif method=='forward':
        for i in range (n-1):
            deriv[i]=(f[i+1]-f[i])/(x[i+1]-x[i])
    else:
        print("Wrong difference method!")
        return None
    return deriv

x=np.array([1, 1.5, 1.6, 2.5, 3.5])
f=np.array([0.6767, 0.3734, 0.3261, 0.08422, 0.01596])
dfdx=lambda x: np.exp(-2*x)*(5-10*x)
der_central=derivative(f, x)
der_backward=derivative(f,x, 'backward')
der_forward=derivative(f, x, 'forward')
der_true=dfdx(x)   # true derivative
print('  x    true derivative  central_difference  backward_difference forward_difference')
print(' _________________________________________________________________________________')
    
for i in range (len(x)):
    print(f'{x[i]:5.2f} {der_true[i]:10.5f}  {der_central[i]:10.5f} {der_backward[i]:10.5f} {der_forward[i]:10.5f}')
    
x_new=np.linspace(0, 4, 100)
y_new=dfdx(x_new)
plt.plot(x, der_central, 'ro', label='central difference')
plt.plot(x, der_backward, 'b*', label='backward difference')
plt.plot(x, der_forward, 'gs', label='forward difference')
plt.plot(x_new, y_new, label='True derivative')
plt.grid()
plt.legend()
plt.show()
