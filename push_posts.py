from src.mongo import Mongo
import praw
from decouple import config
import pprint
import re
import string
import json

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
    #top_subreddit = subreddit.top(limit=80)
    new_subreddit = subreddit.new()
    create_posts(new_subreddit)
    # create_posts(top_subreddit)


def run_test():
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent,
                         username=username,
                         password=password)
    subreddit = reddit.subreddit('progresspics')
    cat_subreddit = subreddit.new()
    with open("reddit_posts.json", "w") as reddit_data_file:
        for raw_post in cat_subreddit:
            if is_valid_thumbnail(raw_post) == True and check_post_title(raw_post.title) == True:
                json.dump(get_parsed_post(raw_post),
                          reddit_data_file, indent=4, sort_keys=True)


def create_posts(sub):
    MongoDB = Mongo(config('MONGO_URI'))
    for raw_post in sub:
        if is_valid_thumbnail(raw_post) == True and check_post_title(raw_post.title) == True:
            MongoDB.insert_one(get_parsed_post(raw_post))


def get_parsed_post(post):
    print("title:", post.title)
    progress_type = assign_type(post.title)
    person, progress = post.title.split("[", 1)
    gender, age, height = person.split("/")
    progress = progress.split("]")[0]
    print(progress)
    starting_lbs = get_starting_lbs(progress)
    current_lbs = get_current_lbs(progress)
    change_in_lbs = get_change_lbs(progress)
    height_inches = height_to_inches(height)
    db_post = {"post_id": post.id, "post_title": post.title, "post_permalink": post.permalink, "person_details": person,
               "gender": gender, "age": int(age), "height": height_inches, "progress": progress, "starting_lbs": starting_lbs, "current_lbs": current_lbs,
               "change_in_lbs": change_in_lbs, "type": progress_type, "manual_fix": False, "needs_check": False,
               "post_url": post.url, "post_thumbnail": post.thumbnail, "post_preview": post.preview['images'][0]['resolutions']}
    return mark_for_cleanup(db_post)


def assign_type(title):
    loss_words = ["loss", "lost", "lose",
                  "losing", "fat", "obese",
                  "overweight", "diet", "exercise",
                  "exercising", "exercised"]
    gain_words = ["gained", "anorexia", "anorexic",
                  "bulimic", "bulimia", "addict"]
    progress_type = 1
    for w in title.split():
        if any(w.strip().lower().strip(string.punctuation) == word for word in loss_words):
            progress_type = 1
        if any(w.strip().lower().strip(string.punctuation) == word for word in gain_words):
            progress_type = 2
    return progress_type


def is_valid_thumbnail(post):
    valid = False
    if "https" in post.thumbnail:
        valid = True
    return valid


def mark_for_cleanup(post):
    if -1 in post.values():
        post['needs_check'] = True
    return post


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


def height_to_inches(height):
    ht = re.sub("’|'|\"|”|cm|in|ft|feet", "'", height.strip())
    ht = ht.strip("'")
    if ht.count("'") == 0:
        inches = "0"
        ft = ht
    else:
        ft, inches = ht.split("'")
    total_inches = int(ft) * 12 + int(inches)
    # sanity check
    if total_inches > 84:
        return -1
    return total_inches


def get_starting_lbs(progress):
    starting = -1
    if ">" in progress:
        starting = progress.split(
            ">")[0].strip().strip(string.ascii_letters)
    return format_as_int(starting)


def get_current_lbs(progress):
    current = -1
    if ">" in progress:
        current = progress.split(">")[1].strip().strip(string.ascii_letters)
        if "=" in current:
            current = current.split(
                "=")[0].strip().strip(string.ascii_letters)
    return format_as_int(current)


def get_change_lbs(progress):
    change_lbs = -1
    if check_progress_change(progress) == True:
        change_lbs = progress.split("=")[1].strip().strip(
            string.ascii_letters).strip(string.whitespace).strip(string.ascii_letters)
    return format_as_int(change_lbs)


if __name__ == "__main__":
    run_reddit_client()
