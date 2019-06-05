'''
This program allows to connect to an
PostgreSQL database.

@author Rodriguez Acosta Ernesto Antonio
'''
import psycopg2

connection_str = "dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'"

def create_table():

    #1) Create the database connection
    #   - If we don't have the database file yet, it will be created
    #     by this line of code and the connection will be established.
    db_connection = psycopg2.connect(connection_str)

    #2) Create the cursor object
    cursor = db_connection.cursor()

    #3) Writing the SQL query
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    #4) Commit the changes
    db_connection.commit()

    #5) Close the database connection
    db_connection.close()


def insert_data(item, quantity, price):
    db_connection = psycopg2.connect(connection_str)

    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))

    db_connection.commit()
    db_connection.close()

def view():
    db_connection = psycopg2.connect(connection_str)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM store")
    store_db_data = cursor.fetchall()

    db_connection.close()

    return store_db_data    # The variable is returned as a list

def delete(item):
    db_connection = psycopg2.connect(connection_str)
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM store WHERE item = %s", (item,))

    db_connection.commit()
    db_connection.close()

def update(item, quantity, price):
    db_connection = psycopg2.connect(connection_str)
    cursor = db_connection.cursor()
    cursor.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s ", (quantity, price, item))

    db_connection.commit()
    db_connection.close()



create_table()

#insert_data("Orange", 10, 15)

#delete('Orange')

update('Apple', 20, 15.0)

print(view())
