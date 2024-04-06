import numpy as np

def inverse_matrix(M, stage = 0, A = np.array([0])):
  length = len(M)
  M = M.astype('f')
  if(stage == length):
    return M
 
  if len(A) == 1:
    A = np.zeros((length, length))
    for a in range(length):
      A[a][a] = 1

  factor = 0
  for i in range(stage, length):
    if M[stage][i] != 0:
      factor = M[i][stage]
      temp = np.copy(M[i])
      M[i] = M[stage]
      M[stage] = temp
      temp = np.copy(A[i])
      A[i] = A[stage]
      A[stage] = temp
      break

  if factor == 0:
    raise Exception("The Matrix M has no inverse")

  for i in range(stage, length):
    M[stage][i] /= factor
  for i in range (length):
    A[stage][i] /= factor
  
  for i in range(stage + 1, length):
    a = M[i][stage]
    for j in range(stage, length):
      M[i][j] -= a*M[stage][j]
    for j in range(length):
      A[i][j] -= a*A[stage][j]

  M = inverse_matrix(M, stage + 1, A)

  for i in range(0, stage):
    a = M[i][stage]
    M[i][stage] = 0
    for j in range(length):
      A[i][j] -= a*A[stage][j]

  if stage == 0:
    return A

  return M

# M = np.array([[1, 2, 3], [2, 5, 3], [1, 0, 8]])
# print(inverse_matrix(M))