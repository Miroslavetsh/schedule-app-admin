import redis
from redis.commands.json.path import Path
import uuid

def get_all_groups():
    with redis.Redis() as client:
        return client.json().get('groups')

def get_groups(id):
    with redis.Redis() as client:
        for group in client.json().get("groups"):
            if str(group['name']) == str(id):
                return group
            return None


def create_group(name):
    data = {'id': str(uuid.uuid4()), "name":name}
    with redis.Redis() as client:
        return client.json().arrappend('groups', Path.root_path(), data)


def delete_group(id):
    with redis.Redis() as client:
      groups = client.json().get('groups')
      
      for group in groups:
        if group['id'] == id:
          groups.remove(group)

      return client.json().set('groups', Path.root_path(), groups)

def update_group(name, subjectId, time):
    delete_group(name)
    create_group(name, subjectId, time)