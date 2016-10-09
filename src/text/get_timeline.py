import sys
sys.path.append("..")
import json
import re
from tweepy import Cursor
from twitter_client import get_twitter_client
from pymongo import *


'''
def remove_emoji(data):
    try:
    # UCS-4
        patt = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
    except re.error:
    # UCS-2
        patt = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    return patt.sub('', data)
'''


def get_timeline(user, count):
    client = get_twitter_client()
    emoji = re.compile(u'['
    u'\U0001F300-\U0001F5FF'
    u'\U0001F600-\U0001F64F'
    u'\U0001F680-\U0001F6FF'
    u'\u2500-\u25FF\u2600-\u26FF\u2700-\u27BF]+',
    re.UNICODE)
    link = re.compile(u'[a-zA-z]+://[^\s]*')
    patt = re.compile(
        u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
    with open('output/' + user + '_user_timeline.txt', "w") as f:
        for status in Cursor(client.user_timeline, screen_name=user).items(count):
            tweet_filtered = emoji.sub("", status.text)
            tweet_filtered = link.sub("", tweet_filtered)
            tweet_filtered = patt.sub("", tweet_filtered)
            tweet_filtered = re.sub('RT ', '', tweet_filtered)
            tweet_filtered = re.sub('#', '', tweet_filtered)
            tweet_filtered = re.sub('@', '', tweet_filtered)
            tweet_filtered = re.sub('\n', '', tweet_filtered)
            f.write(json.dumps(tweet_filtered) + "\n")
    f.close()


if __name__ == '__main__':
    '''
    Separate the part of getting data from Twitter
    '''
    # user = "LFC"
    # get_timeline(user, 100)

    # get users from database
