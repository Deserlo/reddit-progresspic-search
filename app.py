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

#app = Flask(__name__)
app = Flask(__name__, static_folder='react-reddit-app/build',
            static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/home')
def retrieve_posts():
    docs = MongoDB.get_random()
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


def format_type(t):
    if t == "all":
        return [1, 2]
    else:
        return [int(t), ]


def format_height(h):
    if "-" not in h:
        h = h + "-" + h
    return h


def parse_arg(arg, name):
    return str(arg).split(name)[1].split("prop")[0]


def parse_beg_range(range):
    if int(range.split("-")[0]) == 0:
        return int(range.split("-")[0])-1
    else:
        return int(range.split("-")[0])


def parse_end_range(range):
    return int(range.split("-")[1])


def format_query(args):
    genders = format_gender(parse_arg(args, 'gender='))
    types = format_type(parse_arg(args, 'type='))
    range_age = parse_arg(args, 'age=')
    height = format_height(parse_arg(args, 'height='))
    range_start = parse_arg(args, 'starting=')
    range_end = parse_arg(args, 'current=')
    regx = re.compile("jpg$", re.IGNORECASE)
    query = {"$and": [{"gender": {"$in": genders}},
                      {"type": {"$in": types}},
                      {"height": {"$gte": parse_beg_range(height),
                                  "$lte": parse_end_range(height)}},
                      {"age": {"$gte": parse_beg_range(
                          range_age), "$lte": parse_end_range(range_age)}},
                      {"starting_lbs": {"$gte": parse_beg_range(range_start),
                                        "$lte": parse_end_range(range_start)}},
                      {"current_lbs": {"$gte": parse_beg_range(range_end),
                                       "$lte": parse_end_range(range_end)}},
                      {"post_url": regx}
                      ]}
    return query


# @app.route('/search/<gender>/<type>/<starting>/<pounds>', methods=['GET'])
@ app.route('/search/<args>')
def filter_posts(args):
    print(str(args))
    query = format_query(args)
    print(query)
    docs = MongoDB.filter(query)
    print(docs)
    return docs


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 5000))
