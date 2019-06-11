import sqlite3

class Database:
    '''
    Making the connection to the database.
    '''
    def __init__(self, db_name):
        self.db_name = db_name
        database_connection = self.open_connection()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")

        self.close_connection(database_connection)

    '''
    Opening a connection to the database.
    '''
    def open_connection(self):
        database_connection = sqlite3.connect(self.db_name)
        self.cursor = database_connection.cursor()

        return database_connection

    '''
    Closing the connection to the database.
    '''
    def close_connection(self, database_connection):
        database_connection.commit()
        database_connection.close()

    '''
    Inserting a book in the database.
    '''
    def insert(self, title, author, year, isbn):
        database_connection = self.open_connection()
        self.cursor.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))

        self.close_connection(database_connection)

    '''
    Select all books from the database.
    '''
    def view(self):
        database_connection = self.open_connection()
        self.cursor.execute("SELECT * FROM book")

        books_list = self.cursor.fetchall()

        self.close_connection(database_connection)

        return books_list

    '''
    Search for a book in the database.
    '''
    def search(self, title="", author="", year="", isbn=""):
        database_connection = self.open_connection()
        self.cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))

        books_list = self.cursor.fetchall()

        self.close_connection(database_connection)

        return books_list

    '''
    Delete a book in the database.
    '''
    def delete(self, book_id):
        database_connection = self.open_connection()
        self.cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))

        self.close_connection(database_connection)

    '''
    Update a book in the database.
    '''
    def update(self, id, title, author, year, isbn):
        database_connection = self.open_connection()
        self.cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))

        self.close_connection(database_connection)
