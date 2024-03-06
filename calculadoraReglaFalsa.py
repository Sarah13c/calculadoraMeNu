import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import sympy as sp


def salir():
    root.destroy()

def determinar_func(func, valor):
    ecuacion = sp.sympify(func)
    simbolo = sp.symbols('x')
    result = ecuacion.evalf(subs={simbolo: float(valor)})
    return result

def resultado_falsa_pos():
    func = funcionEntry.get()
    a = float(limInferiorEntry.get())
    b = float(limSuperiorEntry.get())
    error_accept = str(errorToleraEntry.get())

    resultado = metodo_falsa_posicion(func, a, b, error_accept)
    print(resultado)

def metodo_falsa_posicion(func, xi, xf, error):

    ri = 0
    conta = 0
    error_calculado = 1
    iteracion = []
    raiz = []
    relativo = []
    ite = 50
    if float(determinar_func(func, xi)) * float(determinar_func(func, xf)) <= 0:
        while conta < ite and float(error_calculado) > float(error):
            conta += 1
            ri = float((float(xf)) - ((float(determinar_func(func, xf)) * (float(xf) - float(xi))) / (
                    float(determinar_func(func, xf)) - float(determinar_func(func, xi)))))
            error_calculado = abs((float(ri) - float(xi)) / float(ri))
            iteracion.append(conta)
            raiz.append(ri)
            relativo.append(error_calculado)
            if float(determinar_func(func, xi)) * float(determinar_func(func, ri)) > 0:
                xi = ri
            else:
                xf = ri

            paraLaTabla(conta, ri, error_calculado, xi, xf)
        matriz = []
        filas = conta
        for i in range(filas):
            fila = ["Iteracion: ", iteracion[i], "Raiz: ", raiz[i], 'Error: ', relativo[i]]
            matriz.append(fila)

        raizVar.set(str(ri))
        errorRelVar.set(str(relativo[len(relativo)-1]))
        numIterVar.set(str(conta))
        return '{:.5f}'.format(ri), '{:.8f}'.format(error_calculado), conta, matriz


    else:
        raizVar.set(str(ri))
        errorRelVar.set(str(relativo[len(relativo)-1]))
        numIterVar.set(str(conta))
        return False, False



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
metodoLabel = Label(root, text="MÉTODO DE REGLA FALSA", width="45", font=("helvetica", 12, "bold"),
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
                     bg="LightSkyBlue1", fg="black", command=resultado_falsa_pos)
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

func = "exp(x-2)-ln(x)-2.5"
print(resultado_falsa_pos(func,3,4,0.0001))