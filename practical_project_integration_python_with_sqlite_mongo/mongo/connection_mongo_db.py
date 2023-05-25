import pymongo
import pprint

print("start connection with mongoDB")

# create connection with mongo
connection = pymongo.MongoClient("url_mongo")

# create the database and collection
db = connection.bank
collection = db.clients

# Document information
new_clients = [
    {
        "agency": 789,
        "name": "Giovani Trevisol",
        "cpf": "1123.654.789.10",
        "address": "Rua qualquer, nr 123",
        "account": ["cc", 980012],
        "balance": 100001.86
    },
    {
        "agency": 123,
        "name": "Lara Talita",
        "cpf": "111.222.333.44",
        "address": "Rua alguma coisa, nr 99",
        "account": ["cp", 191109],
        "balance": 299.91
    },
    {
        "agency": 567,
        "name": "Pedro da Silva",
        "cpf": "888.999.666.77",
        "address": "Rua seila, nr 899",
        "account": ["cc", 120841],
        "balance": 4788.13
    }
]

print("\nSave data into mongoDB")
clients = db.clients
result = clients.insert_many(new_clients)
print(result.inserted_ids)

print("\n Retrieving client information:")
pprint.pprint(db.clients.find_one({"name": "Giovani Trevisol"}))

print("\nList os customers:")
for client in clients.find():
    pprint.pprint(client)

print("\n Retrieving customer information sorted by name:")
for client in clients.find({}).sort("name"):
    pprint.pprint(client)

print("\nagency clients:")
for client in clients.find({"agency": 789}):
    pprint.pprint(client)

print("\nCustomers with cp account:")
for client in clients.find({"account": "cp"}):
    pprint.pprint(client)

print("\n Customers with cc account:")
for client in clients.find({"account": "cc"}):
    pprint.pprint(client)
