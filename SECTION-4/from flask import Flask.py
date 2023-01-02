from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Student(Resource):
    def get(self,name):                              # here we define our own get function which process get request
        return {'student': name}

api.add_resource(Student, '/student/<string:name>')  #https://127.0.0.1:5000/student/rolf   

app.run(port=5000)