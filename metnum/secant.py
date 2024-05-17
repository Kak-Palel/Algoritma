import math

def secant(f, x1, x2, ate = 1e-4):
  iterasi = 1
  while abs(x2-x1)>ate:
    print("iterasi: ", iterasi)
    temp = x2
    x2 = (x1*f(x2) - x2*f(x1))/(f(x2)-f(x1))
    x1 = temp
    print("x1 = ",x1)
    print("x2 = ",x2)
    iterasi += 1
  return (x1+x2)/2

# f = lambda x : 0.1*x**3 - x**2 -x + 8 + math.exp(-x)
# print("soal nomor 1 A akar 1:")
# print("hasil: ",secant(f, 2, 5))
# print("soal nomor 1 A akar 2:")
# print("hasil: ",secant(f, 8, 12))
# print("\nsoal nomor 1 B:")
# print("hasil: ",secant(f, 3, 5))
# print("hasil: ",secant(f, 15, 16))