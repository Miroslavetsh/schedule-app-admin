import json

from models.subject import Subject
from services import base


def get_all():
    return base.get_all(Subject.tablename)


def get(id):
    return base.get(Subject.tablename, id)


def get_by_teacher_id(id):
    all_subjects = base.get_all(Subject.tablename)
    subjects = []

    for subject in all_subjects:
        if (str(subject["teacherId"]) == id):
            subjects.append(subject)

    return json.dumps(subjects)


def post(body):
    subject = Subject(**body)
    return base.post(Subject.tablename, subject.__dict__)


def put(id, body):
    subject = Subject(**body)
    subject.__dict__["id"] = id
    return base.put(Subject.tablename, subject.__dict__)


def delete(id):
    return base.delete(Subject.tablename, id)
