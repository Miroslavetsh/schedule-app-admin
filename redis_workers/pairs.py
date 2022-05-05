import redis
from redis.commands.json.path import Path
import uuid

from redis_workers.subjects import get_subjects


def get_pairs_by_teacher_id(id):
    pairs = []
    subjects_assigned_to_the_teacher = []

    for subject in get_subjects():
            if str(subject['teacherId']) == str(id):
                subjects_assigned_to_the_teacher.append(subject)

    with redis.Redis() as client:

        for pair in client.json().get('pairs'):
            for subject in subjects_assigned_to_the_teacher:
                if str(pair['subjectId']) == str(subject['id']):
                    pairs.append(pair)

    return pairs



def pairs_notexist(name):
    return get_pairs(name) == None

def get_pairs(id):
    with redis.Redis() as client:
        for pair in client.json().get("pairs"):
            if str(pair['id']) == str(id):
                return pair
            return None


def create_pairs(subjectId, time):
    if pairs_notexist:
        data = {'id': str(uuid.uuid4()),"subjectid":subjectId, "time":time}
        with redis.Redis() as client:
            client.json().arrappend('pairs', Path.root_path(), data)
            return True
    else:
        return False

def delete_pairs(name):
    if not pairs_notexist:
        with redis.Redis() as client:
            client.execute_command(f'JSON.DEL pairs $.{name}', Path.root_path())
            return True
    else:
        return False

def update_pair(name, subjectId, time):
    delete_pairs(name)
    create_pairs(name, subjectId, time)
