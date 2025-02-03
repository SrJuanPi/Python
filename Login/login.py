from tkinter import *
from PIL import ImageTk, ImageColor, Image
import os

root = Tk()
root.title("User Login Window")
ruta = os.path.dirname(__file__)
root.iconbitmap(os.path.join(ruta, "icon.ico"))

logo = ImageTk.PhotoImage(Image.open(os.path.join(ruta, "pylogo.png")).resize((250,250)))
mostrarlogo = Label(root, image=logo, text="Tkinter Window", compound="left", font=("Axiforma", 30))
mostrarlogo.pack()

usuariolbl = Label(root, text="Usuario:", font=("Axiforma", 20))
usuariolbl.pack()

usuario_input = Entry(root, border=3, font=("", 12))
usuario_input.insert(0, "Ej: Robert399_")
def borrar_usuario(x=False):
    if usuario_input.get() == "Ej: Robert399_" and x==False:
        usuario_input.delete(0,END)
    elif x:
        usuario_input.delete(0,END)
    else:pass
usuario_input.bind("<Button-1>", lambda x:borrar_usuario())
usuario_input.pack()

contrasenalbl = Label(root, text="Contraseña:", font=("Axiforma", 20))
contrasenalbl.pack()

contrasena_input = Entry(root, border=3, font=("", 12))
contrasena_input.insert(0, "*"*7)
def borrar_contraseña(x=False):
    if contrasena_input.get() == "*"*7 and x==False:
        contrasena_input.delete(0,END)
    elif x:
        contrasena_input.delete(0,END)
    else:pass
contrasena_input.bind("<Button-1>", lambda x:borrar_contraseña())
contrasena_input.pack()

def Enviar():
    usuario = usuario_input.get()
    contrasena = contrasena_input.get()
    u = (usuario != "" and usuario != "Ej: Robert399_")
    c = (contrasena != "" and contrasena != "*"*7)
    
    if u and c:
        borrar_usuario(True)
        borrar_contraseña(True)
        enviar_boton.config(text="ENVIADO!")
        print(f"Recibido.\nusuario={usuario}\ncontraseña={contrasena}")
        usuario_input.insert(0, "Ej: Robert399_")
        contrasena_input.insert(0, "*"*7)
        
    else:enviar_boton.config(text="ENVIAR")
    
enviar_boton = Button(root, command=Enviar,text="ENVIAR", font=("Axiforma", 15), border=5, background="white")
enviar_boton.pack()

root.mainloop()

# LIIISTOOOOOOOO