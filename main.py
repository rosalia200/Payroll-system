#importing flask class
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from config import Development,Testing
#instatiating class Flask
app = Flask(__name__)
app.config.from_object(Development)
# app.config.from_object(Testing)#comment if you want to develop
#app.config.from_object(Production)

db= SQLAlchemy(app)
from models.Employees import  EmployeeModel
from models.Derpartments import DepartmentModel

#this decorator helps im
#TODO:read about flask-migrate
@app.before_first_request
def create_tables():
    db.create_all()


#this is a config parameter that shows where oour database lives
#registering a route
@app.route('/employees/<int:dept_id>')
def employees(dept_id):
    departments = DepartmentModel.fetch_all()
    return render_template('employees.html',idara=departments)


@app.route('/')
#fuction to run when clients visit this route
def hello_world():
    departments = DepartmentModel.fetch_all()
    return render_template('index.html',idara=departments)
@app.route('/name')
def name():
    return "rosalia nambuya"
@app.route('/location')
def location():
    return "langata"

@app.route('/newDepartment',methods=['POST'])
def newDepartment():
    department_name = request.form['department']
    if DepartmentModel.fetch_by_name(department_name):
        #read more on bootsrap alert with flash
        flash("Department " + department_name+" already exist")
        return redirect((url_for('hello_world')))
    department = DepartmentModel(name=department_name)
    department.insert_to_db()
    return redirect(url_for('hello_world'))



@app.route('/newEmployee',methods=['POST'])
def newEmployee():
    name_of_employee = request.form['name']
    kra_pin = request.form['kra_pin']
    gender = request.form['gender']
    email = request.form['email']
    department = request.form['department']
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']
    national_id = request.form['national_id']

#run flask
# if __name__ == '__main__':
#     app.run()