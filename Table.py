from tkinter import *
root = Tk()
# root.geometry("190x100")

# This is a single-line comment
"""
    And this is a multi-line comment.
    I knew it was used for multi-line strings,
    but I didn't know it could be used as a comment :o
"""

lbl_first_name = Label(root, text="First name:").grid(row=0, column=0)
lbl_last_name = Label(root, text="Last name:").grid(row=1, column=0)
lbl_age = Label(root, text="Age:").grid(row=2, column=0)

entry_first_name = Entry(root)
entry_last_name = Entry(root)
entry_age = Entry(root)

entry_first_name.grid(row=0, column=1)
entry_last_name.grid(row=1, column=1)
entry_age.grid(row=2, column=1)

def show_phrase():
    first = entry_first_name.get().strip()
    last = entry_last_name.get().strip()
    age = entry_age.get().strip()
    valid_age = age.isdigit()
    if (first != "" and last != "") and valid_age:
        Label(root, text=f"My name is {first.capitalize()} {last.capitalize()} and I am {age} years old.").grid(row=4, column=1)
    elif first == "" and last != "" and valid_age:
        Label(root, text=f"My last name is {last.capitalize()} and I am {age} years old.").grid(row=4, column=1)
    elif first != "" and last == "" and valid_age:
        Label(root, text=f"My name is {first.capitalize()} and I am {age} years old.").grid(row=4, column=1)
    else:
        pass

Button(root, text="SUBMIT", command=show_phrase).grid(row=3, column=1)

root.mainloop()