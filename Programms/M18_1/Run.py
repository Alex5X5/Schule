import sqlite3

con = sqlite3.connect('test.db')
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS TestData (OrderId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Anzahl INTEGER NOT NULL, Alter INTEGER NOT NULL)""")
cursor.execute("""SELECT COUNT(*) FROM TestData""")
con.commit()
