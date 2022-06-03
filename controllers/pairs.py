import json
from flask import Blueprint, request

import services.pair as pair_service

api = Blueprint('pairs', __name__)


@api.route('/pairs', methods=['GET'])
def get_all_pairs():
    return json.dumps(pair_service.get_all())


@api.route('/pairs/<string:id>', methods=['GET'])
def get_pair(id):
    return json.dumps(pair_service.get(id))


@api.route("/pairs", methods=['POST'])
def add_pair():
    return json.dumps(pair_service.post(request.json))


@api.route('/pairs/<string:id>', methods=['PUT'])
def update_pair(id):
    return json.dumps(pair_service.put(id, request.json))


@api.route('/pairs/<string:id>', methods=['DELETE'])
def delete_pair(id):
    return json.dumps(pair_service.delete(id))
