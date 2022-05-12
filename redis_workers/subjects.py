import base

def get_subjects():
    return base.get_all_items("subjects")

def get_subject(name):
    return base.get(name=name, default_name="name", arr="subjects")

def create_subject(name, place, teacherid):
    return base.set(arr="subjects", name=name, place=place, teacherid=teacherid)

def delete_subject(name):
    return base.delete(arr="subjects", name=name)

def update_subject(name, new_name, place, teacherid):
    return base.update(arr="subjects", name=name, new_name=new_name, place=place, teacherid=teacherid)
