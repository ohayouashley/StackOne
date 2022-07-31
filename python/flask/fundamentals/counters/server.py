from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="keep it safe,keep it secret"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port =5001)

# #every time you refresh the button you're refreshing 
# #that loop. Is this variable already in session, is count in session
# #if it is there (if it's not there make it and set to 1) else increment it
# #and move it up by one
# #

# # cp - copy file copy and space and the new file you want to 

# # cp 00skeleton00/testing123
# # cs -rf 00seleton00

# @app.route('/increment')
# def counter():
#     session['count'] += 1
#     redirect('/')

#     if count == not in session:
#         session['count'] = 1
#     else:
#         session['count'] += 1
#     return render_template("index.html",num=session['count'])


# #a for loop cannot loop through an integer, whats why the loop while loops
# #for loop defined horizontal
# #while loop defined vertically