from models.pair import Pair
from services import base


def get_all():
    return base.get_all(Pair.tablename)


def get(id):
    return base.get(Pair.tablename, id)


def post(body):
    pair = Pair(**body)
    return base.post(Pair.tablename, pair.__dict__)


def put(id, body):
    pair = Pair(**body)
    pair.__dict__["id"] = id
    return base.put(Pair.tablename, pair.__dict__)


def delete(id):
    return base.delete(Pair.tablename, id)
