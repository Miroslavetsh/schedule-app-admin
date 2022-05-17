
from flask import Blueprint, render_template, request
from redis_workers import base
from redis_workers.teachers import get_teachers_list, add_teacher

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


@teachers_page.route('/<teacher_id>/update', methods=['delete', 'patch','post'])
def update_teacher_page(teacher_id):
    form_parameters = request.form.to_dict()
    teachers = base.update("teachers", id=teacher_id,
     name=form_parameters['name'])
    return render_template('teachers.html', teachers=teachers)


@teachers_page.route('/<teacher_id>/delete', methods=['delete', 'post'])
def delete_teacher_page(teacher_id):
    teachers = base.delete("teachers", id=teacher_id)
    return render_template('teachers.html', teachers=teachers)
