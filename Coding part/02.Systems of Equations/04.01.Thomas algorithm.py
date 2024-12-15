import numpy as np

def thomas_algorithm(abovePart, mainDiagonal, belowPart, rightHandSide):
    n = len(mainDiagonal)
    x = np.zeros(n, dtype=float)

    for i in range(1, n):
        factor = belowPart[i-1] / mainDiagonal[i-1]

        mainDiagonal[i] -= abovePart[i-1] * factor
        rightHandSide[i] -= factor * rightHandSide[i-1]

    x[-1] = rightHandSide[-1] / mainDiagonal[-1]

    for i in range(n-2, -1, -1):
        x[i] = (rightHandSide[i] - abovePart[i] * x[i+1]) / mainDiagonal[i]

    return x


matrix = np.array([
    [1, 4, 0, 0],
    [3, 4, 1, 0],
    [0, 2, 3, 4],
    [0, 0, 1, 3]
]) # For checking the results

belowPart = np.array([3, 2, 1], dtype=float)  # sub-diagonal elements
mainDiagonal = np.array([1, 4, 3, 3], dtype=float)  # main diagonal elements
abovePart = np.array([4, 1, 4], dtype=float)  # super-diagonal elements
rightHandSide = np.array([1, 1, 1, 1], dtype=float)  # right-hand side elements

print(f"\nPython numpy build-in function's solution: \n{np.linalg.inv(matrix).dot(rightHandSide)}\n\n")

mySolution = thomas_algorithm(abovePart, mainDiagonal, belowPart, rightHandSide)
print(f"My solution: \n{mySolution}")