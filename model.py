from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class School(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    test = Column(String)
    year = Column(Integer)
    number_of_students = Column(Integer)
    nationality = Column(String)
    number_of_teachers = Column(Integer)
    location = Column(String)
    specialty = Column(String)
    average = Column(Integer)
    link = Column(String)

    def __repr__(self):
        return ("School name: {}".format(self.name))