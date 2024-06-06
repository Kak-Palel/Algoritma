import regression as reg

def centralDifferenceFirst(f , x : float, h : float = 10e-5 ):
    return (f(x+h) - f(x-h))/(2*h)

def centralDifferenceSecond(f, x : float, h : float = 10e-5):
    return (f(x+2*h) - 2*f(x+h) + 2*f(x-h) - f(x-2*h))/(2 * h**3)

def forwardDifferenceFirst(f, x : float, h : float = 10e-5):
    return (f(x+h) - f(x))/h

def backwardDifferenceFirst(f, x : float, h : float = 10e-5):
    return (f(x) - f(x-h))/h

def nonCentranDifferenceSecond1(f, x : float, h : float = 10e-5):
    return (-3*f(x) + 4*f(x+h) - f(x+2*h))/(2*h)

def nonCentranDifferenceSecond2(f, x : float, h : float = 10e-5):
    return (2*f(x) - 5*f(x+h) + 4*f(x+2*h) - 1*f(x+3*h))/(h**2)

def nonCentranDifferenceSecond3(f, x : float, h : float = 10e-5):
    return (-5*f(x) + 18*f(x+h) - 24*f(x+2*h) + 14*f(x+3*h) - 3*f(x+4*h))/(2*h**3)

def nonCentranDifferenceSecond4(f, x : float, h : float = 10e-5):
    return (3*f(x) - 14*f(x+h) + 26*f(x+2*h) - 24*f(x+3*h) + 11*f(x+4*h) - 2*f(x+5*h))/(h**4)

# x = list([0, 0.1, 0.2, 0.3, 0.4])
# y = list([0, 0.0819, 0.1341, 0.1646, 0.1797])
# print("x    : ", x)
# print("f(x) : ", y)

# cof = reg.interpolate(x, y)

# print("setelah melakukan interpolasi, didapatkan f(x) = ", cof[0], " + ", cof[1], "x + ", cof[2], "x^2 + ", cof[3], "x^3 + ", cof[4], "x^4")

# print(cof)
# def f(x):
#     return cof[0] + cof[1]*x + cof[2]*x**2 + cof[3]*x**3 + cof[4]*x**4

# print("f'(0)      : ",nonCentranDifferenceSecond1(f, 0))
# print("f'(0.2)    : ",nonCentranDifferenceSecond1(f, 0.2))
# print("f''(0)     : ",nonCentranDifferenceSecond2(f, 0))
# print("f''(0.2)   : ",nonCentranDifferenceSecond2(f, 0.2))
# print("f'''(0)    : ",nonCentranDifferenceSecond3(f, 0))
# print("f'''(0.2)  : ",nonCentranDifferenceSecond3(f, 0.2))
# print("f''''(0)   : ",nonCentranDifferenceSecond4(f, 0))
# print("f''''(0.2) : ",nonCentranDifferenceSecond4(f, 0.2))