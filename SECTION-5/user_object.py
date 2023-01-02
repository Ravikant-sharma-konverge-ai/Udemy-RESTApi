import sqlite3
from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id  = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls,username):          # as we are using the same class inside therefore we have make it as a class method decorartor as no where in this fuction self is used
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"   # here Where is used to filter only username    
        result = cursor.execute(query,(username,))  # here the second argument in execte must  be a tuple there fore username with coma
        row = result.fetchone() # fetchone() will return the first row , if no row then it will give None

        if row:            # or if row is not None:
            user = cls(*row)# or could be writeen cls(*row)
        else:
            user = None

        connection.close()
        return user        

    @classmethod
    def find_by_id(cls,_id):          # as we are using the same class inside therefore we have make it as a class method decorartor as no where in this fuction self is used
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"   # here Where is used to filter only username    
        result = cursor.execute(query,(_id,))  # here the second argument in execte must  be a tuple there fore username with coma
        row = result.fetchone() # fetchone() will return the first row , if no row then it will give None

        if row:            # or if row is not None:
            user = cls(*row)# or could be writeen cls(*row)
        else:
            user = None

        connection.close()
        return user

class UserRegister(Resource):                                      # this one is created to signup the user
    parser = reqparse.RequestParser()
    parser.add_argument('username', type = str,required = True,help="this field cannot be blank")
    parser.add_argument('password', type = str,required = True,help="this field cannot be blank")


    def post(self):
        data  =  UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):    # to find the user already exists or not
            return {"message": "User with that username already exists."}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL,?,?)"   # we put id as NULL as it is auto incremental
        cursor.execute(query,(data['username'],data['password']))

        connection.commit()
        connection.close()

        return {'message':'usre created successfully'},201