import base

def get_all_groups():
    return base.get_all_items("groups")

def get_groups(name):
    return base.get(name=name, default_name="name", arr="groups")

def create_group(name):
    return base.set(arr="groups", name=name)

def delete_group(name):
    return base.delete(arr="groups", name=name)

def update_group(name, new_name, subjectId, time):
    return base.update(arr="groups", name=name, new_name=new_name, subjectId=subjectId, time=time)