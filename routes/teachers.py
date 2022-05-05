
from flask import Blueprint, render_template, request

from redis_workers.teachers import get_teacher_by_name, get_teachers_list, add_teacher

teachers_page = Blueprint('/teachers', __name__, template_folder='templates')


@teachers_page.route('/', methods=['get'])
def get_teachers_page():
    teachers = get_teachers_list()

    return render_template('teachers.html', teachers=teachers)


@teachers_page.route("/add", methods=['get', 'post'])
def add_teacher_page():

    if request.method == "POST":
        form_parameters = request.form.to_dict()
        add_teacher(form_parameters['teacher_name'])
        teachers = get_teachers_list()

        return render_template('teachers.html', teachers=teachers)
    else:
        return render_template('teachers.html', teachers=teachers)
