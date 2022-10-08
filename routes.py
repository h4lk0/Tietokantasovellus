from crypt import methods
from email import message
from app import app
from flask import render_template, request, redirect

import storage
import users

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/frontpage")
        else:
            return render_template("loginerror.html", message = "Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("signuperror.html", message="Salasanat eivät täsmää")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("signuperror.html", message="Rekisteröinti epäonnistui")

@app.route("/user")
def userpage():
    return render_template("user.html")

@app.route("/admin")
def adminpage():
    if users.check_admin():
        list = storage.get_all()
        return render_template("admin.html", show=True, items=list, message="Hei ylläpitäjä")
    else:
        return render_template("admin.html", show=False, message="Et ole ylläpitäjä")

@app.route("/frontpage")
def frontpage():
    shelters = storage.get_list("shelters")
    tools = storage.get_list("tools")
    misc = storage.get_list("misc")
    return render_template("frontpage.html", items1=shelters, items2=tools, items3=misc)