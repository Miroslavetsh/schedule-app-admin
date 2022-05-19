import json
from flask import Blueprint
from redis_workers import base

db_api = Blueprint('/api/db', __name__,
                   template_folder='templates')


@db_api.route('/', methods=['get'])
def get_all_schedules():
    response = {}

    list_of_entities = ["subjects", "teachers",
                        "groups", "schedules", "pairs", "days"]
    for key in list_of_entities:
        response[key] = base.get_all_items(key)

    return json.dumps(response)
