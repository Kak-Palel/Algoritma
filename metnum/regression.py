import spl_solver as spl
import differentiation as diff
import math

def linear(x, y):
  """
  Performs linear regression using the method of least squares.

  Parameters:
  - x (list): List of x-values.
  - y (list): List of y-values.

  Returns:
  - list: List of coefficients [a, b] for the linear equation y = a + bx.
  """
  sumX = sum(x)
  sumY = sum(y)
  x_squared = list(i*i for i in x)
  sumXsquared = sum(x_squared)
  sumXY = 0
  for i in range(len(x)):
    sumXY += x[i]*y[i]
  return spl.cramer(list([[len(x), sumX], [sumX, sumXsquared]]), list([sumY, sumXY]))

def Cx_power_b(x, y):
  """
  Performs regression for the equation y = Cx^b using logarithmic transformation.

  Parameters:
  - x (list): List of x-values.
  - y (list): List of y-values.

  Returns:
  - list: List of coefficients [C, b] for the equation y = Cx^b.
  """
  lnx = list([math.log(i) for i in x])
  lny = list([math.log(i) for i in y])
  sol = linear(lnx, lny)
  sol[0] = math.e ** sol[0]
  return sol

def polynomial(x, y, order=2):
  """
  Performs polynomial regression of given order using the method of least squares.

  Parameters:
  - x (list): List of x-values.
  - y (list): List of y-values.
  - order (int): Order of the polynomial regression (default is 2).

  Returns:
  - list: List of coefficients [a0, a1, ..., an] for the polynomial equation y = a0 + a1*x + ... + an*x^n.
  """
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
  """
  Calculates the root mean square error (RMSE) between the actual y-values and the predicted y-values.

  Parameters:
  - x (list): List of x-values.
  - y (list): List of y-values.
  - f (callable): Function that predicts y-values based on x-values.

  Returns:
  - float: Root mean square error (RMSE) between the actual y-values and the predicted y-values.
  """
  fx = [f(i) for i in x]
  err = [(fx[i]-y[i])**2 for i in range(6)]
  return math.sqrt(sum(err)/6)

def mcLaurin(f : callable, order):
  """
  Calculates the coefficients of the Maclaurin series expansion of a function.

  Parameters:
  - f (callable): The function to expand.
  - order (int): The order of the Maclaurin series expansion.

  Returns:
  - list: List of coefficients [a0, a1, ..., an] for the Maclaurin series expansion.
  """
  a : list = []
  for i in range(order + 1):
    a.append(diff.getNthDiff(f, 0, i) / math.factorial(i))
    print(a[i])
  return a

def taylor(f : callable, x0, order):
  """
  Calculates the coefficients of the Taylor series expansion of a function.

  Parameters:
  - f (callable): The function to expand.
  - x0 (float): The point at which to expand the function.
  - order (int): The order of the Taylor series expansion.

  Returns:
  - list: List of coefficients [a0, a1, ..., an] for the Taylor series expansion.
  """
  a : list = []
  for i in range(order + 1):
    a.append(diff.getNthDiff(f, x0, i) / math.factorial(i))
  return a

def interpolate(x , y, order = -1):
  """
  Performs polynomial interpolation of given order using the method of Lagrange or Newton.

  Parameters:
  - x (list): List of x-values.
  - y (list): List of y-values.
  - order (int): Order of the polynomial interpolation (default is -1, which means using the highest order possible).

  Returns:
  - list: List of coefficients [a0, a1, ..., an] for the polynomial equation y = a0 + a1*x + ... + an*x^n.
  """
  if order == -1:
    order = len(x) - 1
  if order == 1:
    return linear(x, y)
  else:
    m = list([[x[j]**i for i in range(order+1)] for j in range(0, len(x))])
    return spl.cramer(m, y)

def interpolate_lagrange(Xset : list, Yset : list, x):
  """
  Performs polynomial interpolation using the Lagrange method.

  Parameters:
  - Xset (list): List of x-values in the dataset.
  - Yset (list): List of y-values in the dataset.
  - x (float): The x-value to interpolate.

  Returns:
  - float: The interpolated y-value at x.
  """
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
  """
  Performs polynomial interpolation using the Newton method.

  Parameters:
  - Xset (list): List of x-values in the dataset.
  - Yset (list): List of y-values in the dataset.
  - x (float): The x-value to interpolate.

  Returns:
  - float: The interpolated y-value at x.
  """
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


def ode_euler(ft : callable, x0, y0, x, h = 0):
  """
  Solves an ordinary differential equation (ODE) using Euler's method.

  Parameters:
  - ft (callable): The derivative function f(x, y).
  - x0 (float): Initial x-value.
  - y0 (float): Initial y-value.
  - x (float): The x-value to solve for.
  - h (float): Step size (default is 0, which means automatically determined).

  Returns:
  - float: The approximate y-value at x.
  """
  if(h == 0):
    h = (x - x0)/1000
  x_ = x0
  y = y0
  while math.fabs(x_ - x) > math.fabs(h):
    y = y + h * ft(x_)
    x_ += h
  return y

def ode_heun(ft : callable, x0, y0, x, h = 0):
  """
  Solves an ordinary differential equation (ODE) using Heun's method.

  Parameters:
  - ft (callable): The derivative function f(x, y).
  - x0 (float): Initial x-value.
  - y0 (float): Initial y-value.
  - x (float): The x-value to solve for.
  - h (float): Step size (default is 0, which means automatically determined).

  Returns:
  - float: The approximate y-value at x.
  """
  if(h == 0):
    h = (x - x0)/1000
  x_ = x0
  y = y0
  while math.fabs(x_ - x) > math.fabs(h):
    y = y + h * (ft(x_) + ft(x_ + h))/2
    x_ += h
  return y

def ode_polygon(ft : callable, x0, y0, x, h = 0):
  """
  Solves an ordinary differential equation (ODE) using the Polygon method.

  Parameters:
  - ft (callable): The derivative function f(x, y).
  - x0 (float): Initial x-value.
  - y0 (float): Initial y-value.
  - x (float): The x-value to solve for.
  - h (float): Step size (default is 0, which means automatically determined).

  Returns:
  - float: The approximate y-value at x.
  """
  if(h == 0):
    h = (x - x0)/1000
  x_ = x0
  y = y0
  while math.fabs(x_ - x) > math.fabs(h):
    y = y + h * ft(x_ + h/2)
    x_ += h
  return y

def ode_raltson(ft : callable, x0, y0, x, h = 0):
  """
  Solves an ordinary differential equation (ODE) using Ralston's method.

  Parameters:
  - ft (callable): The derivative function f(x, y).
  - x0 (float): Initial x-value.
  - y0 (float): Initial y-value.
  - x (float): The x-value to solve for.
  - h (float): Step size (default is 0, which means automatically determined).

  Returns:
  - float: The approximate y-value at x.
  """
  if(h == 0):
    h = (x - x0)/1000
  x_ = x0
  y = y0
  while math.fabs(x_ - x) > math.fabs(h):
    y = y + h * (ft(x_) + 2*ft(x_+0.75*h))/3
    x_ += h
  return y

def ode_runge_kutta(ft : callable, x0, y0, x, h = 0):
  """
  Solves an ordinary differential equation (ODE) using the Runge-Kutta method.

  Parameters:
  - ft (callable): The derivative function f(x, y).
  - x0 (float): Initial x-value.
  - y0 (float): Initial y-value.
  - x (float): The x-value to solve for.
  - h (float): Step size (default is 0, which means automatically determined).

  Returns:
  - float: The approximate y-value at x.
  """
  if(h == 0):
    h = (x - x0)/1000
  x_ = x0
  y = y0
  while math.fabs(x_ - x) > math.fabs(h):
    y = y + h * (ft(x_) + 4*ft(x_+ h/2) + ft(x_ + h))/6
    x_ += h
  return y
