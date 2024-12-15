import numpy as np

def gaussianElimination(matrix, b):
    n, m = len(matrix), len(matrix[0])

    if n != m:
        print("Failed! Matrix should be square!")
        return None
    
    # Forward elimination
    for pivotIndex in range(n-1):
        if matrix[pivotIndex][pivotIndex] == 0:
            print("Failed! Matrix should not be singular!")
            return None
        
        for i in range(pivotIndex+1, n):
            factor = matrix[i][pivotIndex] / matrix[pivotIndex][pivotIndex]

            for j in range(pivotIndex, n):
                matrix[i][j] -= factor * matrix[pivotIndex][j]

            b[i] -= factor * b[pivotIndex]
    
    # Back substition

    resultList = n * [0]
    resultList[n-1] = b[n-1] / matrix[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum = b[i]

        for j in range(i+1, n):
            sum -= matrix[i][j] * resultList[j]
        
        resultList[i] = sum / matrix[i][i]
    
    return resultList

matrix = [
    [1, 2, 3, 1],
    [2, 3, 4, 5],
    [3, 4, 1, 2],
    [4, 1, 2, 3]
]

b = [1, 2, 1, 3]

resultsList = gaussianElimination(matrix, b)

print(resultsList)