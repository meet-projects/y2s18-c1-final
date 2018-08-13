# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session

# Add functions you need from databases.py to the next line!
from databases import add_school, query_all, query_by_id, query_by_name

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/school_id/<school_id>')
def school(school_id):
    return render_template(
        'school.html',
        school_id=school_id,
        school=query_by_id(school_id))

@app.route('/search', methods='POST')
def search_bar():
    return render_template('search.html')
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
