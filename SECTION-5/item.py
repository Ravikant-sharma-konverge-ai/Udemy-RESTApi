import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    #@jwt_required()                            #authenticate before the get request
    def get(self,name):                              # here we define our own get function which process get request
        #for item in items:
            #f item['name']==name:
                #return item
        #item = next(filter(lambda x: x['name'] == name, items),None)   #next gives us the first item in filter and will cause error if filter sequence is empty  thats why we return NOne in that case  
        #return {'item': item}, 200 if item else 404            #404 is error code
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()
        
        if row:
            return{'item':{'name':row[0],'price':row[1]}}
        return {'message':'item not found'},404

    def post(self,name):
        if next(filter(lambda x: x['name'] == name, items),None) is not None: #if name is already in it and they try to post it again
            return {'message':f"an item name {name} already exists."}
        
        data = Item.parser.parse_args()
        #data  = request.get_json()     #.get_json(force = True) means that it does not look in content type header
        item = {'name':name,'price':data['price']}  
        items.append(item)                      #201 is craeted code
        return item, 201
    #@jwt_required()   this will also enable authentication in delete also
    def delete(self,name):
        global items                              #we use this because othrewise it will think that the itms passed in lamdba is local function variable which could lead to error in original list
        items = list(filter(lambda x: x['name'] != name,items)) 
        return {'message':'item deleted'}

    def put(self,name):
        #parser = reqparse.RequestParser() #view sec 4 last secnd video, try to do this in other requests to
        #parser.add_argument('price',type = float, required = True,help = 'this field cannot be left blank!')
        data = Item.parser.parse_args()

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