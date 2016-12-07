from .cursorListener import *
import os

conf = {}
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
execfile(os.path.join(BASE_DIR,"source/config.py"), conf)

auth = tweepy.OAuthHandler(conf["consumer_key"],conf["consumer_secret"])
auth.set_access_token(conf["access_key"],conf["access_secret"])
tweepy_api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def getTweetObject(q):
    tweets = CursorListener(topic=q, tweepy_api=tweepy_api)
    return tweets.getTweets()
