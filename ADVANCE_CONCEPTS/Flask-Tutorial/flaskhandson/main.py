from flask import Flask, request, render_template, make_response
from markupsafe import escape

# create flask object
app = Flask(__name__)  # __name__ -> __main__

studentdb = [
    {"name": "bhanu", "course": "python", "duration": 3},
    {"name": "lasya", "course": "java", "duration": 6},
    {"name": "teja", "course": "ruby", "duration": 2}
]

users = {
    'username': 'kumar',
    'password': 'kumar123'
}


# routes
@app.get('/')
def root() -> dict:
    return {'status': 'Welcome to flask'}


@app.get("/status")
def status() -> str:
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


# LOGIN routes

@app.route('/login')
def view_form():
    return render_template('getpost.html')


@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        username = request.args['username']
        password = request.args['password']
        if username == users.get('username') and password == users.get("password"):
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('getpost.html')


@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username == users.get('username') and password == users.get("password"):
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('getpost.html')


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name: str = None):
    return render_template('hello.html', name=name)


#  Cookies
@app.route("/getcooky")
def testcookies():
    cookies = request.cookies
    print(cookies)
    return "testing cookies"


@app.route("/setcooky")
def setcooky():
    resp = make_response(render_template('hello.html'))
    resp.set_cookie('username', 'kumar')
    resp.set_cookie("movie_name", "avengers")
    resp.set_cookie("year", "2023")
    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=1133)
