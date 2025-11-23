from tkinter import *
from pathlib import Path
import os

app = Tk()
app.title("COUNTER")
app.geometry("300x200")
app.resizable(False, False)  # disable window resizing for consistent layout

# try to load icon safely
img_dir = Path(__file__).parent / "imagenes"
icon_path = img_dir / "python-logo.ico"
try:
    if icon_path.exists():
        app.iconbitmap(str(icon_path))
except Exception:
    pass  # ignore icon errors

frame = LabelFrame(app, padx=15, pady=15, border=0)
frame.place(anchor="center", relx=0.5, rely=0.5)

# use IntVar to avoid globals and keep state in Tk variable
count = IntVar(value=0)

label = Label(frame, text="You haven't pressed the button yet", font=("Axiforma", 10))
label.pack()

def increment(event=None):
    """Increase the counter and update the label (can be called from button or Enter key)."""
    count.set(count.get() + 1)
    times = count.get()
    plural = "time" if times == 1 else "times"
    label.config(text=f"You have pressed the button {times} {plural}.")

# main button
button = Button(
    frame,
    text="CLICK ME!",
    command=increment,
    font=("Axiforma", 12),
    fg="black",
    bg="dark turquoise",
    bd=3,
    height=3,
)
button.pack()

# Bind Enter key to increment so keyboard works too
app.bind("<Return>", increment)

app.mainloop()