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
def add_school(name, test, principal, nationality, location, specialty,language):	
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
    
def query_comment_by_school_id(school_id):
    school=query_by_id(school_id)
    return session.query(Comment).filter_by(
        school=school).all()

def query_all():
	schools = session.query(School).all()
	return schools

def query_by_comment_id(comment_id):
    return session.query(Comment).filter_by(
        id=comment_id).first()


def query_by_id(school_id):
    return session.query(School).filter_by(
        id=school_id).first()

def delete_comment_by_id(comment_id):
    session.query(Comment).filter_by(
        id=comment_id).delete()

    session.commit()

  

add_school("jhs","sat","karine","american","jerusalem","normal","english")


if __name__ == "__main__":
    app.run(debug=True)
def query_by_nation(nationality):
    print("filter:",nationality)
    a = session.query(School).filter_by(nationality=nationality).all()
    print("a:",a)
    return a

def query_by_spec(specialty):
    return session.query(School).filter_by(specialty=specialty).all()


if __name__ == "__main__":
    add_school("IASA","Bagrot", "Etai Benovich","Israeli", "Haim Kolitz 1", "Arts", "Hebrew" )
    add_school("St.George School","Tawjihi", "The Very Reverend Hosam Naoum","Palestinian", "18 Nablus", "Regular", "Arabic" )
    add_school("Anglican International School Jerusalem","IB", "Rosemary Saunders","International", "Hanevi'im 82", "Regular", "English" )
    add_school("College des Frere- Biet Hanina","GSCE", "George Naber","Palestinian", " Beit Hanina", "Science", "English" )
