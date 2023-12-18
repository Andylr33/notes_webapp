from flask import Flask, render_template, request, flash, redirect, session
import os
from werkzeug.security import check_password_hash, generate_password_hash
from database import create_user_account, add_note, check_if_user_exists, get_user_info
from flask_login import login_user, login_required, logout_user, current_user
from flask_session import Session
from helpers import login_required

app = Flask(__name__)



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    # Forget any user_id
    session.clear()

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        data = request.form
        user = get_user_info(data) # dictionary of users information/credentials
        if check_if_user_exists(data):
            if check_password_hash(user['hash'], password):
                flash("Logged in successfully!", category="success")
                
                # remember which user has logged in
                session["user_id"] = user['id']
                # set logged in to True
                session['logged_in'] = True

                return redirect("/")
            else:
                flash("Incorrect password, try again.", category="danger")
        else:
            flash("Email does not exist.", category="danger")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    # Forget any user_id
    session.clear()
    session['logged_in'] = False
    
    return redirect("/")

@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    # forget any user id
    session.clear()

    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('full_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        data = request.form # dictionary that contains data from sign up page

        # verify information
        if check_if_user_exists(data):
            flash("An account with that email already exists!", category='danger')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='danger')
        elif len(full_name) < 4:
            flash('Full name must be greater than 3 characters.', category='danger')
        elif password1 != password2:
            flash('Passwords do not match.', category='danger')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='danger')
        else:
            # add user to database
            
            create_user_account(data)
            flash('Your account was created!', category='success')

            user = get_user_info(data)
            session["user_id"] = user['id']
            # set logged in to True
            session['logged_in'] = True

            return redirect("/")
    return render_template("sign_up.html")

# Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.environ.get('SECRET_KEY')

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

if __name__ == '__main__':
    app.run(debug=True)