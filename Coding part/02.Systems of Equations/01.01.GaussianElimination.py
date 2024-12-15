import numpy as np

def forwardElimination(matrix, b):
    n, m = len(matrix), len(matrix[0])

    if n != m:
        print("Failed! The matrix should be square!")
        return None
    
    for k in range(n - 1):
        if matrix[k][k] == 0:
            return "Failed! Matrix should not be singular!"
        
        for i in range(k+1, n): # iteration rows
            factor = matrix[i][k] / matrix[k][k]

            for j in range(k, n): # iteration columns
                matrix[i][j] -= factor * matrix[k][j]
            b[i] -= factor * b[k]
    return matrix, b

def backSubstitution(matrix, b):
    n = len(matrix)
    resultsList = [0] * n

    resultsList[n-1] = b[n-1] / matrix[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum = b[i]

        for j in range(i+1, n):
            sum -= matrix[i][j] * resultsList[j]
        
        resultsList[i] = sum / matrix[i][i]
    
    return resultsList

matrix = [
    [1, 1, 1],
    [2, 4, -3],
    [-1, 2, 2]
]

b = [4, -9, 2]

m = forwardElimination(matrix, b)
resultList = backSubstitution(m[0], m[1])
print(matrix)
print(b)
print(resultList)
