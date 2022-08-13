from flask import Flask, render_template, redirect, request
from user import User #! grabbing user.py file pull User class
app = Flask(__name__)

app.secret_key="keep it safe"

@app.route('/')
def index():
    users = User.get_all() 
    return render_template('index.html', users = users)#! tied to the for loop 'users'

@app.route('/users/new') #! first step show user form (post route next)
def user_form():
    return render_template('create.html')

@app.route('/new/process', methods=['POST']) #! need to have a post route in order to use request.form - always use redirect on POST route
def user_process():
    User.save(request.form)
    return redirect('/') 



if __name__=="__main__":
    app.run(debug=True, port =5001)


#* 1. created database in workbench
#* 2. created pages 
#* 3. linking database to pages
#todo 