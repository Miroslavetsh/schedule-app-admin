import json
from flask import Blueprint, request

import services.subject as subject_service

api = Blueprint('subjects', __name__)


@api.route('/subjects', methods=['GET'])
def get_all_subjects():
    return json.dumps(subject_service.get_all())


@api.route('/subjects/<string:id>', methods=['GET'])
def get_subject(id):
    return json.dumps(subject_service.get(id))


@api.route("/subjects", methods=['POST'])
def add_subject():
    return json.dumps(subject_service.post(request.json))


@api.route('/subjects/<string:id>', methods=['PUT'])
def update_subject(id):
    return json.dumps(subject_service.put(id, request.json))


@api.route('/subjects/<string:id>', methods=['DELETE'])
def delete_subject(id):
    return json.dumps(subject_service.delete(id))
