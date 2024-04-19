import numpy as np
import spl_solver as spl

# f = lambda x:x*1.5 + 1.5

# x = list(range(20))
# y = list(f(i) for i in x)

def linear(x, y):
  sumX = sum(x)
  sumY = sum(y)
  x_squared = list(i*i for i in x)
  sumXsquared = sum(x_squared)
  sumXY = 0
  for i in range(len(x)):
    sumXY += x[i]*y[i]
  return spl.cramer(np.array([[len(x), sumX], [sumX, sumXsquared]]), np.array([sumY, sumXY]))

# print(linear(x, y))