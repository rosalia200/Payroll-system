class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:sevani@127.0.0.1:5432/July_payroll'
    environment = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = ''

    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = False
    environment = 'production'
class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:sevani@127.0.0.1:5432/July_payroll'
    environment='development'
    DEBUG = True

class Testing(Config):
    debug = True


class Production(Config):
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = False
    environment = 'production'
