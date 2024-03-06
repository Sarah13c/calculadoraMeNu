import tkinter
from tkinter import simpledialog, messagebox, Button, Entry
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import sympy as sp

import matplotlib.pyplot as plt
import numpy as np


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math as mt

# lf=["mt.sin(2*x)-(x**3)+1", "1 / (1 + mt.exp(-x))", "(x**3)+6", "mt.sin(2*x)"]

#lf = ["mt.exp(x-2)-mt.log(x)-2.5"]


def evaluar(funcion, x):
    var2 = eval(funcion)
    return var2

lf  = []
def recibirDatos():
        seguir = "yes"
        while seguir:
            lf.append(simpledialog.askstring("funciones", "Ingrese las funciones"))
            seguir = messagebox.askyesno("seguir", "Desea registrar otra Funcion?")

def graficar():

    # asignamos un rango de valores a graficar
    var = range(-10, 15)
    ecuacionEje = 'x*0'

    plt.plot(var, [evaluar(ecuacionEje, i) for i in var], color='black', label='eje x')
    for k in range(len(lf)):
        plt.plot(var, [evaluar(lf[k], i) for i in var], label=lf[k])
        """plt.plot(var,[evaluar(lf[1],i) for i in var], label= 'Funcion 1')
        plt.plot(var,[evaluar(lf[2],i) for i in var], label= lf[2])
        plt.plot(var,[evaluar(lf[3],i) for i in var], label= lf[3])"""
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        # colocamos la leyenda en la parte inferior derecha
        plt.legend(loc='lower right')
        plt.show()


# Interfaz gráfica
root = Tk()
root.title("Calculadora Método de New Raphson")
root.geometry("836x740")


errorToleranciaLabel = tkinter.Label(root, text="Error de tolerancia ET", width="17", font=("helvetica", 12, "bold"),
                                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
errorToleranciaLabel.place(x=15, y=108)


# Solo para mostrar

raizLabel = Label(root, text="Raíz", width="17", font=("helvetica", 12, "bold"),
                  padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
raizLabel.place(x=15, y=200)


errorTolerVar = tkinter.DoubleVar()



errorToleraEntry = Entry(root, textvariable=errorTolerVar, font=10, width=30)
errorToleraEntry.place(x=200, y=113)



# Botones

btnCalcular = Button(root, text="Recibir", width="10", font=("helvetica", 12, "bold"),
                     bg="LightSkyBlue1", fg="black", command=recibirDatos)
btnCalcular.place(x=60, y=150)

btnGrafica = Button(root, text="Graficar", width="10", font=("helvetica", 12, "bold"),
                  bg="LightSkyBlue1", fg="black", command=graficar)
btnGrafica.place(x=200, y=310)


root.mainloop()
