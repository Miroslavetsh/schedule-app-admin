import base
from services import base

def get_subjects():
    return base.get_all_items("subjects")

def get_subject(name):
    return base.get(name=name, default_name="name", arr="subjects")

def create_subject(name, place, teacher_id):
    return base.set(arr="subjects", name=name, place=place, teacher_id=teacher_id)

def delete_subject(id):
    return base.delete(arr="subjects", id=id)

def update_subject(id, new_name, place, teacher_id):
    return base.update(arr="subjects", id=id, new_name=new_name, place=place, teacher_id=teacher_id)
