from twitter_client import get_twitter_client

api = get_twitter_client()
# read from file and use loop
user = api.get_user('choiyoojungnet')
friends = user.friends()


# get id and judge if there are any links
for friend in friends:
    print(friend.screen_name)

#for friend in tweepy.Cursor(user.friends).items():
#    print(friend.screen_name)