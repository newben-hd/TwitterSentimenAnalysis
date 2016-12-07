import tweepy
import Tweet

class CursorListener():
    def __init__(self, topic, tweepy_api, max_limit=10):
        self.topic = topic
        self.tweepy_api = tweepy_api
        self.max_limit=10
        self.csv_path = ""
        
    def getTweets(self):
        searched = [status for status in tweepy.Cursor(self.tweepy_api.search, q=self.topic).items(self.max_limit)]

        tweets = []
        for status in searched:

            tweet_id = status.id
            text = repr(status.text)
            retweet_count = status.retweet_count
            quotes_count = "--not implemented--"  # HOW to get this?
            favorites_count = status.favorite_count
            author = status.author
            is_news = "--not implemented--"  # DEFINE LIST OF VALID NEWS AUTHORS
            timestamp = status.created_at

            # Instantiate tweet object, which processes the info
            tweet = Tweet.Tweet(tweet_id=tweet_id, text=text, retweet_count=retweet_count,
                                quotes_count=quotes_count, favorites_count=favorites_count,
                                author=author, is_news=is_news, timestamp=timestamp)

            tweets.append(tweet)
        return tweets
