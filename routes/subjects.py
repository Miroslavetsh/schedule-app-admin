from flask import Blueprint, render_template


subjects_page = Blueprint('/subjects', __name__,
                          template_folder='templates')


@subjects_page.route('/', methods=['get'])
def get_subjects_page():
    subjects = []

    return render_template('subjects.html', subjects=subjects)


@subjects_page.route('/add', methods=['post'])
def add_subject_page():
    pass


@subjects_page.route('/<subject_id>/update', methods=['post'])
def update_group_page(subject_id):
    pass


@subjects_page.route('/<subject_id>/delete', methods=['post'])
def delete_group_page(subject_id):
    pass
