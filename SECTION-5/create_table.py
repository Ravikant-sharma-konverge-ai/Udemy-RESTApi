
import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" # the INTEGER PRIMARY KEY  is used to crate incemantal column means the id of user will automatically be +1 when ever any new user signup

cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)" # create a nwe table items
cursor.execute(create_table)
cursor.execute("INSERT INTO items VALUES('test',10.99)")

cursor.execute(create_table)

connection.commit()

connection.close()