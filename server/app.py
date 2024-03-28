from flask import Flask, request, session, make_response
from flask_restful import Api, Resource
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from config import database_user_password, secret_key

app = Flask(__name__)
app.config["SECRET_KEY"] = secret_key
bcrypt = Bcrypt(app)
app.json.compact = False
api = Api(app)

client = MongoClient(f"mongodb+srv://teklumezgebo:{database_user_password}@thejournal.fiahiep.mongodb.net/?retryWrites=true&w=majority&appName=TheJournal")
db = client["TheJournal"]
users = db["Users"]



class SignUp(Resource):

    def post(self):

        form = request.get_json()
        first_name = form.get("first_name")
        last_name = form.get("last_name")
        email = form.get("email")
        username = form.get("username")
        password = form.get("password")

        existing_user = users.find_one({"$or": [{"username": username}, {"email": email}]})

        if existing_user:
            if existing_user.get('username') == username:
                return make_response({"error": 'Username is taken.'}, 400)
            elif existing_user.get('email') == email:
                return make_response({"error": 'Email is taken.'}, 400)

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        users.insert_one({
            "first_name": first_name, 
            "last_name": last_name, 
            "email": email, 
            "username": username, 
            "password": hashed_password
        })

        session["user_id"] = str(users.find_one({"username": username})["_id"])

        return make_response({"message": "User created."}, 201)

api.add_resource(SignUp, "/signup")

class Login(Resource):

    def post(self):

        form = request.get_json()
        username = form.get("username")
        password = form.get("password")

        user = users.find_one({"username": username})

        if user and bcrypt.check_password_hash(user["password"], password.encode("utf-8")):
            session["user_id"] = str(user["_id"])

            return make_response({
                "user": {
                    "first_name": user["first_name"],
                    "last_name": user["last_name"],
                    "username": user["username"],
                    "email": user["email"],
                    "journals": []
                }
            })
        else:
            return make_response({
                "error": "Username or password is incorrect."
            })

api.add_resource(Login, "/login")

class Logout(Resource):

    def delete(self):
        session["user_id"] = None
        return make_response({"message": "204: No Content"}, 204)

api.add_resource(Logout, "/logout")

if __name__ == '__main__':
    app.run(port=5555,  debug=True)