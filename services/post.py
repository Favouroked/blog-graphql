import os
from bson.objectid import ObjectId
from pymongo import MongoClient

mongodb_uri = os.getenv('MONGODB_URI', 'mongodb://localhost/')
db_name = os.getenv('DB_NAME', 'graphql-blog')
collection_name = 'posts'

client = MongoClient(mongodb_uri)
db = client[db_name]
posts = db[collection_name]


def add_post(user_id, title, body):
    data = {'user_id': ObjectId(user_id), 'title': title, 'body': body}
    posts.insert_one(data)
    return data


def get_post(post_id):
    return posts.find_one({'_id': ObjectId(post_id)})


def get_posts():
    posts_data = []
    results = posts.find({})
    for data in results:
        posts_data.append(data)
    return posts_data


def get_user_posts(user_id):
    posts_data = []
    results = posts.find({'user_id': ObjectId(user_id)})
    for data in results:
        posts_data.append(data)
    return posts_data


def update_post(post_id, data):
    post = posts.find_one_and_update({'_id': ObjectId(post_id)}, {'$set': data}, return_document=True)
    return post


def delete_post(post_id):
    posts.find_one_and_delete({'_id': ObjectId(post_id)})
    return True
