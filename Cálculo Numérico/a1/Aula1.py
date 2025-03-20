from math import pi

def soma(a, b):
    return a + b

def operacoes(a, b):
    return a + b, a*b

def vol(r):
    v_pi = 3.1415
    return (4/3)*pi*r**3

def polinomio(a, b, c=1):
    return a**2 + b - c

if __name__ == "__main__":
    # sum = soma(3, 4)
    # print(sum)

    # operar = operacoes(3,4)
    # print(operar)

    # volume = vol(5.5)
    # print(volume)

    poli = polinomio(2.2, -1.7,)
    print(poli)


    
    