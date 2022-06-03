import uuid


class Pair(object):
    tablename = "pairs"

    def __init__(self, subjectId, time):
        self.id = str(uuid.uuid4())
        self.subjectId = subjectId
        self.time = time
