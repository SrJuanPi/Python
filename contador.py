from tkinter import *
import os
app = Tk()
app.title("CONTADOR")
app.geometry("300x200")
ruta = os.path.dirname(__file__)
ruta = os.path.join(ruta, "imagenes")
app.iconbitmap(os.path.join(ruta, "python-logo.ico"))
app.tk_bisque()

marco = LabelFrame(app, padx=15, pady=15, border=0)
marco.place(anchor="center", relx=0.5, rely=0.5,)

label = Label(marco, text="No has presionado el botón", font=("Axiforma", 10))
n = 0
def contador():
    global n # para poder acceder a varias globales :O
    n += 1
    label.config(text=f"Has presionado el botón {n} veces.")
label.pack()

boton = Button(marco, text="¡PRESIÓNAME!", command=contador,
               font=("Axiforma", 12), foreground="black",
               background="dark turquoise", border=3, height=3)
boton.pack()

app.mainloop()