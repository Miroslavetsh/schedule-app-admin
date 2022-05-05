# Third-party libs
from flask import Flask, render_template, request
import logging
# Our libs
import redis_sql
from redis_workers.pairs import get_pairs_by_teacher_id
from redis_workers.teachers import get_teachers_list
from routes.groups import groups_page
from routes.teachers import teachers_page

logging.basicConfig(filename="logfile.txt",
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.debug("Logging test...")

app = Flask(__name__, template_folder='templates')
app.register_blueprint(groups_page, url_prefix='/groups')
app.register_blueprint(teachers_page, url_prefix='/teachers')


@app.route('/')
def index():
    teachers = get_teachers_list()
    return render_template('index.html', teachers=teachers)


@app.route('/schedules', methods=['get', 'post'])
def changing_sc():
    if request.method == 'post':
        # Here create a new schedule in redis
        output = request.form.to_dict()
        redis_sql.changing_sc(output)
    else:
        return render_template('changing_sc.html', subjects=redis_sql.get_subjects())


@app.route('/pairs', methods=['get', 'post'])
def get_pairs():
    if request.method == 'POST':
        form_params = request.form.to_dict()
        pairs = get_pairs_by_teacher_id(form_params['teacher_id'])

        return render_template('pairs.html', pairs=pairs)
    else:
        return render_template('pairs.html', pairs=[])


if __name__ == "__main__":
    app.run(debug=True)
