from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    pass

@app.route("/register")
def register():
    pass

@app.route("/user")
def userpage():
    return render_template("user.html")

@app.route("/admin")
def adminpage():
    return render_template("admin.html")

@app.route("/default")
def frontpage():
    return render_template("frontpage.html")