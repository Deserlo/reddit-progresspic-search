from pymongo import MongoClient
import datetime


class Mongo(object):
    '''
    '''
    def __init__(self, connection_string, database, collection):
        self.connection_string = connection_string
        self.database = database
        self.collection = collection
        self.client = MongoClient(self.connection_string).database.collection
        
   
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

    



        

        

