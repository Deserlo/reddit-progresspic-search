from src.mongo import Mongo
import praw
from decouple import config

client_id=config('CLIENT_ID')
client_secret=config('CLIENT_SECRET')
user_agent=config('USER_AGENT')
username=config('USER_NAME')
password=config('PASSWORD')


def run_reddit_client():
    reddit = praw.Reddit(client_id=client_id, \
                        client_secret=client_secret, \
                        user_agent=user_agent, \
                        username=username, \
                        password=password)
    subreddit = reddit.subreddit('progresspics')
    top_subreddit = subreddit.top(limit=20)
    MongoDB = Mongo(config('MONGO_URI'))
    posts = []
    for post in top_subreddit:
        print(post.score, post.url, post.title)
        #pprint.pprint(vars(post))
        if check_post_title(post.title) == True:
            person, progress = post.title.split("[", 1)
            gender, age, height = person.split("/")
            progress = progress.split("]")[0]
            post = { "post_id": post.id, "post_title": post.title,"person_details": person, "gender": gender, "age": age, "height": height, "progress": progress, \
            "post_url": post.url, "post_thumbnail": post.thumbnail, "post_preview": post.preview['images'][0]['resolutions']}
            posts.append(post)
            MongoDB.insert_one(post)


def check_post_title(title):
    if "[" in title and "]" in title:
        return True
    else:
        return False




if __name__=="__main__":
    run_reddit_client()