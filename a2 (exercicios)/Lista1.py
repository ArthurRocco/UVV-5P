def CalcA(a, b, c):
    return a + b * c

print(CalcA(10, 20, 30))

def CalcB(a,b):
    return a**2 / b

print(CalcB(4, 30))

def CalcC(a, b, c, d):
    return (a**4 + b) * c - d

print(CalcC(9, 2, 6, 1))

def Calc2(a, b, c, d, e, f, g):
    return a % b * c**2 + d - e * (f / g)
print(Calc2(10, 3, 10, 1, 10, 4, 2))

def Calc3(a, b, c):
    return a + b + c
print(Calc3(1, 2, 3))

def Calc4(a, b):
    return a + (a * b)
print(Calc4(750, 0.15))

def Calc5(d, h, m, s):
    return  (s + (m * 60) + (h * 3600) + (d * 86400))
print(Calc5(10, 10, 10, 10))

def Calc6():
    a = input('Insira um numero')
    b = input('Insira um numero')
    c = input('Insira um numero')
    return max(a, b, c)

    print(Calc6())
from math import sqrt

def Calc7(x):
    if x < 2:
        return False
    if x == 2:
        return False
    if x % 2 == 0:
        return False

    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False
    return x

print(Calc7(13))


