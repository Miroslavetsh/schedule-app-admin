from models.teacher import Teacher
from services import base


def get_all():
    return base.get_all(Teacher.tablename)


def get(id):
    return base.get(Teacher.tablename, id)


def post(body):
    teacher = Teacher(**body)
    return base.post(Teacher.tablename, teacher.__dict__)


def put(id, body):
    teacher = Teacher(**body)
    teacher.__dict__["id"] = id
    return base.put(Teacher.tablename, teacher.__dict__)


def delete(id):
    return base.delete(Teacher.tablename, id)
