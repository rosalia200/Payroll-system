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
