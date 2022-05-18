import redis
from redis.commands.json.path import Path
import uuid


def not_exist(var, var2, arr):
    return get(var, var2, arr) == None

def get_all_items(arr):
    with redis.Redis() as client:
        return client.json().get(arr)

def build_data( name=None, groupId=None, days=None, subjectId=None, time=None, place=None, teacher_id=None):
    if place != None and teacher_id != None:
        data = {'id': str(uuid.uuid4()), "name":name, "place":place, "teacherId": teacher_id}
    elif  groupId != None and days != None:
        data = {'id': str(uuid.uuid4()), "groupId":groupId, "days":days}
    elif  subjectId != None and time != None:
        data = {'id': str(uuid.uuid4()), "subjectId":subjectId, "time":time}
    else:
         data = {'id': str(uuid.uuid4()), "name":name}
    return data


def get(name, default_name, arr):
    with redis.Redis() as client:
        for array in client.json().get(str(arr)):
            if str(array[str(default_name)]) == str(name):
                return array
            return None


def set(arr, name=None, groupId=None, days=None, subjectId=None, time=None, place=None, teacher_id=None):
    if not_exist(name, "name", arr) or not_exist(name, "id", arr): 
        data = build_data(name, groupId, days, subjectId, time, place, teacher_id)
        with redis.Redis() as client:
            try:
                client.json().arrappend(arr, Path.root_path(), data)
                return True
            except:
                return False


def delete(arr, id):
    with redis.Redis() as client:
        client.execute_command(f'JSON.DEL {arr} $.{id}', Path.root_path())
        return True


def update(arr, id=None, new_name=None, groupId=None, days=None, subjectId=None, time=None, place=None, teacher_id=None):
    delete(arr, id)
    set(arr, new_name, groupId, days, subjectId, time, place, teacher_id)
    return True
