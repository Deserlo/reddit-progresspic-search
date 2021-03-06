from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import datetime
from decouple import config
import pprint
import json
import re

page_size = 36


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
        self.client.update(
            {"post_id": doc["post_id"], "manual_fix": False}, doc, upsert=True)

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
        cursor = self.client.aggregate([{"$sample": {"size": 50}}])
        list_cur = list(cursor)
        json_docs = dumps(list_cur)
        return json_docs

    def main(self):
        '''
        Shows most recent
        '''
        regx = re.compile("jpg$", re.IGNORECASE)
        cursor = self.client.find({"post_url": regx}).sort(
            "_id", -1).limit(page_size)
        list_cur = list(cursor)
        json_docs = dumps(list_cur)
        return json_docs

    def filter(self, query):
        '''
        '''
        cursor = self.client.find(query).sort("_id", -1).limit(page_size)
        list_cur = list(cursor)
        json_docs = dumps(list_cur)
        return json_docs

    def page(self, query):
        '''
        '''
        cursor = self.client.find(query).sort("_id", -1).limit(page_size)
        list_cur = list(cursor)
        json_docs = dumps(list_cur)
        return json_docs


'''
myQuery = {"$and": [{"$or": [{"gender": "F"}, {"gender": "M"}]},
                    {"$or": [{"type": 1}, {"type": 2}]},
                    {"age": {"$gte": "28", "$lte": "42"}},
                    {"starting_lbs": {"$gte": 200, "$lte": 350}},
                    {"change_in_lbs": {"$gte": 20, "$lte": 100}}
                    ]}

MongoDB = Mongo(config('MONGO_URI'))
docs = MongoDB.filter(myQuery)
print(docs)

'''
