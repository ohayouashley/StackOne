from flask import Flask, render_template, session, redirect, request
import pprint 
app = Flask(__name__)

app.secret_key="keep it safe,keep it secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST']) 
def result(): 
    print("------TEST------")
    print(request.form.to_dict())
    print("------TEST------") 
    pprint.pprint(request.form)
    session['name'] = request.form['name'] #dictionary 
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/complete')
    # return render_template('form_result') #under def result

@app.route('/complete')
def page_2():
    return render_template('complete.html')

if __name__=="__main__":
    app.run(debug=True, port =5001)
#return render template
#render template - new html page


