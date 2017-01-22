import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as declarative
from zope.sqlalchemy import ZopeTransactionExtension as ZTE

DBSession = orm.scoped_session(orm.sessionmaker(extension=ZTE()))
Base = declarative.declarative_base()

class login(Base):
    __tablename__ = "login"
    
    username = sa.Column(sa.Unicode(100), nullable=False, primary_key=True)
    role = sa.Column(sa.Unicode(100), nullable=False)
    password = sa.Column(sa.Unicode(100), nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
class Student(Base):
    __tablename__ = "student"

    student_id = sa.Column(sa.Integer, primary_key=True)
    student_name = sa.Column(sa.Unicode(100), nullable=False)
    email = sa.Column(sa.Unicode(100), nullable=False)
    address = sa.Column(sa.Unicode(500), nullable=False)
    contact_number = sa.Column(sa.Integer(10), nullable=False)
    percentage = sa.Column(sa.float, nullable=False)
    department = sa.Column(sa.Unicode(3), nullable=False)
    
    def __init__(self, student_id, student_name, email, address, contact_number, percentage, department):
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.address = address
        self.contact_number = contact_number
        self.percentage = percentage
        self.department = department
     

    
    
    
    
    
    
