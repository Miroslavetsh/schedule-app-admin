from flask import Blueprint, render_template, request
from services import base

api = Blueprint('schedules', __name__,
                template_folder='templates')


@api.route('/', methods=['get'])
def get_schedules():
    groups = base.get_all_items('groups')
    days = base.get_all_items('days')
    pairs = base.get_all_items('pairs')

    for pair in pairs:
        subj = base.get_entity_from_collection_by_id(
            'subjects', pair['subjectId'])
        teacher = base.get_entity_from_collection_by_id(
            'teachers', subj['teacherId'])

        pair['name'] = subj['name']
        pair['teacher'] = teacher['name']

    return render_template('schedules.html', groups=groups, days=days, pairs=pairs)


@api.route('/add', methods=['post'])
def add_schedule():
    form_parameters = request.form.to_dict()
    schedules = base.set(
        arr="schedules", groupId=form_parameters['groupId'], days=form_parameters['days'])
    return render_template('schedules.html', schedules=schedules)


@api.route('/<schedule_id>/update', methods=['delete', 'patch', 'post'])
def update_schedule(schedule_id):
    form_parameters = request.form.to_dict()
    schedules = base.update(arr="schedules", id=schedule_id,
                            groupId=form_parameters['groupId'], days=form_parameters['days'])
    return render_template('schedules.html', schedules=schedules)


@api.route('/<schedule_id>/delete', methods=['delete', 'post'])
def delete_schedule(schedule_id):
    schedules = base.delete("schedules", schedule_id)
    return render_template('schedules.html', schedules=schedules)
