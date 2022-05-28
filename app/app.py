from config import app
from controllers.teachers import api as teachers_api
from controllers.groups import api as groups_api
from controllers.pairs import api as pairs_api
# from controllers.schedules import api as schedules_api
# from controllers.subjects import api as subjects_api
from controllers.db import api as db_api


# @app.route('/')
# def index():
#     teachers = get_all_teachers()
#     return render_template('index.html', teachers=teachers)


app.register_blueprint(teachers_api)
app.register_blueprint(groups_api)
app.register_blueprint(pairs_api)
# app.register_blueprint(schedules_api)
# app.register_blueprint(subjects_api)
app.register_blueprint(db_api)


if __name__ == "__main__":
    app.run(debug=True)
