from flask import Blueprint, render_template, request
from redis_workers import base
from redis_workers.pairs import get_pairs_by_teacher_id


pairs_page = Blueprint('/pairs', __name__,
                       template_folder='templates')


@pairs_page.route('/', methods=['get'])
def get_pairs():
    pairs = base.get_all_items("pairs")
    return render_template('pairs.html', pairs=pairs)


@pairs_page.route('/<teacher_id>', methods=['post'])
def get_pairs_by_teacher_id(teacher_id):
    pairs = get_pairs_by_teacher_id(teacher_id)
    return render_template('pairs.html', pairs=pairs)


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
