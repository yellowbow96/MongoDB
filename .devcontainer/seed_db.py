from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017/")
db = client["template_db"]

# Clear existing data
db.users.drop()

# Insert sample data
db.users.insert_many([
    {"name": "Admin User", "email": "admin@example.com", "role": "admin"},
    {"name": "Regular User", "email": "user@example.com", "role": "user"}
])

print("✅ Database seeded with sample data!")
