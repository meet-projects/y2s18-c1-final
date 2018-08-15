# Database related imports
# Make sure to import your tables!

from model import Base, School, User, Comment

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
def add_school(name, test, principal, nationality, number_of_teachers, location, specialty,language):	
    school_object = School(
        name=name,
        test = test,
        principal = principal,
        nationality = nationality,
        location = location,
        specialty = specialty,
        language=language)

    session.add(school_object)
    session.commit()

def add_user(first_name, last_name, username, password, ):	
    user_object = User(
        first_name=first_name,
        last_name=last_name,
        username=username,
        password=password)

    session.add(user_object)
    session.commit()

def add_comment(text, user, school):
    comment_object = Comment(
        text=text,
        user=user,
        school=school)

    session.add(comment_object)
    session.commit()   

def query_by_name(name):
    return session.query(School).filter(School.name.contains(name))

def query_by_username(username):
    return session.query(User).filter_by(
        username=username).first()

def query_comment_by_user(username):
    user=query_by_username(username)
    return session.query(Comment).filter_by(
        user=user).all()
    


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
        id=school_id).first()

# def add_school(name, year, test, principle, number_of_students,
#  nationality, number_of_teachers, location, specialty, average,language):

add_school("IASA","Bagrot", "Etai Benovich","Israeli", 20, "Haim Kolitz 1", "Arts", "Hebrew" )
