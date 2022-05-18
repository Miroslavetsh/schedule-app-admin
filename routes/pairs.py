from flask import Blueprint, render_template, request
from redis_workers import base
from redis_workers.pairs import get_pairs_by_teacher_id
import json


pairs_page = Blueprint('/pairs', __name__,
                       template_folder='templates')


@pairs_page.route('/', methods=['get'])
def get_pairs():
    pairs = base.get_all_items("pairs")
    subjects = base.get_all_items("subjects")
    return render_template('pairs.html', pairs=pairs, subjects=subjects)


@pairs_page.route('/<teacher_id>', methods=['get'])
def get_pairs_page_by_teacher_id(teacher_id):
    pairs = get_pairs_by_teacher_id(teacher_id)
    return json.dumps(pairs)


@pairs_page.route('/add', methods=['post'])
def add_pair():
    # TODO: provide an adding of pair
    pairs = base.get_all_items("pairs")
    form_parameters = request.form.to_dict()
    form_parameters['subjectId']
    form_parameters['time']


@pairs_page.route('/<pair_id>/update', methods=['delete', 'patch', 'post'])
def update_pair(pair_id):
    form_parameters = request.form.to_dict()
    pairs = base.update(arr="pairs", id=pair_id,
                        subjectId=form_parameters['subjectId'],
                        time=form_parameters['time'])
    return render_template('pairs.html', pairs=pairs)


@pairs_page.route('/<pair_id>/delete', methods=['delete', 'post'])
def delete_pair_page(pair_id):
    subjects = base.delete("pairs", id=pair_id)
    return render_template('pairs.html', subjects=subjects)
