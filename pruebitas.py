import numpy as np
import matplotlib.pyplot as plt

from numpy import linspace
from sympy.abc import x

from sympy import integrate, exp, sin, cos, pi

def f(x):
    funcion = exp(x) * sin(x)
    print("tipooo",type(funcion))
    return funcion


"""def graficar():
    x = linspace(0, 3.1415, 101)
    plt.plot(x, f(x))
    plt.grid()
    plt.show()

"""


def simpson13(f, a, b):
    m = ((a + b) / 2)
    integral = ((b - a) / 6) * (f(a) + 4 * f(m) + f(b))
    return integral


a = 0
b = pi
n = 2
h = ((b - a) / n)
suma = 0
for i in range(n):
    b = a + h
    area = simpson13(f, a, b)
    suma = suma + area
    a = b


# print("area: ", suma)
def calculo_error():

    integralBonita = integrate(exp(x) * sin(x), (x, 0, pi))
    print(integralBonita, type(integralBonita))
    print(float(integralBonita))
    print(suma)
    errorPorcentual = abs((float(integralBonita) - float(suma)) / float(integralBonita))
    return errorPorcentual

#graficar()
print("error porcentual = ", calculo_error())


