import redis
import base

def get_subjects():
    subjects = []
    with redis.Redis() as client:
        for subject in client.json().get("subjects"):
            subjects.append(subject)
    return subjects

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


def get_pairs(id):
    return base.get(name=id, default_name="id", arr="pairs")


def create_pairs(subjectId, time):
    return base.set(arr="pairs", subjectId=subjectId, time=time)

def delete_pairs(name):
    return base.update(arr="pairs", name=name)


def update_pair(name, subjectId, time):
    return base.update(arr="pairs", name=name, subjectId=subjectId, time=time)
