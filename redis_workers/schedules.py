from redis_workers import base

def get_schedules(id):
    return base.get(name=id, default_name="id", arr="schedules")

def create_schedules(groupId, days):
    return base.set(arr="schedules", groupId=groupId, days=days)

def delete_schedules(name):
    return base.delete("schedules", name)

def update_subject(name, groupId, days):
    return base.update(arr="schedules",name=name, groupId=groupId, days=days)