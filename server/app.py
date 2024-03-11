from flask import Flask
from pymongo import MongoClient
from flask_restful import Api, Resource
from config import password

app = Flask(__name__)

cluster = MongoClient(f"mongodb+srv://teklumezgebo:{password}@thejournal.fiahiep.mongodb.net/?retryWrites=true&w=majority&appName=TheJournal")

db = cluster["TheJournal"]

users = db["Users"]


if __name__ == '__main__':
    app.run(port=5555,  debug=True)