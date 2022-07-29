# from flask import Flask, render_template  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# @app.route('/')
# def index():
#     return render_template('index.html', phrase="hello", times=5) #this index.html is a string and must be called the same name as your file. 

# @app.route('/play') 



# @app.run(debug=True, port =5001)

#*If you see error with % 
#!Since our browser doesn't understand Python code, the render_template function sends our HTML file along with any data passed
#! through the template engine to resolve any code into HTL. The final product is the response to the client

#! ::PASSING DATA TO HTML::
#! Below in our render template function call we are now passing three arguments. The first one is still the name of the
#! html file but the other two have names and values. 

#! hello_flask/server.py
#? How do we use that data on the HTML? Here are 2 special inpts we can use to insert python-like code into our flask templates:
#? {{some variable}}
#? {%some expression%}

#? Now lets update our index.html file
#? ::see index.html (note)::

#! forms going to be on the templates
#?look up button onclick()=popup.remove - means when you get a pop up
#*build naughty bye bye code.
#?look up return false
#? if book.user_id == session.user_id is saying that they can edit it if both of them match
#?methods = ['post', 'GET'] why? calling post and get used - post is getting the form submission#? 
#? get is the default request. It brings you do this form (page)
#? if you go through the same route using post it gives you the form data.
#? Hyperlink get request | forms post request
#* never use render on a post request
#* just in this insteanceso that they don't lost their data when 
#*? session - think of it like a brief case. 
#? To be clear; should POST always be used when changing anything in session? A yes we can use one route as a post of get method
#?Not necessarily changing things in session, but it will always be POST when we are taking in information from a form
#?so we can use the path for both post and get.  We would have to include a if statement to check if it a "GET" request.  When we load the edit page that's a get request, when we submit that's a poast
#? on the backend/server we may use session to store the data from the form, or we may call a method to save the data in our database
