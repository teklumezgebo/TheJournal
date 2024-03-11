from flask import Flask, make_response
from pymongo import MongoClient
from flask_restful import Api, Resource
from bson.objectid import ObjectId
from config import database_user_password

app = Flask(__name__)

api = Api(app)

cluster = MongoClient(f"mongodb+srv://teklumezgebo:{database_user_password}@thejournal.fiahiep.mongodb.net/?retryWrites=true&w=majority&appName=TheJournal")

db = cluster["TheJournal"]

users = db["Users"]

class User(Resource):
    
    def get(self):
        pass

api.add_resource(User, '/')

if __name__ == '__main__':
    app.run(port=5555,  debug=True)