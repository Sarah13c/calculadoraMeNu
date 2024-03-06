import sympy as sp
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk


def salir():
    root.destroy()


def calcular():
    funcion = str(funcionEntry.get())

    numero = float(numeroEntry.get())

    x = sp.symbols('x')
    p_d = sp.diff(funcion, x)
    s_d = sp.diff(funcion, x, 2)
    r_pd = float(sp.diff(funcion, x).evalf(subs={x: numero}))
    r_sd = float(sp.diff(funcion, x, 2).evalf(subs={x: numero}))
    # p_d es primera derivada
    # s_d es Segunda derivada
    # r_pd resultado primera
    # r_sd resultado segunda
    primeraVar.set(str(r_pd))
    segundaVar.set(str(r_sd))



def borrar():
    funcionEntry.delete(0, END)
    numeroEntry.delete(0, END)
    primeraVar.set("")
    segundaVar.set("")


# Interfaz gráfica
root = Tk()
root.title("Calculadora de derivadas")
root.geometry("500x290")

# Labels de la parte izquierda
metodoLabel = Label(root, text="DERIVADAS", width="45", font=("helvetica", 12, "bold"),
                    padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
metodoLabel.place(x=15, y=12)

funcionLabel = Label(root, text="Función", width="17", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
funcionLabel.place(x=15, y=48)

x0Label = Label(root, text="Número (xₒ)", width="17", font=("helvetica", 12, "bold"),
                padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
x0Label.place(x=15, y=80)

# Solo para mostrar

primeraDerivadaLabel = Label(root, text="Primera derivada", width="17", font=("helvetica", 12, "bold"),
                             padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
primeraDerivadaLabel.place(x=15, y=190)

segundaDerivadaLabel = Label(root, text="Segunda derivada", width="17", font=("helvetica", 12, "bold"),
                             padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
segundaDerivadaLabel.place(x=15, y=220)

# Campos de texto
funcionVar = tkinter.StringVar()
numeroVar = tkinter.DoubleVar()

primeraVar = StringVar()
segundaVar = StringVar()

funcionEntry = Entry(root, textvariable=funcionVar, font=10, width=30)
funcionEntry.place(x=200, y=53)

numeroEntry = Entry(root, textvariable=numeroVar, font=10, width=30)
numeroEntry.place(x=200, y=83)

# Solo para mostrar
primeraDerivadaEntry = Entry(root, textvariable=primeraVar, font=10, width=30, state="readonly")
primeraDerivadaEntry.place(x=200, y=190)

segundaDerivadaEntry = Entry(root, textvariable=segundaVar, font=10, width=30, state="readonly")
segundaDerivadaEntry.place(x=200, y=220)

# Botones

btnCalcular = Button(root, text="Calcular", width="10", font=("helvetica", 12, "bold"),
                     bg="LightSkyBlue1", fg="black", command=calcular)
btnCalcular.place(x=60, y=130)

btnBorrar = Button(root, text="Borrar", width="10", font=("helvetica", 12, "bold"),
                   bg="LightSkyBlue1", fg="black", command=borrar)
btnBorrar.place(x=200, y=130)

btnSalir = Button(root, text="Salir", width="10", font=("helvetica", 12, "bold"),
                  bg="LightSkyBlue1", fg="black", command=salir)
btnSalir.place(x=340, y=130)

borrar()
root.mainloop()
