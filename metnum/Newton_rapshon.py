def nrd(f, ft, x, ate = 1e-4):
  y = f(x)
  while abs(y)>ate:
    x = x - y/ft(x)
    y=f(x)
    print(x)
  
  return x

# f = lambda x : x*x -2*x - 1
# ft = lambda x : 2*x - 2
# print(nrd(f,ft,))