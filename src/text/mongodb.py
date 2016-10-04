from pymongo import *

def get_db():
    client = MongoClient('localhost', 27017)
    db = client['twitter']
    return db

def get_collection(db, name):
    collection = db[name]
    return collection

def insert(db, collection, data):
    col = db[collection]
    id = col.insert(data)
    print ("The data " + id + " is inserted.\n")

