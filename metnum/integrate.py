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

# Example usage
def f(x):
    return x**2

a = 0
b = 1
n = 100

print("Numerical integration square:", square(f, a, b))
print("Numerical integration trapezoid:", trapezoid(f, a, b))
print("Numerical integration middle point:", middlePoint(f, a, b))
print("Numerical integration simpsons rule:", simpsons_rule(f, a, b, n))
