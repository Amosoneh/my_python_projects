import json
import pathlib
from my_exercise import twitter

file_path = pathlib.Path('./json/twitter_users.json').resolve()
# file_path.parent.mkdir(parents=True, exist_ok=True)

with file_path.open(mode='w', encoding='utf-8') as file:
    json.dump(twitter.twitter_users, file)

print(file_path)