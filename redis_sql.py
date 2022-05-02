import redis
from redis.commands.json.path import Path

jane = {
     'name': ["Jane","greb"], 
     'Age': 33, 
     'Location': "Chawton"
   }

def get_lessons(full_name):
    with redis.Redis() as client:
        return client.get('full_name')

def changing_sc():
    pass


with redis.Redis() as client:
    client.json().set('lesson',Path.root_path(), jane)
    print(client.json().get('lesson'))


#json.set firsttable $ {"subjects":{"id":1, "name":"OOP", "teacherid":1}