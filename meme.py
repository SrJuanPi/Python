from tkinter import *
import os
from PIL import ImageTk, Image, ImageColor

root = Tk()
root.title("Curso Python PFacil")

# ruta = os.path.dirname("C:/users/juanp/workspace/cursos/python/pfacil")
ruta_principal = os.path.dirname(__file__)
ruta_imagenes = os.path.join(ruta_principal, "imagenes")

root.iconbitmap(os.path.join(ruta_imagenes, "python-logo.ico"))

meme = ImageTk.PhotoImage(Image.open(os.path.join(ruta_imagenes, "meme-redondeado.png")))
etiqueta = Label(root, image=meme)
etiqueta.pack()

root.mainloop() 