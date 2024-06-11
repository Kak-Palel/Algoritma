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
    return  area

def simpsons_rule(f, a, b, dx = 10e-5):
    squareCount = (b - a) / dx
    area = f(a) + f(b)

    for i in range(1, int(squareCount)):
        a += dx
        if i % 2 == 0:
            area += 2 * f(a)
        else:
            area += 4 * f(a)

    return (dx / 3) * area

f = lambda x : -0.05*x**2 - 0.1*x + 4.25

# print(f(2.5/2))
# print(f(3.5/2))
# print(f(4.5/2))
# print(f(5.5/2))

def count(a):
    return (a - 0.003125*(-1/math.sqrt(3))**2 - 0.025*(-1/math.sqrt(3)) + 4.25)/4 + (a - 0.003125*(1/math.sqrt(3))**2 - 0.025*(1/math.sqrt(3)) + 4.25)/4

L1 = f(2 - 1/math.sqrt(3))
L2 = f(2 + 1/math.sqrt(3))
print(L1)
print(L2)
print(L1 + L2)
# L3 = 
# print("--------------------")
# print(L1)
# print(L2)
# print(L3)
# print(L4)
# print(L1 + L2 + L3 + L4)
# print(middlePoint(f, 1, 3))
# sum = 0
# sum+=f(5/4)
# sum+=f(7/4)
# sum+=f(9/4)
# sum+=f(11/4)
# print(sum/2)

def this(a):
    h = 1/6
    return (f(a) + 3*f(a + h) + 3*f(a + 2*h) + f(a + 3*h))/16
A1 = this(1)
A2 = this(1.5)
A3 = this(2)
A4 = this(2.5)

print(A1)
print(A2)
print(A3)
print(A4)
print(A1 + A2 + A3 + A4)
# Example usage
# def f(x):
#     return x**2

# a = 0
# b = 1
# n = 100

# print("Numerical integration square:", square(f, a, b))
# print("Numerical integration trapezoid:", trapezoid(f, a, b))
# print("Numerical integration middle point:", middlePoint(f, a, b))
# print("Numerical integration simpsons rule:", simpsons_rule(f, a, b, n))
