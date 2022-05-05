
from flask import render_template

from redis_workers.groups import get_groups

from __main__ import app


@app.route('/groups', methods=['get'])
def get_groups():
    groups = get_groups()

    return render_template('groups.html', groups=groups)


@app.route('/groups/add', methods=['post'])
def add_group():
    pass


@app.route('/groups/<group_id>/update', methods=['post'])
def update_group(group_id):
    pass


@app.route('/groups/<group_id>/delete', methods=['post'])
def delete_group(group_id):
    pass
