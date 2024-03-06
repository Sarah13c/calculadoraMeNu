from tkinter import *
import math

from matplotlib import pyplot as plt

ventana = Tk()
ventana.title("Graficadora")
ventana.geometry("900x680")
ventana.resizable(False, False)
ventana.configure(background="ivory3")

color_boton = "gray99"
ancho_boton = 10
alto_boton = 3
operador = ""
operador_grafica = ""
texto_pantalla = StringVar()


def clear():
    global operador
    global operador_grafica
    operador_grafica = ""
    operador = ""
    texto_pantalla.set("")


def click(b):
    global operador
    global operador_grafica
    operador_grafica += str(b)

    if b == "math.exp":
        b = "exp"
    if b == "math.sqrt":
        b = "√"
    if b == "math.pi":
        b = "π"
    if b == "math.log":
        b = "log"
    if b == "math.cos":
        b = "cos"
    if b == "math.sin":
        b = "sen"
    if b == "math.tan":
        b = "tan"



    operador += str(b)
    texto_pantalla.set(operador)



def evaluar(funcion, x):
    var2 = eval(funcion)
    return var2

def resultado():
    global operador
    global operador_grafica
    arreglo = [operador_grafica]
    lf = ["24.5*(x**7)-5.5*x*mt.exp(-x)-5"]
    var = range(-5, 20)
    try:
        ecuacionEje = 'x*0'
        plt.plot(var, [evaluar(ecuacionEje, i) for i in var], color='black', label='eje x')
        plt.plot(var, [evaluar(str(arreglo[0]), i) for i in var], label=str(arreglo[0]))
        #r = str(eval(operador))
        plt.xlim(-10, 10)
        # colocamos la leyenda en la parte inferior derecha
        plt.legend(loc='lower right')
        plt.show()
        print(operador_grafica)

    except:
        r = "ERROR"
        texto_pantalla.set(r)
        print(operador_grafica)


clear()
# BOTONES DE LA PRIMERA FILA
Boton0 = Button(ventana, text="0", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(0)).grid(row=1, column=0, pady=10)
Boton1 = Button(ventana, text="1", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(1)).grid(row=1, column=1, pady=10)
Boton2 = Button(ventana, text="2", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(2)).grid(row=1, column=2, pady=10)
Boton3 = Button(ventana, text="3", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(3)).grid(row=1, column=3, pady=10)
# BOTONES DE LA SEGUNDA FILA
Boton4 = Button(ventana, text="4", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(4)).grid(row=2, column=0, pady=10)
Boton5 = Button(ventana, text="5", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(5)).grid(row=2, column=1, pady=10)
Boton6 = Button(ventana, text="6", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(6)).grid(row=2, column=2, pady=10)
Boton7 = Button(ventana, text="7", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(7)).grid(row=2, column=3, pady=10)
# BOTONES DE LA TERCERA FILA
Boton8 = Button(ventana, text="8", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(8)).grid(row=3, column=0, pady=10)
Boton9 = Button(ventana, text="9", bg=color_boton, width=ancho_boton,
                height=alto_boton, command=lambda: click(9)).grid(row=3, column=1, pady=10)
BotonPi = Button(ventana, text="π", bg=color_boton, width=ancho_boton,
                 height=alto_boton, command=lambda: click("math.pi")).grid(row=3, column=2, pady=10)
BotonPunto = Button(ventana, text=".", bg=color_boton, width=ancho_boton,
                    height=alto_boton, command=lambda: click(".")).grid(row=3, column=3, pady=10)
# BOTONES DE LA CUARTA FILA
BotonSuma = Button(ventana, text="+", bg=color_boton, width=ancho_boton,
                   height=alto_boton, command=lambda: click("+")).grid(row=4, column=0, pady=10)
BotonResta = Button(ventana, text="-", bg=color_boton, width=ancho_boton,
                    height=alto_boton, command=lambda: click("-")).grid(row=4, column=1, pady=10)
BotonMult = Button(ventana, text="*", bg=color_boton, width=ancho_boton,
                   height=alto_boton, command=lambda: click("*")).grid(row=4, column=2, pady=10)
BotonDiv = Button(ventana, text="/", bg=color_boton, width=ancho_boton,
                  height=alto_boton, command=lambda: click("/")).grid(row=4, column=3, pady=10)
# BOTONES DE LA QUINTA FILA
BotonRaiz = Button(ventana, text="√", bg=color_boton, width=ancho_boton,
                   height=alto_boton, command=lambda: click("math.sqrt")).grid(row=5, column=0, pady=10)
BotonClear = Button(ventana, text="clear", bg=color_boton, width=ancho_boton,
                    height=alto_boton, command=clear).grid(row=7, column=2, pady=10)
BotonEXP = Button(ventana, text="exp", bg=color_boton, width=ancho_boton,
                  height=alto_boton, command=lambda: click("math.exp")).grid(row=5, column=2, pady=10)
BotonIgual = Button(ventana, text="=", bg=color_boton, width=ancho_boton,
                    height=alto_boton, command=resultado).grid(row=7, column=3, pady=10)
# BOTONES DE LA SEXTA FILA
BotonParenIzq = Button(ventana, text="(", bg=color_boton, width=ancho_boton,
                       height=alto_boton, command=lambda: click("(")).grid(row=7, column=0, pady=10)
BotonParenDer = Button(ventana, text=")", bg=color_boton, width=ancho_boton,
                       height=alto_boton, command=lambda: click(")")).grid(row=7, column=1, pady=10)
BotonMod = Button(ventana, text="%", bg=color_boton, width=ancho_boton,
                  height=alto_boton, command=lambda: click("%")).grid(row=5, column=1, pady=10)
BotonLN = Button(ventana, text="log", bg=color_boton, width=ancho_boton,
                 height=alto_boton, command=lambda: click("math.log")).grid(row=5, column=3, pady=10)

#BOTONES DE LA SEPTIMA FILA
BotonCos = Button(ventana, text="cos", bg=color_boton, width=ancho_boton,
                 height=alto_boton, command=lambda: click("math.cos")).grid(row=6, column=0, pady=10)
BotonSen= Button(ventana, text="sen", bg=color_boton, width=ancho_boton,
                 height=alto_boton, command=lambda: click("math.sin")).grid(row=6, column=1, pady=10)
BotonTan= Button(ventana, text="tan", bg=color_boton, width=ancho_boton,
                 height=alto_boton, command=lambda: click("math.tan")).grid(row=6, column=2, pady=10)
BotonX= Button(ventana, text="x", bg=color_boton, width=ancho_boton,
                 height=alto_boton, command=lambda: click("x")).grid(row=6, column=3, pady=10)

Pantalla = Entry(ventana, font=("arial", 20, "bold"), width=56,
                 borderwidth=10, background="light grey", textvariable=texto_pantalla)
Pantalla.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

ventana.mainloop()