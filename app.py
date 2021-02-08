from flask import Flask
import os
import pprint
import datetime as dt
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


@app.route('/search/<gender>/<type>', methods=['GET'])
def filter_posts(gender=None, type=0):
    print("filtering..")
    query = {"gender": str(gender), "type": int(type)}
    print(query)
    docs = MongoDB.filter(query)
    return docs


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 5000))
