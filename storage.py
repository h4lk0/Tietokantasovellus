from unittest import result
from db import db

def get_list():
    sql = "SELECT name, info, in_storage FROM shelters;"
    result = db.session.execute(sql)
    return result.fetchall()

def get_loans(username):
    sql = "SELECT name, amount FROM loans WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    return result.fetchall()

def get_all():
    sql = "SELECT username, name, amount FROM loans"
    result = db.session.execute(sql)
    loans = result.fetchall()
    if not loans:
        loans.insert(0, ("Ei lainoja", "tällä hetkellä", 0))
    return loans