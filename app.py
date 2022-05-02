import redis
from flask import Flask, render_template, request
import redis_sql



app = Flask(__name__)

@app.route('/', methods=['get','post'])
def index():
    if request.method == "POST":
        pass
    else:
        return render_template('index.html')

@app.route('/teachers', methods=['get','post'])
def teachers():
    if request.method == "post":
        output = request.form.to_dict()['full_name']
        return render_template('teachers.html', lessons=redis_sql.get_lessons(output))
    else:
        return render_template('teachers.html')

@app.route('/changing_sc', methods=['get','post'])
def changing_sc():
    if request.method == 'post':
        pass
    else:
        return render_template('changing_sc.html')


if __name__ == "__main__":
    app.run(debug=True)