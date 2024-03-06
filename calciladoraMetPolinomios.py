import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import math

import numpy
import numpy as np
from sympy import *

#Creación ventana
ventana = tkinter.Tk()
ventana.geometry("460x500")


#Título
metodoLabel = Label(ventana, text="Calculadora de Polinomios", width="40", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove").place(x=15, y=12)


#Declaración de Labels Izquierda
funcLabel = Label(ventana, text="Ecuación", width="15", font=("helvetica", 12, "bold"),
                  padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 60)

xInicialLabel = Label(ventana, text="X inicial", width="15", font=("helvetica", 12, "bold"),
                  padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 100)

gradoLabel = Label(ventana, text="Grado de la función", width="15", font=("helvetica", 12, "bold"),
                  padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove").place(x=15, y= 200)


#VARIABLES CAMP TEXTO
funcVar = tkinter.StringVar()
gradoVar = tkinter.StringVar()
xInicialVar = tkinter.DoubleVar()



#ENTRADA
funcCampoTexto = Entry(ventana, textvariable=funcVar, font=10, width=26)
funcCampoTexto.place(x=185, y=64)

xInicialCampoTexto = Entry(ventana, textvariable=xInicialVar, font=10, width=26)
xInicialCampoTexto.place(x=185, y=104)


#SALIDA
gradoCampoTexto = Entry(ventana, textvariable=gradoVar, font=10, width=26, state= DISABLED)

gradoCampoTexto.place(x=185, y=205)

def borrar():
    funcCampoTexto.delete(0, END)
    gradoCampoTexto.config(state=NORMAL)
    gradoCampoTexto.delete(0, END)
    gradoCampoTexto.config(state=DISABLED)
    tablaD.delete(*tablaD.get_children())
    xInicialCampoTexto.delete(0, END)
    datosTabla.clear()

def salir():
    ventana.destroy()

def insert_asterisks(equation):
    return equation.replace('x', '*x')


def separarTerminos(polinomio:str) -> []:

    # quitar los space
    polinomio = polinomio.replace(' ','')

    terminoActual = ''
    terminos = []
    numeroParentesis = 0

    # Por cada caracter en polinomio
    for i in range(len(polinomio)):
        caracterActual = polinomio[i]

        # El primero caracter, siempre se agrega a terminoActual
        if i == 0:
            terminoActual = terminoActual + caracterActual

        # El ultimo caracter
        elif i == len(polinomio) - 1:
            terminoActual = terminoActual + caracterActual
            terminos.append(terminoActual)

        # Otros caracteres
        else:

            # Si se encuentra parentesis, actualizamos el valor de numeroParentesis
            if caracterActual == '(':
                numeroParentesis += 1
                terminoActual = terminoActual + caracterActual
            elif caracterActual == ')':
                numeroParentesis -= 1
                terminoActual = terminoActual + caracterActual

            # Si se encuentra operador '+' o '-'
            elif caracterActual == '+' or caracterActual == '-':

                # Si estamos dentro de parentesis
                if numeroParentesis > 0:
                    terminoActual = terminoActual + caracterActual

                # Si estamos fuera de parentesis, crea un nuevo termino
                else:
                    terminos.append(terminoActual)
                    terminoActual = caracterActual

            # Otros caracteres
            else:
                terminoActual = terminoActual + caracterActual

    return terminos

def encontrarX(termino):
    status = False
    pos = 0
    for i in range(len(termino)):
        if termino[i] == 'x':
            print(termino)
            pos = i
            print(pos)
            status == True
            return pos

    if status == False:
        return False


    #coef = termino[:pos-1]
    #print("COEFICIENTE")
    #print(coef)

    #grado = termino[pos-len(termino)+3:]
    #print("GRADO")
    #print(grado)

def extractorCoeficientes(funcion, grado):
    terminos = separarTerminos(funcion)
    aux = []
    coeficientes = numpy.zeros(shape=(grado+1))
    n = 1

    for i in terminos:
        x = encontrarX(i)
        print("ESTE ES X: ", x)
        print("ESTE ES EL TAMAÑO DEL TÉRMINO: ", len(i))
        #CUANDO EL TÉRMINO ES X
        if x == len(i) - 1:

            print("-------------------------------")
            print("TÉRMINO ", n)
            print("LINEAL")


            coef = float(i[:x-1])
            print("COEFICIENTE")
            print(coef)
            gradoC= 1
            print("GRADO")
            print(gradoC)
            n+=1

            coeficientes[abs(gradoC-grado)] = coef

        elif x == 0:

            print("-------------------------------")
            print("TÉRMINO ", n)
            print("SIN X")

            coef = float(i)
            print("COEFICIENTE")
            print(coef)
            gradoC= 0
            print("GRADO")
            print(gradoC)
            n+=1

            coeficientes[abs(gradoC-grado)] = coef

        else:

            print("-------------------------------")
            print("TÉRMINO ", n)
            print("MAYOR A 1")

            coef = float(i[:x-1])
            print("COEFICIENTE")
            print(coef)
            gradoC= int(i[x-len(i)+3:])
            print("GRADO")
            print(gradoC)
            n+=1

            coeficientes[abs(gradoC-grado)] = coef



    print("TERMINOS")
    print(terminos)

    print("ARRAY DE COEFICIENTES")
    print(coeficientes)

    for i in coeficientes:
        print(i)

    return coeficientes


def newtonHorner(grado, xo, poli):
    ite = 0
    tol =  1e-20
    e = 100
    nr = grado
    aux1 = (poli)
    aux2 = (poli)
    j = 1
    r = grado

    for k in range(nr):
        aux1 = (aux2)
        aux2 = ([1]*r)

        aux1[0]=float(poli[0])
        aux2[0]=float(poli[0])

        while e > tol:
            y=float(aux1[0])
            z=float(aux1[0])
            i=1
            while i<r:
                y=((float(xo)*y)+aux1[i])
                aux2[j]=y
                j+=1
                z=(float(xo)*z)+y
                i+=1
            y=(float(xo)*y)+aux1[-1]
            xnuevo=float(xo)-(y/z)
            e = abs((xnuevo-float(xo)))
            xo = xnuevo
            ite+=1
            j=1

        r-=1
        print("La raíz ", k+1, " es: ", xo)
        print("Las iteraciones fueron: ", ite)

        paraLaTabla(xo, "Real")
        e=100
        ite=0


def newtonHornerRoots(poli):
    raices = np.roots(poli)
    print("RAÍCES ROOTS")
    print(raices)

    for i in raices:
        if np.iscomplex(i) == False:
            paraLaTabla(i, "Real")
        elif np.iscomplex(i) == True:
            paraLaTabla(i, "Complejo")


def paraLaTabla(raiz, tipo):
    datosTabla.append((raiz, tipo))

def tabla():
    for dato in datosTabla:
        tablaD.insert('', tkinter.END, values=dato)

def calcular():

    x=Symbol('x')
    func = funcCampoTexto.get()
    #print(func)
    funcion = simplify(func)
    grado= degree(funcion)
    #print(funcion)
    #print(grado)

    xInicial = xInicialCampoTexto.get()

    gradoCampoTexto.config(state=NORMAL)
    gradoCampoTexto.insert(0, grado)
    gradoCampoTexto.config(state=DISABLED)

    print("------------------------------------------")
    #EXTRAER LOS COEFICIENTES EN ORDEN
    coeficientes = extractorCoeficientes(func,grado)
    print(extractorCoeficientes(func,grado))

    #SE EJECUTA EL MÉTODO DE NEWTON - HORNER
    #newtonHorner(grado, xInicial, coeficientes)
    newtonHornerRoots(coeficientes)
    tabla()


#2 COMPLEJAS 1 REAL 3*x**3-2

#BOTONES 1*x**3+7*x**2-6*x-72

btnCalcular = Button(ventana, text="Calcular", width="8", font=("helvetica", 12, "bold"),
                     bg="LightSkyBlue1", fg="black", command=calcular)
btnCalcular.place(x=50, y=150)

btnBorrar = Button(ventana, text="Borrar", width="8", font=("helvetica", 12, "bold"),
                   bg="LightSkyBlue1", fg="black", command=borrar)

btnBorrar.place(x=190, y=150)

btnSalir = Button(ventana, text="Salir", width="8", font=("helvetica", 12, "bold"),
                  bg="LightSkyBlue1", fg="black", command=salir)
btnSalir.place(x=330, y=150)



#Tabla

#Para la tabla
columns = ('Raíces', 'Tipo')

tablaD = ttk.Treeview(ventana, columns=columns, show='headings')

tablaD.heading('Raíces', text='Raíces')
tablaD.heading('Tipo', text='Tipo')
datosTabla = []

#tablaD.grid(padx=0, pady= 5, row=4, column=1)

scrollbar = ttk.Scrollbar(ventana, orient=tkinter.VERTICAL, command=tablaD.yview)
tablaD.configure(yscroll=scrollbar.set)
tablaD.place(x=25, y=260)
scrollbar.place(x=628,y=261)


ventana.mainloop()
