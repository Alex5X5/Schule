from mysql import connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor

conn:MySQLConnection = connector.connect(user='root', password='root', host='localhost', port=3306)
cursor:MySQLCursor = conn.cursor()
cursor.execute("""CREATE DATABASE IF NOT EXISTS Bibliothek""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Bibliothek.Buecher (id INT PRIMARY KEY,  titel VARCHAR(100),  autor VARCHAR(100),  erscheinungsjahr YEAR,  isbn VARCHAR(20))""")
conn.close()