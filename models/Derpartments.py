from main import db
from models.Employees import EmployeeModel
#importing sqlalchmey object from main file


class DepartmentModel(db.Model):
    __tablename__="departments"
    department_id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True,nullable=False)
    employees=db.relationship(EmployeeModel,backref='department')

    #create
    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()
    #read
    #read more on classes
    @classmethod
    def fetch_by_name(cls,name):
        return cls.query.filter_by(name = name).first()
    @classmethod
    def fetch_by_id(cls,dept_id):
        return cls.query.filter_by(department_id=dept_id).first()
    @classmethod
    def fetch_all(cls):
        return cls.query.all()
    @classmethod
    def fetch_total_payrol_by_id(cls,department_id):
        this_dept=cls.fetch_by_id(department_id)
        total_payroll=0
        for each_employee in this_dept.employees:
            total_payroll+=each_employee.basic_salary + each_employee.benefits
        return total_payroll
    #update
    @classmethod
    def update_by_dept_id(cls,department_id,name=None):
        dep= cls.fetch_by_id(department_id)
        if name:
            dep.name = name

        db.session.commit()
        return True