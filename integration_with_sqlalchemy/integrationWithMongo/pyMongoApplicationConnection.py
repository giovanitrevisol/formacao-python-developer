
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb://root:giovani!@localhost:27017"
# uri = "mongodb+srv://giovani:<password>@cluster0.s72qnbf.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print(">>>>>>>>>>>>>>>>")
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print(">>>>>>>>>>>>>>>>")
except Exception as e:
    print(e)