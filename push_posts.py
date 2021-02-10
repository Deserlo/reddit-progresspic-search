from src.mongo import Mongo
import praw
from decouple import config
import pprint
import re
import string

client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')
user_agent = config('USER_AGENT')
username = config('USER_NAME')
password = config('PASSWORD')


def run_reddit_client():
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent,
                         username=username,
                         password=password)
    subreddit = reddit.subreddit('progresspics')
    top_subreddit = subreddit.top(limit=50)
    MongoDB = Mongo(config('MONGO_URI'))
    posts = []
    for post in top_subreddit:
        # print(post.score, post.url, post.title)
        # pprint.pprint(vars(post))
        if check_post_title(post.title) == True:
            progress_type = assign_type(post.title)
            person, progress = post.title.split("[", 1)
            gender, age, height = person.split("/")
            progress = progress.split("]")[0]
            print(progress)
            starting_lbs = get_starting_lbs(progress)
            current_lbs = get_current_lbs(progress)
            change_in_lbs = get_change_lbs(progress)
            post = {"post_id": post.id, "post_title": post.title, "post_permalink": post.permalink, "person_details": person,
                    "gender": gender, "age": age, "height": height, "progress": progress, "starting_lbs": starting_lbs, "current_lbs": current_lbs,
                    "change_in_lbs": change_in_lbs, "type": progress_type, "manual_fix": False,
                    "post_url": post.url, "post_thumbnail": post.thumbnail, "post_preview": post.preview['images'][0]['resolutions']}
            if is_valid_thumbnail(post) == True:
                posts.append(post)
                MongoDB.insert_one(post)


def assign_type(title):
    loss_words = ["loss", "lost", "lose",
                  "losing", "fat", "obese",
                  "overweight", "diet", "exercise",
                  "exercising", "exercised"]
    gain_words = ["gained", "anorexia", "anorexic",
                  "bulimic", "bulimia"]
    progress_type = 1
    for w in title.split():
        if any(w.strip().lower().strip(string.punctuation) == word for word in loss_words):
            progress_type = 1
        if any(w.strip().lower().strip(string.punctuation) == word for word in gain_words):
            progress_type = 2
    return progress_type


def is_valid_thumbnail(post):
    valid = False
    if "https" in post['post_thumbnail']:
        valid = True
    return valid


def check_post_title(title):
    if "[" in title and "]" in title:
        return True
    else:
        return False


def check_progress_change(progress):
    if "=" in progress:
        return True
    else:
        return False


def check_progress_format(progress):
    formatters = ["<", ">", "-", "->", "--", "~", "to"]
    if any(formatters) in progress:
        return True
    else:
        return False


def format_as_int(measure):
    if measure != -1:
        measure = re.sub(r'[^\d.]+', '', measure)
        return int(round(float(measure)))
    else:
        return measure


def get_starting_lbs(progress):
    starting = -1
    if ">" in progress:
        starting = progress.split(
            ">")[0].strip().strip(string.ascii_letters)
        print("starting: ", str(starting))
    return format_as_int(starting)


def get_current_lbs(progress):
    current = -1
    if ">" in progress:
        current = progress.split(">")[1].strip().strip(string.ascii_letters)
        if "=" in current:
            current = current.split(
                "=")[0].strip().strip(string.ascii_letters)
        print("current: ", str(current))
    return format_as_int(current)


def get_change_lbs(progress):
    change_lbs = -1
    if check_progress_change(progress) == True:
        change_lbs = progress.split("=")[1].strip().strip(
            string.ascii_letters).strip(string.whitespace).strip(string.ascii_letters)
        print("change: ", str(change_lbs))
    return format_as_int(change_lbs)


if __name__ == "__main__":
    run_reddit_client()
