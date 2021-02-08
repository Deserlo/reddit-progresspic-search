from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import datetime
from decouple import config
import pprint

page_size = 6


class Mongo(object):

    def __init__(self, mongo_uri):
        self.connection_string = mongo_uri
        self.client = MongoClient(self.connection_string).Reddit.ProgressPics

    def insert_many(self, list):
        '''
        '''
        self.client.insert_many(list)

    def insert_one(self, doc):
        '''
        '''
        self.client.update({"post_id": doc["post_id"]}, doc, upsert=True)

    def delete_many(self):
        '''
        Deletes all documents
        '''
        count = self.client.delete_many({})
        print(count.deleted_count, " documents deleted.")

    def update_one(self, query):
        '''
        '''
        self.client.update_one(query)

    def find(self):
        '''
        Finds all documents 
        '''
        cursor = self.client.find({})
        list_cur = list(cursor)
        json_docs = dumps(list_cur)
        return json_docs

    def get_random(self):
        '''
        Finds random documents 
        '''
        cursor = self.client.aggregate([{"$sample": {"size": 20}}])
        list_cur = list(cursor)
        json_docs = dumps(list_cur)
        return json_docs

    def filter(self, query):
        '''
        '''
        cursor = self.client.find(query)
        list_cur = list(cursor)
        json_docs = dumps(list_cur)
        return json_docs

    def page(self, last_id):
        cursor = self.client.find({'_id' > last_id}).limit(page_size)
        list_cur = list(cursor)
        json_docs = dumps(list_cur)
        return json_docs


'''
query = {"gender": "F", "age": {"$gt": '40'}}
MongoDB = Mongo(config('MONGO_URI'))
print(MongoDB.filter(query))
'''
