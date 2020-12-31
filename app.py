from flask import Flask
import praw
import pprint
import datetime as dt
from src.mongo import Mongo
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

    top_subreddit = subreddit.top(limit=5)
    posts = []
    MongoDB = Mongo(config('MONGO_URI'))
    for post in top_subreddit:
        print(post.score, post.url, post.title, post.thumbnail, post.preview['images'][0]['resolutions'])
        #pprint.pprint(vars(post))
        person, progress = post.title.split("[")
        gender, age, height = person.split("/")
        progress = progress.split("]")[0]
        post = { "post_id": post.id, "post_title": post.title,"person_details": person, "gender": gender, "age": age, "height": height, "progress": progress, \
         "post_url": post.url, "post_thumbnail": post.thumbnail, "post_preview": post.preview['images'][0]['resolutions']}
        posts.append(post)
        MongoDB.insert_one(post)

    return { "data": { "title": "eyeyes", "id": "pewpoe"} }
    '''
    return { "data": [
        {"title": post.title, "id": post.id, "url": post.url, "thumbnail": post.thumbnail, "preview": post.preview['images'][0]['resolutions']}
        for post  in posts
    ]}
    '''

if __name__=="__main__":
    app.run(debug=True)

