# from main import db
#
#
# class PayrollsModel(db.Model):
#     __tablename__= "payrolls"
#     id=db.Column(db.Integer,primary=False)
#     monthYear=db.Column(db.String,unique=True)
#     gross_salary=db.Column(db.Integer)
#     nhif=db.Column(db.Float)
#     nssf=db.Column(db.Float)
#     paye=db.Column(db.Float)
#     loan_deducted=db.Column(db.Float)
#     advance_pay=db.Column(db.Float)
#     overtime=db.Column(db.Float)
#     persomal_relief=db.Column(db.Float)
#     taxable_income=db.Column(db.Float)
#     net_salary=db.Column(db.Float)
#     employee_id=db.Column(db.Integer,db.ForeignKey('employees.id'))
#
#     def insert_to_db(self):
#         db.session.add(self)
#         db.session.commit()
