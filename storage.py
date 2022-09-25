from re import X
from db import db

def get_list():
    sql = "SELECT name, info, in_storage FROM shelters;"
    result = db.session.execute(sql)
    return result.fetchall()

