import sqlite3
from flask_restful import Resource, reqparse
from models.User import UserModel

class UserRegister(Resource):                                      # this one is created to signup the user
    parser = reqparse.RequestParser()
    parser.add_argument('username', type = str,required = True,help="this field cannot be blank")
    parser.add_argument('password', type = str,required = True,help="this field cannot be blank")


    def post(self):
        data  =  UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):    # to find the user already exists or not
            return {"message": "User with that username already exists."}, 400

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO users VALUES (NULL,?,?)"   # we put id as NULL as it is auto incremental
        # cursor.execute(query,(data['username'],data['password']))

        # connection.commit()
        # connection.close()
        user = UserModel(**data)  #UserModel(data['username'],data['password'])
        user.save_to_db()

        return {'message':'usre created successfully'},201