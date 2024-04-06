import numpy as np
import determinant_cofactor as dt
import inverse_matrix as im
import basic_operator as bo

def change(m, ans, index):
  r = np.copy(m)
  for j, i in enumerate(ans):
    r[j][index] = i
    j += 1
  return r

def cramer(m, ans):
  resmat = np.array([])
  deter = dt.determinant_cofactor(m)
  for i in range(0, len(m)):
    resmat = np.append(resmat, dt.determinant_cofactor(change(m, ans, i))/deter)
  return resmat

def inverse_solver(m, ans):
  inv = im.inverse_matrix(m)
  return bo.multiply_matrix(inv, ans)
  
# m = np.array([[1, 2, 1], [3, 6, 0], [2, 8, 4]])
# ans = np.array([2, 9, 6])
# print(cramer(m, ans))
# print(inverse_solver(m, ans))
