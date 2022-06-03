# Automatic Redis Cloud filling with some new data, !!Uncomment from 16 line to process
import json
import os
from redis.commands.json.path import Path

from config import db as client

path_to_example = '\example.json'

with open(os.path.dirname('helpers' + path_to_example) + path_to_example, "r", encoding='utf-8') as jsonFile, client:
    jsonObject = json.load(jsonFile)

    for i, o in jsonObject.items():
        client.json().set(i, Path.root_path(), o)
    # random entities for testing
    for i in client.json().get('teachers'):
        print(i, sep='/n')
    jsonFile.close()
