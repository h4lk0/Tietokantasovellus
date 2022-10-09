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

@app.route("/user", methods=["GET", "POST"])
def userpage():
    user_id = users.user_id()
    list = storage.get_loans(user_id)
    if request.method == "GET":
        if not list:
            return render_template("user.html", message="Ei lainoja tällä hetkellä")
        else:
            return render_template("user.html", items=list, message="Lainasi")
    if request.method == "POST":
        loan_id = request.form("loan_id")
        storage.item_return(loan_id[0])
        return redirect("/user")

@app.route("/admin")
def adminpage():
    if users.check_admin():
        list = storage.get_all_loans()
        if not list:
            return render_template("admin.html", show=True, message="Ei lainoja tällä hetkellä")
        else:
            return render_template("admin.html", show=True, items=list, message="Hei ylläpitäjä")
    else:
        return render_template("admin.html", show=False, message="Et ole ylläpitäjä")

@app.route("/frontpage", methods=["GET", "POST"])
def frontpage():
    list = storage.get_list()
    shelters = []
    tools = []
    misc = []
    available = storage.get_available_items()
    for i in list:
        if i[2] == "shelter":
            shelters.append(i)
        if i[2] == "tool":
            tools.append(i)
        if i[2] == "misc":
            misc.append(i)
    if request.method == "GET":
        return render_template("frontpage.html", items1=shelters, items2=tools, items3=misc, available=available)
    if request.method == "POST":
        user_id = users.user_id()
        object_id = request.form("object")
        storage.new_loan(user_id, object_id[0])
        return redirect("/frontpage")