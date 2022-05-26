
import json
from flask import Blueprint, request
import services.teacher as teacher_service

api = Blueprint('teachers', __name__, template_folder='templates')


@api.route('/teachers', methods=['GET'])
def get_all_teachers():
    return json.dumps(teacher_service.get_all())


@api.route('/teachers/<string:id>', methods=['GET'])
def get_teacher(id):
    return json.dumps(teacher_service.get(id))


@api.route("/teachers", methods=['POST'])
def add_teacher():
    return json.dumps(teacher_service.post(request.json))


@api.route('/teachers/<string:id>', methods=['PUT'])
def update_teacher(id):
    teacher_service.put(id, request.json)


@api.route('/teachers/<string:id>', methods=['DELETE'])
def delete_teacher(id):
    teacher_service.delete(id)
