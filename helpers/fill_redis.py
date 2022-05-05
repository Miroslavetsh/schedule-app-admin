# Automatic Redis filling with some new data
# import redis
# from redis.commands.json.path import Path

# base_name = 'days'
# data = [
#       { "id": 1, "name": "Понеділок" },
#       { "id": 2, "name": "Вівторок" },
#       { "id": 3, "name": "Середа" },
#       { "id": 4, "name": "Четвер" },
#       { "id": 5, "name": "П'ятниця" },
#       { "id": 6, "name": "Субота" },
#       { "id": 7, "name": "Неділя" }
#     ]

# with redis.Redis() as client:
#     client.json().set(base_name, Path.root_path(), data)
#     print(client.json().get(base_name))
