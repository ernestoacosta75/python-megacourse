'''
This program expects a kilogram input value and converts
that value to grams, pounds, and ounces when the user
pushes the Convert button.

@author Rodriguez Acosta Ernesto Antonio
'''

from tkinter import *

window = Tk()
window.title("Kg-Converter")
window.geometry("")                     # Auto resize

def kg_converter():
    print(kg_entry_value.get())

    txt_grams.delete(1.0, END)
    txt_pounds.delete(1.0, END)
    txt_ounces.delete(1.0, END)

    kg_to_grams = float(kg_entry_value.get()) * 1000
    kg_to_pounds = float(kg_entry_value.get()) * 2.20462
    kg_to_ounces = float(kg_entry_value.get()) * 35.274

    txt_grams.insert(END,kg_to_grams)
    txt_pounds.insert(END,kg_to_pounds)
    txt_ounces.insert(END,kg_to_ounces)

kg_label = Label(window, text="Kg")
kg_label.grid(row=0, column=0)

kg_entry_value = StringVar()

kg_entry = Entry(window, textvariable=kg_entry_value)
kg_entry.grid(row=0, column=1)

btn_convert = Button(window, text="Convert", justify=LEFT, command=kg_converter)
btn_convert.grid(row=0, column=2)

txt_grams = Text(window, height=1, width=20)
txt_grams.grid(row=1, column=0)

txt_pounds = Text(window, height=1, width=20)
txt_pounds.grid(row=1, column=1)

txt_ounces = Text(window, height=1, width=20)
txt_ounces.grid(row=1, column=2)

window.mainloop()