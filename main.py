from databases.mongoHandler import MongoHandler
from databases.entities import User
from pymongo import MongoClient
if __name__ == '__main__':
    handler = MongoHandler()
    auth = handler.authenticate(username='ProjectMongo', password='dbProject')
    print(auth)