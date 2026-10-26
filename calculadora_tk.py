import tkinter as tk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora - Tkinter")
        self.root.geometry("320x420")
        self.root.resizable(False, False)
        self.root.config(bg="#222222")

        self.expression = ""
        self.text_input = tk.StringVar()
        
        self.entry = tk.Entry(
            root, 
            textvariable=self.text_input, 
            font=('Arial', 22, 'bold'), 
            bd=5, 
            relief=tk.FLAT, 
            justify='right', 
            bg="#121012", 
            fg="#ffffff"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=15)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                bg_color = "#7B074C"
                fg_color = "#ffffff"
                cmd = self.calcular
            elif text == 'C':
                bg_color = "#ff4fb0"
                fg_color = "#ffffff"
                cmd = self.limpiar
            elif text in ('/', '*', '-', '+'):
                bg_color = "#fc7fd0"
                fg_color = "#ffffff"
                cmd = lambda t=text: self.click_boton(t)
            else:
                bg_color = "#333333"
                fg_color = "#f8c6ee"
                cmd = lambda t=text: self.click_boton(t)

            btn = tk.Button(
                root, 
                text=text, 
                font=('Arial', 16, 'bold'), 
                bg=bg_color, 
                fg=fg_color, 
                bd=1, 
                relief=tk.RAISED,
                command=cmd
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

        for i in range(5):
            root.rowconfigure(i, weight=1)
        for i in range(4):
            root.columnconfigure(i, weight=1)

    def click_boton(self, value):
        if self.expression in ("Error", "Math Error"):
            self.expression = ""
            
        self.expression += str(value)
        self.text_input.set(self.expression)

    def limpiar(self):
        self.expression = ""
        self.text_input.set("")

    def calcular(self):
        try:
            if not self.expression:
                return
            result = str(eval(self.expression))
            self.text_input.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.text_input.set("Math Error")
            self.expression = "Math Error"
        except Exception:
            self.text_input.set("Error")
            self.expression = "Error"

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()