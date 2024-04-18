from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

tasks = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/add_task')
def add_task():
    task = request.form['task']
    task_id = len(tasks) + 1
    tasks[task_id] = task
    return jsonify({'task_id': task_id, 'task': task})

@app.post('/delete_task')
def delete_task():
    task_id = int(request.form['task_id'])
    if task_id in tasks:
        del tasks[task_id]
    return jsonify({'success': True})

@app.get('/get_tasks')
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)