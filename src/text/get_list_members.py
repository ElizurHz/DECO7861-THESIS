from twitter_client import get_twitter_client
import json

client = get_twitter_client()
members = client.list_members('elizurhz', 'rv', count=200)
with open('rv.json', 'w') as f:
    for member in members:
        f.write(json.dumps(member._json)+"\n")   # save a backup for users