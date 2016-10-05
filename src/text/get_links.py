from twitter_client import get_twitter_client
from pymongo import *
from mongodb import Links

api = get_twitter_client()
client = MongoClient()
db = client.twitter
collection = db.list_members
# read from mongodb
'''
for user in collection.find():
    print(user['id_str'])
'''
user = api.get_user(collection.find_one()['_id'])
friends = user.friends()

# get id and judge if there are any links
for friend in friends:
    if (collection.find_one(friend.screen_name)):
        print("Creating link between " + friend.screen_name + " and " + collection.find_one()['_id'])
        new_link = Links(
            user_screen_name=collection.find_one()['_id'],
            user_id = collection.find_one()['id_str'],
            friend_screen_name = friend.screen_name,
            friend_id = friend.id_str
        )
        new_link.save()
