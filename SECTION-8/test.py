# test 
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate,identity #our own created file
from resources.user_object import UserRegister
from resources.item_improved import Item,ItemList
from resources.store_res import Store, StoreList
from db import db
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'  #where sqlachemy find our database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #its a bit advanced ,in order to know had changed but not being saved the extention tracking every thing which takes some resource so we are turning it off as its not very requred so basically it just trun off the modification trcker not the selalcamy it self

app.secret_key = 'jose'  #has to be secret and not ot be visilbe or share with anybody else
api = Api(app)



jwt = JWT(app, authenticate, identity) #jwt creates a new end point that is /auth

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')  #https://127.0.0.1:5000/student/rolf   
api.add_resource(ItemList, '/items')  # for difftrent link we create get in new class itemlist
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister,'/register')

if __name__ =='__main__': # we do this because let say we import test.py in some file then every time we import the app.run will activate and the api runs , so we only want it to run  when it is open 
    db.init_app(app)
    app.run(port=5000, debug=True) # the debug True will let flask to give you good and usefull error message if something happens

