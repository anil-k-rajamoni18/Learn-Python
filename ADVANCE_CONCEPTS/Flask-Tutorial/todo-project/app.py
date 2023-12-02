from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

#object creation
app = Flask(__name__)
app.secret_key = b'_53oi3uriq9pifpff;apl'
csrf = CSRFProtect(app)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])



#create route
@app.route('/')
def hello_world():
    return '<h2 style= "color:red">Hi Hello World to Flask Framework Learning... </h2>'

@app.route("/home")
def home_page():
    return render_template('home.html')




@app.route("/protected_form", methods=['GET', 'POST'])
def protected_form():
    print(request.form)
    form = LoginForm(request.form)
    print(form.validate_on_submit())
    if request.method == 'POST':
        name = request.form['email']
        password = request.form['password']
        return f'Hello {name } and logged in with {password}'
    return render_template('index.html')

@app.route("/unprotected_form", methods=['GET', 'POST'])
def unprotected_form():
    print(request.form)
    if request.method == 'POST':
        name = request.form['name']
        return (' Hello ' + name + '!!!')
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    print(request.form, form.validate_on_submit())
    if request.method == 'POST' and  form.validate_on_submit():
        email = request.form['username']
        password = request.form['password']
        return f'email : {form.username.data} , password: {form.password.data}'
    else:
        print("validation failed....")
        return render_template('login.html',form=form)
#main method
if __name__ == '__main__':
    app.run(debug= True)