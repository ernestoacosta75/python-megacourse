import sqlite3

db_name = 'books.db'

'''
Making the connection to the database.
'''
def books_db_connection():
    book_db_connection = sqlite3.connect(db_name)
    cursor = book_db_connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    book_db_connection.commit()
    book_db_connection.close()

'''
Inserting a book in the database.
'''
def insert(title, author, year, isbn):
    book_db_connection = sqlite3.connect(db_name)
    cursor = book_db_connection.cursor()
    cursor.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    book_db_connection.commit()
    book_db_connection.close()

'''
Select all books from the database.
'''
def view():
    book_db_connection = sqlite3.connect(db_name)
    cursor = book_db_connection.cursor()
    cursor.execute("SELECT * FROM book")

    books_list = cursor.fetchall()

    book_db_connection.close()

    return books_list

'''
Search for a book in the database.
'''
def search(title="", author="", year="", isbn=""):
    book_db_connection = sqlite3.connect(db_name)
    cursor = book_db_connection.cursor()
    cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))

    books_list = cursor.fetchall()

    book_db_connection.close()

    return books_list

'''
Delete a book in the database.
'''
def delete(book_id):
    book_db_connection = sqlite3.connect(db_name)
    cursor = book_db_connection.cursor()
    cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
    book_db_connection.commit()
    book_db_connection.close()

'''
Update a book in the database.
'''
def update(id, title="", author="", year="", isbn=""):
    book_db_connection = sqlite3.connect(db_name)
    cursor = book_db_connection.cursor()
    cursor.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    book_db_connection.commit()
    book_db_connection.close()

books_db_connection()

print(view())
#insert("The Sun", "John Smith", 1918, 913123132)
#delete(1)
update(3, "The moon", "John Smooth", 1917, 99999)
print(view())
print(search(author='John Smith'))