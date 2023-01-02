# test 

from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate,identity #our own created file
from user_object import UserRegister
from item_improved import Item,ItemList
app = Flask(__name__)
app.secret_key = 'jose'  #has to be secret and not ot be visilbe or share with anybody else
api = Api(app)

jwt = JWT(app, authenticate, identity) #jwt creates a new end point that is /auth


api.add_resource(Item, '/item/<string:name>')  #https://127.0.0.1:5000/student/rolf   
api.add_resource(ItemList, '/items')  # for difftrent link we create get in new class itemlist
api.add_resource(UserRegister,'/register')

if __name__ =='__main__': # we do this because let say we import test.py in some file then every time we import the app.run will activate and the api runs , so we only want it to run  when it is open 
    
    app.run(port=5000, debug=True) # the debug True will let flask to give you good and usefull error message if something happens

