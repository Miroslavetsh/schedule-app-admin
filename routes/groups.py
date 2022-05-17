from flask import Blueprint, render_template, request
from redis_workers import base

groups_page = Blueprint('/groups', __name__,
                        template_folder='templates')


@groups_page.route('/', methods=['get'])
def get_groups_page():
    groups = base.get_all_items("groups")
    return render_template('groups.html', groups=groups)


@groups_page.route('/add', methods=['post'])
def add_group_page():
    form_parameters = request.form.to_dict()
    groups = base.set(arr="groups", name=form_parameters['name'])
    return render_template('groups.html', groups=groups)



@groups_page.route('/<group_id>/update', methods=['delete', 'patch', 'post'])
def update_group_page(group_id):
    form_parameters = request.form.to_dict()
    groups = base.update(arr="groups", id=group_id, new_name=form_parameters['new_name'])
    return render_template('groups.html', groups=groups)


@groups_page.route('/<group_id>/delete', methods=['delete', 'post'])
def delete_group_page(group_id):
    groups = base.delete(arr="groups", id=group_id)
    return render_template('groups.html', groups=groups)