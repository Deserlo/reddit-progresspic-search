from flask import Flask

import pprint
import datetime as dt
from src.mongo import Mongo
from decouple import config

MongoDB = Mongo(config('MONGO_URI'))

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello, world!"


@app.route('/home')
def retrieve_posts():
    docs = MongoDB.find()
    print(docs)
    return docs


@app.route('/search', methods=['GET'])
def filter_posts():
    query = {"gender": "F", "age": {"$gt": '24'}}
    docs = MongoDB.filter(query)
    print(docs)
    return docs


if __name__ == "__main__":
    app.run(debug=True)
