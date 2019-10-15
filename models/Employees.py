from main import db
from models.Payrolls import PayrollsModel

class EmployeeModel(db.Model):
    __tablename__='employees'
    id=db.Column(db.Integer,primary_key=True)
    full_name=db.Column(db.String(50),nullable=False)
    gender = db.Column(db.String(20),nullable=False)
    kra_pin=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(30),unique=True,nullable=True)
    national_id=db.Column(db.String,unique=True,nullable=False)
    department_id=db.Column(db.Integer,db.ForeignKey('departments.department_id'))
    basic_salary=db.Column(db.Float(3))
    benefits=db.Column(db.Float(3))
    payrolls=db.relationship('PayrollsModel',backref='wafanyakazi', lazy=True)

    #create
    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()
        #read
    @classmethod
    def fetch_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    #update
    @classmethod
        #read on keyword functions
    def update_by_id(cls,id,full_name=None,kra_pin=None,email=None,national_id=None,gender=None,basic_salary=None,department_id=None,benefits=None):
        record= cls.fetch_by_id(id=id)
        if full_name:
            record.full_name=full_name
        if gender:
            record.gender = gender
        if kra_pin:
            record.kra_pin = kra_pin
        if email:
            record.email = email
        if national_id:
            record.national_id = national_id
        if department_id:
            record.department_id = department_id
        if basic_salary:
            record.basic_salary = basic_salary
        if benefits:
            record.benefits = benefits
        db.session.commit()
        return True
    @classmethod
    def update_dep_id(cls,id,department_id=None):
        rec= cls.fetch_by_id(id=id)
        if department_id:
            rec.department_id = department_id
        db.session.commit()
        return True

    #delete
    @classmethod
    def delete_by_id(cls,id):
        record=cls.query.filter_by(id=id)
        record.delete()
        db.session.commit()
        return True
