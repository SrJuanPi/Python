from tkinter import *
from PIL import Image, ImageColor, ImageTk
import os

# Resources
main = os.path.dirname(__file__)
# icons = os.path.join(main, "icons")
# images = os.path.join(main, "images")

# Init
root = Tk()
root.title("BMI")
root.resizable(False,False)
# root.iconbitmap(os.path.join(icons, "logo.ico"))

# Window Display Orentation Function (init)
bg = LabelFrame(root, background="gray75")
bg.pack(padx=10, pady=10, fill="both", expand=True)

vertical = Button(bg, text="Vertical", border=5, height=5, width=12, anchor="center",
                  command=None)
vertical.grid(row=0,column=0, padx=20, pady=20)
horizontal = Button(bg, text="Horizontal", border=5, height=5, width=12, anchor="center",
                    command=None)
horizontal.grid(row=0,column=1, padx=20, pady=20)

# Vertical Mode

# Horizontal Mode

root.mainloop()