# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session

# Add functions you need from databases.py to the next line!
from databases import add_school, query_all, query_by_id, query_by_name, add_user, query_by_username, add_comment

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
            # TODO check if password matches
            if user.password==password:
                login_session['id'] = user.id
                login_session['username']= user.username
                login_session['first_name']=user.first_name
                login_session['last_name']=user.last_name
                return redirect(url_for('home'))

            else:
                return "Wrong Password"
        

    if request.method=="GET":
        return render_template('login.html')
 
@app.route('/signup',methods=["GET", "POST"])
def signup():
    if request.method=="POST":
        username = request.form['username']
        password= request.form["password"]
        confirm= request.form["confirm"]
        if password==confirm:
            add_user(first_name, last_name, username, password)

    if request.method=="GET":
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
        text=request.form["text"]
        user=query_by_username(login_session['username'])
        school=query_by_id(school_id)
        add_comment(text, user, school)
        return render_template(
            'school.html',
            school_id=school_id,
            school=school)


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
