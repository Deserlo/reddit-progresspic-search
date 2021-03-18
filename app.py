from flask import Flask
import os
import pprint
import datetime as dt
import re
from src.mongo import Mongo
from decouple import config
import pprint


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


def format_beginning(input):
    print("input before:", input)
    if int(input) == 0:
        new_input = int(input)-1
        print('new input:', str(new_input))
        return new_input
    else:
        return int(input)


def format_gender(g):
    if g == "all":
        return ["F", "M"]
    else:
        return [g, ]


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
