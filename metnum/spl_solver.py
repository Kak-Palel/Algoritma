import determinant_cofactor as dt
import inverse_matrix as im
import basic_operator as bo
import copy

def change(m, ans, index):
    r = copy.deepcopy(m)
    for j, i in enumerate(ans):
        r[j][index] = i
    return r

def cramer(m, ans):
  resmat = list([])
  deter = dt.determinant_cofactor(m)
  if deter == 0:
    return "The system does not have a unique solution"
  for i in range(0, len(m)):
    resmat.append(dt.determinant_cofactor(change(m, ans, i))/deter)
  return resmat

def inverse_solver(m, ans):
  inv = im.inverse_matrix(m)
  return bo.multiply_matrix(inv, ans)

# M = list([[1, 8, 64], [1, 9, 81], [1, 9.5, 90.25]])
# A = list([2.0794, 2.1972, 2.2513])
# print(inverse_solver(M, A))