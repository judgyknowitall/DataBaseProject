# StudentMeetsIn Helper funtions


# Get Students in location
def get_studentsInLoc(pc=None, dist=None, city=None, country=None):

    sqlCommand = 'SELECT * FROM location, student_meets_in AS T '
    sqlCommand+= 'WHERE location.PostalCode = T.PostalCode'

    if country is not None:
        sqlCommand+= ' AND Country = %s' % (country)

        if city is not None:
            sqlCommand+= ' AND City = %s' % (city)

            if dist is not None:
                sqlCommand+= ' AND District = %s' % (dist)
    
    if pc is not None:
        sqlCommand+= ' AND location.PostalCode = %s' % (pc)

    sqlCommand+= ';'
    return sqlCommand

# Get location of a student
def get_locOfStudent(sid):

    sqlCommand = 'SELECT * FROM location, student_meets_in AS T '
    sqlCommand+= 'WHERE location.PostalCode = T.PostalCode '
    sqlCommand+= 'AND SUserName = %s;' % (sid)
    
    return sqlCommand

# Post a new studentMeetsIn
def new_studentMeetsIn(sid, pc):
    sqlCommand = 'INSERT INTO student_meets_in VALUES'
    sqlCommand+= '(%s, %s);' % (sid, pc)
    return sqlCommand

# Delete an existing studentMeetsIn
def delete_studentMeetsIn(sid, pc):
    sqlCommand = 'DELETE FROM student_meets_in WHERE '
    sqlCommand+= 'SUserName = %s AND PostalCode = %s;' % (sid,pc)
    return sqlCommand
