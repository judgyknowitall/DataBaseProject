# school SQL Queries

def get_schools():
    return "SELECT * FROM school;"

def get_school(sname):
    return "SELECT * FROM school WHERE SchoolName= %s;" % (sname,)

def get_someSchools(pcode):
    return "SELECT * FROM school WHERE PostalCode= %s;" % (pcode,)

def post_school(sname,pcode):
    if pcode == "":
        pcode = "''"
    return "INSERT INTO school VALUES(%s,%s);" % (sname,pcode,)

def put_school(sname,pcode):
    if pcode == "":
        pcode = "''"
    return "UPDATE school SET PostalCode=%s WHERE SchoolName=%s;" % (pcode,sname,)

def delete_school(sname):
    return "DELETE FROM school WHERE SchoolName=%s;" % (sname)