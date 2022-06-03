import uuid


class Subject(object):
    tablename = "subjects"

    def __init__(self, name, place, teacherId):
        self.id = str(uuid.uuid4())
        self.name = name
        self.place = place
        self.teacherId = teacherId
