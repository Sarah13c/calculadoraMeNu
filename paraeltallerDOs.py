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
from math import log

#lf=["mt.sin(2*x)-(x**3)+1", "1 / (1 + mt.exp(-x))", "(x**3)+6", "mt.sin(2*x)"]
lf= ["mt.exp(-0.005*x)*(mt.cos(0.2*10**6-0.005*x**2)**0.5)-100"]
#lf= ["np.exp(x-2)-np.log(x)-2.5"]
#lf= ["np.exp(-x)+2*np.log(x)-1"]


def evaluar(funcion, x):
    var2 = eval(funcion)
    return var2



# asignamos un rango de valores a graficar
var = range(-1000, 1000)
ecuacionEje = 'x*0'
plt.plot(var, [evaluar(ecuacionEje, i) for i in var], color='black', label='eje x')
plt.axvline(0, color="black")
plt.plot(var, [evaluar(lf[0], i) for i in var], label=lf[0])
#plt.plot(var,[evaluar(lf[1],i) for i in var], label= lf[1])
#plt.plot(var,[evaluar(lf[2],i) for i in var], label= lf[2])
#plt.plot(var,[evaluar(lf[3],i) for i in var], label= lf[3])


plt.xlim(-10, 10)
plt.ylim(-10, 10)
# colocamos la leyenda en la parte inferior derecha
plt.legend(loc='lower right')
plt.show()
