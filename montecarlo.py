import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import tkinter
from tkinter import *
from numpy import linspace
from sympy.abc import x
from sympy import integrate, exp, sin, cos, pi
from scipy import random

# Creación ventana
from sympy import integrate

ventana = tkinter.Tk()
ventana.title("Integración por método de Montecarlo")
ventana.geometry("450x530")

# Título
integracionLabel = Label(ventana, text="Integración numérica por Montecarlo ", width="40",
                         font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15,
                                                                                                               y=12)

# Declaración de Labels Entrada
entradaLabel = Label(ventana, text="Entrada: ", width="13", font=("helvetica", 11, "bold"),
                     padx=5, pady=5, fg="black", borderwidth=2).place(x=35, y=60)

funcLabel = Label(ventana, text="Función", width="15", font=("helvetica", 12, "bold"),
                  padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y=90)

intervaloLabel = Label(ventana, text="Intervalo: ", width="13", font=("helvetica", 11, "bold"),
                       padx=5, pady=5).place(x=35, y=130)

extremoIzqLabel = Label(ventana, text="Extremo Izquierdo", width="15", font=("helvetica", 12, "bold"),
                        padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15,
                                                                                                              y=160)
extremoDerLabel = Label(ventana, text="Extremo Derecho", width="15", font=("helvetica", 12, "bold"),
                        padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15,
                                                                                                              y=200)

numParticionesLabel = Label(ventana, text="Núm de particiones", width="15", font=("helvetica", 12, "bold"),
                            padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15,
                                                                                                                  y=240)
# ---------------------------------------------------------------------------------------------------------------------------
# Declaración de Labels Salida
salidaLabel = Label(ventana, text="Salida: ", width="13", font=("helvetica", 11, "bold"),
                    padx=5, pady=5, fg="black", borderwidth=2).place(x=25, y=350)

integralLabel = Label(ventana, text="Integral", width="15", font=("helvetica", 12, "bold"),
                      padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y=380)

valorIntegralSalidaLabel = Label(ventana, text="Valor de la integral", width="15", font=("helvetica", 12, "bold"),
                                 padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(
    x=15, y=420)


# VARIABLES CAMP TEXTO
funcVar = tkinter.StringVar()
extremoIzq = tkinter.DoubleVar()
extremoDer = tkinter.DoubleVar()
numParticiones = tkinter.IntVar()

# ENTRADA
funcCampoTexto = Entry(ventana, textvariable=funcVar, font=10, width=26)
funcCampoTexto.place(x=185, y=95)

extremoIzqText = Entry(ventana, textvariable=extremoIzq, font=10, width=26)
extremoIzqText.place(x=185, y=165)

extremoDerText = Entry(ventana, textvariable=extremoDer, font=10, width=26)
extremoDerText.place(x=185, y=205)

numParticionesTexto = Entry(ventana, textvariable=numParticiones, font=10, width=26)
numParticionesTexto.place(x=185, y=245)

# ----------------------------------------------------------------------------------------------------------------------------

# VARIABLES CAMP TEXTO
valorAreaSalida = tkinter.DoubleVar()

# SALIDA
valorAreaSalidaText = Entry(ventana, textvariable=valorAreaSalida, font=10, width=26, state='readonly')
valorAreaSalidaText.place(x=185, y=425)



# --------------------------------------------------------------------------------------------------------

# FUNCIONES


def borrar():
    funcCampoTexto.delete(0, END)
    extremoIzqText.delete(0, END)
    extremoDerText.delete(0, END)
    numParticionesTexto.delete(0, END)

    valorAreaSalidaText.config(state=NORMAL)
    valorAreaSalidaText.delete(0, END)
    valorAreaSalidaText.config(state='readonly')


def salir():
    ventana.destroy()


# -------------------------------------------------------------------------------------------------
def f(x):
    # funcion de prueba ----> exp(x) * sin(x)
    funcion = funcCampoTexto.get()
    ecuacion = sp.sympify(funcion)
    stringEcuacion = str(ecuacion)
    evaluada = eval(stringEcuacion)
    return evaluada


def montecarlo(nPuntos, intervaloInf, intevraloSup):
    ans = []
    plt_vals = []
    for i in range(nPuntos):

        ar = np.zeros(nPuntos)

        for i in range(len(ar)):
            ar[i] = random.uniform(intervaloInf, intevraloSup)

        integral = 0.0

        for i in ar:
            integral += f(i)

        ans.append((intevraloSup - intervaloInf) / float(nPuntos) * integral)


    areaFinal = ans[len(ans) - 1]

    return areaFinal

def graficar(nPuntos, intervaloInf, intevraloSup):
    plt_vals = []

    for i in range(nPuntos):
        ar = np.zeros(nPuntos)
        for i in range(len(ar)):
            ar[i] = random.uniform(intervaloInf, intevraloSup)
        integral = 0.0

        for i in ar:
            integral += f(i)
        ans = (intevraloSup - intervaloInf) / float(nPuntos) * integral
        plt_vals.append(ans)

    plt.title("Distribuciones de áreas calculada")
    X_opt = np.array(plt_vals, dtype=float)
    plt.hist(X_opt, bins=30, ec="black")
    plt.xlabel("Áreas")
    plt.show()

def integracionGeneral():

    #------------ para borrar lo que ya está calculado anteriormente----------

    valorAreaSalidaText.config(state=NORMAL)
    valorAreaSalidaText.delete(0, END)
    valorAreaSalidaText.config(state='readonly')

    # ------------ para borrar lo que ya está calculado anteriormente----------

    a = float(extremoIzqText.get())
    b = float(extremoDerText.get())
    n = int(numParticionesTexto.get())

    area_total = montecarlo(n, a, b)

    valorAreaSalidaText.config(state=NORMAL)
    valorAreaSalidaText.insert(0, str(area_total))
    valorAreaSalidaText.config(state=DISABLED)
    graficar(n, a, b)


# -------------------------------------------------------------------------------------------


# BOTONES

btnCalcular = Button(ventana, text="Calcular", width="10", font=("helvetica", 12, "bold"),
                     bg="LightSkyBlue1", fg="black", command=integracionGeneral)
btnCalcular.place(x=15, y=300)

btnBorrar = Button(ventana, text="Borrar", width="10", font=("helvetica", 12, "bold"),
                   bg="LightSkyBlue1", fg="black", command=borrar)
btnBorrar.place(x=155, y=300)

btnSalir = Button(ventana, text="Salir", width="10", font=("helvetica", 12, "bold"),
                  bg="LightSkyBlue1", fg="black", command=salir)
btnSalir.place(x=295, y=300)



borrar()
ventana.mainloop()
