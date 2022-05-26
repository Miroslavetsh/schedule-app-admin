from models.teacher import Teacher
from services import base


def get_all():
    return base.get_all("teachers")


def get(id):
    return base.get("teachers", id)


def post(body):
    teacher = Teacher(**body)
    return base.post("teachers", teacher.__dict__)


def put(body):
    teacher = Teacher(**body)
    return base.put("teachers", teacher["id"], teacher.__dict__)


def delete(id):
    return base.delete("teachers", id)
