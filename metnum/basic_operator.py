def add(A, B):
  """
  Adds two matrices element-wise.

  Parameters:
  - A (list of lists): The first matrix.
  - B (list of lists): The second matrix.

  Returns:
  - list of lists: The resulting matrix after addition.
  """
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j] += B[i][j]
  return A

def substract(A, B):
  """
  Subtracts two matrices element-wise.

  Parameters:
  - A (list of lists): The first matrix.
  - B (list of lists): The second matrix.

  Returns:
  - list of lists: The resulting matrix after subtraction.
  """
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j] -= B[i][j]
  return A

def multiply_constant(A, c):
  """
  Multiplies a matrix by a constant.

  Parameters:
  - A (list of lists): The matrix.
  - c (float or int): The constant.

  Returns:
  - list of lists: The resulting matrix after multiplication.
  """
  for i in range(len(A)):
    for j in range(len(A[0])):
      A[i][j] *= c
  return A

def multiply_matrix(a, b):
  """
  Multiplies two matrices.

  Parameters:
  - a (list of lists): The first matrix.
  - b (list of lists or float or int): The second matrix or scalar.

  Returns:
  - list of lists: The resulting matrix after multiplication.
  """
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
  """
  Computes the inverse of a matrix using Gaussian elimination.

  Parameters:
  - matrix (list of lists): The matrix.

  Returns:
  - list of lists or None: The inverse matrix if it exists, None otherwise.
  """
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

# A = [[1, 2],
#      [3, 4]]
# B = [[5, 6],
#      [7, 8]]
# print(add(A, B))