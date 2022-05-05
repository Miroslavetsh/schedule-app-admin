import redis
from redis.commands.json.path import Path
import uuid


def changing_sc(changes_list):
    with redis.Redis() as client:
        for i in changes_list:
            if changes_list[i] != None:
                client.json().set(i, Path.root_path(), changes_list[i])


# json.set firsttable $ {"subjects":{"id":1, "name":"OOP", "teacherid":1}
