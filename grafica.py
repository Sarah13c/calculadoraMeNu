import numpy as np
import matplotlib.pyplot as plt
import graficadora as gf
import math as mt

listadoPuntosX = []
listadoPuntosY = []
listadoFunciones = ["mt.sin(2*x)"]


def graficar():
    try:
        print('grafico')
        print(listadoPuntosX)
        print(listadoPuntosY)
        # ax.scatter(x=self.listadoPuntosX,y=self.listadoPuntosY)
        for i in range(0, len(listadoFunciones)):
            print(listadoFunciones[i])
            color = colorAleatorio()[0]
            print(color, type(colorAleatorio()))
            gf.graficaParaGraficador(listadoFunciones[i], color, i)
        for i in range(0, len(listadoPuntosX)):
            color = colorAleatorio()[0]
            gf.graficarPunto(listadoPuntosX[i], listadoPuntosY[i], color)
        plt.grid()
        plt.legend()
        plt.xlim(-50, 50)
        plt.ylim(-50, 50)

        # plt.xticks(range(0,100))
        # plt.yticks(range(0,100))
        # print(self.listadoFunciones)
        plt.show()
    except:
        print('revisa los datos a graficar')


def colorAleatorio():
    import random
    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    return color


graficar()
