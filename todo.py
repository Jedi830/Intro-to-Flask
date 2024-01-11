from flask import Flask, render_template, request, redirect
import pymysql
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


authentication = HTTPBasicAuth()
app = Flask(__name__)

users = {
    "jedaiah": generate_password_hash("Jedaiahd2")
}

connection = pymysql.connect(
    database = "jdelacruz_todos",
    user = "jdelacruz",
    password = "229770375",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor,
)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/')
@authentication.login_required
def index():
    if request.method == 'POST':
        new_todo = request.form["new_todo"]
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO `todos`(`description`) VALUES ('{new_todo}')")
        cursor.close
        connection.commit

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `todos` ORDER BY `complete`")
    results = cursor.fetchall() 
    cursor.close()
    return render_template("jtodo.html.jinja", js_todos = results)
     

@app.route('/delete_todo/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index} ")
    cursor.close
    connection.commit
    return redirect('/')

@app.route('/complete_todo/<int:todo_index>', methods = ['POST'])
def todo_complete(todo_index):
    cursor = connection.cursor()
    cursor.execute("UPDATE `todos` SET `complete` = 1 WHERE `id` = {todo_index}")
    cursor.close
    connection.commit
    return redirect('/')

@authentication.verify_password
def verify_pasword(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


