import tkinter as tk

class Calculadora:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora - Tkinter")
        self.raiz.geometry("320x420")
        self.raiz.resizable(False, False)
        self.raiz.config(bg="#222222")

        self.expresion = ""
        self.entrada_texto = tk.StringVar()
        
        self.pantalla = tk.Entry(
            raiz, 
            textvariable=self.entrada_texto, 
            font=('Arial', 22, 'bold'), 
            bd=5, 
            relief=tk.FLAT, 
            justify='right', 
            bg="#121012", 
            fg="#ffffff"
        )
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=15)

        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (texto, fila, columna) in botones:
            if texto == '=':
                color_fondo = "#7B074C"
                color_texto = "#ffffff"
                comando = self.calcular
            elif texto == 'C':
                color_fondo = "#ff4fb0"
                color_texto = "#ffffff"
                comando = self.limpiar
            elif texto in ('/', '*', '-', '+'):
                color_fondo = "#fc7fd0"
                color_texto = "#ffffff"
                comando = lambda t=texto: self.click_boton(t)
            else:
                color_fondo = "#333333"
                color_texto = "#f8c6ee"
                comando = lambda t=texto: self.click_boton(t)

            boton = tk.Button(
                raiz, 
                text=texto, 
                font=('Arial', 16, 'bold'), 
                bg=color_fondo, 
                fg=color_texto, 
                bd=1, 
                relief=tk.RAISED,
                command=comando
            )
            boton.grid(row=fila, column=columna, sticky="nsew", padx=4, pady=4)

        for i in range(5):
            raiz.rowconfigure(i, weight=1)
        for i in range(4):
            raiz.columnconfigure(i, weight=1)

    def click_boton(self, valor):
        if self.expresion in ("Error", "Math Error"):
            self.expresion = ""
            
        self.expresion += str(valor)
        self.entrada_texto.set(self.expresion)

    def limpiar(self):
        self.expresion = ""
        self.entrada_texto.set("")

    def calcular(self):
        try:
            if not self.expresion:
                return
            resultado = str(eval(self.expresion))
            self.entrada_texto.set(resultado)
            self.expresion = resultado
        except ZeroDivisionError:
            self.entrada_texto.set("Math Error")
            self.expresion = "Math Error"
        except Exception:
            self.entrada_texto.set("Error")
            self.expresion = "Error"

if __name__ == "__main__":
    raiz = tk.Tk()
    app = Calculadora(raiz)
    raiz.mainloop()