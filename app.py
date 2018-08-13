# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session

# Add functions you need from databases.py to the next line!
from databases import add_school, query_all, query_by_id, query_by_name, add_user, query_by_username

# Starting the flask app
app = Flask(__name__)

# App routing code here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    #POST
    if request.method=="POST":
        username = request.form['username']
        password= request.form["password"]
        user=query_by_username(username)
        if user==None:
            return "User doesn't exist."
        else:
            login_session['id'] = user.id
            login_session['username']= user.username
            login_session['first_name']=user.first_name
            login_session['last_name']=user.last_name
            return redirect('home')

    if request.method=="GET":
        return render_template('login.html')
 
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/school_id/<school_id>', methods=["GET", "POST"])
def school(school_id):
    if request.method=='GET':
        return render_template(
            'school.html',
            school_id=school_id,
            school=query_by_id(school_id))
    else:
        pass
        #alllow users to post comments here


@app.route('/search', methods=['POST'])
def search_bar():
    return render_template('search.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/logout')
def logout():
    del login_session['id']
    del login_session['username']
    del login_session['first_name']
    del login_session['last_name']

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
