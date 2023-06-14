from pymongo import MongoClient

# from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://RajneeshKumar:<password>@cluster0.qgsxb7q.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient("mongodb+srv://RajneeshKumar:<password>@cluster0.qgsxb7q.mongodb.net/?retryWrites=true&w=majority")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.get_database("newdatabase")
collection = db.get_collection("newdatabase")
db = client.test
