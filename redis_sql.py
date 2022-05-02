import redis
from redis.commands.json.path import Path


def get_teacher_id(full_name):
    with redis.Redis() as client:
        for i in client.json().get('teachers'):
            if i['name'] == full_name:
                return i["id"]

def get_lesson(full_name):
    lessons = []
    subjects = []
    with redis.Redis() as client:
        for i in client.json().get('subjects'):
            if i['teacherId'] == get_teacher_id(full_name):
                pass

def changing_sc(changes_list):
    with redis.Redis() as client:
        for i in changes_list:
            if changes_list[i] != None:
                client.json().set(i ,Path.root_path(), changes_list[i])



#json.set firsttable $ {"subjects":{"id":1, "name":"OOP", "teacherid":1}