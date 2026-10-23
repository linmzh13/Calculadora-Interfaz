import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("370x450")
ventana.resizable(False, False)

pantalla = tk.Entry(
    ventana,
    font=("Arial", 22),
    justify="right",
    bd=10
)
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

def escribir(numero):
    pantalla.insert(tk.END, numero)

def borrar():
    pantalla.delete(0, tk.END)

def borrar_uno():
    texto = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, texto[:-1])

def calcular():
    try:
        operacion = pantalla.get()
        resultado = eval(operacion)

        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))

    except ZeroDivisionError:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "No se puede dividir por cero")

    except Exception:
        pantalla.delete(0, tk.END)
        pantalla.insert(0, "Error")

botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("%", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for texto, fila, columna in botones:

    if texto == "=":
        boton = tk.Button(
            ventana,
            text=texto,
            font=("Arial", 16),
            width=5,
            height=2,
            command=calcular
        )
    else:
        boton = tk.Button(
            ventana,
            text=texto,
            font=("Arial", 16),
            width=5,
            height=2,
            command=lambda valor=texto: escribir(valor)
        )

    boton.grid(row=fila, column=columna, padx=3, pady=3)

boton_borrar = tk.Button(
    ventana,
    text="C",
    font=("Arial", 14),
    width=11,
    height=2,
    command=borrar
)
boton_borrar.grid(row=5, column=0, columnspan=2, padx=3, pady=5)

boton_borrar_uno = tk.Button(
    ventana,
    text="⌫",
    font=("Arial", 14),
    width=11,
    height=2,
    command=borrar_uno
)
boton_borrar_uno.grid(row=5, column=2, columnspan=2, padx=3, pady=5)

ventana.mainloop()