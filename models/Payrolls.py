from app import db


class PayrollModel(db.Model):
    __tablename__= "payrolls"
    id=db.Column(db.Integer,primary=False)
    monthYear=db.Column(db.String,unique=True)
    gross_salary=db.Column(db.Integer)
    nhif=db.Column(db.Float)
    nssf=db.Column(db.Float)
    paye=db.Column(db.Float)
    taxable_income=db.Column(db.Float)
    netpay=db.Column(db.Float)
    overtime=db.Column(db.Float)
    employee_id=db.Column(db.String(20),db.ForeignKey('employees.id'))