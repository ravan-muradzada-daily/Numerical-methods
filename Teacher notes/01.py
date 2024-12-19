import numpy as np


def f(v, t):
    return 1 - 2 * v**2 - t

def f_prime(v, t, dv_dt):
    return -4 * v * dv_dt - 1


v0 = 1
t0 = 0
dt = 0.01
steps = 100


t_values = np.arange(t0, t0 + dt * steps, dt)
v_values = np.zeros(steps)
v_values[0] = v0


for i in range(1, steps):
    t = t_values[i-1]
    v = v_values[i-1]

    dv_dt = f(v, t)
    d2v_dt2 = f_prime(v, t, dv_dt)
    
    v_values[i] = v + dt * dv_dt + (dt**2 / 2) * d2v_dt2


for i in range(len(t_values)):
    print(f"{t_values[i]:.3f}\t{v_values[i]:.3f}")