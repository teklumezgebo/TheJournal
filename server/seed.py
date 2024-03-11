from app import users_collection
from faker import Faker

fake = Faker()

i = 0

print("Creating Seed Data...")

while i < 50:
    
    users_collection.insert_one({
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "journals": []
    })
    
    i += 1

print("Seeding Complete!")