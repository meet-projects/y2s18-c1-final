# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session

# Add functions you need from databases.py to the next line!
from databases import add_school, query_all, query_by_id, query_by_name, add_user, query_by_comment_id, query_by_username, add_comment, query_comment_by_user, query_comment_by_school_id, delete_comment_by_id

# Starting the flask app
app = Flask(__name__)
app.secret_key = "super secret key"

# App routing code here
@app.route('/')
def home():
    un=query_by_username(login_session.get('username'))
    return render_template('home.html', login_session=login_session, un=un, schools=query_all())


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

@app.route('/delete_comment/<comment_id>')
def delete_comment(comment_id):
    comment=query_by_comment_id(comment_id)
    school_id=comment.school_id
    delete_comment_by_id(comment_id)
    
    return redirect(url_for("school",school_id=school_id))
 
@app.route('/signup',methods=["GET", "POST"])
def signup():
    if request.method=="POST":
        username = request.form['username']
        password= request.form["password"]
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]
        confirm= request.form["confirm"]
        if password==confirm:
            add_user(first_name, last_name, username, password)
            login_session['id'] = query_by_username(username).id
            login_session['username']= username
            login_session['first_name']=first_name
            login_session['last_name']=last_name
            return redirect(url_for('home'))
            
        else:
            return render_template('signup.html', confirm=False)

    if request.method=="GET":
        return render_template('signup.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')



@app.route('/school_id/<school_id>', methods=["GET", "POST"])
def school(school_id):
    school=query_by_id(school_id)
    if request.method=='POST':
        if login_session.get("username")==None:
            return redirect(url_for("signup"))

        text=request.form["text"]
        user=query_by_username(login_session['username'])
        add_comment(text, user, school)
    return render_template(
        'school.html',
        school_id=school_id,
        school=school,
        comments=query_comment_by_school_id(school_id),user_id=login_session.get("id"))


@app.route('/search', methods=['POST'])
def search_bar():
    # todo: get value of search textbox
    # filter schools by search query_by_name, store it in variable called wtv
    # render school.html with list of schools from previous step
    if request.method=='POST':
        search=request.form["search"]
        schools=query_by_name(name=search).all()

        return render_template('search.html', results=schools)
    return render_template('home.html',login_session=login_session )

@app.route('/users/<string:username>')
def users(username):
    comments=query_comment_by_user(username)
    return render_template('users.html', u=query_by_username(login_session['username']), comments=comments)

@app.route('/logout')
def logout():
    login_session.clear()
    return redirect(url_for("home"))
    # del login_session['id']
    # del login_session['username']
    # del login_session['first_name']
    # del login_session['last_name']

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)