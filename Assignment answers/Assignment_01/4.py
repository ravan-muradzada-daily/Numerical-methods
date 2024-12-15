from math import *

error = 0.01

def calculateCurrentTerm(x):
    k = 0
    sumOfExp = 0

    while True:
        currTerm = ((-0.5 * x)**k) / factorial(k)

        if abs(currTerm) <= error:
            break

        k += 1
        sumOfExp += currTerm

    return k, sumOfExp

i = -1

while i <= 1:
    termCount, sum = calculateCurrentTerm(i)
    print(f"The number of terms: {termCount}\t{abs(exp(-0.5*i)-sum)}")
    i += 1