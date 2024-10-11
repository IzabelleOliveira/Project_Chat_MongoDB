from pymongo import MongoClient
from databases.entities import User, Message


class MongoHandler:
    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://user:qwerty123456@mongochat.s8eiy.mongodb.net/chat?retryWrites=true&w=majority")

    def connect(self, databases_name):
        return self.client[databases_name]

    def authenticate(self, nickname, password, email):
        db = self.connect("chat")
        user = db.users.find_one({"nickname": nickname, "password": password, "email": email})
        if user:
            return True
        else:
            return False

    def getMessages(self, nickname_to):
        db = self.connect("chat")
        messages = db.message.find({"nickname_to": nickname_to})
        return list(messages)

    def saveMessage(self, nickname_from, nickname_to, message):
        db = self.connect("chat")
        message_document = {
            'nickname_from': nickname_from,
            'nickname_to': nickname_to,
            'message': message
        }
        result = db.message.insert_one(message_document)
        return result.inserted_id
