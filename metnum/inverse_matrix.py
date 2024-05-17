def inverse_matrix(matrix):
    n = len(matrix)
    identity = [[float(i == j) for i in range(n)] for j in range(n)]
    for i in range(n):
        if matrix[i][i] == 0.0:
            for j in range(i+1, n):
                if matrix[j][i] != 0.0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    identity[i], identity[j] = identity[j], identity[i]
                    break
            else:
                return None
        pivot = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] /= pivot
        for j in range(n):
            identity[i][j] /= pivot
        for j in range(n):
            if i != j:
                ratio = matrix[j][i]
                for k in range(i, n):
                    matrix[j][k] -= ratio * matrix[i][k]
                for k in range(n):
                    identity[j][k] -= ratio * identity[i][k]
    print(identity)
    print()
    return identity

# M = list([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
# print(inverse_matrix(M))