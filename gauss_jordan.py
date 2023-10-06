def gauss_jordan_elimination(matrix, n):
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        for j in range(n):
            if j != i:
                factor = matrix[j][i]
                for k in range(i, n + 1):
                    matrix[j][k] -= factor * matrix[i][k]
    solution = [row[n] for row in matrix]

    return solution
if __name__ == "__main__":
    matrix = [
        [2, 1, -1, 8],
        [-3, -1, 2, -11],
        [-2, 1, 2, -3]
    ]

    n = len(matrix)
    solution = gauss_jordan_elimination(matrix, n)
    variables = ["x" , "y" , "z"]
    for i, val in enumerate(solution):
    	print("{} : {}".format(variables[i] , val))
