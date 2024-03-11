from flask import Flask, request, make_response
from pymongo import MongoClient
from flask_restful import Api, Resource
from config import database_user_password

app = Flask(__name__)
app.json.compact = False

api = Api(app)

cluster = MongoClient(f"mongodb+srv://teklumezgebo:{database_user_password}@thejournal.fiahiep.mongodb.net/?retryWrites=true&w=majority&appName=TheJournal")

db = cluster["TheJournal"]

users = db["Users"]

class SignUp(Resource):

    def post(self):
        pass

class Login(Resource):
    
    def post(self):
        pass

if __name__ == '__main__':
    app.run(port=5555,  debug=True)