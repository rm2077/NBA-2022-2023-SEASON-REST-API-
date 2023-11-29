import sqlite3

connection = sqlite3.connect("nba.db")
cursor = connection.cursor()

cursor.execute("SELECT * ")


    

except Exception as e:
    print("Error ", e)