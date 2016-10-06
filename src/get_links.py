from twitter_client import get_twitter_client
from pymongo import *
from mongodb import Links
import time

api = get_twitter_client()
client = MongoClient()
db = client.twitter
collection = db.list_members

for user in collection.find(no_cursor_timeout=True):
    current_user = api.get_user(user['_id'])
    friends = current_user.friends()
    for friend in friends:
        for existing_user in collection.find():
            if (friend.screen_name == existing_user['_id']):
                print("Creating link between " + user['_id'] + " and " + friend.screen_name)
                new_link = Links(
                    user_screen_name=user['_id'],
                    user_id=user['id_str'],
                    friend_screen_name=friend.screen_name,
                    friend_id=friend.id_str
                )
                new_link.save()
    time.sleep(61)
