import uuid


class Teacher(object):
    tablename = "teachers"

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
