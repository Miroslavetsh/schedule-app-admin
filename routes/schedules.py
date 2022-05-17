from flask import Blueprint, render_template, request
from redis_workers import base

schedules_page = Blueprint('/schedules', __name__,
                           template_folder='templates')


@schedules_page.route('/', methods=['get'])
def get_schedules():
    form_parameters = request.form.to_dict()
    schedules = base.get(form_parameters['id'], form_parameters['id'], "schedules")
    return render_template('schedules.html', schedules=schedules)

@schedules_page.route('/add', methods=['post'])
def add_schedule():
    form_parameters = request.form.to_dict()
    schedules = base.set(arr="schedules", groupId=form_parameters['groupId'], days=form_parameters['days'])
    return render_template('schedules.html', schedules=schedules)

@schedules_page.route('/<schedule_id>/update', methods=['delete', 'patch', 'post'])
def update_schedule(schedule_id):
    form_parameters = request.form.to_dict()
    schedules = base.update(arr="schedules", id=schedule_id, groupId=form_parameters['groupId'], days=form_parameters['days'])
    return render_template('schedules.html', schedules=schedules)

@schedules_page.route('/<schedule_id>/delete', methods=['delete', 'post'])
def delete_schedule(schedule_id):
    schedules = base.delete("schedules", schedule_id)
    return render_template('schedules.html', schedules=schedules)
