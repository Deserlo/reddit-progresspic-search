#! python3
import praw
import datetime as dt
from src.mongo import Mongo

mongo = Mongo("mongodb+srv://eva:corona@cluster0-q2hqi.mongodb.net/Reddit?retryWrites=true&w=majority", 
              "Reddit", 
              "ProgressPics")


reddit = praw.Reddit(client_id='gIUKkZXSybpMyw', \
                     client_secret='IR0VXfPQ9oTbH1CbGBsQX9QiRWs', \
                     user_agent='reddit-api-app', \
                     username='evaswayy', \
                     password='Menudo65!')

subreddit = reddit.subreddit('progresspics')

top_subreddit = subreddit.top(limit=5)

for post in top_subreddit:
    print(post.title, post.id)
    post = { "title": post.title, 
             "id": post.id }
    mongo.insert_one(post)