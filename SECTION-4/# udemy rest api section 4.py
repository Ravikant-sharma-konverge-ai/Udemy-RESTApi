#Udemy REST api section 4
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Student(Resource):
    def get(self,name):                              # here we define our own get function which process get request
        return {'student': name}

api.add_resource(Student, '/student/<string:name>')  #https://127.0.0.1:5000/student/rolf   

app.run(port=5000)

## creating a proper api now as per the plan we set in postman
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []    # will introduce databases in next section so for now we use lists

class Student(Resource):
    def get(self,name):                              # here we define our own get function which process get request
        for item in items:
            if item['name']==name:
                return item

    def post(self,name):
        item = {'name':name,'price':12.00}  
        items.appned(item)
        return item

api.add_resource(Student, '/item/<string:name>')  #https://127.0.0.1:5000/student/rolf   

app.run(port=5000)
 