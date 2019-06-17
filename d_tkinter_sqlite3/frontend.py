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

from backend import Database

database = Database('books.db')

class BookStoreFrontend(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title("Book Store")
        self.window.geometry("")

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
        self.title_data = StringVar();
        title_entry = Entry(window, textvariable=self.title_data)
        title_entry.grid(row=0, column=1)

        self.year_data = IntVar()
        year_entry = Entry(window, textvariable=self.year_data)
        year_entry.grid(row=1, column=1)

        self.author_data = StringVar()
        author_entry = Entry(window, textvariable=self.author_data)
        author_entry.grid(row=0, column=3)

        self.isbn_data = IntVar()
        isbn_entry = Entry(window, textvariable=self.isbn_data)
        isbn_entry.grid(row=1, column=3)

        # Creating the listbox
        self.books_listbox = Listbox(window, height=6, width=35)
        self.books_listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

        # Creating the scrollbar
        scroll_bar = Scrollbar(window)
        scroll_bar.grid(row=2, column=2, rowspan=6)

        # Linking listbox with the scroll bar
        self.books_listbox.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.configure(command=self.books_listbox.yview)

        #Binding the ListboxSelect event to a function
        self.books_listbox.bind("<<ListboxSelect>>", self.get_selected_row)

        # Creating the buttons
        view_btn = Button(window, text="View all", width=12, command=self.view_command)
        view_btn.grid(row=2, column=3)

        search_btn = Button(window, text="Search entry", width=12, command=self.search_command)
        search_btn.grid(row=3, column=3)

        add_btn = Button(window, text="Add entry", width=12, command=self.insert_command)
        add_btn.grid(row=4, column=3)

        update_btn = Button(window, text="Update", width=12, command=self.update_command)
        update_btn.grid(row=5, column=3)

        delete_btn = Button(window, text="Delete", width=12, command=self.delete_command)
        delete_btn.grid(row=6, column=3)

        close_btn = Button(window, text="Close", width=12, command=window.destroy)
        close_btn.grid(row=7, column=3)

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.books_listbox.curselection()[0]
            selected_tuple = self.books_listbox.get(index)

            self.title_entry.delete(0, END)
            self.author_entry.delete(0, END)
            self.year_entry.delete(0, END)
            self.isbn_entry.delete(0, END)

            self.title_entry.insert(END, selected_tuple[1])
            self.author_entry.insert(END, selected_tuple[2])
            self.year_entry.insert(END, selected_tuple[3])
            self.isbn_entry.insert(END, selected_tuple[4])
        except IndexError:
            pass
    '''
    Wrapper function for the database's view function.
    '''
    def view_command(self):
        self.books_listbox.delete(0, END)        # Cleaning the list box content
        for row in database.view():
            self.books_listbox.insert(END, row)

    '''
    Wrapper function for the database's search function.
    '''
    def search_command(self):
        self.books_listbox.delete(0, END)

        for row in database.search(self.title_data.get(), self.author_data.get(), self.year_data.get(), self.isbn_data.get()):
            self.books_listbox.insert(END, row)

        if (self.books_listbox.size() == 0):
            messagebox.showerror("Error", "There isn't any book that satisfy the search criteria.")

    '''
    Wrapper function for the database's insert function.
    '''
    def insert_command(self):
        self.books_listbox.delete(0, END)

        books_list = database.search(self.title_data.get(), self.author_data.get(), self.year_data.get(), self.isbn_data.get())

        if(len(books_list) == 0):
            database.insert(self.title_data.get(), self.author_data.get(), self.year_data.get(), self.isbn_data.get())
        else:
            messagebox.showerror("Error", "This book already exists")

        self.view_command()

    '''
    Wrapper function for the database's delete function.
    '''
    def delete_command(self):
        if not self.books_listbox.curselection():
            messagebox.showerror("Error", "Select a valid entry to delete.")
        else:
            database.delete(selected_tuple[0])
            self.view_command()
            messagebox.showinfo("Info", "Entry deleted.")

    '''
    Wrapper function for the database's update function.
    '''
    def update_command(self):
        database.update(selected_tuple[0], self.title_data.get(), self.author_data.get(), self.year_data.get(), self.isbn_data.get())
        self.view_command()
        messagebox.showinfo("Info", "Entry updated.")

window = Tk()
bookStore = BookStoreFrontend(window)
window.mainloop()