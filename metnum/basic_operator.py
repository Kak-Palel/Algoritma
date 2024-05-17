import inverse_matrix as im

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