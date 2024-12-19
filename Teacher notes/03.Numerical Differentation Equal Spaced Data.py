# numerical differenciation
import numpy as np
import matplotlib.pyplot as plt

def derivative(f,a,method='central',h=0.01):
    '''Compute the difference formula for f'(a) with step size h.

    Parameters
    ----------
    f : function
        Vectorized function of one variable
    a : Compute derivative at x = a
    method : 'forward', 'backward' or 'central'
    h : Step size in difference formula

    Returns
        Difference formula:
            central: f(a+h) - f(a-h))/2h
            forward: f(a+h) - f(a))/h
            backward: f(a) - f(a-h))/h            
    '''
    if method == 'central':
        return (f(a + h) - f(a - h))/(2*h)
    elif method == 'forward':
        return (f(a + h) - f(a))/h
    elif method == 'backward':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")

x = np.linspace(-2*np.pi,2*np.pi,100)
f = lambda x: np.sin(x)
y = f(x)
#xnew=0.5
dydx = derivative(f,x, 'central', 0.5)
#dx_new=derivative(f, xnew)
#print(xnew, 'df(0.5)=', dx_new)
dx=np.cos(x)

plt.plot(x,y,label='y=f(x)')
plt.plot(x,dydx,'*r', label="Central Difference y=f'(x)")
plt.plot(x,dx, label="y'(x)=cos(x)")
#plt.plot(xnew,dx_new,'sr', label="derivative for 0.5")
plt.legend()
plt.grid()
plt.show()