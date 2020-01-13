import os
from bson.objectid import ObjectId
from pymongo import MongoClient

mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost/')
db_name = os.getenv('DB_NAME', 'graphql-blog')
collection_name = 'users'

client = MongoClient(mongodb_uri)
db = client[db_name]
users = db[collection_name]


def add_user(name):
    data = {'name': name}
    users.insert_one(data)
    return data


def get_user(user_id):
    return users.find_one({'_id': ObjectId(user_id)})


def delete_user(user_id):
    users.find_one_and_delete({'_id': ObjectId(user_id)})
    return True


def get_users():
    users_data = []
    results = users.find({})
    for data in results:
        users_data.append(data)
    return users_data
