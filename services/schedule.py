from models.schedule import Schedule
from services import base


def get_all():
    return base.get_all(Schedule.tablename)


def get(id):
    return base.get(Schedule.tablename, id)


def post(body):
    schedule = Schedule(**body)
    return base.post(Schedule.tablename, schedule.__dict__)


def put(id, body):
    schedule = Schedule(**body)
    schedule.__dict__["id"] = id
    return base.put(Schedule.tablename, schedule.__dict__)


def delete(id):
    return base.delete(Schedule.tablename, id)
