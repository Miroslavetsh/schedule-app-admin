# Third-party libs
from flask import Flask, render_template
import logging
# Our libs
from redis_workers.teachers import get_teachers_list
from routes.groups import groups_page
from routes.teachers import teachers_page
from routes.pairs import pairs_page
from routes.schedules import schedules_page

logging.basicConfig(filename="logfile.txt",
                    filemode='w',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.debug("Logging test...")

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    teachers = get_teachers_list()
    return render_template('index.html', teachers=teachers)


app.register_blueprint(groups_page, url_prefix='/groups')
app.register_blueprint(teachers_page, url_prefix='/teachers')
app.register_blueprint(pairs_page, url_prefix='/pairs')
app.register_blueprint(schedules_page, url_prefix='/schedules')


if __name__ == "__main__":
    app.run(debug=True)
