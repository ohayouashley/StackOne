from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
#set a secret key for security purposes ^^^s
@app.route('/')
def index():
    return render_template("index.html") #! Needs this home route

@app.route('/users', methods=['POST'])
def create_user():
    print("$$$$$$$$$$$$$$$") #!see easier in terminal
    print("Got Post Info")
    print("$$$$$$$$$$$$$$$")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    #? session side - declaring or creating session variable.
    #? session is now equal to the value at request.form of the key 'name'
#!key on left side | value on right side
    session['useremail'] = request.form['email']
    return redirect('/show')
    #!redirect - go look for this (/show) route and execute that route.


@app.route('/show') #! this line just finds it. Doesn't display yet.
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])
    #! return render_templates displays the page
    #! must put your name_on_template variable in render_templates function in order to be displayed on html page.




if __name__=="__main__":
    app.run(debug=True, port =5001)

