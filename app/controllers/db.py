import json
from flask import Blueprint
from services import base

api = Blueprint('db', __name__,
                template_folder='templates')


@api.route('/', methods=['get'])
def get_all_schedules():
    response = {}

    list_of_entities = ["subjects", "teachers",
                        "groups", "schedules", "pairs", "days"]
    for key in list_of_entities:
        response[key] = base.get_all_items(key)

    return json.dumps(response)
