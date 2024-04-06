import numpy as np
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

def multiply_matrix(A, B):
  if(type(B[0]) != type(A[0])):
    L = 1
  else:
    L = len(B[0])
  C = np.zeros((1, len(A)))
  for k in range(L):
    res = np.array([])
    for i in range(len(A)):
      temp = 0
      for j in range(len(A[0])):
        if L == 1:
          temp += A[i][j] * B[j]
        else:
          temp += A[i][j] * B[j][k]
      res = np.append(res, temp)
    C = np.vstack((C,res))
  C = np.delete(C, [0, 0], axis=0)

  if L == 1:
    return C[0]
  return C

# A = np.array([[1, 2, 4], [2, 6, 0]])
# B = np.array([[4, 1, 4, 3], [0, -1, 3, 1], [2, 7, 5, 2]])
# C = np.array([1, 2, 3])

# print(multiply_matrix(A, B))
# print("Risu cantikk")
# print(multiply_matrix(A, C))