from flask import Flask
import praw
import datetime as dt
#from src.mongo import Mongo
from decouple import config


client_id=config('CLIENT_ID')
client_secret=config('CLIENT_SECRET')
user_agent=config('USER_AGENT')
username=config('USER_NAME')
password=config('PASSWORD')


app = Flask(__name__)


@app.route('/')
def run_reddit_client():
    '''
    reddit = praw.Reddit(client_id=client_id, \
                        client_secret=client_secret, \
                        user_agent=user_agent, \
                        username=username, \
                        password=password)

    subreddit = reddit.subreddit('progresspics')

    top_subreddit = subreddit.hot()

    for post in top_subreddit:
        print(post.title, post.id)
        post = { "title": post.title, 
                "id": post.id }
    '''
    return "Reddit Flask React App"

if __name__=="__main__":
    app.run(debug=True)

