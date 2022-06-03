import json
from flask import Blueprint, request

import services.schedule as schedule_service

api = Blueprint('schedules', __name__)


@api.route('/schedules', methods=['GET'])
def get_all_schedules():
    return json.dumps(schedule_service.get_all())


@api.route('/schedules/<string:id>', methods=['GET'])
def get_schedule(id):
    return json.dumps(schedule_service.get(id))


@api.route("/schedules", methods=['POST'])
def add_schedule():
    return json.dumps(schedule_service.post(request.json))


@api.route('/schedules/<string:id>', methods=['PUT'])
def update_schedule(id):
    return json.dumps(schedule_service.put(id, request.json))


@api.route('/schedules/<string:id>', methods=['DELETE'])
def delete_schedule(id):
    return json.dumps(schedule_service.delete(id))
