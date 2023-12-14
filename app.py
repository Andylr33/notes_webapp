from flask import Flask, render_template, request
# add flask_login library

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return "<p> Login <p>"

@app.route("/logout")
def logout():
    return "<p> Logout <p>"

@app.route("/sign-up")
def sign_up():
    return "<p> Sign Up <p>"

if __name__ == '__main__':
    app.run(debug=True)