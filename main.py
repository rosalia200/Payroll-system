#importing flask class
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from config import Development,Testing
from config import Production
import pygal
from resources.payroll import Payroll
#instatiating class Flask
app = Flask(__name__)
app.config.from_object(Development)
# app.config.from_object(Testing)#comment if you want to develop
#app.config.from_object(Production)

db= SQLAlchemy(app)
from models.Employees import  EmployeeModel
from models.Derpartments import DepartmentModel
from models.Payrolls import PayrollsModel

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
    this_department=DepartmentModel.fetch_by_id(dept_id)
    employees=this_department.employees

    return render_template('employees.html',this_department=this_department,idara=departments)


@app.route('/')
#fuction to run when clients visit this route
def hello_world():
    departments = DepartmentModel.fetch_all()
    all_employees=EmployeeModel.fetch_all()
    male=0
    female=0
    others=0
    for each in all_employees:
        if each.gender=='m':
            male+=1
        elif each.gender=='f':
            female += 1
        else:
            others+=1

    pie_chart = pygal.Pie()
    pie_chart.title = 'Comparing Company Employee by Gender'
    pie_chart.add('Male', male)
    pie_chart.add('Female', female)
    pie_chart.add('Others', others)
    graph=pie_chart.render_data_uri()
    #print(graph)
    line_chart = pygal.Bar()
    line_chart.title = 'Salary Cost per Department'
    for each_dept in departments:
        line_chart.add(each_dept.name,DepartmentModel.fetch_total_payrol_by_id(each_dept.department_id))
    bar_graph=line_chart.render_data_uri()


    return render_template('index.html',idara=departments,graph=graph,bar_graph=bar_graph)
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
    department = int(request.form['department'])
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']
    national_id = request.form['national_id']
    emp = EmployeeModel(full_name=name_of_employee,gender=gender,kra_pin=kra_pin,email=email,national_id=national_id,department_id=department,basic_salary=basic_salary,benefits=benefits)


    emp.insert_to_db()
    return redirect(url_for('hello_world'))
#run flask
# if __name__ == '__main__':
#     app.run()
@app.route('/payrolls/<int:emp_id>')
def payrolls(emp_id):
    employee=EmployeeModel.fetch_by_id(emp_id)
    return render_template('payroll.html',employee=employee)
@app.route('/generate_payroll/<int:id>',methods=['POST'])
def generate_payroll(id):
    this_employee=EmployeeModel.fetch_by_id(id)
    overtime = request.form['overtime']

    payroll = Payroll( this_employee.basic_salary, this_employee.benefits, float(overtime))


    month = request.form['month']
    loan = request.form['loan']
    salary_advance = request.form['salary_advance']
    gross_salary = payroll.gross_salary
    taxable_income = payroll.taxable_income
    nssf = round(payroll.nssf_deductions, 2)
    paye = round(payroll.payee, 2)
    personal_relief = payroll.personal_relief
    #tax_net_off_relief = round(payroll.after_relief, 2)
    nhif = payroll.nhif_deductions
    net_salary = round(payroll.net_salary, 2)
    take_home_pay = net_salary - (float(loan) + float(salary_advance))

    payslip = PayrollsModel( monthYear=month, overtime=overtime, loan_deducted=loan,
                           salary_advance=salary_advance, gross_salary=gross_salary, nssf=nssf,
                           taxable_income=taxable_income, paye=paye, personal_relief=personal_relief,
                            nhif=nhif, net_salary=net_salary,
                           take_home_pay=take_home_pay, employee_id=this_employee.id)
    payslip.insert_to_db()
    flash('Payslip for ' + this_employee.full_name + ' has been successfully generated', 'success')
    return redirect(url_for('payrolls', emp_id=this_employee.id))


@app.route('/editEmployee/<int:id>',methods=['POST'])
def editEmployee(id):
    name_of_employee = request.form['name']
    kra_pin = request.form['kra_pin']
    gender = request.form['gender']
    email = request.form['email']
    department = int(request.form['department'])
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']
    national_id = request.form['national_id']

    if gender=="na":
        gender=None
    if department=="0":
        department=None

    EmployeeModel.update_by_id(id=id,full_name=name_of_employee, gender=gender, kra_pin=kra_pin, email=email,national_id=national_id, department_id=department, basic_salary=basic_salary, benefits=benefits)
    this_emp=EmployeeModel.fetch_by_id(id=id)
    this_dept=this_emp.department

    return redirect(url_for('employees',dept_id=this_dept.department_id))


@app.route('/editDepartment/<int:department_id>',methods=['POST'])
def editDepartment (department_id):
    name_of_department=request.form['name']
    DepartmentModel.update_by_dept_id(department_id=department_id,name=name_of_department)
    # department = request.form['department']
    # if department=="0":
    #     department=None
    # EmployeeModel.update_dep_id(id=id,department_id=department)


    return redirect(url_for('hello_world'))


@app.route('/deleteEmployee/<int:id>')
def deleteEmployee(id):
    this_emp = EmployeeModel.fetch_by_id(id=id)
    this_dept = this_emp.department
    EmployeeModel.delete_by_id(id)
    return redirect(url_for('employees',dept_id=this_dept.department_id))
@app.route('/deleteDepartment/<int:department_id>')
def deleteDepartment(department_id):
    this_dept=DepartmentModel.delete_by_dept_id(department_id)
    employees=EmployeeModel.delete_by_id(id)

    return redirect(url_for('hello_world'))
