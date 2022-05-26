from services import base


def get_all():
    return base.get_all("teachers")


def get(id):
    return base.get("teachers", id)


def post(body):
    return base.post("teachers", **body)


def put(body):
    return base.put("teachers", body["id"], **body)


def delete(id):
    return base.delete("teachers", id)
