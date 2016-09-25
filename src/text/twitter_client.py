import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    """Setup Twitter authentication.

    Return: tweepy.OAuthHandler object
    """
    try:
        consumer_key = "irGVBapfaXBvP6PgcvIm4j9te"
        consumer_secret = "SoF8aNqVl1OeaDhaJIlL34dDJ96jeQxtGoWLJvXVNUx9rGQ4ae"
        access_token = "235837403-iWmSjvgLjwEYKG8rD2BhNouXeN5wqEB2UFKblYMO"
        access_secret = "oKw43AZG23NeWLNdqZszyx3n3SVdVzajCeiieG2p3zDB2"
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    """Setup Twitter API client.

    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client
