import os
import redis
from redis_workers import base
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = int(os.environ['REDIS_PORT'])
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)


def get_subjects():
    subjects = []
    with client:
        for subject in client.json().get("subjects"):
            subjects.append(subject)
    return subjects


def get_pairs_by_teacher_id(id):
    pairs = []
    subjects_assigned_to_the_teacher = []

    for subject in get_subjects():
        if str(subject['teacherId']) == str(id):
            subjects_assigned_to_the_teacher.append(subject)

    with client:

        for pair in client.json().get('pairs'):
            for subject in subjects_assigned_to_the_teacher:
                if str(pair['subjectId']) == str(subject['id']):
                    pairs.append(pair)
    return pairs


def get_pairs(id):
    return base.get(name=id, default_name="id", arr="pairs")


def create_pairs(subjectId, time):
    return base.set(arr="pairs", subjectId=subjectId, time=time)


def delete_pairs(id):
    return base.update(arr="pairs", id=id)


def update_pair(id, subjectId, time):
    return base.update(arr="pairs", id=id, subjectId=subjectId, time=time)
