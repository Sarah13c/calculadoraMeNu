import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import sympy as sp

def salir():
    root.destroy()

def determinarFunc(func,valor):
    ecuacion = sp.sympify(func)
    simbolo = sp.symbols('x')
    result = ecuacion.evalf(subs={simbolo:float(valor)})
    return result

def calcular():
    func = funcionEntry.get()
    inferior = float(limInferiorEntry.get())
    superior = float(limSuperiorEntry.get())
    error_accept = str(errorToleraEntry.get())

    num_iter = 50
    f_x_2 = 0

    for i in range(1, num_iter, 1):
        f_x_1 = float(determinarFunc(func, inferior))
        f_x_2 = float(determinarFunc(func, superior))
        paraLaTabla(i,superior, f_x_2, inferior, superior)
        print(f"{i} iteracion, raiz:  {superior}, error relativo: {f_x_2}")
        if abs(f_x_2) < float(error_accept):
            break


        raiz = superior - f_x_2 * ((superior - inferior) / (f_x_2 - f_x_1))
        inferior = superior
        superior = raiz

        print(f"Your root is located at: [{superior} , {f_x_2} ]")


    raizVar.set(str(superior))
    errorRelVar.set(str(f_x_2))
    numIterVar.set(str(len(datosTabla)))


def resultado_secante(funcion,xi,xf,et):
    result,error, cont, matriz = metodo_secante(funcion,xi,xf,et)

def metodo_secante(func,xi,xf,error_tol):
    funcion = str(func)
    x0 = float(xi)
    x1 = float(xf)
    tolerancia = float(error_tol)
    raiz = 0
    i = 0
    error = 1
    iteracion = []
    raizAr = []
    relativo = []
    while float(error) > float(tolerancia) and i <= 50:
        raiz = float(float(x1) * float(determinarFunc(funcion, x0)) - float(x0) *float(determinarFunc(funcion, x1))) / (
            float(determinarFunc(funcion, x0)) - float(determinarFunc(funcion, x1)))
        error = abs((float(x1) - float(raiz)) / float(raiz))
        x0 = float(x1)
        x1 = float(raiz)
        i = i + 1
        iteracion.append(i)
        raizAr.append(raiz)
        relativo.append(error)
    matriz = []
    filas = i
    for i in range(filas):
        fila = ["Iteracion: ", iteracion[i], "Raiz: ", raizAr[i], 'Error: ', relativo[i]]
        matriz.append(fila)
    return '{:.5f}'.format(raiz), '{:.10f}'.format(error), i, matriz

def paraLaTabla(iteraciones, raiz, errorRela, extremoInfe, extremoSupe):
    datosTabla.append((iteraciones, raiz,errorRela, extremoInfe, extremoSupe))

def tabla():
    for dato in datosTabla:
        tablaD.insert('', tk.END, values=dato)

def borrar():
    funcionEntry.delete(0, END)
    limInferiorEntry.delete(0, END)
    limSuperiorEntry.delete(0, END)
    errorToleraEntry.delete(0, END)
    raizVar.set("")
    errorRelVar.set("")
    numIterVar.set("")
    tablaD.delete(*tablaD.get_children())
    datosTabla.clear()

#Interfaz gráfica
root = Tk()
root.title("Calculadora conversión de bases")
root.geometry("1050x740")

# Labels de la parte izquierda
metodoLabel = Label(root, text="MÉTODO DE LA SECANTE", width="45", font=("helvetica", 12, "bold"),
                  padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
metodoLabel.place(x=15, y=12)

funcionLabel = Label(root, text="Función f(x)", width="17", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
funcionLabel.place(x=15, y=48)

intervalLabel = Label(root, text="Intérvalo:", width="17", font=("helvetica", 11, "bold"),
                     padx=5, pady=5, fg="black")
intervalLabel.place(x=15, y=80)

inferiorLabel = Label(root, text="Límite inferior  a", width="17", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
inferiorLabel.place(x=15, y=108)

superiorLabel = Label(root, text="Límite superior  b", width="17", font=("helvetica", 12, "bold"),
                   padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
superiorLabel.place(x=15, y=138)

errorToleranciaLabel = Label(root, text="Error de tolerancia ET", width="17", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
errorToleranciaLabel.place(x=15, y=168)


#Solo para mostrar

raizLabel = Label(root, text="Raíz", width="17", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
raizLabel.place(x=15, y=270)

errorRelativoLabel = Label(root, text="Error relativo", width="17", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
errorRelativoLabel.place(x=15, y=300)

iteracionesLabel = Label(root, text="Número de iteraciones", width="17", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
iteracionesLabel.place(x=15, y=330)


#Campos de texto
funcionVar = tkinter.DoubleVar()
inferiorVar = tkinter.DoubleVar()
superiorVar = tkinter.DoubleVar()
errorTolerVar = tkinter.DoubleVar()

raizVar = StringVar()
errorRelVar = StringVar()
numIterVar= StringVar()

funcionEntry = Entry(root, textvariable=funcionVar, font=10, width=30)
funcionEntry.place(x=200, y=53)

limInferiorEntry = Entry(root, textvariable=inferiorVar, font=10, width=30)
limInferiorEntry.place(x=200, y=113)

limSuperiorEntry = Entry(root, textvariable=superiorVar, font=10, width=30)
limSuperiorEntry.place(x=200, y=143)

errorToleraEntry = Entry(root, textvariable=errorTolerVar, font=10, width=30)
errorToleraEntry.place(x=200, y=173)


raizEntry = Entry(root, textvariable=raizVar, font=10, width=30, state="readonly")
raizEntry.place(x=200, y=270)

errorRelativoEntry = Entry(root, textvariable=errorRelVar, font=10, width=30, state="readonly")
errorRelativoEntry.place(x=200, y=305)

numIteracionesEntry = Entry(root, textvariable=numIterVar, font=10, width=30, state="readonly")
numIteracionesEntry.place(x=200, y=335)


# Botones

btnCalcular = Button(root, text="Calcular", width="10", font=("helvetica", 12, "bold"),
                     bg="LightSkyBlue1", fg="black", command=calcular)
btnCalcular.place(x=60, y=215)

btnBorrar = Button(root, text="Borrar", width="10", font=("helvetica", 12, "bold"),
                   bg="LightSkyBlue1", fg="black", command=borrar)
btnBorrar.place(x=200, y=215)

btnSalir = Button(root, text="Salir", width="10", font=("helvetica", 12, "bold"),
                  bg="LightSkyBlue1", fg="black", command=salir)
btnSalir.place(x=340, y=215)


btnTabla = Button(root, text="Tabla", width="10", font=("helvetica", 12, "bold"),
                  bg="LightSkyBlue1", fg="black", command=tabla)
btnTabla.place(x=200, y=380)


#Para la tabla
columns = ('Iteraciones', 'Raíz', 'Error relativo', 'Límite inferior', 'Límite superior')

tablaD = ttk.Treeview(root, columns=columns, show='headings')

tablaD.heading('Iteraciones', text='Iteraciones')
tablaD.heading('Raíz', text='Raíz')
tablaD.heading('Error relativo', text='Error relativo')
tablaD.heading('Límite inferior', text='Límite inferior')
tablaD.heading('Límite superior', text='Límite superior')
datosTabla = []


tablaD.place(x=12, y=440)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tablaD.yview)
tablaD.configure(yscroll=scrollbar.set)
scrollbar.place(x=1015, y=440)

borrar()
root.mainloop()
