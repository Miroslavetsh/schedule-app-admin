import uuid


class Schedule(object):
    tablename = "schedules"

    def __init__(self, groupId, days):
        self.id = str(uuid.uuid4())
        self.groupId = groupId
        self.days = days
