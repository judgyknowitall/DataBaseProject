# admin SQL Queries

def get_admin():
    return "SELECT * FROM admin;"

def get_oneAdmin(aid):
    return "SELECT * FROM admin WHERE AUserName= %s;" % (aid,)

def post_admin(aid,name,password):
    if name == "":
        name = "''"
    if password == "":
        password = "''"
    return "INSERT INTO admin VALUES(%s,%s,%s);" % (aid,name,password,)

def put_admin(aid,name,password):
    if name == "":
        name = "''"
    if password == "":
        password = "''"
    return "UPDATE admin SET AName=%s,APassword=%s WHERE AUserName=%s;" % (name,password,aid,)

def delete_admin(aid):
    return "DELETE FROM admin WHERE AUserName=%s;" % (aid,)
