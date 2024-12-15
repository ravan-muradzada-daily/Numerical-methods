import numpy as np

def gaussian_elimination(matrix, right_hand_side):
    n = len(right_hand_side)

    for i in range(n-1):
        if matrix[i][i] == 0:
            print("Matrix is singular!")
            return None
        
        for j in range(i+1, n):
            factor = matrix[j][i] / matrix[i][i]
            for c in range(i, n):
                matrix[j][c] -= factor * matrix[i][c] 
            right_hand_side[j] -= factor *  right_hand_side[i]

    x = np.zeros(n, dtype=float)
    x[-1] = right_hand_side[-1] / matrix[-1][-1]

    for i in range(n-2, -1, -1):
        sum = right_hand_side[i]

        for j in range(i+1, n):
            sum -= x[j] * matrix[i][j]
        
        x[i] = sum / matrix[i][i]
    
    return x

matrix = np.array([
    [2, 5, 4, 1],
    [1, 3, 2, 1],
    [2, 10, 9, 7],
    [3, 8, 9, 2]
], dtype=float)

right_hand_side = np.array([20, 11, 40, 37], dtype=float)

result = gaussian_elimination(matrix, right_hand_side)

print(result)