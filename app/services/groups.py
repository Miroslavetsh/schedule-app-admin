from services import base

def get_all_groups():
    return base.get_all_items("groups")

def get_groups(name):
    return base.get(name=name, default_name="name", arr="groups")

def create_group(name):
    return base.set(arr="groups", name=name)

def delete_group(id):
    return base.delete(arr="groups", id=id)

def update_group(id, new_name):
    return base.update(arr="groups", id=id, new_name=new_name)