from app import db
from models.Employees import EmployeeModel
#importing sqlalchmey object from main file


class DepartmentModel(db.Model):
    __tablename__="departments"
    department_id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),unique=True,nullable=False)
    employees=db.relationship(EmployeeModel,backref='department')
