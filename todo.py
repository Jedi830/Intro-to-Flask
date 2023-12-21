from flask import Flask, render_template, request

app = Flask(__name__)

todos = ["Play Lego fortnite,","Work out consistently"]

@app.route('/', methods = ['GET', 'POST'])
def index():
    new_todo = request.form["new_todo"]
    todos.append = (new_todo)
    return render_template("jtodo.html.jinja", js_todos = todos)


