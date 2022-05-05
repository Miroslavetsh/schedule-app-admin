from flask import Blueprint, render_template

from redis_workers.groups import get_all_groups

groups_page = Blueprint('groups_page', __name__,
                        template_folder='templates')


@groups_page.route('/', methods=['get'])
def get_groups_page():
    groups = get_all_groups()

    return render_template('groups.html', groups=groups)


@groups_page.route('/add', methods=['post'])
def add_group_page():
    pass


@groups_page.route('/<group_id>/update', methods=['post'])
def update_group_page(group_id):
    pass


@groups_page.route('/<group_id>/delete', methods=['post'])
def delete_group_page(group_id):
    pass
