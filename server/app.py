from flask import Flask, request, make_response
from pymongo import MongoClient
from flask_restful import Api, Resource
from config import database_user_password

app = Flask(__name__)
app.json.compact = False
api = Api(app)

client = MongoClient(f"mongodb+srv://teklumezgebo:{database_user_password}@thejournal.fiahiep.mongodb.net/?retryWrites=true&w=majority&appName=TheJournal")
db = client["TheJournal"]
users_collection = db["Users"]

class SignUp(Resource):

    def post(self):

        print(users_collection.find_one({"username": "teklumezgebo"}))

        # users_collection.insert_one({
        #     "username": request.get_json()["username"],
        #     "email": request.get_json()["email"],
        #     "password": request.get_json()["password"]
        # })

        # response = make_response({
        #     "username":request.get_json()["username"],
        #     "email": request.get_json()["email"],
        #     "password": request.get_json()["password"]
        # }, 201)

        # return response

api.add_resource(SignUp, "/signup")

class Login(Resource):
    
    def post(self):
        pass

api.add_resource(Login, "/login")

if __name__ == '__main__':
    app.run(port=5555,  debug=True)