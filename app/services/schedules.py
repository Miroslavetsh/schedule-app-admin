from services import base

def get_schedules(id):
    return base.get(name=id, default_name="id", arr="schedules")

def create_schedules(groupId, days):
    return base.set(arr="schedules", groupId=groupId, days=days)

def delete_schedules(id):
    return base.delete("schedules", id)

def update_subject(id, groupId, days):
    return base.update(arr="schedules",id=id, groupId=groupId, days=days)