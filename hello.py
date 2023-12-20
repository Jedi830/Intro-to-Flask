from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index ():
    user_name = "xxNOTFAZExx"

    return render_template("home.html.jinja", gamertag = user_name)


@app.route ('/ping')
def ping ():
    return "<h1>Pong</h1>"

@app.route('/hello/<name>')
def hello(name):
   # return "hello" + name
    return f"hello {name}"

