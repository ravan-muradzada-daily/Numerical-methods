import numpy as np
from scipy.interpolate import interp1d

def forward_difference(t, v, i):
    return (v[i+1] - v[i]) / (t[i+1] - t[i])

def central_difference(t, v, i):
    return (v[i+1] - v[i-1]) / (t[i+1] - t[i-1])

def trapezoidal_integration(t, v, start, end):
    distance = 0.0

    for i in range(start, end):
        distance += 0.5 * (t[i+1] - t[i]) * (v[i+1] + v[i])
    
    return distance

#----------------------------------------------------#
# Input data

t = np.array([0, 4, 8, 12, 16, 20, 24, 28, 32, 36], dtype=float)
v = np.array([0, 34.7, 61.8, 82.8, 99.2, 112, 121.9, 129.7, 135.7, 140.4], dtype=float)

print()

#----------------------------------------------------#
# a
start = 0 # index when t = 0
end = 7# index when t = 28

distance = trapezoidal_integration(t, v, start, end)
print(f"Distance t = 0 to 28: {distance:.3f}\n\n")

#----------------------------------------------------#
# b

i = 7 # index for 28 in time array
estimation_1 = central_difference(t, v, i)
print(f"Best estimation for t={t[i]}: a={estimation_1:.3f}\n\n")

#----------------------------------------------------#
# c

j = 0 # index for 0 in time array

estimation_2 = forward_difference(t, v, j)
print(f"Best estimation for t={t[j]}: a={estimation_2:.3f}\n\n")