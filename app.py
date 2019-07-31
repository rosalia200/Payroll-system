#importing flask class
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from config import Development,Testing
#instatiating class Flask
app = Flask(__name__)
app.config.from_object(Development)
# app.config.from_object(Testing)#comment if you want to develop

db= SQLAlchemy(app)
from models.Employees import  EmployeeModel
from models.Derpartments import DepartmentModel


@app.before_first_request
def create_tables():
    db.create_all()

#this is a config parameter that shows where oour database lives
#registering a route
@app.route('/')
#fuction to run when clients visit this route
def hello_world():
    return render_template('index.html')
@app.route('/name')
def name():
    return "rosalia nambuya"
@app.route('/location')
def location():
    return "langata"

#run flask
# if __name__ == '__main__':
#     app.run()
