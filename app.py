from flask import Flask
import praw
import pprint
import datetime as dt
#from src.mongo import Mongo
from decouple import config


client_id=config('CLIENT_ID')
client_secret=config('CLIENT_SECRET')
user_agent=config('USER_AGENT')
username=config('USER_NAME')
password=config('PASSWORD')


app = Flask(__name__)


@app.route('/home')
def run_reddit_client():
    reddit = praw.Reddit(client_id=client_id, \
                        client_secret=client_secret, \
                        user_agent=user_agent, \
                        username=username, \
                        password=password)

    subreddit = reddit.subreddit('progresspics')

    top_subreddit = subreddit.top(limit=2)
    posts = []
    for post in top_subreddit:
        print(post.score, post.url, post.title, post.thumbnail, post.preview['images'][0]['resolutions'])
        pprint.pprint(vars(post))
        '''
        post = { "title": post.title, 
                "id": post.id }
        '''
        posts.append(post)

    return { "data": [
        {"id": post.id, "title": post.title}
        for post  in posts
    ]}

if __name__=="__main__":
    app.run(debug=True)

