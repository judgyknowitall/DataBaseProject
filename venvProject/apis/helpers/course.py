# course SQL Queries

def get_courses():
    return "SELECT * FROM course;"

def get_someCourses(cname,cnum,level,sub):
    if cname != "" and cnum != "":
        return "SELECT * FROM course WHERE CName= %s AND CNumber=%s;" % (cname,cnum,) 
    if level != "" and sub == "":
        return "SELECT * FROM course WHERE Level= %s;" % (level,) 
    if level == "" and sub != "":
        return "SELECT * FROM course WHERE Subject= %s;" % (sub,) 
    if level != "" and sub != "":
        return "SELECT * FROM course WHERE Level= %s AND Subject= %s;" % (level,sub,) 

def put_course(cname,cnum,level,sub):
    if level == "":
        level = "''"
    if sub == "":
        sub = "''"
    return "UPDATE course SET Level=%s,Subject=%s WHERE CName=%s AND CNumber=%s;" % (level,sub,cname,cnum,)

def post_course(cname,cnum,level,sub):
    if level == "":
        level = "''"
    if sub == "":
        sub = "''"
    return "INSERT INTO course VALUES(%s,%s,%s,%s);" % (cname,cnum,level,sub,)

def delete_course(cname,cnum):
    return "DELETE FROM course WHERE CName=%s AND CNumber=%s;" % (cname,cnum)