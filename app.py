from flask import Flask
import os
import pprint
import datetime as dt
import re
from src.mongo import Mongo
from bson.objectid import ObjectId
from decouple import config
import pprint
import json


MONGO_URI = os.getenv("MONGO_URI")
MongoDB = Mongo(MONGO_URI)

# app = Flask(__name__)
app = Flask(__name__, static_folder='react-reddit-app/build',
            static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/home')
def retrieve_posts():
    docs = MongoDB.main()
    return docs


def format_query(args):
    regx = re.compile("jpg$", re.IGNORECASE)
    addl = json.loads(args)
    for a, b in addl.items():
        if "height" in a.lower():
            addl['height'] = int(b)
        if "age" in a.lower():
            addl['age'] = {"$gte": int(
                b.split("-")[0]), "$lte": int(b.split("-")[1])}
        if "starting" in a.lower():
            addl[a] = {"$gte": int(
                b.split("-")[0]), "$lte": int(b.split("-")[1])}
        if "change" in a.lower():
            addl[a] = {"$gte": int(
                b.split("-")[0]), "$lte": int(b.split("-")[1])}
        if "current" in a.lower():
            addl[a] = {"$gte": int(
                b.split("-")[0]), "$lte": int(b.split("-")[1])}
        if "type" in a.lower():
            addl['type'] = int(b)
    query = {"$and": [{"post_url": regx}, addl]}
    print("add'l query:", addl)
    print("filtering posts:", query)
    return query


def format_next_query(args, last_id):
    regx = re.compile("jpg$", re.IGNORECASE)
    if args == "all":
        query = {"$and": [{"post_url": regx},
                          {'_id': {"$lt": ObjectId(last_id)}}
                          ]}
    else:
        addl = format_query(args)
        query = {"$and": [{"post_url": regx},
                          {'_id': {"$lt": ObjectId(last_id)}},
                          addl]}
        print(query)
    return query


@ app.route('/next/<args>/<last_id>')
def next(args, last_id):
    query = format_next_query(str(args), str(last_id))
    docs = MongoDB.page(query)
    return docs


@ app.route('/search/<args>')
def filter_posts(args):
    print(str(args))
    query = format_query(args)
    docs = MongoDB.filter(query)
    print(docs)
    if len(docs) > 0:
        return docs
    else:
        return "no data"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 5000))
