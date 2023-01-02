#SQLite in python
import sqlite3

connection = sqlite3.connect('data.db') #this gonna create a file data.db in our current directory 
cursor = connection.cursor() # a cursur allow you to select things and start things , responsible for execting the query, and also storing the rsult

create_table  = "CREATE TABLE users (id int,username text,password text)" # this means the users table gonna have 3 columns , id,username,password

cursor.execute(create_table) # query has been created now run it 


user = (1,'jose','asdf') # user values in tuple form

insert_query = 'INSERT INTO users VALUES (?,?,?)'  # writing query to atke the previous user values into the table

cursor.execute(insert_query,user) # executing the written query

users = [                           # list of  values as tuples
    (2,'rolf','asdf'),
    (3,'anne','xyz')
]

cursor.executemany(insert_query,users)  # executing the all elemts in list users in inster_query format

select_query = "SELECT * FROM users" # query to retrive data back , the * means to return all the colums value like id,name,pass, if we write "SELECT id FROM users" it will only gonna give id values

for row in cursor.execute(select_query): # can itrate over it like a itratable
    print(row)

connection.commit() # tells connection to save our latest values

connection.close() # never forget to close the connection


