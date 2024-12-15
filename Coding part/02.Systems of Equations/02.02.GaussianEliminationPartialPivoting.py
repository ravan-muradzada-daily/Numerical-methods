import numpy as np


def gaussianEliminationPartialPivoting(matrix, b):
    if len(matrix) != len(matrix[0]):
        print("Matrix should be square matrix!")
        return None

    n = len(matrix)
    indexArray = list(range(n))
    maximumNumsArray = [max(currRow) for currRow in matrix]

    for i in range(n-1):
        ratios = []
        for j in range(i, n):
            if maximumNumsArray[j] == 0:
                ratios.append(0)
            else:
                ratios.append(np.abs(matrix[j][i] / maximumNumsArray[j]))

        maxRatio = max(ratios)
        pivot = i + ratios.index(maxRatio)

        if matrix[indexArray[pivot]][i] == 0:
            continue

        indexArray[i], indexArray[pivot] = indexArray[pivot], indexArray[i]

        for row in indexArray:
            if row == pivot:
                continue

            factor = matrix[row][i] / matrix[pivot][i]

            for col in range(n):
                matrix[row][col] -= matrix[pivot][col] * factor
            b[row] -= factor * b[pivot]

    resultsArray = np.zeros(n)

    for i in range(n-1, -1, -1):
        resultsArray[i] = b[indexArray[i]]

        for j in range(i+1, n):
            resultsArray[i] -= matrix[indexArray[i]][j] * resultsArray[j]

        resultsArray[i] /= matrix[indexArray[i]][i]

    return resultsArray

matrix = np.array([[1, 4, 5], [2, 2, 5], [-4, 1, 3]], dtype=float)
b = np.array([1, 2, 3], dtype=float)

resultsArray_1 = gaussianEliminationPartialPivoting(matrix, b)
resultsArray_2 = np.linalg.inv(matrix).dot(b) # build-in function

print(f"Result array: {resultsArray_1}")
print(f"Result array (build-in): {resultsArray_2}")