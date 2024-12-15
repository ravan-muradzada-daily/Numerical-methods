import numpy as np


#----------------------------------------------------#
# Numerical differences

def forward_difference(t, y, i):
    return (y[i+1] - y[i]) / (t[i+1] - t[i])

def backward_difference(t, y, i):
    return (y[i] - y[i-1]) / (t[i] - t[i-1])

def central_difference(t, y, i):
    return (y[i+1] - y[i-1]) / (t[i+1] - t[i-1])

#----------------------------------------------------#
# Given data

t = np.array([0, 25, 50, 75, 100, 125], dtype=float)
y = np.array([0, 32, 58, 78, 92, 100], dtype=float)

#----------------------------------------------------#
# Finding velocities and accelerations

n = len(t)
velocities = np.zeros(n)
accelerations = np.zeros(n)

for i in range(n):
    if i == 0:
        velocities[i] = forward_difference(t, y, i)
    elif i == n-1:
        velocities[i] =  backward_difference(t, y, i)
    else:
        velocities[i] = central_difference(t, y, i)


print()

print("I tried to use mostly central difference, because it is the best one, when it is not available to use it, I used forward or backward difference.\n")

for i in range(n):
    print(i+1, end=") ")

    if i == 0:
        accelerations[i] = forward_difference(t, velocities, i)
    elif i == n-1:
        accelerations[i] =  backward_difference(t, velocities, i)
    else:
        accelerations[i] = central_difference(t, velocities, i)

    print(f"t={t[i]}, current velocity: {velocities[i]:.3f} km/s, current acceleration: {accelerations[i]:.3f} km/s^2\n")
    