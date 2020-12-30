from pymongo import MongoClient
import datetime
from decouple import config


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
        self.client.insert_one(doc)

    
    def delete_many(self):
        '''
        '''
        count = self.client.delete_many({})
        print (count.deleted_count, " documents deleted.")

    def update_one(self, query):
        '''
        '''
        self.client.update_one(query)

    



        

        

