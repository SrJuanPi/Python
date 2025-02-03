from tkinter import *
root = Tk()
# root.geometry("190x100")

# Esto es un comentario single-line
""" 
    Y esto es un       Sabía que servía para variables de
    comentario         múltiples líneas, pero no sabía que
    multi-line         se podía usar como comentario :o
"""

txt_nombre = Label(root, text="Nombre:").grid(row=0, column=0)
txt_apellido = Label(root, text="Apellido:").grid(row=1, column=0)
txt_edad = Label(root, text="Edad:").grid(row=2, column=0)

input_nombre = Entry(root)
input_apellido = Entry(root)
input_edad = Entry(root)

input_nombre.grid(row=0, column=1)
input_apellido.grid(row=1, column=1)
input_edad.grid(row=2, column=1)

def mostrar_frase():
    nombre = input_nombre.get()
    apellido = input_apellido.get()
    edad = input_edad.get()
    confirm = edad.isdigit()
    if (nombre != "" and apellido != "") and confirm:
        Label(root, text=f"Mi nombre es {nombre.capitalize()} {apellido.capitalize()} y tengo {edad} años.").grid(row=4, column=1)
    elif nombre == "" and apellido != "" and confirm:
        Label(root, text=f"Mi apellido es {apellido.capitalize()} y tengo {edad} años.").grid(row=4, column=1)
    elif nombre != "" and apellido == "" and confirm:
        Label(root, text=f"Mi nombre es {nombre.capitalize()} y tengo {edad} años.").grid(row=4, column=1)
    else: pass

Button(root, text="ENVIAR", command=mostrar_frase).grid(row=3, column=1)

root.mainloop()