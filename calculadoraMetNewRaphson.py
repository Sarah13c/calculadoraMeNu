import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import sympy as sp

import matplotlib.pyplot as plt
import numpy as np


def salir():
    root.destroy()


def primerDerivada(funcion1):
    funcion1 = funcion1.replace('math.', '')
    variable1 = 'x'
    imprimir1 = sp.diff(funcion1, variable1)
    return imprimir1


def calculoRaiz(funcion, x_0, Error_t):
    # funcion = traductor(funcion)
    raiz = 0
    x0 = float(x_0)
    tol = float(Error_t)
    x = sp.symbols('x')  # Crea variable x
    df = primerDerivada(funcion)
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('pi', 'math.pi')
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('acos', 'math.acos')
    df = str(df).replace('asin', 'math.asin')

    # sp.diff(funcion)  # Sacamos la derivada de la funcion
    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f
    df = sp.lambdify(x, df)  # Creamos simbolicamente a df
    contador = 1
    i = 1
    ri_arreglo = []
    ri_arreglo.append(0)
    conta = 0
    salir = False
    while salir == False:
        conta += 1
        xr = x0 - (f(x0) / df(x0))
        ri_arreglo.append(xr)
        E_r = abs((ri_arreglo[i - 1] - ri_arreglo[i]) / ri_arreglo[i])
        if i >= 50 or E_r < float(Error_t):
            raiz = xr
            salir = True
        else:
            x0 = xr
            i += 1
        paraLaTabla(conta, x0, xr)
    return raiz


def calculoContador(funcion, x_0, Error_t):
    # funcion = traductor(funcion)
    raiz = 0
    x0 = float(x_0)
    tol = float(Error_t)
    x = sp.symbols('x')  # Crea variable x
    df = primerDerivada(funcion)
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('pi', 'math.pi')
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('acos', 'math.acos')
    df = str(df).replace('asin', 'math.asin')

    # sp.diff(funcion)  # Sacamos la derivada de la funcion
    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f
    df = sp.lambdify(x, df)  # Creamos simbolicamente a df
    contador = 1
    i = 1
    ri_arreglo = []
    ri_arreglo.append(0)
    conta = 0
    salir = False
    while salir == False:
        conta += 1
        xr = x0 - (f(x0) / df(x0))
        ri_arreglo.append(xr)
        E_r = abs((ri_arreglo[i - 1] - ri_arreglo[i]) / ri_arreglo[i])
        if i >= 50 or E_r < float(Error_t):
            conta += 1
            raiz = xr
            salir = True
        else:
            x0 = xr
            i += 1

    return conta


# 50*ln(x)+5*x-160

# 0.5*exp(-x/2)-3.1415926*cos(x/2)

def calculoError(funcion, x_0, Error_t):
    # funcion=traductor(funcion)

    raiz = 0
    x0 = float(x_0)
    tol = float(Error_t)
    x = sp.symbols('x')  # Crea variable x
    df = primerDerivada(funcion)
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('acos', 'math.acos')
    df = str(df).replace('asin', 'math.asin')
    df = str(df).replace('pi', 'math.pi')

    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f
    df = sp.lambdify(x, df)  # Creamos simbolicamente a df
    i = 1
    ri_arreglo = []
    ri_arreglo.append(0)
    salida = 0
    salir = False
    while salir == False:
        xr = x0 - (f(x0) / df(x0))
        ri_arreglo.append(xr)
        E_r = abs((ri_arreglo[i - 1] - ri_arreglo[i]) / ri_arreglo[i])
        if i >= 50 or E_r < float(Error_t):
            raiz = xr
            salida = E_r
            salir = True
        else:
            x0 = xr
            i += 1

    return salida


def graficar():
    funcion = funcionEntry.get()
    x_0 = x0Entry.get()
    Error_t = errorToleraEntry.get()
    # funcion = traductor(funcion)
    raiz = 0
    x0 = float(x_0)
    tol = float(Error_t)
    x = sp.symbols('x')  # Crea variable x
    df = primerDerivada(funcion)
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('pi', 'math.pi')
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('acos', 'math.acos')
    df = str(df).replace('asin', 'math.asin')

    # sp.diff(funcion)  # Sacamos la derivada de la funcion
    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f
    df = sp.lambdify(x, df)  # Creamos simbolicamente a df
    contador = 1
    i = 1
    ri_arreglo = []
    ri_arreglo.append(0)
    conta = 0
    salir = False
    while salir == False:
        conta += 1
        xr = x0 - (f(x0) / df(x0))
        ri_arreglo.append(xr)
        E_r = abs((ri_arreglo[i - 1] - ri_arreglo[i]) / ri_arreglo[i])
        if i >= 50 or E_r < float(Error_t):
            raiz = xr
            salir = True
        else:
            x0 = xr
            i += 1

    # SALIDA

    # definición del intervalo

    x = np.arange(-3.0, 3.0, 0.2)
    plt.plot(x, df(x))
    plt.plot(x, 0 * x)
    plt.plot(x0, df(x0), 'bo', color="k")
    plt.show()
    # salida
    np.set_printoptions(precision=4)


def paraLaTabla(cont, xi, xnuevo):
    datosTabla.append((cont, xi, xnuevo))


def tabla():
    for dato in datosTabla:
        tablaD.insert('', tk.END, values=dato)


def calcular():
    funcion = funcionEntry.get()
    limite = x0Entry.get()
    errorTole = errorToleraEntry.get()
    # se hace los calculos respectivos con las variables anteriores
    cont = calculoContador(funcion, limite, errorTole)
    raiz = calculoRaiz(funcion, limite, errorTole)
    salida = calculoError(funcion, limite, errorTole)
    # se actualizan los label de los resultados, o sea ya muestran los resultados
    raizVar.set(str(raiz))
    errorRelVar.set(str(salida))
    numIterVar.set(str(cont - 1))


def borrar():
    funcionEntry.delete(0, END)
    x0Entry.delete(0, END)
    errorToleraEntry.delete(0, END)
    raizVar.set("")
    errorRelVar.set("")
    numIterVar.set("")
    tablaD.delete(*tablaD.get_children())
    datosTabla.clear()


# Interfaz gráfica
root = Tk()
root.title("Calculadora Método de New Raphson")
root.geometry("836x740")

# Labels de la parte izquierda
metodoLabel = Label(root, text="MÉTODO NEW RAPHSON", width="45", font=("helvetica", 12, "bold"),
                    padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
metodoLabel.place(x=15, y=12)

funcionLabel = Label(root, text="Función f(x)", width="17", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
funcionLabel.place(x=15, y=48)

x0Label = Label(root, text="xₒ", width="17", font=("helvetica", 12, "bold"),
                padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
x0Label.place(x=15, y=80)

errorToleranciaLabel = Label(root, text="Error de tolerancia ET", width="17", font=("helvetica", 12, "bold"),
                             padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
errorToleranciaLabel.place(x=15, y=108)

# Solo para mostrar

raizLabel = Label(root, text="Raíz", width="17", font=("helvetica", 12, "bold"),
                  padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
raizLabel.place(x=15, y=200)

errorRelativoLabel = Label(root, text="Error relativo", width="17", font=("helvetica", 12, "bold"),
                           padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
errorRelativoLabel.place(x=15, y=230)

iteracionesLabel = Label(root, text="Número de iteraciones", width="17", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
iteracionesLabel.place(x=15, y=260)

# Campos de texto
funcionVar = tkinter.StringVar()
xoVar = tkinter.DoubleVar()
errorTolerVar = tkinter.DoubleVar()

raizVar = StringVar()
errorRelVar = StringVar()
numIterVar = StringVar()

funcionEntry = Entry(root, textvariable=funcionVar, font=10, width=30)
funcionEntry.place(x=200, y=53)

x0Entry = Entry(root, textvariable=xoVar, font=10, width=30)
x0Entry.place(x=200, y=83)

errorToleraEntry = Entry(root, textvariable=errorTolerVar, font=10, width=30)
errorToleraEntry.place(x=200, y=113)

# Solo para mostrar
raizEntry = Entry(root, textvariable=raizVar, font=10, width=30, state="readonly")
raizEntry.place(x=200, y=200)

errorRelativoEntry = Entry(root, textvariable=errorRelVar, font=10, width=30, state="readonly")
errorRelativoEntry.place(x=200, y=230)

numIteracionesEntry = Entry(root, textvariable=numIterVar, font=10, width=30, state="readonly")
numIteracionesEntry.place(x=200, y=264)

# Botones

btnCalcular = Button(root, text="Calcular", width="10", font=("helvetica", 12, "bold"),
                     bg="LightSkyBlue1", fg="black", command=calcular)
btnCalcular.place(x=60, y=150)

btnBorrar = Button(root, text="Borrar", width="10", font=("helvetica", 12, "bold"),
                   bg="LightSkyBlue1", fg="black", command=borrar)
btnBorrar.place(x=200, y=150)

btnSalir = Button(root, text="Salir", width="10", font=("helvetica", 12, "bold"),
                  bg="LightSkyBlue1", fg="black", command=salir)
btnSalir.place(x=340, y=150)

btnTabla = Button(root, text="Tabla", width="10", font=("helvetica", 12, "bold"),
                  bg="LightSkyBlue1", fg="black", command=tabla)
btnTabla.place(x=200, y=380)

btnGrafica = Button(root, text="Graficar", width="10", font=("helvetica", 12, "bold"),
                    bg="LightSkyBlue1", fg="black", command=graficar)
btnGrafica.place(x=200, y=310)

# Para la tabla
columns = ('Iteraciones', 'xᵢ', 'n+1')

tablaD = ttk.Treeview(root, columns=columns, show='headings')

tablaD.heading('Iteraciones', text='Iteraciones')
tablaD.heading('xᵢ', text='xᵢ')
tablaD.heading('n+1', text='xₙ₊₁')
tablaD.heading('n+1', text='xₙ₊₁')
datosTabla = []

tablaD.place(x=12, y=440)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tablaD.yview)
tablaD.configure(yscroll=scrollbar.set)
scrollbar.place(x=818, y=440)

borrar()
root.mainloop()
