import determinant as dt
import basic_operator as bo
import math
import copy

def change(m, ans, index):
  """
  Change the matrix `m` by replacing the values in a specific column with the values in `ans`.

  Parameters:
  - m (list): The matrix to be changed.
  - ans (list): The values to be inserted into the matrix.
  - index (int): The index of the column to be changed.

  Returns:
  - r (list): The modified matrix.
  """
  r = copy.deepcopy(m)
  for j, i in enumerate(ans):
    r[j][index] = i
  return r

def cramer(m, ans):
  """
  Solve a system of linear equations using Cramer's rule.

  Parameters:
  - m (list): The coefficient matrix of the system.
  - ans (list): The right-hand side values of the system.

  Returns:
  - resmat (list): The solution to the system of linear equations.
  """
  resmat = list([])
  deter = dt.determinant_cofactor(m)
  if deter == 0:
    return "The system does not have a unique solution"
  for i in range(0, len(m)):
    resmat.append(dt.determinant_cofactor(change(m, ans, i))/deter)
  return resmat

def inverse_solver(m, ans):
  """
  Solve a system of linear equations using the inverse matrix method.

  Parameters:
  - m (list): The coefficient matrix of the system.
  - ans (list): The right-hand side values of the system.

  Returns:
  - result (list): The solution to the system of linear equations.
  """
  inv = bo.inverse_matrix(m)
  return bo.multiply_matrix(inv, ans)

def gaussian_elimination(M, A=None, stage=0, triangleMode=False):
  """
  Solve a system of linear equations using Gaussian elimination.

  Parameters:
  - M (list): The augmented matrix of the system.
  - A (list): The right-hand side values of the system. (optional)
  - stage (int): The current stage of the Gaussian elimination process. (optional)
  - triangleMode (bool): Flag to indicate whether to return the matrix in triangle mode. (optional)

  Returns:
  - M (list): The modified augmented matrix or the triangular matrix.
  """
  if A is not None:
    for i in range(0, len(M)):
      M[i].append(A[i])

  length = len(M)
  lengthH = len(M[0])

  if stage == length:
    return M

  # Find a row with a non-zero element in the same column
  for i in range(stage, length):
    if M[i][stage] != 0:
      M[stage], M[i] = M[i], M[stage]
      break
  else:
    raise Exception("Matrix is singular")

  factor = M[stage][stage]
  for i in range(stage, lengthH):
    M[stage][i] /= factor

  for i in range(stage + 1, length):
    a = M[i][stage]
    for j in range(stage, lengthH):
      M[i][j] -= a * M[stage][j]

  M = gaussian_elimination(M, stage=stage + 1)
  if triangleMode or stage > 0:
    return M

  # Backward substitution
  for i in range(1, length):
    for k in range(0, length - i):
      c = M[k][length - i]
      for j in range(0, len(M[0])):
        M[k][j] -= c * M[length - i][j]

  ans = list([])
  for i in range(0, length):
    ans.append(M[i][lengthH - 1])

  return ans

def gauss_seidel(M, ans, tolerance=10e-5):
  """
  Solve a system of linear equations using the Gauss-Seidel method.

  Parameters:
  - M (list): The coefficient matrix of the system.
  - ans (list): The right-hand side values of the system.
  - tolerance (float): The tolerance value for convergence. (optional)

  Returns:
  - x (list): The solution to the system of linear equations.
  """
  length = len(M)
  error = 1
  x = list([0 for _ in range(length)])
  xback = copy.deepcopy(x)
  while error > tolerance:
    for i in range(0, length):
      s = 0
      for j in range(0, length):
        if i != j:
          s += M[i][j] * x[j]
      x[i] = (ans[i] - s) / M[i][i]
    error = 0
    for i in range(0, length):
      error += (x[i] - xback[i]) ** 2
    error = math.sqrt(error)
    xback = copy.deepcopy(x)
  return x

# M = list([[3,  1, -1],
#           [1,  4,  2],
#           [2, -2,  5]])
# ans = list([12, 9, -3])

# print(gauss_seidel(M, ans))