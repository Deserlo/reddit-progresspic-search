from flask import Flask
import os
import pprint
import datetime as dt
from src.mongo import Mongo
from decouple import config


MONGO_URI = os.getenv("MONGO_URI")
MongoDB = Mongo(MONGO_URI)

#app = Flask(__name__)
app = Flask(__name__, static_folder='../build', static_url_path='/')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/home')
def retrieve_posts():
    docs = MongoDB.find()
    print("Home..")
    return docs


@app.route('/search/<args>', methods=['GET'])
def filter_posts(args):
    print("filtering..")
    print(str(args))
    if str(args) == "M":
        query = {"gender": "M"}
    if str(args) == "F":
        query = {"gender": "F"}
    #query = {"gender": "F", "age": {"$gt": '24'}}
    docs = MongoDB.filter(query)
    return docs


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
