from tkinter import *
from PIL import ImageTk, ImageColor, Image
import os

root = Tk()
root.title("User Login Window")
path = os.path.dirname(__file__)
root.iconbitmap(os.path.join(path, "icon.ico"))

logo = ImageTk.PhotoImage(Image.open(os.path.join(path, "pylogo.png")).resize((250, 250)))
show_logo = Label(root, image=logo, text="Tkinter Window", compound="left", font=("Axiforma", 30))
show_logo.pack()

user_label = Label(root, text="Username:", font=("Axiforma", 20))
user_label.pack()

user_input = Entry(root, border=3, font=("", 12))
user_input.insert(0, "Ex: Username")

def clear_user(x=False):
    if user_input.get() == "Ex: Username:" and x == False:
        user_input.delete(0, END)
    elif x:
        user_input.delete(0, END)
    else:
        pass

user_input.bind("<Button-1>", lambda x: clear_user())
user_input.pack()

password_label = Label(root, text="Password:", font=("Axiforma", 20))
password_label.pack()

password_input = Entry(root, border=3, font=("", 12))
password_input.insert(0, "*" * 7)

def clear_password(x=False):
    if password_input.get() == "*" * 7 and x == False:
        password_input.delete(0, END)
    elif x:
        password_input.delete(0, END)
    else:
        pass

password_input.bind("<Button-1>", lambda x: clear_password())
password_input.pack()

def submit():
    user = user_input.get()
    password = password_input.get()
    u = (user != "" and user != "Ex: Username:")
    c = (password != "" and password != "*" * 7)
    
    if u and c:
        clear_user(True)
        clear_password(True)
        submit_button.config(text="SENT!")
        print(f"Received.\nuser={user}\npassword={password}")
        user_input.insert(0, "Ex: Username:")
        password_input.insert(0, "*" * 7)
    else:
        submit_button.config(text="SEND")

submit_button = Button(root, command=submit, text="SEND", font=("Axiforma", 15), border=5, background="white")
submit_button.pack()

root.mainloop()

# DONE!