import base

def get_teachers_list():
    return base.get_all_items("teachers")

def get_teacher_by_name(name):
    return base.get(name=name, default_name="name", arr="teachers")

def add_teacher(name):
    return base.set(arr="teacher", name=name)

def delete_teacher(name):
    return base.delete(arr="teachers",name=name)

def update_teacher(name, new_name):
    return base.update(arr="teachers", name=name, new_name=new_name)
