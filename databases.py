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

def query_by_nation(nationality):
    print("filter:",nationality)
    a = session.query(School).filter_by(nationality=nationality).all()
    print("a:",a)
    return a

def query_by_spec(specialty):
    return session.query(School).filter_by(specialty=specialty).all()


if __name__ == "__main__":
    add_school:("Anglican International School Jerusalem", "IB", "Rosemary Saunders", "International","Hanevi'im 82, DownTown Jerusalem", "Regular","English"  )

    add_school("College des Frere- Beit Hanina", "GSCE", "George Naber ", "Palestinian", "Biet Hanina Rd. 287", "Science", "English")
    add_school("The Hebrew Gymnasia", "Bagrot", "Danny Leibovich", "Israeli", "Keren Kayemet LeIsrael 14", "Regular", "Hebrew")
    add_school("Keshet highschool", "Bagrot", "Shimon Avichazar", "Israeli", "Alecsandrion st. 24, katamon, Jerusalem", "Regular", "Hebrew")
    add_school("Ort givat ram", "test", "David Granko", "Israeli", "the Hebrew University Givat Ram , Jerusalem", "Regular", "Hebrew")
    add_school("Rene Cassin", "Bagrot", "", "Israeli", "Karl Neter st. 1, Jerusalem", "Regular", "Hebrew")
    add_school("Rosary sister high school", "GSCE", "sir Lucy", "Palestinian", "Beit Hanina, Jerusalem", "Regular", "Arabic")
    add_school("Schmidt School", "Abitur", "Eva Schonemann", "German", "Nablos Rd. 97, Jerusalem", "Regular", "English")
    add_school("Scientific technological", "Bagrot", "Hani Sandouqa", "Israeli", "Faidi alami st-beit hanina", "Science", "Arabic")
    add_school("St.Georges School ", "Tawjihi", "waseem ali", "Palestinian", "Jerusalem Nablus St. 18", "Regular", "Arabic")
    add_school("Reut", "Bagrot", "erez amber", "Israeli", "eliezer Ha-Gadol 4 Jerusalem", "Regular", "Hebrew")
    add_school("Omanoyot", "Bagrot", "Tomer Bality", "Israeli", "Yzhak elhanan , rehavya", "Arts", "Hebrew")
    add_school("Pelech","Bagrot", "Sophy peper", "Israeli", "yehoda st. 31, Jerusalem", "Regular", "Hebrew")
