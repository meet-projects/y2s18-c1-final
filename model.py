from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
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
    principal = Column(String)
    nationality = Column(String)
    number_of_teachers = Column(Integer)
    location = Column(String)
    specialty = Column(String)
    language= Column(String)
    comments=relationship("Comment", back_populates="school") 



    def __repr__(self):
        return ("School name: {}".format(self.name))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name=Column(String)
    username=Column(String, unique=True)
    password=Column(String)
    comments=relationship("Comment", back_populates="user") 
   
   
    def __repr__(self):
        return ("User name: {}".format(self.name))

class Comment(Base):
    __tablename__="comments"
    id=Column(Integer, primary_key = True)
    text=Column(String)
    user_id=Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="comments")
    school_id=Column(Integer, ForeignKey('schools.id'))
    school = relationship("School", back_populates="comments")

   
