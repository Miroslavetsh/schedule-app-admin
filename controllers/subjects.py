import json
from flask import Blueprint, request
from flask_cors import cross_origin
import services.subject as service

api = Blueprint('subjects', __name__)


@api.route('/subjects', methods=['GET'])
def get_all_subjects():
    return json.dumps(service.get_all())


@api.route('/subjects/<string:id>', methods=['GET'])
def get_subject(id):
    return json.dumps(service.get(id))


@api.route('/subjects/get-by-teacher-id/<string:id>', methods=['GET'])
@cross_origin()
def get_all_subjects_by_teacher_id(id):
    return json.dumps(service.get_by_teacher_id(id))


@api.route("/subjects", methods=['POST'])
def add_subject():
    return json.dumps(service.post(request.json))


@api.route('/subjects/<string:id>', methods=['PUT'])
def update_subject(id):
    return json.dumps(service.put(id, request.json))


@api.route('/subjects/<string:id>', methods=['DELETE'])
def delete_subject(id):
    return json.dumps(service.delete(id))
