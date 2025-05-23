from flask import Blueprint, render_template, request, redirect, url_for
from app.db import get_db

app = Blueprint('app', __name__)

# 「/」というURLにアクセスしたときの処理
@app.route('/')
def index():
    db = get_db()
    todos = db.execute('SELECT id, task FROM todos WHERE task IS NOT NULL').fetchall()
    if todos:
        print(todos)
        print(todos[0])
        print(type(todos[0]))
    return render_template("index.html", todos=todos)

# /addにアクセスしたときの処理(addボタンを押したとき)
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        db = get_db()
        db.execute('INSERT INTO todos (task) VALUES (?)', (task,))
        db.commit()
    return redirect(url_for('app.index'))

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete(task_id):
    db = get_db()
    db.execute('DELETE FROM todos WHERE id = ?', (task_id,))
    db.commit()
    return redirect(url_for('app.index'))
