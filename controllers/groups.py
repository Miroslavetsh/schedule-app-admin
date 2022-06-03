import json
from flask import Blueprint, request

import services.group as group_service

api = Blueprint('groups', __name__)


@api.route('/groups', methods=['GET'])
def get_all_groups():
    return json.dumps(group_service.get_all())


@api.route('/groups/<string:id>', methods=['GET'])
def get_group(id):
    return json.dumps(group_service.get(id))


@api.route("/groups", methods=['POST'])
def add_group():
    return json.dumps(group_service.post(request.json))


@api.route('/groups/<string:id>', methods=['PUT'])
def update_group(id):
    return json.dumps(group_service.put(id, request.json))


@api.route('/groups/<string:id>', methods=['DELETE'])
def delete_group(id):
    return json.dumps(group_service.delete(id))
