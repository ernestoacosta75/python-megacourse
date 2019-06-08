'''
This program stores book information:

Title, Author
Year, ISBN

The user can:

View all records
Search an entry
Add entry
Update entry
Delete entry
Close

'''
from tkinter import *
from tkinter import messagebox

import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index = books_listbox.curselection()[0]
        selected_tuple = books_listbox.get(index)

        title_entry.delete(0, END)
        author_entry.delete(0, END)
        year_entry.delete(0, END)
        isbn_entry.delete(0, END)

        title_entry.insert(END, selected_tuple[1])
        author_entry.insert(END, selected_tuple[2])
        year_entry.insert(END, selected_tuple[3])
        isbn_entry.insert(END, selected_tuple[4])
    except IndexError:
        pass
'''
Wrapper function for the backend's view function.
'''
def view_command():
    books_listbox.delete(0, END)        # Cleaning the list box content
    for row in backend.view():
        books_listbox.insert(END, row)

'''
Wrapper function for the backend's search function.
'''
def search_command():
    books_listbox.delete(0, END)

    for row in backend.search(title_data.get(), author_data.get(), year_data.get(), isbn_data.get()):
        books_listbox.insert(END, row)

'''
Wrapper function for the backend's insert function.
'''
def insert_command():
    books_listbox.delete(0, END)

    books_list = backend.search(title_data.get(), author_data.get(), year_data.get(), isbn_data.get())

    if(len(books_list) == 0):
        backend.insert(title_data.get(), author_data.get(), year_data.get(), isbn_data.get())
    else:
        messagebox.showerror("Error", "This book already exists")

    view_command()

'''
Wrapper function for the backend's delete function.
'''
def delete_command():
    if not selected_tuple:
        messagebox.showerror("Error", "Select a valid entry to delete.")
    else:
        backend.delete(selected_tuple[0])
        view_command()
        messagebox.showinfo("Info", "Entry deleted.")

'''
Wrapper function for the backend's update function.
'''
def update_command():
    backend.update(selected_tuple[0], title_data.get(), author_data.get(), year_data.get(), isbn_data.get())
    view_command()
    messagebox.showinfo("Info", "Entry updated.")


window = Tk()
window.wm_title("Book Store")
window.geometry("")

# Creating the labels
title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)

# Creating the entries
title_data = StringVar();
title_entry = Entry(window, textvariable=title_data)
title_entry.grid(row=0, column=1)

year_data = IntVar()
year_entry = Entry(window, textvariable=year_data)
year_entry.grid(row=1, column=1)

author_data = StringVar()
author_entry = Entry(window, textvariable=author_data)
author_entry.grid(row=0, column=3)

isbn_data = IntVar()
isbn_entry = Entry(window, textvariable=isbn_data)
isbn_entry.grid(row=1, column=3)

# Creating the listbox
books_listbox = Listbox(window, height=6, width=35)
books_listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

# Creating the scrollbar
scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2, column=2, rowspan=6)

# Linking listbox with the scroll bar
books_listbox.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=books_listbox.yview)

#Binding the ListboxSelect event to a function
books_listbox.bind("<<ListboxSelect>>", get_selected_row)

# Creating the buttons
view_btn = Button(window, text="View all", width=12, command=view_command)
view_btn.grid(row=2, column=3)

search_btn = Button(window, text="Search entry", width=12, command=search_command)
search_btn.grid(row=3, column=3)

add_btn = Button(window, text="Add entry", width=12, command=insert_command)
add_btn.grid(row=4, column=3)

update_btn = Button(window, text="Update", width=12, command=update_command)
update_btn.grid(row=5, column=3)

delete_btn = Button(window, text="Delete", width=12, command=delete_command)
delete_btn.grid(row=6, column=3)

close_btn = Button(window, text="Close", width=12, command=window.destroy)
close_btn.grid(row=7, column=3)

window.mainloop()