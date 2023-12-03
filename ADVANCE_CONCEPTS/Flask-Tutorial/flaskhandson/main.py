from flask import Flask, request, render_template
from markupsafe import escape

# create flask object
app = Flask(__name__)

studentdb = [
    {"name": "bhanu", "course": "python", "duration": 3}
]


# routes
@app.get('/')
def root() -> dict:
    return {'status': 'Welcome to flask'}


@app.get("/hello")
def hello() -> str:
    return "Hello Flask 3.0.0 version app"


# get with path variable
@app.get("/welcome/<name>")
def welcome(name: str) -> dict:
    return {'message': f'Hello Welcome user {name}'}


# get with request param
@app.get("/add")
def addition() -> dict:
    args = request.args  # Immutable Dictionary
    print(args)
    num1 = int(args.get('num1'))
    num2 = int(args.get('num2'))
    return {'addition': f'result of {num1} + {num2} = {num1 + num2}'}


# Variable Rules
# <converter:variablename>
# converter: int, float, path, uuid

@app.route("/user/<username>")
def show_user_profile(username) -> str:
    return f'User {escape(username)}'


@app.route("/post/<float:post_id>")
def show_post(post_id) -> str:
    print(post_id, type(post_id))
    return f'Post {escape(post_id)}'


@app.route("/path/<path:subpath>")
def show_subpath(subpath) -> str:
    return f'SubPath {escape(subpath)}'


# ReDirection

@app.get("/home")
def home():
    return "Home page"


@app.get("/contact")
def contact_us():
    return "contact us page"


# POST
@app.post("/student")
def add_student() -> list[dict]:
    print('invoking add student method')
    student = request.get_json()  # request object
    print(student)
    studentdb.append(student)
    return studentdb


## HTML Rending

@app.get("/api/welcome/<loginusername>")
def welcome_user(loginusername: str):
    return render_template("welcome.html", data=loginusername)


@app.get("/api/student/display")
def display_student():
    return render_template("welcome.html", studentdata=studentdb)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=1133)
