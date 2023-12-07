from flask import Flask, render_template, request, redirect, url_for, session, abort, flash
from db.connection import MongoDBConnection
from db.utils import json_helper,verify_password

app = Flask(__name__)  # flask object creation
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
ATLAS_MONGODB_URI = 'MONGODB_URI';
collection = MongoDBConnection(dbName='training', collName='users', dbUrl=ATLAS_MONGODB_URI).create_connection()


@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('home.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        dbuser = collection.find_one({'username': username})
        if dbuser:
            if dbuser['username'] == username and verify_password(password, dbuser['password']):
                session['username'] = username
                flash('You were successfully logged in')
                return redirect(url_for('home'))
            else:
                return render_template('userlogin.html', error='Invalid Username or Password')
        else:
            app.logger.error(f'user not found with name : {username}')
            redirect(url_for('error'))
    return render_template('userlogin.html')


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = json_helper(request.form)
        print(user)
        collection.insert_one(user)
        app.logger.info(f'register user : {user['username']} successfully')
        flash('You were successfully registered')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/error')
def error():
    abort(404)


if __name__ == '__main__':
    app.run(debug=True, port=1144)
