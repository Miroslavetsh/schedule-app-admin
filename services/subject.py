from models.subject import Subject
from services import base


def get_all():
    return base.get_all(Subject.tablename)


def get(id):
    return base.get(Subject.tablename, id)


def post(body):
    subject = Subject(**body)
    return base.post(Subject.tablename, subject.__dict__)


def put(id, body):
    subject = Subject(**body)
    subject.__dict__["id"] = id
    return base.put(Subject.tablename, subject.__dict__)


def delete(id):
    return base.delete(Subject.tablename, id)
