from flask import Blueprint, render_template


schedules_page = Blueprint('/schedules', __name__,
                           template_folder='templates')


@schedules_page.route('/', methods=['get'])
def get_schedules():
    # TODO: normal schedules getting from DB
    schedules=[]

    return render_template('schedules.html', schedules=schedules)

@schedules_page.route('/add', methods=['post'])
def add_schedule():
    # TODO: schedules adding to DB
    schedules=[]

    return render_template('schedules.html', schedules=schedules)

@schedules_page.route('/<schedule_id>/update', methods=['post'])
def update_schedule(schedule_id):
    # TODO: schedules changing and save to DB
    schedules=[]

    return render_template('schedules.html', schedules=schedules)

@schedules_page.route('/<schedule_id>/delete', methods=['post'])
def delete_schedule(schedule_id):
    # TODO: schedules changing and save to DB
    schedules=[]

    return render_template('schedules.html', schedules=schedules)
