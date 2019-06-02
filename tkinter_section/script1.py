'''
This script allows to build e GUI using the
Tkinter library.
@author Rodriguez Acosta Ernesto Antonio
'''
from tkinter import *

window = Tk()
window.title("Tkinter GUI Demo")
window.geometry("")                     # Auto resize

def km_to_miles():
    t1.delete(1.0, END)                 # Delete all tesx from the widget

    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)               # Inserting text into the widget

# Adding widgets
b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)          # Entry widget
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)          # Text widget
t1.grid(row=0, column=2)

window.mainloop()
