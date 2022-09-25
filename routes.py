from app import app
from flask import render_template

import storage

@app.route("/")
def index():
    return render_template("index.html")

#@app.route("/login")
#def login():
#    pass

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/user")
def userpage():
    return render_template("user.html")

@app.route("/admin")
def adminpage():
    return render_template("admin.html")

@app.route("/frontpage")
def frontpage():
    list = storage.get_list()
    return render_template("frontpage.html", items=list)