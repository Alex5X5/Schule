import sqlite3

con = sqlite3.connect('test.db')
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS TestData (OrderId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Anzahl INTEGER NOT NULL, Dicke INTEGER NOT NULL)""")
cursor.execute("""INSERT INTO TestData (Anzahl, Dicke) VALUES (?, ?)""", (10,1))
cursor.execute("""SELECT COUNT(*) FROM TestData""")
con.commit()
print(cursor.fetchall())

cursor.execute("""SELECT COUNT(OrderId) FROM TestData""")
con.commit()
print(cursor.fetchall())