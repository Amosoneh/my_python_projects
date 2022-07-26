import json
import pathlib
from my_exercise.twitter import twitter_users

file_path = pathlib.Path('./json/twitter_users.json').resolve()
# file_path.parent.mkdir(parents=True, exist_ok=True)

with file_path.open(mode='w', encoding='utf-8') as file:
    json.dump(twitter_users, file, indent=4)
    # twitter = json.load(file)

print(twitter_users)
