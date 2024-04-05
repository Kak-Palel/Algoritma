import numpy as np

def det3x3(m):
  return m[0][0]*m[1][1]*m[2][2] + m[0][1]*m[1][2]*m[2][0] + m[0][2]*m[1][0]*m[2][1] - m[0][2]*m[1][1]*m[2][0] - m[1][2]*m[2][1]*m[0][0] - m[0][1]*m[1][0]*m[2][2]

def change(m, ans, index):
  r = np.copy(m)
  j = 0
  for i in ans:
    r[j][index] = i
    j += 1
  
  return r

#CHANGE THIS
#--------------------------------------------------#
m = np.array([[1, 2, 1], [3, 6, 0], [2, 8, 4]])    #
ans = np.array([2, 9, 6])                          #
#--------------------------------------------------#

deter = det3x3(m)

m1 = change(m, ans, 0)
print(m1)
m2 = change(m, ans, 1)
print(m2)
m3 = change(m, ans, 2)
print(m3)

print(det3x3(m1)/deter)
print(det3x3(m2)/deter)
print(det3x3(m3)/deter)

