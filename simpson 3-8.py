import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import tkinter
from tkinter import *
from numpy import linspace
from sympy.abc import x
from sympy import integrate, exp, sin, cos, pi

# Creación ventana
from sympy import integrate

ventana = tkinter.Tk()
ventana.title("Integración por Simpson 3/8")
ventana.geometry("450x530")

# Título
integracionLabel = Label(ventana, text="Integración numérica por Simpson 3/8 ", width="40",
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
errorSalidaLabel = Label(ventana, text="Error", width="15", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(
    x=15, y=460)

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
errorIntegralSalida = tkinter.DoubleVar()
valorAreaSalida = tkinter.DoubleVar()

# SALIDA
valorAreaSalidaText = Entry(ventana, textvariable=valorAreaSalida, font=10, width=26, state='readonly')
valorAreaSalidaText.place(x=185, y=425)

errorIntegralSalidaText = Entry(ventana, textvariable=errorIntegralSalida, font=10, width=26, state='readonly')
errorIntegralSalidaText.place(x=185, y=465)


# --------------------------------------------------------------------------------------------------------

# FUNCIONES


def borrar():
    funcCampoTexto.delete(0, END)
    extremoIzqText.delete(0, END)
    extremoDerText.delete(0, END)
    numParticionesTexto.delete(0, END)

    errorIntegralSalidaText.config(state=NORMAL)
    errorIntegralSalidaText.delete(0, END)
    errorIntegralSalidaText.config(state='readonly')

    valorAreaSalidaText.config(state=NORMAL)
    valorAreaSalidaText.delete(0, END)
    valorAreaSalidaText.config(state='readonly')

#(x*0.5-1/3)*exp(-0.5*x**2)+sin(3.1415926/2*x)
#-2.0978423 izq
#0.1606918
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


def simpson38(f, a, b):
    m1 = ((2 * a + b) / 3)
    m2 = ((a + 2 * b) / 3)
    integral = ((b - a) / 8) * (f(a) + 3 * f(m1) + 3 * f(m2) + f(b))
    return integral

def obtenerArea(a,b,n):
    h = ((b - a) / n)
    suma = 0
    for i in range(n):
        b = a + h
        area = simpson38(f, a, b)
        suma = suma + area
        a = b
    return suma


def calculo_error(a,b,n):
    suma = obtenerArea(a,b,n)
    integralBonita = integrate(funcCampoTexto.get(), (x, a, b))
    print(integralBonita, type(integralBonita))
    print(float(integralBonita))
    print(suma)
    print(suma,type(suma), "suma")
    errorPorcentual = abs((integralBonita - suma) / integralBonita)
    return errorPorcentual


def integracionGeneral():

    #------------ para borrar lo que ya está calculado anteriormente----------
    errorIntegralSalidaText.config(state=NORMAL)
    errorIntegralSalidaText.delete(0, END)
    errorIntegralSalidaText.config(state='readonly')

    valorAreaSalidaText.config(state=NORMAL)
    valorAreaSalidaText.delete(0, END)
    valorAreaSalidaText.config(state='readonly')

    # ------------ para borrar lo que ya está calculado anteriormente----------

    a = float(extremoIzqText.get())
    b = float(extremoDerText.get())
    n = int(numParticionesTexto.get())

    area = obtenerArea(a,b,n)
    area_float = float(area)


    error = calculo_error(a,b,n)
    error_float = float(error)

    errorIntegralSalidaText.config(state=NORMAL)
    errorIntegralSalidaText.insert(0, str(error_float))
    errorIntegralSalidaText.config(state=DISABLED)

    valorAreaSalidaText.config(state=NORMAL)
    valorAreaSalidaText.insert(0, str(area_float))
    valorAreaSalidaText.config(state=DISABLED)



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
