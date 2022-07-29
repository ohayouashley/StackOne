from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


# import statements, maybe some other routes
    
@app.route('/success')
def success():
   return "success"
    

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name
    #carrot defaults to string - if you put number, will not work because no route for integer.


@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/hi/<names>')
def hi(names):
    print(names)
    return "Hi, " + names

@app.route('/hello/<string:name>/<int:num>')
def hello(name,num):
    return f"Hello {name * num}"
    #? ??? Ask Kyle

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port =5001)    # Run the app in debug mode.
    # app.run(debug=True) should be the very last statement! 
#make sure to exit program when  you're done working in it to avoid errors.