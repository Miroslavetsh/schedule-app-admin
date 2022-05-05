import redis

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
