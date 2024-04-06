import numpy as np

def determinant_cofactor(m):
  if len(m[0]) == 2:
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]
  
  neg = 1
  result = 0
  for i, a in enumerate(m[0]):
    tempM = np.copy(m)
    tempM = np.delete(tempM, 0, axis = 0)
    tempM = np.delete(tempM, i, axis = 1)
    result += neg*m[0][i]*determinant_cofactor(tempM)
    neg *= -1
  return result

# M = np.array([[3, -1, 2], [5, 0, 4], [8, 2, -3]])
# print(determinant_cofactor(M))