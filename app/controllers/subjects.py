from flask import Blueprint, render_template, request
from services import base


api = Blueprint('subjects', __name__,
                template_folder='templates')


@api.route('/', methods=['get'])
def get_api():
    subjects = base.get_all_items("subjects")
    teachers = base.get_all_items('teachers')
    return render_template('subjects.html', subjects=subjects, teachers=teachers)


@api.route('/add', methods=['post'])
def add_subject_page():
    form_parameters = request.form.to_dict()
    subjects = base.set("subjects",
                        name=form_parameters['name'],
                        place=form_parameters['place'],
                        teacher_id=form_parameters['teacherId'])
    return render_template('subjects.html', subjects=subjects)


@api.route('/<subject_id>/update', methods=['delete', 'patch', 'post'])
def update_group_page(subject_id):
    form_parameters = request.form.to_dict()
    subjects = base.update("subjects", id=subject_id,
                           name=form_parameters['name'],
                           place=form_parameters['place'],
                           teacher_id=form_parameters["teacherId"])
    return render_template('subjects.html', subjects=subjects)


@api.route('/<subject_id>/delete', methods=['delete', 'post'])
def delete_group_page(subject_id):
    subjects = base.delete("subjects", id=subject_id)
    return render_template('subjects.html', subjects=subjects)
