from pickle import FALSE
from db import db
from flask import abort, request, session
from secrets import token_hex
from werkzeug.security import generate_password_hash, check_password_hash

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = username
            session["csrf_token"] = token_hex(16)
            return True
        else:
            return False

def logout(username):
    del session["user_id"]
    del session["username"]
    del session ["csrf_token"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        permission = False
        sql = "INSERT into users (username, password, is_admin) VALUES (:username, :password, :permission)"
        db.session.execute(sql, {"username":username, "password":hash_value, "permission":permission})
        db.session.commit()
    except:
        return False
    return login(username, password)

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)

def check_admin():
    id = session["user_id"]
    sql = "SELECT is_admin FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    permission = result.fetchone()
    return permission

def user_id():
    return session.get("user_id",0)

def get_username():
    username = session["username"]
    return username