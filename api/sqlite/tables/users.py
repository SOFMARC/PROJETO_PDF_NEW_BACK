import sqlite3

connection_database = sqlite3.connect('api/sqlite/database/nfs_database.db')

cursor = connection_database.cursor()

cursor.execute("CREATE TABLE users (name text, email text UNIQUE, password text)")

connection_database.commit()



