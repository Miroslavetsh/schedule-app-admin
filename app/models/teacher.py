import uuid


class Teacher(object):
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
