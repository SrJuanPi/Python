from tkinter import *
from PIL import Image, ImageColor, ImageTk
import os

# Inicio del Programa
root = Tk()
root.title("Mario Bros: Character Selector")
ruta = os.path.dirname(__file__)
imagenes = os.path.join(ruta, "imagenes")
icon = os.path.join(imagenes, "icon.ico")
root.iconbitmap(icon)
root.configure(background="sky blue")

# Imagenes de Personajes
mario = ImageTk.PhotoImage(Image.open(os.path.join(imagenes, "mario.png")).resize((200,200)))
luigi = ImageTk.PhotoImage(Image.open(os.path.join(imagenes, "luigi.png")).resize((200,200)))
toad = ImageTk.PhotoImage(Image.open(os.path.join(imagenes, "toad.png")).resize((200,200)))
peach = ImageTk.PhotoImage(Image.open(os.path.join(imagenes, "peach.png")).resize((200,200)))
boton_img= ImageTk.PhotoImage(Image.open(os.path.join(imagenes, "button.png")))
# Marco
marco = LabelFrame(root, padx=10, pady=10, border=0, background="sky blue")
marco.pack(padx=10, pady=10)

# Labels
label_mario = Label(marco, image=mario, background="sky blue")
label_luigi = Label(marco, image=luigi, background="sky blue")
label_toad = Label(marco, image=toad, background="sky blue")
label_peach= Label(marco, image=peach, background="sky blue")

# Default
personaje = StringVar()
personaje.set("none")  # Inicializar con un valor que no coincida con ninguno de los valores de los radio-buttons
confirmar = Label(root, text="", font=("Axiforma", 12), foreground="red")

def opcion():
    x = personaje.get()
    if x == "none":
        confirmar.config(text="¡Tienes que escoger un personaje!", font=("Axiforma", 12), foreground="red", background="sky blue")
        confirmar.pack()
    else:
        confirmar.config(text="Conectando con el Servidor...", font=("Axiforma", 10), foreground="black",background="sky blue")
        confirmar.pack()
    print(x)

# Radio Buttons
radio_mario = Radiobutton(marco, text="Mario", variable=personaje, value="mario", command=None,
                          font=("Axiforma", 10), border=5, background="red2")
radio_luigi = Radiobutton(marco, text="Luigi", variable=personaje, value="luigi", command=None,
                          font=("Axiforma", 10), border=5, background="green3")
radio_toad = Radiobutton(marco, text="Toad", variable=personaje, value="toad", command=None,
                          font=("Axiforma", 10), border=5, background="light sky blue")
radio_peach = Radiobutton(marco, text="Peach", variable=personaje, value="peach", command=None,
                          font=("Axiforma", 10), border=5, background="hot pink")

jugar = Button(root, image=boton_img, command=opcion, border=0, background="sky blue", activebackground="sky blue")
# Grids
label_mario.grid(row=0, column=0)
radio_mario.grid(row=1 , column=0)

label_luigi.grid(row=0, column=1)
radio_luigi.grid(row=1 , column=1)

label_toad.grid(row=2, column=0)
radio_toad.grid(row=3, column=0)

label_peach.grid(row=2, column=1)
radio_peach.grid(row=3, column=1)

jugar.pack(padx=10, pady=10)
root.mainloop()