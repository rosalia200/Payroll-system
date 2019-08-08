class Payroll:
    basic_salary = 0
    benefits = 0
    gross_salary=0
    nssf_deductions=0
    taxable_income=0
    personal_relief=1408
    nhif_deductions=0
    payee=0
    overtime=0
    total_deductions=0
    net_salary=0

    def __init__(self, basic_salary, benefits,overtime):
        self.basic_salary = basic_salary
        self.benefits = benefits
        self.overtime=overtime
        self.gross_salary()
        self.nssf_deductions()
        self.taxable_income()
        self.nhif_deductions()
        self.payee()
        self.total_deductions()
        self.net_salary()




    def gross_salary(self):
        self.gross_salary= self.basic_salary + self.benefits

    def nssf_deductions(self):
        if self.gross_salary <= 18000:
            self.nssf_deductions =( self.gross_salary * 0.06)
        else:
            self.nssf_deductions= 18000 * 0.06
    def taxable_income(self):
        self.taxable_income = self.gross_salary -self.nssf_deductions

    def payee(self):
        if self.taxable_income<12298:
            self.payee= self.taxable_income*0.01
        elif self.taxable_income<23885:
            self.payee = (12298*0.01)+((self.taxable_income-12298)*.15)
        elif self.taxable_income<35472:
            self.payee = (12298*0.01)+ ((23885-12298)*0.15)+((self.taxable_income-23885)*0.2)
        elif self.taxable_income<47059:
            self.payee = (12298*0.01)+ ((23885-12298)*0.15)+((35472-23885)*.2)+((self.taxable_income-35472)*.25)
        else:
            self.payee = (12298*0.01)+ ((23885-12298)*0.15)+((35472-23885)*.2)+((47059-35472)*.25)+((self.taxable_income-47059)*.3)


    def nhif_deductions(self):
        if self.gross_salary<6000:
            self.nhif_deductions= 150
        elif self.gross_salary<8000:
            self.nhif_deductions = 300
        elif self.gross_salary<12000:
            self.nhif_deductions = 400
        elif self.gross_salary<15000:
            self.nhif_deductions = 500
        elif self.gross_salary<20000:
            self.nhif_deductions = 600
        elif self.gross_salary<25000:
            self.nhif_deductions = 750
        elif self.gross_salary<30000:
            self.nhif_deductions = 850
        elif self.gross_salary<35000:
            self.nhif_deductions = 900
        elif self.gross_salary<40000:
            self.nhif_deductions = 950
        elif self.gross_salary<45000:
            self.nhif_deductions = 1000
        elif self.gross_salary<50000:
            self.nhif_deductions = 1100
        elif self.gross_salary<60000:
            self.nhif_deductions = 1200
        elif self.gross_salary<70000:
            self.nhif_deductions = 1300
        elif self.gross_salary<80000:
            self.nhif_deductions = 1400
        elif self.gross_salary<90000:
            self.nhif_deductions = 1500
        elif self.gross_salary<100000:
            self.nhif_deductions = 1600
        else:
            self.nhif_deductions = 1700

    def total_deductions(self):
        self.total_deductions = self.payee+self.nhif_deductions
    def net_salary(self):
        self.net_salary= self.taxable_income-self.total_deductions+self.personal_relief


