from pymongo import MongoClient
from config import database_user_password

cluster = MongoClient(f"mongodb+srv://teklumezgebo:{database_user_password}@thejournal.fiahiep.mongodb.net/?retryWrites=true&w=majority&appName=TheJournal")

db = cluster["TheJournal"]

users = db["Users"]