import json
from flask import Blueprint
from services import base

api = Blueprint('db', __name__)


@api.route('/db', methods=['GET'])
def get_db():
    response = {}

    tables = ["subjects", "teachers",
              "groups", "schedules", "pairs", "days"]
    for key in tables:
        response[key] = base.get_all(key)

    return json.dumps(response)
