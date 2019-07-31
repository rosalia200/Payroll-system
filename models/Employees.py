from app import db
#from models.Payrolls import PayrollModel

class EmployeeModel(db.Model):
    __tablename__='employees'
    id=db.Column(db.Integer,primary_key=True)
    full_name=db.Column(db.String(50),nullable=False)
    kra_pin=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(30),unique=True,nullable=True)
    national_id=db.Column(db.String,unique=True,nullable=False)
    department_id=db.Column(db.Integer,db.ForeignKey('departments.department_id'))
    basic_salary=db.Column(db.Float(3))
    benefits=db.Column(db.Float(3))
    #payrolls=db.relationship(PayrollModel,backref='employee')