import sqlite3
from db import db
class UserModel(db.Model):

    __tablename__ = 'users'                       # Telling db the table name which is created below in finf_by method
    id = db.Column(db.Integer,primary_key=True)   #  Telling db the column name the inetger type and telling it that it is the primary key(means unique, indexed based on this)
    username = db.Column(db.String(80))          # telling it this is a string and should not be more than 80 chactrs
    password = db.Column(db.String(80))
    # below defined id user and pass must match the cloumn to be get saved in the users table
    def __init__(self, username, password):
        #self.id  = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()    
    
    @classmethod
    def find_by_username(cls,username):          # as we are using the same class inside therefore we have make it as a class method decorartor as no where in this fuction self is used
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM users WHERE username=?"   # here Where is used to filter only username    
        # result = cursor.execute(query,(username,))  # here the second argument in execte must  be a tuple there fore username with coma
        # row = result.fetchone() # fetchone() will return the first row , if no row then it will give None

        # if row:            # or if row is not None:
        #     user = cls(*row)# or could be writeen cls(*row)
        # else:
        #     user = None

        # connection.close()
        # return user  
        return cls.query.filter_by(username=username).first()      

    @classmethod
    def find_by_id(cls,_id):          # as we are using the same class inside therefore we have make it as a class method decorartor as no where in this fuction self is used
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM users WHERE id=?"   # here Where is used to filter only username    
        # result = cursor.execute(query,(_id,))  # here the second argument in execte must  be a tuple there fore username with coma
        # row = result.fetchone() # fetchone() will return the first row , if no row then it will give None

        # if row:            # or if row is not None:
        #     user = cls(*row)# or could be writeen cls(*row)
        # else:
        #     user = None

        # connection.close()
        # return user
        return cls.query.filter_by(id=_id).first()