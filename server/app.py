from flask import Flask
from pymongo import MongoClient
from flask_restful import Api, Resource

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555,  debug=True)