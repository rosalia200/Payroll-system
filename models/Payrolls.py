from main import db
#from models.Employees import EmployeeModel

class PayrollsModel(db.Model):
    __tablename__= "payrolls"
    id=db.Column(db.Integer,primary_key=True)
    monthYear=db.Column(db.String,unique=True)
    gross_salary=db.Column(db.Integer)
    nhif=db.Column(db.Float)
    nssf=db.Column(db.Float)
    paye=db.Column(db.Float)
    loan_deducted=db.Column(db.Float)
    salary_advance=db.Column(db.Float)
    overtime=db.Column(db.Float)
    persomal_relief=db.Column(db.Float)
    taxable_income=db.Column(db.Float)
    net_salary=db.Column(db.Float)
    take_home_pay=db.Column(db.Float)

    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    employee = db.relationship('EmployeeModel',backref=db.backref("payrolls", single_parent=True, lazy=True, cascade='all,delete'))

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def fetch_by_employee(cls,id):
        return cls.query.filter_by(id=id)
