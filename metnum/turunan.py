def centralDifferenceFirst(f , x : float, h : float = 10e-5 ):
    return (f(x+h) - f(x-h))/(2*h)

def centralDifferenceSecond(f, x : float, h : float = 10e-5):
    return (f(x+2*h) - 2*f(x+h) + 2*f(x-h) - f(x-2*h))/(2 * h**3)

def forwardDifferenceFirst(f, x : float, h : float = 10e-5):
    return (f(x+h) - f(x))/h

def backwardDifferenceFirst(f, x : float, h : float = 10e-5):
    return (f(x) - f(x-h))/h

def nonCentranDifferenceSecond(f, x : float, h : float = 10e-5):
    return (-1*f(x+2*h) + 4*f(x+h) - 3*f(x))/(2*h)

# f = lambda x: x**3
# ft = lambda x:3*x**2
# x = list(range(1,5))
# hsl = lambda f,xl : list(map(f,xl))

# print(x)
# print(hsl(f,x))
# print(hsl(ft,x))
# for i in x:
#     print(centralDifferenceFirst(f, i), end= " ")

# print("")
# for i in x:
#     print(forwardDifferenceFirst(f, i), end= " ")

# print("")
# for i in x:
#     print(backwardDifferenceFirst(f, i), end= " ")

# print(centralDifferenceFirst(f, 3))