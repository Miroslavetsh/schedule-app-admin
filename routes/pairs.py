from flask import Blueprint, redirect, render_template, request

from redis_workers.pairs import get_pairs_by_teacher_id


pairs_page = Blueprint('/pairs', __name__,
                       template_folder='templates')


@pairs_page.route('/', methods=['get'])
def get_pairs():
    pairs = []

    return render_template('pairs.html', pairs=pairs)


@pairs_page.route('/<teacher_id>', methods=['post'])
def get_pairs_by_teacher_id(teacher_id):
    pairs = get_pairs_by_teacher_id(teacher_id)

    return render_template('pairs.html', pairs=pairs)


@pairs_page.route('/<pair_id>/update', methods=['post'])
def update_pair(pair_id):
    # TODO: postpone for a while or cancel
    pass
