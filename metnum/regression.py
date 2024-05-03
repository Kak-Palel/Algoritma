import numpy as np
import spl_solver as spl
import math

def linear(x, y):
  sumX = sum(x)
  sumY = sum(y)
  x_squared = list(i*i for i in x)
  sumXsquared = sum(x_squared)
  sumXY = 0
  for i in range(len(x)):
    sumXY += x[i]*y[i]
  return spl.cramer(np.array([[len(x), sumX], [sumX, sumXsquared]]), np.array([sumY, sumXY]))

def Cx_power_b(x, y):
  lnx = list([math.log(i) for i in x])
  lny = list([math.log(i) for i in y])
  sol = linear(lnx, lny)
  sol[0] = math.e ** sol[0]
  return sol

def polynomial(x, y, order=2):
  matrix_x = [[]]
  frstRow = [order]
  matrix_y = []

  for i in range(1, order +1):
    xPower = [u**i for u in x]
    frstRow.append(sum(xPower))
  matrix_x[0] = frstRow
  a = frstRow.copy()
  for i in range(order + 1, 2*order + 1):
    b = a.copy()
    xPower = [u**i for u in x]
    b.pop(0)
    b.append(sum(xPower))
    matrix_x.append(b)
    a = b
  for i in range(0, order + 1):
    temp = [y[j]*(x[j]**(i)) for j in range(0, len(y))]
    matrix_y.append(sum(temp))
  return spl.cramer(matrix_x, matrix_y)

def error(x, y, f):
  fx = [f(i) for i in x]
  err = [(fx[i]-y[i])**2 for i in range(6)]
  return math.sqrt(sum(err)/6)

