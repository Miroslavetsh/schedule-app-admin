import redis
from redis.commands.json.path import Path


def get_groups():
    with redis.Redis() as client:
        return client.json().get('groups')


def create_group(data):
    with redis.Redis() as client:
        return client.json().arrappend('groups', Path.root_path(), data)


def delete_group(id):
    with redis.Redis() as client:
      groups = client.json().get('groups')
      
      for group in groups:
        if group['id'] == id:
          groups.remove(group)

      return client.json().set('groups', Path.root_path(), groups)
