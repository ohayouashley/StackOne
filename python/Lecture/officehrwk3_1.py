#!OFFICE HOUR
#!python3 -m pipenv install flask
#?1.download task
#? Make sure your server is running before you add anything else in your code after pipfile and pipfile.lock
#? White error page NOT FOund means its working but I don't have it yet.
#? Create templates folder in hello_flask
#? index.html file do hello world
#? In server.py connect html file > safe > make sure it works
#? render_template('index.html') << this is a function
#? @app.route('/') | def index(): | home_page = rednder_template('index.html') | return home_page
#? we need to get information to the user:
#? <h1> my picnic</h1>
#? <form action="/order" method="post">::NEED LABEL AND INPUT TAGS
# ?<label>Name:<input type="text" name="" id="name"</form> ::name is used to access server.py id is used for html/js/and associate input to label. 
#? @app.route('/order')
#? def place_order():
#?     pass
#? make sure to use input type email for email andn ot text. you need to use text for password.  
#? display: block on label 

#* use dot notation on jinja
#* never put render_template on a POST request. 
#*only be able to edit and delete profile if you are logged in


#! We imported the Flask class. You will need this line in every application you build with Flask.
# !We made an instance of the Flask class called "app". You will need this line in every application you build with Flask.
# !We set up a routing rule using the "@" decorator with the route method: @app.route("/route_string").
# !The routing rule is associated with the function immediately following it.
# !Finally, we ran the app! This takes all of our routing rules that we set up and actually starts up the server.

#?HTTP method GET, POST, PUT, PATCH, DELETE)
#? URL

#? ::SETTING UP YOUR ROUTES::
#? Let's add another route to our server.py file.
#! import statements, maybe some other routes


