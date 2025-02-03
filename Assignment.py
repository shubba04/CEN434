import numpy as np
# Import the numpy library for numerical operations

a = [1, 2, 3, 4, 5]
b = [0, 1, 2, 3, 4]
# Define two lists a and b

a = np.array(a)
b = np.array(b)
# Convert the lists to numpy arrays

print(a + b)
# Add the two numpy arrays element-wise and print the result

import pymongo
# Import the pymongo library to interact with MongoDB

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# Create a MongoDB client connected to the localhost on port 27017

mydb = myclient["mydatabase"]
# Create a database named "mydatabase" (will be created if it doesn't exist)

print(myclient.list_database_names())
# Print the list of database names in the MongoDB server

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists")
# Check if "mydatabase" exists in the list of databases and print a message

mycol = mydb["vemrinji"]
# Create a collection named "vemrinji" in "mydatabase" (will be created if it doesn't exist)

mydata = {"Name": "Queendolin", "Room": "Dorcas A302"}
y = mycol.insert_one(mydata)
# Insert a document into the "vemrinji" collection

mydata2 = [
    {"Name": "Rinji", "Room": "Daniel F009"},
    {"Name": "Oluwapelumi", "Room": "Daniel F107"},
    {"Name": "Levi", "Room": "Daniel F109"},
    {"Name": "Vem", "Room": "Daniel F009"}
]
z = mycol.insert_many(mydata2)
# Insert multiple documents into the "vemrinji" collection

print(z.inserted_ids)
# Print the IDs of the inserted documents

myquery = {"Name": "Q"}
myans = mycol.find(myquery)
# Query the collection to find documents where the "Name" is "Q"

for n in myans:
    print(n)
# Print the documents found by the query
