from flask import Blueprint, render_template

from redis_workers.groups import get_all_groups

groups_page = Blueprint('groups_page', __name__,
                        template_folder='templates')


@groups_page.route('/', methods=['get'])
def get_groups():
    # print('here')
    groups = get_all_groups()

    return render_template('groups.html', groups=groups)


@groups_page.route('/add', methods=['post'])
def add_group():
    pass


@groups_page.route('/<group_id>/update', methods=['post'])
def update_group(group_id):
    pass


@groups_page.route('/<group_id>/delete', methods=['post'])
def delete_group(group_id):
    pass

# @groups_page.route('/', defaults={'page': 'index'})
# @groups_page.route('/<page>')
# def show(page):
#     try:
#         return render_template(f'pages/{page}.html')
#     except TemplateNotFound:
#         abort(404)
