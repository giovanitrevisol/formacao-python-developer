from pymongo import MongoClient

client = MongoClient("mongodb://giovani:giovani@localhost:27017/")

db = client.dio_project

trends_collection = db.trends