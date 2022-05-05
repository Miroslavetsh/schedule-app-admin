from flask import Blueprint, render_template, request

from redis_workers.pairs import get_pairs_by_teacher_id


pairs_page = Blueprint('/pairs', __name__,
                       template_folder='templates')


@pairs_page.route('/', methods=['get', 'post'])
def get_pairs():
    if request.method == 'POST':
        form_params = request.form.to_dict()
        pairs = get_pairs_by_teacher_id(form_params['teacher_id'])

        return render_template('pairs.html', pairs=pairs)
    else:
        return render_template('pairs.html', pairs=[])
