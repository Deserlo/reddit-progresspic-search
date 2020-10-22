#! python3
import praw
import datetime as dt
from src.mongo import Mongo
from decouple import config

MONGO_URI=config('MONGO_URI')
client_id=config('CLIENT_ID')
client_secret=config('CLIENT_SECRET')
user_agent=config('USER_AGENT')
username=config('USER_NAME')
password=config('PASSWORD')

mongo = Mongo(MONGO_URI, "Reddit", "ProgressPics")

reddit = praw.Reddit(client_id=client_id, \
                    client_secret=client_secret, \
                    user_agent=user_agent, \
                    username=username, \
                    password=password)

subreddit = reddit.subreddit('progresspics')

top_subreddit = subreddit.top(limit=5)

for post in top_subreddit:
    print(post.title, post.id)
    post = { "title": post.title, 
             "id": post.id }
    #mongo.insert_one(post)