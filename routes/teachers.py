
import json
from flask import Blueprint, render_template, request
from redis_workers import base
from redis_workers.teachers import get_teachers_list, add_teacher

teachers_page = Blueprint('/teachers', __name__, template_folder='templates')


@teachers_page.route('/', methods=['get'])
def get_all_teachers():
    teachers = get_teachers_list()

    return json.dumps(teachers)


@teachers_page.route("/create", methods=['post'])
def create_teacher():
    pass


@teachers_page.route('/<teacher_id>/update', methods=['delete', 'patch', 'post'])
def update_teacher(teacher_id):
    pass


@teachers_page.route('/<teacher_id>/delete', methods=['delete', 'patch', 'post'])
def delete_teacher(teacher_id):
    pass
