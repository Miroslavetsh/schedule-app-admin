# Automatic Redis Cloud filling with some new data, !!Uncomment from 16 line to process
import os
from redis.commands.json.path import Path
import redis
import json
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = int(os.environ['REDIS_PORT'])
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

path_to_example = '\example.json'

with open(os.path.dirname('helpers' + path_to_example) + path_to_example, "r", encoding='utf-8') as jsonFile, redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD) as client:
    #     jsonObject = json.load(jsonFile)

    #     for i, o in jsonObject.items():
    #         client.json().set(i, Path.root_path(), o)
    #     # random entities for testing
    for i in client.json().get('teachers'):
        print(i, sep='/n')
    jsonFile.close()
