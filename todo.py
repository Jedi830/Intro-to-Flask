from flask import Flask, render_template, request, redirect
import pymysql
from pprint import pprint as print

app = Flask(__name__)

connection = pymysql.connect(
    database = "jdelacruz_todos",
    user = "jdelacruz",
    password = "229770375",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor,
)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        todo.append(new_todo)
    cursor = connection.cursor()
    cursor.execute("SELECT `description` FROM `todos` ")
    results = cursor.fetchall() 
    return render_template("jtodo.html.jinja", js_todos = results)
     

@app.route('/delete_todo/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
    del todos[todo_index]
    return redirect('/')



