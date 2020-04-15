# canTutor SQL Queries

def get_canTutor():
    return "SELECT * FROM can_tutor;"

def get_oneTutor(tid,cname,cnum):
    # To get all rows with a tutors id, all courses they can tutor
    if cname == "" and cnum == "":
        return "SELECT * FROM can_tutor WHERE TUserName= %s;" % (tid,)
    # Gets all the course names a tutor can teach with a course number
    if  tid != "" and cname != "" and cnum == "":
        return "SELECT * FROM can_tutor WHERE TUserName= %s AND CName=%s;" % (tid,cname,) 
    # Gets all the course numbers a tutor can teach with a course name
    if  tid != "" and cname == "" and cnum != "":
        return "SELECT * FROM can_tutor WHERE TUserName= %s AND CNumber=%s;" % (tid,cnum,) 

# All fields need to be specified, no need to check the params to make sure they are specified, if they aren't it will error
def post_canTutor(tid,cname,cnum):
    return "INSERT INTO can_tutor VALUES(%s,%s,%s);" % (tid,cname,cnum,)

# Can either delete by a tutor id only, deleting all rows with them, or one specific row with all fields specified
def delete_canTutor(tid,cname,cnum):
    if cname == "" and cnum == "":
        print(cname)
        print(cnum)
        return "DELETE FROM can_tutor WHERE TUserName=%s;" % (tid,)
    if  tid != "" and cname != "" and cnum != "":
        return "DELETE FROM can_tutor WHERE TUserName=%s AND CName=%s AND CNumber=%s;" % (tid,cname,cnum,)