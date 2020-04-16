# enrolled_in SQL Queries

def get_enrolled_in():
    return "SELECT * FROM enrolled_in;"

def get_sEnrolled_in(sname):
        return "SELECT * FROM enrolled_in WHERE SUserName= %s;" % (sname,)

def get_cEnrolled_in(cname,cnum):
    # Gets all the student names that are enrolled in a course name and course number
    if cname != "" and cnum != "":
        return "SELECT * FROM enrolled_in WHERE CName=%s AND CNumber= %s;" % (cname,cnum,) 

# All fields need to be specified, no need to check the params to make sure they are specified, if they aren't it will error
def post_enrolled_in(sname,cname,cnum):
    return "INSERT INTO enrolled_in VALUES(%s,%s,%s);" % (sname,cname,cnum,)

# Can either delete by a student username only, deleting all rows with them, or one specific row with all fields specified
def delete_enrolled_in(sname,cname,cnum):
    if cname == "" and cnum == "":
        return "DELETE FROM enrolled_in WHERE SUserName=%s;" % (sname,)
    if  sname != "" and cname != "" and cnum != "":
        return "DELETE FROM enrolled_in WHERE SUserName=%s AND CName=%s AND CNumber=%s;" % (sname,cname,cnum,)