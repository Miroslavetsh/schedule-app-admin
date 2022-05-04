import redis
from flask import Flask, render_template, request
import redis_sql
import logging

logging.basicConfig(filename="logfile.txt",
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.debug("Logging test...")

redis_sql.add_teacher('Myroslav Toloshnyi')

app = Flask(__name__)

@app.route('/')
def index():
    logging.warning('route index')
    return render_template('index.html')

@app.route('/teachers', methods=['get','post'])
def teachers():
    logging.warning('route teachers post1 method')
    if request.method == "post": # не працює!!!!!!!
        output = request.form['full_name']
        logging.warning('route teachers post2 method')
        logging.error(output)
        return render_template('teachers.html', lessons=redis_sql.get_lessons(output))
    else:
        logging.warning('route teachers get method')
        return render_template('teachers.html')

@app.route("/create_teacher", methods=['get','post'])
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


@app.route('/changing_sc', methods=['get','post'])
def changing_sc():
    if request.method == 'post':
        output = request.form.to_dict()
        redis_sql.changing_sc(output)
    else:
        return render_template('changing_sc.html')


if __name__ == "__main__":
    app.run(debug=True)