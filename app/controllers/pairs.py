from flask import Blueprint, render_template, request
from services import base
from services.pairs import get_pairs_by_teacher_id
import json


api = Blueprint('pairs', __name__,
                template_folder='templates')


@api.route('/', methods=['get'])
def get_pairs():
    pairs = base.get_all_items("pairs")
    subjects = base.get_all_items("subjects")
    return render_template('pairs.html', pairs=pairs, subjects=subjects)


@api.route('/<teacher_id>', methods=['get'])
def get_api_by_teacher_id(teacher_id):
    pairs = get_pairs_by_teacher_id(teacher_id)
    return json.dumps(pairs)


@api.route('/add', methods=['post'])
def add_pair():
    pairs = base.get_all_items("pairs")
    form_parameters = request.form.to_dict()
    form_parameters['subjectId']
    form_parameters['startTime']
    form_parameters['endTime']


@api.route('/<pair_id>/update', methods=['delete', 'patch', 'post'])
def update_pair(pair_id):
    form_parameters = request.form.to_dict()
    pairs = base.update(arr="pairs", id=pair_id,
                        subjectId=form_parameters['subjectId'],
                        time=form_parameters['time'])
    return render_template('pairs.html', pairs=pairs)


@api.route('/<pair_id>/delete', methods=['delete', 'post'])
def delete_pair_page(pair_id):
    subjects = base.delete("pairs", id=pair_id)
    return render_template('pairs.html', subjects=subjects)
