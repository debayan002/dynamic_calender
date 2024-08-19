from pymongo import MongoClient

# Create a MongoDB client
client = MongoClient('mongodb://localhost:27017')

# Access the database
db = client.calendar_db

# Access a collection
event_collection = db.events
