import json
import re
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
    # account for testing
    user = "LFC"
    count = 50

    client = get_twitter_client()
    fname = "user_timeline_{}.txt".format(user)
    emoji = re.compile(u'['
    u'\U0001F300-\U0001F5FF'
    u'\U0001F600-\U0001F64F'
    u'\U0001F680-\U0001F6FF'
    u'\u2500-\u25FF\u2600-\u26FF\u2700-\u27BF]+',
    re.UNICODE)
    link = re.compile(u'[a-zA-z]+://[^\s]*')
    with open(fname, "w") as f:
        for status in Cursor(client.user_timeline, screen_name=user).items(count):
            tweet_filtered = emoji.sub("", status.text)
            tweet_filtered = link.sub("", tweet_filtered)
            tweet_filtered = re.sub('RT ', '', tweet_filtered)
            tweet_filtered = re.sub('#', '', tweet_filtered)
            tweet_filtered = re.sub('@', '', tweet_filtered)
            f.write(json.dumps(tweet_filtered) + "\n")