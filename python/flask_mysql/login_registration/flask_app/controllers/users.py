#users.py
from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User

    # store user id into session
    session['user_id'] = User.create(data)
    return redirect('/dashboard')

@app.route('/dashboard')  #?only use method when you post something (form action) 
def dashboard():
    if "user_id" not in session:
        flash("ERROR! Must login")
        return redirect('/') #? checking if user id exists in our dictionary: session | should be on all of your routes.
    user_data={
        'id' : session['user_id']
    }
    user = User.get_user_by_id(user_data)
    return render_template('dashboard.html', user = user) 

@app.route('/logout')
def logout():
    session.clear() 
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
        # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_user_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")