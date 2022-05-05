import uuid
import redis
from redis.commands.json.path import Path


def does_not_teacher_exist_in_db(name):
    return not get_teacher_by_name(name) is None


def get_teacher_by_name(name):
    with redis.Redis() as client:
        for teacher in client.json().get('teachers'):
            if str(teacher['name']) == str(name):
                return teacher
            return None


def add_teacher(name):
    if does_not_teacher_exist_in_db(name):
        teacher_data = {'id': str(uuid.uuid4()), "name": name}

        with redis.Redis() as client:
            client.json().arrappend('teachers', Path.root_path(), teacher_data)
            return True

    else:
        return False


def get_teachers_list():
    with redis.Redis() as client:
        return client.json().get('teachers')


# TODO: update teacher
# TODO: delete teacher
