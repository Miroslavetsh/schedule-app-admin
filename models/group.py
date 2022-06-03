import uuid


class Group(object):
    tablename = "groups"

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
