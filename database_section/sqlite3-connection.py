'''
This program allows to connect to an
SQLite database.

@author Rodriguez Acosta Ernesto Antonio
'''
import sqlite3

def create_table():

    #1) Create the database connection
    #   - If we don't have the database file yet, it will be created
    #     by this line of code and the connection will be established.
    db_connection = sqlite3.connect("lite.db")

    #2) Create the cursor object
    cursor = db_connection.cursor()

    #3) Writing the SQL query
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    #4) Commit the changes
    db_connection.commit()

    #5) Close the database connection
    db_connection.close()


def insert_data(item, quantity, price):
    db_connection = sqlite3.connect("lite.db")

    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))

    db_connection.commit()
    db_connection.close()

def view():
    db_connection = sqlite3.connect("lite.db")
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM store")
    store_db_data = cursor.fetchall()

    db_connection.close()

    return store_db_data    # The variable is returned as a list

def delete(item):
    db_connection = sqlite3.connect("lite.db")
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM store WHERE item = ?", (item,))

    db_connection.commit()
    db_connection.close()

def update(item, quantity):
    db_connection = sqlite3.connect("lite.db")
    cursor = db_connection.cursor()
    cursor.execute("UPDATE store SET quantity = ? WHERE item = ? ", (quantity, item))

    db_connection.commit()
    db_connection.close()



create_table()

#insert_data("Water Glass", 10, 5)
#insert_data("Steel Glass", 11, 5.50)
#delete('Wine Glass')
update('Water Glass', 11)
print(view())