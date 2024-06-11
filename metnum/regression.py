import spl_solver as spl
import differentiation as diff
import math

def linear(x, y):
  sumX = sum(x)
  sumY = sum(y)
  x_squared = list(i*i for i in x)
  sumXsquared = sum(x_squared)
  sumXY = 0
  for i in range(len(x)):
    sumXY += x[i]*y[i]
  return spl.cramer(list([[len(x), sumX], [sumX, sumXsquared]]), list([sumY, sumXY]))

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

def error(x, y, f : callable):
  fx = [f(i) for i in x]
  err = [(fx[i]-y[i])**2 for i in range(6)]
  return math.sqrt(sum(err)/6)

def interpolate(x , y, order = -1):
  if order == -1:
    order = len(x) - 1
  if order == 1:
    return linear(x, y)
  else:
    m = list([[x[j]**i for i in range(order+1)] for j in range(0, len(x))])
    return spl.cramer(m, y)

#only returns the output, not the function, because Im too lazy to implement binomial newton ^^
def interpolate_lagrange(Xset : list, Yset : list, x):
  n = len(Xset)
  result = 0
  for i in range(n):
    temp = Yset[i]
    for j in range(n):
      if j != i:
        temp *= (x - Xset[j])/(Xset[i] - Xset[j])
    result += temp
  return result

def interpolate_newton(Xset : list, Yset : list, x):
  n = len(Xset)
  #the a matrix
  xans = Xset.copy()
  a = Yset.copy()
  for k in range(1, n):
    for i in range(n - 1, k - 1, -1):
      a[i] = (a[i] - a[i - 1])/(xans[i] - xans[i - k])

  n -= 1
  p = a[n]
  for k in range(1, n + 1):
    p = a[n - k] + (x - Xset[n - k])*p
  return p

def mcLaurin(f : callable, order):
  a : list = []
  for i in range(order + 1):
    a.append(diff.getNthDiff(f, 0, i) / math.factorial(i))
    print(a[i])
  return a


f = lambda x : x**4 - 2*x**3 - 3*x**2 + 4*x + 5
print(mcLaurin(f, 4))
# x = [8, 9, 9.5]
# y = [2.0794, 2.1972, 2.2513]
# print(Cx_power_b(x, y))
# print(interpolate(x, y)) #2.875
# print(interpolate_newton(x, y, 1.5)) #2.875
# print(interpolate_lagrange(x, y, 1.5))