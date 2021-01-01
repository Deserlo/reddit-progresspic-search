from flask import Flask

import pprint
import datetime as dt
from src.mongo import Mongo
from decouple import config

MongoDB = Mongo(config('MONGO_URI'))

app = Flask(__name__)

@app.route('/home')
def retrieve_posts():
    docs = MongoDB.find()
    return docs


if __name__=="__main__":
    app.run(debug=True)

