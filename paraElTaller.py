
import numpy as np
import matplotlib.pyplot as plt
from scipy import random
import sympy as sp
from sympy import integrate, exp, sin, cos, pi

intervaloInf = 0
intevraloSup = 1
nPuntos = 20


def f(x):
    funcion = exp(x) * sin(x)
    ecuacion = sp.sympify(funcion)
    stringEcuacion = str(ecuacion)
    evaluada = eval(stringEcuacion)
    return evaluada

def montecarlo():
    plt_vals = []
    for i in range(nPuntos):

        ar = np.zeros(nPuntos)

        for i in range(len(ar)):
            ar[i] = random.uniform(intervaloInf, intevraloSup)

        integral = 0.0

        for i in ar:
            integral += f(i)

        ans = (intevraloSup - intervaloInf) / float(nPuntos) * integral
        print(ans)

        plt_vals.append(ans)
    plt.title("Distribuciones de áreas calculada")
    plt.hist(plt_vals, bins=30, ec="black")
    plt.xlabel("Áreas")
    plt.show()

print(montecarlo())
