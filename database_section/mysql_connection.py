'''
This program allows to connect to a MySQL database.

@author Rodriguez Acosta Ernesto Antonio
'''
import mysql.connector

word = input("Enter a word in English and press Enter: ")

db_connection = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = db_connection.cursor()

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)

results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("We couldn't find any results about that.")