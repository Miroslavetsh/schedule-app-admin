from redis.commands.json.path import Path
import redis
import uuid

def schedules_notexist(name):
    return get_schedules(name) == None

def get_schedules(id):
    with redis.Redis() as client:
        for sc in client.json().get("schedules"):
            if str(sc['id']) == str(id):
                return sc
            return None


def create_schedules(groupId, days):
    if schedules_notexist:
        data = {'id': str(uuid.uuid4()), "groupId":groupId, "days":days}
        with redis.Redis() as client:
            client.json().arrappend('schedules', Path.root_path(), data)
            return True
    else:
        return False

def delete_schedules(name):
    if not schedules_notexist:
        with redis.Redis() as client:
            client.execute_command(f'JSON.DEL schedules $.{name}', Path.root_path())
            return True
    else:
        return False

def update_subject(name, id, days):
    delete_schedules(name)
    create_schedules(name, id, days)
