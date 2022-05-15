#Automatic Redis filling with some new data
import redis
from redis.commands.json.path import Path
import json


with open("D:\project\helpers\example.json", "r", encoding='utf-8') as jsonFile, redis.Redis() as client:
    jsonObject = json.load(jsonFile)
    for i,o in jsonObject.items():
        client.json().set(i, Path.root_path(), o)
    for i in client.json().get('teachers', ):
        print(i, sep='/n')
    jsonFile.close()






# def delete_group(id):
#     with redis.Redis() as client:
#       groups = client.json().get('groups')
      
#       for group in groups:
#         if group['id'] == id:
#           groups.remove(group)

#       return client.json().set('groups', Path.root_path(), groups)