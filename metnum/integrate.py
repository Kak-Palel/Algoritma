import math

def square(f, a, b, dx = 10e-5):
    squareCount = (b-a) / dx
    area = 0
    for i in range(int(squareCount)):
        area += f(a)*dx
        a += dx
    return area

def trapezoid(f, a, b, dx = 10e-5):
    squareCount = (b-a) / dx
    area = 0
    for i in range(int(squareCount)):
        area += (f(a) + f(a+dx))*dx/2
        a += dx
    return area

def middlePoint(f, a, b, dx = 10e-5):
    squareCount = (b-a) / dx
    area = 0
    for i in range(int(squareCount)):
        area += f(a + dx/2)*dx
        a += dx
    return area

def simpsons_rule_1over3(f, a, b):
    h = math.abs(b - a)/2
    return h*(f(a) + 4*f(a + h) + f(b))/3

def simpsons_rule_3over8(f, a, b):
    h = math.abs(b - a)/3
    return 3*h*(f(a) + 3*f(a + h) + 3*f(a + 2*h) + f(b))/8

def gauss_legendre2(f, a, b):
    return (b-a)/2*(f((a+b)/2 - (b-a)*math.sqrt(3)/2) + f((a+b)/2 + (b-a)*math.sqrt(3)/2))

def gauss_legendre3(f, a, b):
    return (b-a)/2*(5*f((a+b)/2 - (b-a)*math.sqrt(3/5)) + 8*f((a+b)/2) + 5*f((a+b)/2 + (b-a)*math.sqrt(3/5)))/9