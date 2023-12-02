from flask import Flask , render_template,request

# create a flask app object 

app = Flask(__name__)


credDB = {
    'username': 'admin',
    'password': 'june123'
}

students = [{
    'name': "fenil",
    'course': 'python',
    'level': 3,
    'isStudent':True,
    'skills' : ['python','IOT']
},
{
    'name': "sowmya",
    'course': 'python',
    'level': 3,
    'isStudent':True,
    'skills' : ['python','java','c']
},
{
    'name': "Ravi",
    'course': 'java',
    'level': 2,
    'isStudent':False,
    'skills' : ['web','c','cpp']
},
{
    'name': "Shivani",
    'course': 'python',
    'level': 2,
    'isStudent':False,
    'skills' : ['c']
},
]

# creates routes with decorates.
@app.route('/')
def home():
    return render_template('home.html',data = 'Hello Welcome to My Web-APP')

@app.route('/students')
def students_data():
    #return {'data': students}
    return render_template('students.html',students = students)

@app.route('/students/<name>')
def get_student(name):
    print(name)

    for student in students:
        if name in student['name']:
            return student    
    else:
        return {'data': f'student with name {name} not found..'}
 

@app.route("/welcome")
def welcome():
    return render_template('welcome.html' , name = 'Kumar')


@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['uname']
        password = request.form['psw']
        print(f'{username } , {password}')

        if username == credDB['username'] and password == credDB['password']:
            return render_template('response.html' , data = f'LOGIN SUCCESS Weclome {username}')
        else:
            return render_template('response.html' , data = f'Invalid Creds Please check , try again...')

    return render_template('login.html')


@app.route("/contact")
def contact():
    address = 'PO BOX NY 5214 Street1'
    email = 'foodcourt@foodie.com'
    return render_template('contactus.html' , address=address , email = email)


@app.route("/about")
def about():
    return render_template('aboutus.html' , data = 'we are rock reciepe food court startup food business...')

if __name__ == '__main__':
    app.run(debug=True)