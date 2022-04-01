import pymongo
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb+srv://web:Thisisustedxku824@firstmeet.qnbqi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client["user_data"]
    collections = db["user"]
    print([c for c in collections.find()])