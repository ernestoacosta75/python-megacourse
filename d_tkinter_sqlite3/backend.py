import sqlite3

class Database:
    db_name = ''

    '''
    Making the connection to the database.
    '''
    def __init__(self, db_name):
        self.db_name = db_name
        connection_database = sqlite3.connect(self.db_name)
        cursor = connection_database.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        connection_database.commit()
        connection_database.close()

    '''
    Inserting a book in the database.
    '''
    def insert(self, title, author, year, isbn):
        connection_database = sqlite3.connect(self.db_name)
        cursor = connection_database.cursor()
        cursor.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        connection_database.commit()
        connection_database.close()

    '''
    Select all books from the database.
    '''
    def view(self):
        connection_database = sqlite3.connect(self.db_name)
        cursor = connection_database.cursor()
        cursor.execute("SELECT * FROM book")

        books_list = cursor.fetchall()

        connection_database.close()

        return books_list

    '''
    Search for a book in the database.
    '''
    def search(self, title="", author="", year="", isbn=""):
        connection_database = sqlite3.connect(self.db_name)
        cursor = connection_database.cursor()
        cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))

        books_list = cursor.fetchall()

        connection_database.close()

        return books_list

    '''
    Delete a book in the database.
    '''
    def delete(self, book_id):
        connection_database = sqlite3.connect(self.db_name)
        cursor = connection_database.cursor()
        cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
        connection_database.commit()
        connection_database.close()

    '''
    Update a book in the database.
    '''
    def update(self, id, title, author, year, isbn):
        connection_database = sqlite3.connect(self.db_name)
        cursor = connection_database.cursor()
        cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        connection_database.commit()
        connection_database.close()
