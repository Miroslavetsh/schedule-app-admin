from redis.commands.json.path import Path
import redis
import uuid

def subject_notexist(name):
    return get_subject(name) == None

def get_subjects():
    subjects = []

    with redis.Redis() as client:
        for subject in client.json().get("subjects"):
            subjects.append(subject)

    return subjects


def get_subject(name):
    with redis.Redis() as client:
        for subject in client.json().get("subjects"):
            if str(subject['name']) == str(name):
                return subject
            return None


def create_subject(name, place, teacherid):
    if subject_notexist:
        sub_data = {'id': str(uuid.uuid4()), "name": name, "place":place, "teacherid":teacherid}
        with redis.Redis() as client:
            client.json().arrappend('subjects', Path.root_path(), sub_data)
            return True
    else:
        return False

def delete_subject(name):
    if not subject_notexist:
        with redis.Redis() as client:
            client.execute_command(f'JSON.DEL subjects $.{name}', Path.root_path())
            return True
    else:
        return False

def update_subject(name, place, teacherid):
    delete_subject(name)
    create_subject(name,place, teacherid)
