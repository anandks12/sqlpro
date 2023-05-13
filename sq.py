import sqlite3
db = sqlite3.connect('my_db.db')
co = db.cursor()
co.close()
db.close()