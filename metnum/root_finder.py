def secant(f, x1, x2, tolerance = 10e-5):
  while abs(x2-x1)>tolerance:
    temp = x2
    x2 = x1 - f(x1)*(x2 - x1)/(f(x2) - f(x1))
    x1 = temp
  return (x1+x2)/2

def regula_falsi(f, x1, x2, tolerace = 10e-5):
  while abs(x2-x1)>tolerace:
    c = x1 - f(x1)*(x2 - x1)/(f(x2) - f(x1))
    if(f(c) == 0):
      return c
    elif f(c)*f(x1)<0:
      x2 = c
    else:
      x1 = c
  return (x1+x2)/2

def bisection_method(f : callable, a, b, tolerance = 10e-5):
  if f(a) * f(b) >= 0:
    print("The function may not have a root in the given interval.")
    return None

  while abs(b - a) > tolerance:
    c = (a + b) / 2
    if f(c) == 0:
      return c
    elif f(c) * f(a) < 0:
      b = c
    else:
      a = c

  return (a + b) / 2

def newton_rhapson(f, ft, x, tolerance = 10e-4):
  y = f(x)
  while abs(y)>tolerance:
    x = x - y/ft(x)
    y=f(x)
    print(x)
  
  return x