# Database related imports
# Make sure to import your tables!

from model import Base, School

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Your database functions are located under here (querying, adding items, etc.)

# Example of adding a student:
def add_school(name, year, test, principle, number_of_students, nationality, number_of_teachers, location, specialty, average, link):	
    school_object = School(
        name=name,
        year=year,
        test = test,
        principle = principle,
        number_of_students = number_of_students,
        nationality = nationality,
        number_of_teachers = number_of_teachers,
        location = location,
        specialty = specialty,
        average = average,
        link = link)

    session.add(school_object)
    session.commit()

def query_by_name(name):
	return session.query(School).filter_by(
		name=name).first()


def query_all():
	schools = session.query(School).all()
	for school in schools:
		print(school)
		print('\n')
	return schools

# def delete_school(name):
# 	session.query(School).filter_by(
# 		name=name).delete()
# 	session.commit()

def query_by_id(school_id):
    return session.query(School).filter_by(
        school_id=school_id).first()
