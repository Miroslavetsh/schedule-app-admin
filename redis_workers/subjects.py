
import redis


def get_subjects():
    subjects = []

    with redis.Redis() as client:
        for subject in client.json().get("subjects"):
            subjects.append(subject)

    return subjects
