from flask import Flask, render_template, request, flash
import os
# from flask_login import UserMixin
# from flask_session import Session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template("login.html")

@app.route("/logout")
def logout():
    return "<p> Logout <p>"

@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # verify information
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='danger')
        elif len(full_name) < 4:
            flash('Full name must be greater than 3 characters.', category='danger')
        elif password1 != password2:
            flash('Passwords do not match.', category='danger')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='danger')
        else:
            # add user to database
            flash('Your account was created!', category='success')
    return render_template("sign_up.html")

# Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.environ.get('SECRET_KEY')

# Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

if __name__ == '__main__':
    app.run(debug=True)