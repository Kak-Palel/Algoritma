def add(A, B):
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j] += B[i][j]
  return A

def substract(A, B):
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j] -= B[i][j]
  return A

def multiply_constant(A, c):
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j] *= c
  return A

def multiply_matrix(a, b):
  if isinstance(b[0], float) or isinstance(b[0], int):
    b = [[i] for i in b]
  elif isinstance(b, float) or isinstance(b, int):
    b = [[b]]
  result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
  for i in range(len(a)):
    for j in range(len(b[0])):
      for k in range(len(b)):
        result[i][j] += a[i][k] * b[k][j]
  return result

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
  return identity