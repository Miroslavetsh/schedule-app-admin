import os
import redis
from redis.commands.json.path import Path
import uuid
from dotenv import load_dotenv
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = int(os.environ['REDIS_PORT'])
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def not_exist(var, var2, arr):
    return get(var, var2, arr) == None


def get_all_items(arr):
    with client:
        return client.json().get(arr)


def build_data(name=None, groupId=None, days=None, subjectId=None, time=None, place=None, teacher_id=None):
    if place != None and teacher_id != None:
        data = {'id': str(uuid.uuid4()), "name": name,
                "place": place, "teacherId": teacher_id}
    elif groupId != None and days != None:
        data = {'id': str(uuid.uuid4()), "groupId": groupId, "days": days}
    elif subjectId != None and time != None:
        data = {'id': str(uuid.uuid4()), "subjectId": subjectId, "time": time}
    else:
        data = {'id': str(uuid.uuid4()), "name": name}
    return data


def get(name, default_name, arr):
    with client:
        for array in client.json().get(str(arr)):
            if str(array[str(default_name)]) == str(name):
                return array
            return None

def get_entity_from_collection_by_id(collection_name, id):
    with client:
        for entity in client.json().get(collection_name):
            if entity['id'] == id:
                return entity


def set(arr, name=None, groupId=None, days=None, subjectId=None, time=None, place=None, teacher_id=None):
    if not_exist(name, "name", arr) or not_exist(name, "id", arr):
        data = build_data(name, groupId, days, subjectId,
                          time, place, teacher_id)
        with client:
            try:
                client.json().arrappend(arr, Path.root_path(), data)
                return True
            except:
                return False


def delete(arr, id):
    with client:
        client.delete(f'JSON.DEL {arr} $.{id}', Path.root_path())
        return True


def update(arr, id=None, new_name=None, groupId=None, days=None, subjectId=None, time=None, place=None, teacher_id=None):
    delete(arr, id)
    set(arr, new_name, groupId, days, subjectId, time, place, teacher_id)
    return True
