from flask_app import app
from flask_app.controllers import users, recipes #always the same just write ,________ (instead of recipes)

if __name__=="__main__":
    app.run(debug=True, port =5001)

#create, dashboard edit log and  reg show 
#take a screenshot of your db workbench. 
#