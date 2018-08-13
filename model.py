from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class School(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    test = Column(String)
    principle = Column(String)
    year = Column(Integer)
    number_of_students = Column(Integer)
    nationality = Column(String)
    number_of_teachers = Column(Integer)
    location = Column(String)
    specialty = Column(String)
    average = Column(Integer)
    language= Column(String)
    link = Column(String)



    def __repr__(self):
        return ("School name: {}".format(self.name))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name=Column(String)
    username=Column(String)
    password=Column(String)
    link = Column(String)
   
    def __repr__(self):
        return ("User name: {}".format(self.name))

