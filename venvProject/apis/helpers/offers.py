# offers SQL Queries

def get_offers():
    return "SELECT * FROM offers;"

def get_sOffers(sname):
        return "SELECT * FROM offers WHERE SchoolName= %s;" % (sname,)

def get_cOffers(cname,cnum):
    # Gets all the course names a school can offer with a course number
    if cname != "" and cnum != "":
        return "SELECT * FROM offers WHERE CName=%s AND CNumber= %s;" % (cname,cnum,) 

# All fields need to be specified, no need to check the params to make sure they are specified, if they aren't it will error
def post_offer(sname,cname,cnum):
    return "INSERT INTO offers VALUES(%s,%s,%s);" % (sname,cname,cnum,)

# Can either delete by a school name only, deleting all rows with them, or one specific row with all fields specified
def delete_offer(sname,cname,cnum):
    if cname == "" and cnum == "":
        return "DELETE FROM offers WHERE SchoolName=%s;" % (sname,)
    if  sname != "" and cname != "" and cnum != "":
        return "DELETE FROM offers WHERE SchoolName=%s AND CName=%s AND CNumber=%s;" % (sname,cname,cnum,)