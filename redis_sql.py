import redis
from redis.commands.json.path import Path
import uuid
from redis_worker import jsonfile

# Это для автоматического создания массивов с уже заполенными данными из example.json
# with redis.Redis() as client:
# client.json().set('subjects', Path.root_path(), jsonfile)


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
                subjects.append(i["id"])
        for i in client.json().get('pairs'):
            if i["subjectId"] in subjects:
                lessons.append(i)
    print(lessons)
    return lessons


def changing_sc(changes_list):
    with redis.Redis() as client:
        for i in changes_list:
            if changes_list[i] != None:
                client.json().set(i, Path.root_path(), changes_list[i])


def check_not_existing_teacher(name):
    with redis.Redis() as client:
        try:
            teachers = client.json().get("teachers")
            for i in teachers:
                if i["name"] == name:
                    return False
        except:
            return True


def add_teacher(name):
    if check_not_existing_teacher(name):
        jsonfile = {'id': str(uuid.uuid4()), "name": name}
        with redis.Redis() as client:
            client.json().arrappend('teachers', Path.root_path(), jsonfile)


def get_subjects():
    subjects = []
    with redis.Redis() as client:
        for i in client.json().get("subjects"):
            subjects.append(i)
    return subjects

#TODO: add_schedule
#TODO: add_subject
#TODO: add_
#TODO: add_schedule

# json.set firsttable $ {"subjects":{"id":1, "name":"OOP", "teacherid":1}
