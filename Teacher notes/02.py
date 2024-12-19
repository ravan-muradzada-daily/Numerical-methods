import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def f(v, t):
    return 1 - 2 * v**2 - t

def f_prime(v, t, dv_dt):
    return -4 * v * dv_dt - 1

def f_double_prime(v, t, dv_dt, d2v_dt2):
    return -4 * (dv_dt**2) - 4 * v * d2v_dt2
# -4 * ((dv_dt**2) + v * d2v_dt2)

v0 = 1
t0 = 0
dt = 0.1
steps = 10


t_values = np.arange(t0, t0 + dt * steps, dt)
euler_values = np.zeros(steps)
first_order_taylor = np.zeros(steps)
second_order_taylor = np.zeros(steps)
third_order_taylor = np.zeros(steps)


euler_values[0] = v0
first_order_taylor[0] = v0
second_order_taylor[0] = v0
third_order_taylor[0] = v0


for i in range(1, steps):
    t = t_values[i-1]
    v_euler = euler_values[i-1]
    v_taylor1 = first_order_taylor[i-1]
    v_taylor2 = second_order_taylor[i-1]
    v_taylor3 = third_order_taylor[i-1]

    #Euler 
    dv_dt = f(v_euler, t)
    euler_values[i] = v_euler + dt * dv_dt

    #First-order Taylor
    dv_dt = f(v_taylor1, t)
    first_order_taylor[i] = v_taylor1 + dt * dv_dt

    #Second-order Taylor
    dv_dt = f(v_taylor2, t)
    d2v_dt2 = f_prime(v_taylor2, t, dv_dt)
    second_order_taylor[i] = v_taylor2 + dt * dv_dt + (dt**2 / 2) * d2v_dt2

    #Third-order Taylor
    dv_dt = f(v_taylor3, t)
    d2v_dt2 = f_prime(v_taylor3, t, dv_dt)
    d3v_dt3 = f_double_prime(v_taylor3, t, dv_dt, d2v_dt2)
    third_order_taylor[i] = (v_taylor3 + dt * dv_dt + (dt**2 / 2) * d2v_dt2 +
                             (dt**3 / 6) * d3v_dt3)


results = pd.DataFrame({
    't': t_values,
    '3rd Order Taylor': third_order_taylor
})


print(results)


plt.figure(figsize=(10, 6))

plt.plot(t_values, euler_values, label='Euler')
plt.plot(t_values, first_order_taylor, label='1st Order Taylor')
plt.plot(t_values, second_order_taylor, label='2nd Order Taylor')
plt.plot(t_values, third_order_taylor, label='3rd Order Taylor')

plt.xlabel('Time (t)')
plt.ylabel('v(t)')
plt.title('Comparison of Euler and Taylor Series Methods')
plt.legend()
plt.grid(True)
plt.show()
