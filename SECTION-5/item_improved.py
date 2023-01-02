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
        item = self.find_by_name(name)
        if item:
            return item  
        return {'message':'item not found'},404
    
    @classmethod                                  # we create a class method so that this function can be accessed by both get and post function
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()
        
        if row:
            return{'item':{'name':row[0],'price':row[1]}}

    def post(self,name):
        if self.find_by_name(name): #if name is already in it and they try to post it again
            return {'message':f"an item name {name} already exists."}
        
        data = Item.parser.parse_args()
        #data  = request.get_json()     #.get_json(force = True) means that it does not look in content type header
        item = {'name':name,'price':data['price']} 
        try:               
            self.insert(item)  
        except:
            return {'message':'an error occured inserting item'},500 #means not inserters fault , internal server error                  
        return item, 201   #201 is craeted code

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query,(item['name'],item['price']))

        connection.commit()
        connection.close()     
    #@jwt_required()   this will also enable authentication in delete also
    def delete(self,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()

        return {'message':'item deleted'}

    def put(self,name):
        #parser = reqparse.RequestParser() #view sec 4 last secnd video, try to do this in other requests to
        #parser.add_argument('price',type = float, required = True,help = 'this field cannot be left blank!')
        data = Item.parser.parse_args()

        item = self.find_by_name(name)
        updated_item = {'name':name,'price':data['price']}
        
        if item is None:
            try:
                self.insert(updated_item)
            except:
                 return {'message':"an error occured inserting the item"},500
        else:
            try:
                item.update(updated_item)
            except:
                return {'message':'an error occured updating the item'},500


        return item  

    @classmethod
    def update(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query,(item['price'],item['name']))
        connection.commit()
        connection.close()
                

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query) # now this is s iterable because not other argument
        
        items = []

        for row in result:
            items.append({'name':row[0],'price':row[1]})
        
        #not connection.commit because we didnt save anything
        connection.close()
        
        return {'items':items}
