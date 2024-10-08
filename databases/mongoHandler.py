import email

from pymongo import MongoClient

class MongoHandler:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://ProjectMongo:Mongo1234@projects.emesx.mongodb.net/?retryWrites=true&w=majority&appName=Projects")

    def connect(self, databases_name):
        return self.client[databases_name]

    def authenticate(self, username, password):
        db = self.connect("chat")
        user = db.users.find_one({"username": username, "password": password})
        if user:
            return True
        else:
            return False