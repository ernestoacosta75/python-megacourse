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

window = Tk()
window.title("Book Store")
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

isbn_data = StringVar()
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

# Creating the buttons
view_btn = Button(window, text="View all", width=12)
view_btn.grid(row=2, column=3)

search_btn = Button(window, text="Search entry", width=12)
search_btn.grid(row=3, column=3)

add_btn = Button(window, text="Add entry", width=12)
add_btn.grid(row=4, column=3)

update_btn = Button(window, text="Update", width=12)
update_btn.grid(row=5, column=3)

delete_btn = Button(window, text="Delete", width=12)
delete_btn.grid(row=6, column=3)

close_btn = Button(window, text="Close", width=12)
close_btn.grid(row=7, column=3)

window.mainloop()