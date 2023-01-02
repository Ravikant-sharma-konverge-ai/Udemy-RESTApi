# test 

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate,identity #our own created file

app = Flask(__name__)
app.secret_key = 'jose'  #has to be secret and not ot be visilbe or share with anybody else
api = Api(app)

jwt = JWT(app, authenticate, identity) #jwt creates a new end point that is /auth

items = []    # will introduce databases in next section so for now we use lists

class Student(Resource):
    @jwt_required()                            #authenticate before the get request
    def get(self,name):                              # here we define our own get function which process get request
        #for item in items:
            #f item['name']==name:
                #return item
        item = next(filter(lambda x: x['name'] == name, items),None)   #next gives us the first item in filter and will cause error if filter sequence is empty  thats why we return NOne in that case  
        return {'item': item}, 200 if item else 404            #404 is error code
    
    def post(self,name):
        if next(filter(lambda x: x['name'] == name, items),None) is not None: #if name is already in it and they try to post it again
            return {'message':f"an item name {name} already exists."}

        data  = request.get_json()     #.get_json(force = True) means that it does not look in content type header
        item = {'name':name,'price':data['price']}  
        items.append(item)                      #201 is craeted code
        return item, 201
    #@jwt_required()   this will also enable authentication in delete also
    def delete(self,name):
        global items                              #we use this because othrewise it will think that the itms passed in lamdba is local function variable which could lead to error in original list
        items = list(filter(lambda x: x['name'] != name,items)) 
        return {'message':'item deleted'}

    def put(self,name):
        parser = reqparse.RequestParser() #view sec 4 last secnd video, try to do this in other requests to
        parser.add_argument('price',type = float, required = True,help = 'this field cannot be left blank!')
        data = parser.parse_args()

        item = next(filter(lambda x:x['name'] ==  name,items),None)
        if item is None:
            item = {'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)

        return item        

class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Student, '/item/<string:name>')  #https://127.0.0.1:5000/student/rolf   
api.add_resource(ItemList, '/items')  # for difftrent link we create get in new class itemlist

app.run(port=5000, debug=True) # the debug True will let flask to give you good and usefull error message if something happens