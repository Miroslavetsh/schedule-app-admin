from models.group import Group
from services import base


def get_all():
    return base.get_all(Group.tablename)


def get(id):
    return base.get(Group.tablename, id)


def post(body):
    group = Group(**body)
    return base.post(Group.tablename, group.__dict__)


def put(id, body):
    group = Group(**body)
    group.__dict__["id"] = id
    return base.put(Group.tablename, group.__dict__)


def delete(id):
    return base.delete(Group.tablename, id)
