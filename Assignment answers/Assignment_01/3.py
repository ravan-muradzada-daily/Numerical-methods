from math import *

errorCount = 0.001

def generateNumber(i):
    res = 4.0 / (2 * i + 1)
    if i % 2 == 1:
        res = -res
    return res

i = 0
sum = 0
while True:
    curr = generateNumber(i)
    if abs(curr) < errorCount:
        break

    sum += curr
    i += 1

print(f"The least amount of terms is {i}")
print(f"The error is {abs(pi-sum)}")