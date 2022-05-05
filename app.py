# Third-party libs
from flask import Flask, render_template, request
import redis_sql
import logging
from redis_workers.pairs import get_pairs_by_teacher_id
# Our libs
from redis_workers.teachers import get_all_teachers

logging.basicConfig(filename="logfile.txt",
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.debug("Logging test...")

app = Flask(__name__)


@app.route('/')
def index():
    teachers = get_all_teachers()
    return render_template('index.html', teachers=teachers)


@app.route('/teachers', methods=['get', 'post'])
def teachers():
    if request.method == "post":
        # Here we are posting a new teacher
        output = request.form['full_name']
        return render_template('teachers.html')
    else:
        # Return a teachers_list to the teachers_page
        return render_template('teachers.html', teachers=teachers)


@app.route("/create_teacher", methods=['get', 'post'])
def create():
    if request.method == "post":
        output = request.form.get('new_name')
        logging.warning('route create teacher post method')
        logging.error(output)
        redis_sql.add_teacher(output)
        return render_template('index.html')
    else:
        logging.warning('route create teacher get method')
        return render_template('create_teacher.html')


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
