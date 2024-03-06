import tkinter
from tkinter import *
from tkinter import messagebox
import math


def salir():
    root.destroy()


def borrar():
    decimalEntry.delete(0, END)
    binariaEntry.delete(0, END)
    octalEntry.delete(0, END)
    hexadecimalEntry.delete(0, END)


def pruebaParaLeerDatosDecimalCalcular():
    if decimalEntry.get() != "":
        decimal = float(decimalEntry.get())
        binariaEntry.insert(0, decimal_a_bases(decimal, 2, "01"))
        octalEntry.insert(0, decimal_a_bases(decimal, 8, "01234567"))
        hexadecimalEntry.insert(0, decimal_a_bases(decimal, 16, "0123456789ABCDEF"))
    elif binariaEntry.get() != "":
        binario = str(binariaEntry.get())
        decimalEntry.insert(0, str(binario_a_decimal(binario, len(binario))))
        octalEntry.insert(0, binario_a_octal(binario))
        hexadecimalEntry.insert(0, binario_a_hexadecimal(binario))
    elif octalEntry.get() != "":
        octal = octalEntry.get()
        decimalEntry.insert(0, str(octal_a_decimal(octal)))
        binariaEntry.insert(0,str(octal_a_binario(octal)))
        hexadecimalEntry.insert(0,str( octal_a_hexadecimal(octal)))
    elif hexadecimalEntry.get() !="":
        hexadecimal = str(hexadecimalEntry.get())
        decimalEntry.insert(0, str(hexadecimal_a_decimal(hexadecimal)))
        binariaEntry.insert(0, str(hexadecimal_a_binario(hexadecimal)))
        octalEntry.insert(0, str(hexadecimal_a_octal(hexadecimal)))
    else:
        messagebox.showerror(message="Ingrese el valor a calcular", title="Error")

# --------DECIMAL A BASES--------
def decimal_a_bases(decimal, base, digitos):
    parte_fraccionaria, parte_entera = math.modf(decimal)
    parte_entera = int(parte_entera)
    cadena_parte_entera = ""
    cadena_parte_fraccionaria = ""
    while parte_entera > 0:
        residuo = parte_entera % base
        digito = digitos[int(residuo)]
        cadena_parte_entera += digito
        parte_entera = int(parte_entera / base)
    # Invertir cadena de parte entera
    cadena_parte_entera = cadena_parte_entera[::-1]
    sobrante = None
    while True:
        resultado = parte_fraccionaria * base
        parte_fraccionaria, sobrante = math.modf(resultado)
        digito = digitos[int(sobrante)]
        cadena_parte_fraccionaria += digito
        if parte_fraccionaria == 0:
            break
    return cadena_parte_entera + "." + cadena_parte_fraccionaria


def decimal_a_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal


def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


# --------BINARIO A BASES--------
def binario_a_decimal(binary, length):
    # Fetch the radix point
    point = binary.find('.')

    # Update point if not found
    if (point == -1):
        point = length

    intDecimal = 0
    fracDecimal = 0
    twos = 1

    # Convert integral part of binary
    # to decimal equivalent
    for i in range(point - 1, -1, -1):
        # Subtract '0' to convert
        # character into integer
        intDecimal += ((ord(binary[i]) -
                        ord('0')) * twos)
        twos *= 2

    # Convert fractional part of binary
    # to decimal equivalent
    twos = 2

    for i in range(point + 1, length):
        fracDecimal += ((ord(binary[i]) -
                         ord('0')) / twos)
        twos *= 2.0

    # Add both integral and fractional part
    ans = intDecimal + fracDecimal

    return ans


def binario_a_octal(binario):
    decimal = str(binario_a_decimal(binario, len(binario)))
    #pasamos del decimal al octal
    octal = decimal_a_bases(float(decimal), 8, "01234567")
    return octal

def binario_a_hexadecimal(binario):
    decimal = str(binario_a_decimal(binario, len (binario)))
    #pasamos del decimal al hexa
    hexadecimal = decimal_a_bases(float(decimal), 16, "0123456789ABCDEF")
    return hexadecimal

# --------OCTAL A BASES--------
def octal_a_decimal(octal):
    valor = 0
    for idx in range(len(octal)):
        if octal[idx] == '.':
            break
        valor = valor * 8 + int(octal[idx])

    fraccion = 1 / 8
    for idx in range(idx + 1, len(octal)):
        valor = valor + int(octal[idx]) * fraccion
        fraccion /= 8
    return valor

def octal_a_binario(octal):
    decimal = float(octal_a_decimal(octal))
    #pasar de decimal a binario
    binario = decimal_a_bases(float(decimal), 2, "01")
    return binario

def octal_a_hexadecimal(octal):
    decimal = float(octal_a_decimal(octal))
    #pasar de decimal a binario
    hexadecimal = decimal_a_bases(float(decimal), 16, "0123456789ABCDEF")
    return hexadecimal


# --------HEXADECIMAL A BASES--------
def hexadecimal_a_decimal(hexadecimal):
    valor = 0
    for idx in range(len(hexadecimal)):
        if hexadecimal[idx] == '.':
            break
        value = int(hexadecimal[idx], 16)
        valor = valor * 16 + value

    fraccion = 1 / 16
    for idx in range(idx + 1, len(hexadecimal)):
        value = int(hexadecimal[idx], 16)
        valor = valor + value * fraccion
        fraccion /= 16
    return valor


"""def octal_a_binario(octal):
    decimal = float(octal_a_decimal(octal))
    #pasar de decimal a binario
    binario = decimal_a_bases(float(decimal), 2, "01")
    return binario"""

def hexadecimal_a_binario(hexadecimal):
    decimal = float(hexadecimal_a_decimal(hexadecimal))
    #pasar de decimal a binario
    binario = decimal_a_bases(float(decimal), 2, "01")
    return binario

def hexadecimal_a_octal(hexadecimal):
    decimal = float(hexadecimal_a_decimal(hexadecimal))
    #pasar de decimal a binario
    octal = decimal_a_bases(float(decimal), 8, "01234567")
    return octal



#Interfaz gráfica
root = Tk()
root.title("Calculadora conversión de bases")
root.geometry("650x250")

# Labels de la parte izquierda
baseLabel = Label(root, text="Base", width="10", font=("helvetica", 12, "bold"),
                  padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
baseLabel.place(x=15, y=12)

decimalLabel = Label(root, text="Decimal", width="10", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
decimalLabel.place(x=15, y=48)

binariaLabel = Label(root, text="Binario", width="10", font=("helvetica", 12, "bold"),
                     padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
binariaLabel.place(x=15, y=78)

octalLabel = Label(root, text="Octal", width="10", font=("helvetica", 12, "bold"),
                   padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
octalLabel.place(x=15, y=108)

hexadecimalLabel = Label(root, text="Hexadecimal", width="10", font=("helvetica", 12, "bold"),
                         padx=5, pady=5, bg="ivory2", fg="black", borderwidth=2, relief="groove")
hexadecimalLabel.place(x=15, y=138)

# Label de la parte derecha

NumLabel = Label(root, text="Numero", width="49", font=("helvetica", 12, "bold"),
                 padx=5, pady=5, bg="LightSkyBlue1", fg="black", borderwidth=2, relief="groove")
NumLabel.place(x=130, y=12)

# Campos de texto
decimalVar = tkinter.DoubleVar()
binariaVar = tkinter.DoubleVar()
octalVar = tkinter.IntVar()
hexadecimalVar = tkinter.StringVar()

decimalEntry = Entry(root, textvariable=decimalVar, font=10, width=55)
decimalEntry.place(x=130, y=53)

binariaEntry = Entry(root, textvariable=binariaVar, font=10, width=55)
binariaEntry.place(x=130, y=83)

octalEntry = Entry(root, textvariable=octalVar, font=10, width=55)
octalEntry.place(x=130, y=113)

hexadecimalEntry = Entry(root, textvariable=hexadecimalVar, font=10, width=55)
hexadecimalEntry.place(x=130, y=143)

# Botones

btnCalcular = Button(root, text="Calcular", width="8", font=("helvetica", 12, "bold"),
                     bg="LightSkyBlue1", fg="black", command=pruebaParaLeerDatosDecimalCalcular)
btnCalcular.place(x=80, y=190)

btnBorrar = Button(root, text="Borrar", width="8", font=("helvetica", 12, "bold"),
                   bg="LightSkyBlue1", fg="black", command=borrar)
btnBorrar.place(x=210, y=190)

btnSalir = Button(root, text="Salir", width="8", font=("helvetica", 12, "bold"),
                  bg="LightSkyBlue1", fg="black", command=salir)
btnSalir.place(x=340, y=190)

borrar()
root.mainloop()
