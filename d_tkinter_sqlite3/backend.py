import sqlite3

class Database:
    db_name = ''

    '''
    Making the connection to the database.
    '''
    def __init__(self, db_name):
        self.db_name = db_name
        database_connection, cursor = self.open_connection()
        cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.close_connection(database_connection)

    def open_connection(self):
        database_connection = sqlite3.connect(self.db_name)
        cursor = database_connection.cursor()

        return database_connection, cursor

    def close_connection(self, database_connection):
        database_connection.commit()
        database_connection.close()

    '''
    Inserting a book in the database.
    '''
    def insert(self, title, author, year, isbn):
        database_connection, cursor = self.open_connection()
        cursor.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.close_connection(database_connection)

    '''
    Select all books from the database.
    '''
    def view(self):
        database_connection, cursor = self.open_connection()
        cursor.execute("SELECT * FROM book")

        books_list = cursor.fetchall()

        self.close_connection(database_connection)

        return books_list

    '''
    Search for a book in the database.
    '''
    def search(self, title="", author="", year="", isbn=""):
        database_connection, cursor = self.open_connection()
        cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))

        books_list = cursor.fetchall()

        self.close_connection(database_connection)

        return books_list

    '''
    Delete a book in the database.
    '''
    def delete(self, book_id):
        database_connection, cursor = self.open_connection()
        cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))

        self.close_connection(database_connection)

    '''
    Update a book in the database.
    '''
    def update(self, id, title, author, year, isbn):
        database_connection, cursor = self.open_connection()
        cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))

        self.close_connection(database_connection)
