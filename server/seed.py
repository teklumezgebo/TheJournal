from pymongo import MongoClient
from config import database_user_password
from faker import Faker

cluster = MongoClient(f"mongodb+srv://teklumezgebo:{database_user_password}@thejournal.fiahiep.mongodb.net/?retryWrites=true&w=majority&appName=TheJournal")

db = cluster["TheJournal"]

users = db["Users"]

fake = Faker()

i = 0

print("Creating Seed Data...")

while i < 50:
    users.insert_one({
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "journals": []
    })
    
    i += 1

print("Seeding Complete!")