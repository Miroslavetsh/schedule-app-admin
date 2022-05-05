import uuid
import redis
from redis.commands.json.path import Path


def check_if_do_not_exist_in_db(name):
    return get_teacher_by_name(name) == None


def get_teacher_by_name(name):
    with redis.Redis() as client:
        for teacher in client.json().get('teachers'):
            if teacher['name'] == name:
                return teacher
            return None


def add_teacher(name):
    if check_if_do_not_exist_in_db(name):
        teacher_data = {'id': str(uuid.uuid4()), "name": name}

        with redis.Redis() as client:
            client.json().arrappend('teachers', Path.root_path(), teacher_data)
            return True

    else:
        return False


def get_all_teachers():
    with redis.Redis() as client:
        return client.json().get('teachers')


# TODO: update teacher
# TODO: delete teacher
