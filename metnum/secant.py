def secant(f, x1, x2, ate = 1e-4):
  while abs(x2-x1)>ate:
    temp = x2
    x2 = (x1*f(x2) - x2*f(x1))/(f(x2)-f(x1))
    x1 = temp
  return (x1+x2)/2

# f = lambda x : x*x -2*x - 1
# print(nrs(f, 1, 2))