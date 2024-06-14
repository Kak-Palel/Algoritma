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

def ode_euler(ft : callable, x0, y0, x, h = 0):
  if(h == 0):
    h = (x - x0)/1000
  x_ = x0
  y = y0
  while math.fabs(x_ - x) > math.fabs(h):
    y = y + h * ft(x_)
    x_ += h
  return y

def ode_heun(ft : callable, x0, y0, x, h = 0):
  if(h == 0):
    h = (x - x0)/1000
  x_ = x0
  y = y0
  while math.fabs(x_ - x) > math.fabs(h):
    y = y + h * (ft(x_) + ft(x_ + h))/2
    x_ += h
  return y

def ode_polygon(ft : callable, x0, y0, x, h = 0):
  if(h == 0):
    h = (x - x0)/1000
  x_ = x0
  y = y0
  while math.fabs(x_ - x) > math.fabs(h):
    y = y + h * ft(x_ + h/2)
    x_ += h
  return y

def ode_raltson(ft : callable, x0, y0, x, h = 0):
  if(h == 0):
    h = (x - x0)/1000
  x_ = x0
  y = y0
  while math.fabs(x_ - x) > math.fabs(h):
    y = y + h * (ft(x_) + 2*ft(x_+0.75*h))/3
    x_ += h
  return y

def ode_runge_kutta(ft : callable, x0, y0, x, h = 0):
  if(h == 0):
    h = (x - x0)/1000
  x_ = x0
  y = y0
  while math.fabs(x_ - x) > math.fabs(h):
    y = y + h * (ft(x_) + 4*ft(x_+ h/2) + ft(x_ + h))/6
    x_ += h
  return y

# f = lambda x: -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1
# ft = lambda x: -2*x**3 + 12*x**2 -20*x + 8.5
# x0 = 0
# y0 = f(x0)
# x = -1
# n = 400
# h = (x - x0)/n

# y = f(x)
# euler = ode_euler(ft, x0, y0, x, h)
# heun = ode_heun(ft, x0, y0, x, h)
# polygon = ode_polygon(ft, x0, y0, x, h)
# raltson = ode_raltson(ft, x0, y0, x, h)
# runge = ode_runge_kutta(ft, x0, y0, x, h)


# print("euler   :" ,euler, "error:", math.fabs(euler - y))
# print("heun    :" ,heun, "error:", math.fabs(heun - y))
# print("polygon :" ,polygon, " error:", math.fabs(polygon - y))
# print("raltson :" ,raltson, " error:", math.fabs(raltson - y))
# print("runge   :" ,runge, "error:", math.fabs(runge - y))